import cv2
from PySide6.QtGui import QIcon
from PySide6.QtCore import QThread, Signal
import numpy as np
import queue
import threading
from pathlib import Path
import os
from datetime import time
from collections import defaultdict

'''
NOTES FOR INTEGRATION
Use the maximum value in the slider to limit the frame - also apply in video detection
'''

class Export_Heatmap_Video_Thread(QThread):
    frames_signal = Signal(object)
    finished_inference = Signal(object)

    def __init__(self, center_video_path, front_video_path, main_window, is_advanced_analytics, directory):
        super().__init__()
        self.main_window = main_window
        self.center_video_path = center_video_path
        self.front_video_path = front_video_path
        self.is_advanced_analytics = is_advanced_analytics
        self.directory = directory

        self.filtered_bboxes_front = self.main_window.filtered_action_results_bboxes_front
        self.filtered_bboxes_center = self.main_window.filtered_action_results_bboxes_center

        self.minimum_value = None
        self.maximum_value = None

        self.center_cap = cv2.VideoCapture(self.center_video_path)
        self.front_cap = cv2.VideoCapture(self.front_video_path)
        
        #For getting the seatplan image hehe
        script_dir = Path(__file__).parent  # Get script's folder
        image_path = script_dir.parent / "assets" / "SEAT_PLAN.png"
        self.seat_plan_picture = cv2.imread(image_path)
        self.seat_plan_picture_previous_frame = self.seat_plan_picture.copy()
        
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        self.heatmap_video_writer = cv2.VideoWriter(os.path.join(self.directory, f"{str(self.main_window.session_name)}_heatmap_output.avi"), self.fourcc, 30, (601, 451))

        #For all
        self.running = True
        self.paused = False

        self.max_size = 30

        # Define 4 corresponding points from the center video frame to the heatmap
        self.src_pts_center = np.array([
                            [655,121],  # Top-left
                            [1939,169],  # Top-right
                            [105,674],  # Bottom-left
                            [2477,722]   # Bottom-right
                        ], dtype=np.float32)

        self.dst_pts_center = np.array([
                            [199,41],  # Top-left
                            [582,41],  # Top-right
                            [199,214],  # Bottom-left
                            [582,214]   # Bottom-right
                        ], dtype=np.float32)

        self.H_center, _ = cv2.findHomography(self.src_pts_center, self.dst_pts_center, cv2.RANSAC)

        # Define homography for front video
        src_pts_front = np.array([
                            [471, 161],  # Top-left
                            [2001, 27],  # Top-right
                            [31, 896],  # Bottom-left
                            [2516, 792]   # Bottom-right
                        ], dtype=np.float32)

        dst_pts_front = np.array([
                        [199,214],  # Top-left
                        [582,214],  # Top-right
                        [199,390],  # Bottom-left
                        [582,390]   # Bottom-right
                    ], dtype=np.float32)

        self.H_front, _ = cv2.findHomography(src_pts_front, dst_pts_front, cv2.RANSAC)
        
        #For drawing classroom heatmap
        self.frame_count = 0
        self.heatmap_overlay_cache = None  # Cache for blended result
        self.lowres_size = (160, 120)  # Lower resolution for the heatmap
        self.fullres_size = (1280, 720)  # Update to match your video frame resolution
        
        self.heatmap_frame_counter = 0
        self.label_buffer = {
            'Front': {},
            'Center': {}
        }
        
        self.play_icon = QIcon(":/icons/play-256.png")   # Play icon from resources
        self.pause_icon = QIcon(":/icons/pause-256.png") # Pause icon from resources
        
        self.gradient_cache = {}
        
        self.action_colors = self.main_window.action_colors
        
        self.classroom_heatmap_frames_queue = queue.Queue(maxsize=self.max_size)
        self.current_frame_index = 0
      
        self.preload_thread = threading.Thread(target=self.preload_frames, daemon=True)
        self.preload_thread.start()  # Start background frame loader
        
        
    #Helper Method
    def draw_heat_circle(self, bbox, label, homography_matrix, radius):
        color = self.action_colors.get(label, (255, 255, 255))
        gradient_circle = self.get_gradient_circle(radius, color, 16)

        if gradient_circle.shape[2] != 4:
            print("[ERROR] Gradient circle must have alpha channel.")
            return

        x1, y1, x2, y2 = map(int, bbox)
        center_point = np.array([[[ (x1 + x2) / 2, (y1 + y2) / 2 ]]], dtype=np.float32)
        transformed_point = cv2.perspectiveTransform(center_point, homography_matrix)
        mapped_x, mapped_y = transformed_point[0][0]

        if not (0 <= mapped_x < self.heatmap_image.shape[1] and 0 <= mapped_y < self.heatmap_image.shape[0]):
            print(f"[DEBUG] Transformed point out of bounds: ({mapped_x}, {mapped_y})")
            return

        self.overlay_image_alpha(
            self.heatmap_image,
            gradient_circle,
            (int(mapped_x - radius), int(mapped_y - radius))
        )

    
    def drawing_classroom_heatmap(self, frame, results_front, results_center, 
                              actions_front=None, actions_center=None,
                              head_posture_front=None, head_posture_center=None,
                              arm_posture_front=None, arm_posture_center=None):
        """
        Draws a heatmap with action-specific gradient circles.
        """

        if not results_front and not results_center:
            print("[INFO] No detections in either camera.")
            return frame

        # 🔹 Prioritize label type
        selected_label_type = None
        if actions_front or actions_center:
            selected_label_type = "actions"
        elif head_posture_front or head_posture_center:
            selected_label_type = "head_posture"
        elif arm_posture_front or arm_posture_center:
            selected_label_type = "arm_posture"
        else:
            print("[INFO] No label data provided.")
            return frame

        # 🔹 Color mapping
        
        label_map = {
                    "Front": {
                        "actions": actions_front,
                        "head_posture": head_posture_front,
                        "arm_posture": arm_posture_front,
                        "results": results_front,
                        "homography": self.H_front
                    },
                    "Center": {
                        "actions": actions_center,
                        "head_posture": head_posture_center,
                        "arm_posture": arm_posture_center,
                        "results": results_center,
                        "homography": self.H_center
                    }
                }


        self.heatmap_image = frame.copy()

        radius = 50

        # 🔹 Process both camera results
        for camera_label, data in label_map.items():
            results = data["results"]
            actions = data[selected_label_type]
            homography_matrix = data["homography"]


            if not results:
                continue
            if not actions:
                continue

            for track_id, bbox in results.items():
                if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
                    continue

                action = actions.get(track_id, "UNKNOWN")

                if isinstance(action, dict):  # For arm_posture with left/right
                    for arm_side, label in action.items():
                        self.draw_heat_circle(bbox, label, homography_matrix, radius)
                        
                else:  # For single string labels like head_posture or actions
                    self.draw_heat_circle(bbox, action, homography_matrix, radius)

        self.seat_plan_picture_previous_frame = self.heatmap_image
        
        return self.heatmap_image

    def create_gradient_circle(self, radius, color, alpha):
        size = radius * 2
        y, x = np.ogrid[:size, :size]
        distance = np.sqrt((x - radius) ** 2 + (y - radius) ** 2)
        mask = distance < radius
        opacity = ((1 - (distance / radius)) * alpha).astype(np.uint8)
        opacity[~mask] = 0

        gradient = np.zeros((size, size, 4), dtype=np.uint8)
        gradient[..., :3] = color
        gradient[..., 3] = opacity
        return gradient

    def get_gradient_circle(self, radius, color, alpha):
        key = (radius, color, alpha)
        if key not in self.gradient_cache:
            self.gradient_cache[key] = self.create_gradient_circle(radius, color, alpha)
        return self.gradient_cache[key]

    # Function to overlay image with alpha
    def overlay_image_alpha(self, img, img_overlay, pos):

        '''
        Blends an overlay image (e.g., heatmap) onto another image with transparency.
        '''
        
        x, y = pos
        h, w = img_overlay.shape[:2]

        # Compute overlap regions
        y1, y2 = max(0, y), min(img.shape[0], y + h)
        x1, x2 = max(0, x), min(img.shape[1], x + w)

        y1o, y2o = max(0, -y), min(h, img.shape[0] - y)
        x1o, x2o = max(0, -x), min(w, img.shape[1] - x)

        if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
            return

        # Alpha blending
        img_overlay_crop = img_overlay[y1o:y2o, x1o:x2o]
        alpha = img_overlay_crop[..., 3:4] / 255.0  # Keep alpha as (h, w, 1) for broadcasting
        img[y1:y2, x1:x2, :3] = (alpha * img_overlay_crop[..., :3] +
                                (1 - alpha) * img[y1:y2, x1:x2, :3]).astype(np.uint8)

    def preload_frames(self):        
        """
        Background thread to keep decoding frames ahead of playback
        """
        
        while self.running:
  
            if (self.current_frame_index > (self.main_window.max_frames - 1)):
                break
                
            heatmap_frame_threshold = 30
            if self.current_frame_index % heatmap_frame_threshold == 0:
                
                if self.is_advanced_analytics:
                    #No shortcuts, just call it dynamically, it does not affect any performance tho
                    processed_classroom_heatmap = self.drawing_classroom_heatmap(
                                                                                frame=self.seat_plan_picture_previous_frame,
                                                                                results_front=self.main_window.filtered_action_results_bboxes_front[int(self.current_frame_index)],  
                                                                                results_center=self.main_window.filtered_action_results_bboxes_center[int(self.current_frame_index)],
                                                                                actions_front= None,
                                                                                actions_center=None,
                                                                                head_posture_front= self.main_window.filtered_head_postures_list_front[int(self.current_frame_index)],
                                                                                head_posture_center= self.main_window.filtered_head_postures_list_center[int(self.current_frame_index)],
                                                                                arm_posture_front=self.main_window.filtered_arms_postures_list_front[int(self.current_frame_index)],
                                                                                arm_posture_center=self.main_window.filtered_arms_postures_list_center[int(self.current_frame_index)],
                                                                                )
                else:
                    processed_classroom_heatmap = self.drawing_classroom_heatmap(
                                                                                frame=self.seat_plan_picture_previous_frame,
                                                                                results_front=self.main_window.filtered_action_results_bboxes_front[int(self.current_frame_index)],  
                                                                                results_center=self.main_window.filtered_action_results_bboxes_center[int(self.current_frame_index)],
                                                                                actions_front=  self.main_window.filtered_action_results_list_front[int(self.current_frame_index)],
                                                                                actions_center=self.main_window.filtered_action_results_list_center[int(self.current_frame_index)],
                                                                                head_posture_front = None,
                                                                                head_posture_center= None,
                                                                                arm_posture_front=None,
                                                                                arm_posture_center=None,
                                                                                )
    
                # Store the heatmap in the queue
                self.classroom_heatmap_frames_queue.put(processed_classroom_heatmap)
                
            else:
                self.classroom_heatmap_frames_queue.put(self.seat_plan_picture_previous_frame)

            self.current_frame_index += 1

    def run(self):
        '''
        Main playback loop, sending frames from queue to UI
        '''
        while self.running:
            if not self.classroom_heatmap_frames_queue.empty():
                classroom_heatmap = self.classroom_heatmap_frames_queue.get()
                self.heatmap_video_writer.write(classroom_heatmap)
                print("HEATMAP SAVED!")
                
        self.finished_inference.emit(True)
      
    def stop(self):
        self.running = False
        self.quit()
        self.wait()

    def pause(self, status):
        self.paused = status



class Export_Heatmap_Image_Thread(QThread):
    frames_signal = Signal(object)
    finished_inference = Signal(object)
    progress_updated = Signal(int)

    def __init__(self, center_video_path, front_video_path, main_window):
        super().__init__()
        self.main_window = main_window
        self.center_video_path = center_video_path
        self.front_video_path = front_video_path

        self.minimum_value = None
        self.maximum_value = None

        self.center_cap = cv2.VideoCapture(self.center_video_path)
        self.front_cap = cv2.VideoCapture(self.front_video_path)
        
        #For getting the seatplan image hehe
        script_dir = Path(__file__).parent  # Get script's folder
        image_path = script_dir.parent / "assets" / "SEAT_PLAN.png"
        self.seat_plan_picture = cv2.imread(image_path)
        self.seat_plan_picture_previous_frame = self.seat_plan_picture.copy()

        #For all
        self.running = True
        self.paused = False

        self.max_size = 30

        # Define 4 corresponding points from the center video frame to the heatmap
        self.src_pts_center = np.array([
                            [655,121],  # Top-left
                            [1939,169],  # Top-right
                            [105,674],  # Bottom-left
                            [2477,722]   # Bottom-right
                        ], dtype=np.float32)

        self.dst_pts_center = np.array([
                            [199,41],  # Top-left
                            [582,41],  # Top-right
                            [199,214],  # Bottom-left
                            [582,214]   # Bottom-right
                        ], dtype=np.float32)

        self.H_center, _ = cv2.findHomography(self.src_pts_center, self.dst_pts_center, cv2.RANSAC)

        # Define homography for front video
        src_pts_front = np.array([
                            [471, 161],  # Top-left
                            [2001, 27],  # Top-right
                            [31, 896],  # Bottom-left
                            [2516, 792]   # Bottom-right
                        ], dtype=np.float32)

        dst_pts_front = np.array([
                        [199,214],  # Top-left
                        [582,214],  # Top-right
                        [199,390],  # Bottom-left
                        [582,390]   # Bottom-right
                    ], dtype=np.float32)

        self.H_front, _ = cv2.findHomography(src_pts_front, dst_pts_front, cv2.RANSAC)
        
        #For drawing classroom heatmap
        self.frame_count = 0
        self.heatmap_overlay_cache = None  # Cache for blended result
        self.lowres_size = (160, 120)  # Lower resolution for the heatmap
        self.fullres_size = (1280, 720)  # Update to match your video frame resolution
        
        self.heatmap_frame_counter = 0
        self.label_buffer = {
            'Front': {},
            'Center': {}
        }
        
        self.play_icon = QIcon(":/icons/play-256.png")   # Play icon from resources
        self.pause_icon = QIcon(":/icons/pause-256.png") # Pause icon from resources
        
        self.gradient_cache = {}
        
        self.action_colors = self.main_window.action_colors
        
        self.classroom_heatmap_frames_queue = queue.Queue(maxsize=self.max_size)
        self.current_frame_index = 0
        
        
    #Helper Method
    def draw_heat_circle(self, bbox, label, homography_matrix, radius):
        color = self.action_colors.get(label, (255, 255, 255))
        gradient_circle = self.get_gradient_circle(radius, color, 16)

        if gradient_circle.shape[2] != 4:
            print("[ERROR] Gradient circle must have alpha channel.")
            return

        x1, y1, x2, y2 = map(int, bbox)
        center_point = np.array([[[ (x1 + x2) / 2, (y1 + y2) / 2 ]]], dtype=np.float32)
        transformed_point = cv2.perspectiveTransform(center_point, homography_matrix)
        mapped_x, mapped_y = transformed_point[0][0]

        if not (0 <= mapped_x < self.heatmap_image.shape[1] and 0 <= mapped_y < self.heatmap_image.shape[0]):
            print(f"[DEBUG] Transformed point out of bounds: ({mapped_x}, {mapped_y})")
            return

        self.overlay_image_alpha(
            self.heatmap_image,
            gradient_circle,
            (int(mapped_x - radius), int(mapped_y - radius))
        )
        
    def draw_heat_circle_indiv(self, bbox, label, homography_matrix, radius, image):
        color = self.action_colors.get(label, (255, 255, 255))
        gradient_circle = self.get_gradient_circle(radius, color, 16)

        if gradient_circle.shape[2] != 4:
            print("[ERROR] Gradient circle must have alpha channel.")
            return

        x1, y1, x2, y2 = map(int, bbox)
        center_point = np.array([[[ (x1 + x2) / 2, (y1 + y2) / 2 ]]], dtype=np.float32)
        transformed_point = cv2.perspectiveTransform(center_point, homography_matrix)
        mapped_x, mapped_y = transformed_point[0][0]

        if not (0 <= mapped_x < image.shape[1] and 0 <= mapped_y < image.shape[0]):
            print(f"[DEBUG] Transformed point out of bounds: ({mapped_x}, {mapped_y})")
            return

        self.overlay_image_alpha(
            image,
            gradient_circle,
            (int(mapped_x - radius), int(mapped_y - radius))
        )



    def drawing_classroom_heatmap(self, frame, results_front, results_center, 
                              actions_front=None, actions_center=None,
                              head_posture_front=None, head_posture_center=None,
                              arm_posture_front=None, arm_posture_center=None):
        """
        Draws a heatmap with action-specific gradient circles.
        """

        if not results_front and not results_center:
            print("[INFO] No detections in either camera.")
            return frame

        # 🔹 Prioritize label type
        selected_label_type = None
        if actions_front or actions_center:
            selected_label_type = "actions"
        elif head_posture_front or head_posture_center:
            selected_label_type = "head_posture"
        elif arm_posture_front or arm_posture_center:
            selected_label_type = "arm_posture"
        else:
            print("[INFO] No label data provided.")
            return frame

        # 🔹 Color mapping
        
        label_map = {
                    "Front": {
                        "actions": actions_front,
                        "head_posture": head_posture_front,
                        "arm_posture": arm_posture_front,
                        "results": results_front,
                        "homography": self.H_front
                    },
                    "Center": {
                        "actions": actions_center,
                        "head_posture": head_posture_center,
                        "arm_posture": arm_posture_center,
                        "results": results_center,
                        "homography": self.H_center
                    }
                }


        self.heatmap_image = frame.copy()

        radius = 50

        # 🔹 Process both camera results
        for camera_label, data in label_map.items():
            results = data["results"]
            actions = data[selected_label_type]
            homography_matrix = data["homography"]


            if not results:
                continue
            if not actions:
                continue

            for track_id, bbox in results.items():
                if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
                    continue

                action = actions.get(track_id, "UNKNOWN")

                if isinstance(action, dict):  # For arm_posture with left/right
                    for arm_side, label in action.items():
                        self.draw_heat_circle(bbox, label, homography_matrix, radius)
                        
                else:  # For single string labels like head_posture or actions
                    self.draw_heat_circle(bbox, action, homography_matrix, radius)

        self.seat_plan_picture_previous_frame = self.heatmap_image
        
        return self.heatmap_image

    def create_gradient_circle(self, radius, color, alpha):
        size = radius * 2
        y, x = np.ogrid[:size, :size]
        distance = np.sqrt((x - radius) ** 2 + (y - radius) ** 2)
        mask = distance < radius
        opacity = ((1 - (distance / radius)) * alpha).astype(np.uint8)
        opacity[~mask] = 0

        gradient = np.zeros((size, size, 4), dtype=np.uint8)
        gradient[..., :3] = color
        gradient[..., 3] = opacity
        return gradient

    def get_gradient_circle(self, radius, color, alpha):
        key = (radius, color, alpha)
        if key not in self.gradient_cache:
            self.gradient_cache[key] = self.create_gradient_circle(radius, color, alpha)
        return self.gradient_cache[key]

    # Function to overlay image with alpha
    def overlay_image_alpha(self, img, img_overlay, pos):

        '''
        Blends an overlay image (e.g., heatmap) onto another image with transparency.
        '''
        
        x, y = pos
        h, w = img_overlay.shape[:2]

        # Compute overlap regions
        y1, y2 = max(0, y), min(img.shape[0], y + h)
        x1, x2 = max(0, x), min(img.shape[1], x + w)

        y1o, y2o = max(0, -y), min(h, img.shape[0] - y)
        x1o, x2o = max(0, -x), min(w, img.shape[1] - x)

        if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
            return

        # Alpha blending
        img_overlay_crop = img_overlay[y1o:y2o, x1o:x2o]
        alpha = img_overlay_crop[..., 3:4] / 255.0  # Keep alpha as (h, w, 1) for broadcasting
        img[y1:y2, x1:x2, :3] = (alpha * img_overlay_crop[..., :3] +
                                (1 - alpha) * img[y1:y2, x1:x2, :3]).astype(np.uint8)

    def drawing_individual_action_heatmaps(self, frame, results_front, results_center,
                                       actions_front=None, actions_center=None,
                                       temp_dir=None, percentage_label=100):
        print("[INFO] Starting drawing_individual_action_heatmaps...")

        print(f"[DEBUG] Total cumulative actions front: {len(actions_front)}")
        print(f"[DEBUG] Total cumulative actions center: {len(actions_center)}")

        if not actions_front and not actions_center:
            print("[INFO] No cumulative action data to process.")
            return

        all_action_labels = set()
        if actions_front:
            all_action_labels.update(actions_front)
        if actions_center:
            all_action_labels.update(actions_center)

        print(f"[DEBUG] Unique action labels to draw: {all_action_labels}")

        radius = 50

        for label_name in all_action_labels:
            heatmap_img = frame.copy()

            for track_id, bbox in results_front.items():
                action_label = actions_front.get(track_id)
                if action_label == label_name:
                    homography = self.H_front
                    self.draw_heat_circle_indiv(bbox, action_label, homography, radius, heatmap_img)

            for track_id, bbox in results_center.items():
                action_label = actions_center.get(track_id)
                if action_label == label_name:
                    homography = self.H_center
                    self.draw_heat_circle_indiv(bbox, action_label, homography, radius, heatmap_img)

            sanitized_label = str(label_name).replace(" ", "_").lower()
            label_path = temp_dir / f"specific_heatmap_{sanitized_label}_at_{percentage_label}.jpg"
            cv2.imwrite(str(label_path), heatmap_img)
            print(f"[SAVED] Label-specific heatmap for '{label_name}' at {percentage_label}% - {label_path}")
            
    def preload_frames(self):
        # For storing all action data over time (dict for drawing with .items())
        self.cumulative_action_bboxes_front = {}
        self.cumulative_action_bboxes_center = {}
        self.cumulative_actions_front = {}
        self.cumulative_actions_center = {}
        
        progress = int((self.current_frame_index / self.main_window.max_frames) * 100)

        self.heatmap_save_checkpoints = [
            int(self.main_window.max_frames * 0.25),
            int(self.main_window.max_frames * 0.5),
            int(self.main_window.max_frames * 0.75),
            int(self.main_window.max_frames * 1.0)
        ]

        processed_classroom_heatmap_advanced = None
        processed_classroom_heatmap_ai = None

        script_dir = Path(__file__).resolve().parent
        temp_dir = script_dir / "temp"
        temp_dir.mkdir(parents=True, exist_ok=True)

        print(f"[INFO] Temp directory path: {temp_dir}")

        while self.running:
            if self.paused:
                time.sleep(0.1)
                continue

            if self.current_frame_index > (self.main_window.max_frames - 1):
                break

            frame_idx = self.current_frame_index

            results_f = self.main_window.filtered_action_results_bboxes_front[frame_idx]
            results_c = self.main_window.filtered_action_results_bboxes_center[frame_idx]
            actions_f = self.main_window.filtered_action_results_list_front[frame_idx]
            actions_c = self.main_window.filtered_action_results_list_center[frame_idx]

            # Accumulate with unique keys (to use .items() later)
            for i, bbox in enumerate(results_f):
                self.cumulative_action_bboxes_front[f"{frame_idx}_f_{i}"] = bbox
            for i, bbox in enumerate(results_c):
                self.cumulative_action_bboxes_center[f"{frame_idx}_c_{i}"] = bbox
            for i, action in enumerate(actions_f):
                self.cumulative_actions_front[f"{frame_idx}_f_{i}"] = action
            for i, action in enumerate(actions_c):
                self.cumulative_actions_center[f"{frame_idx}_c_{i}"] = action

            heatmap_frame_threshold = 30
            if self.current_frame_index % heatmap_frame_threshold == 0:
                processed_classroom_heatmap_ai = self.drawing_classroom_heatmap(
                    frame=self.seat_plan_picture_previous_frame.copy(),
                    results_front=results_f,
                    results_center=results_c,
                    actions_front=actions_f,
                    actions_center=actions_c,
                    head_posture_front=None,
                    head_posture_center=None,
                    arm_posture_front=None,
                    arm_posture_center=None,
                )

                processed_classroom_heatmap_advanced = self.drawing_classroom_heatmap(
                    frame=self.seat_plan_picture_previous_frame.copy(),
                    results_front=results_f,
                    results_center=results_c,
                    actions_front=None,
                    actions_center=None,
                    head_posture_front=self.main_window.filtered_head_postures_list_front[frame_idx],
                    head_posture_center=self.main_window.filtered_head_postures_list_center[frame_idx],
                    arm_posture_front=self.main_window.filtered_arms_postures_list_front[frame_idx],
                    arm_posture_center=self.main_window.filtered_arms_postures_list_center[frame_idx],
                )
            else:
                processed_classroom_heatmap_ai = self.seat_plan_picture_previous_frame
                processed_classroom_heatmap_advanced = self.seat_plan_picture_previous_frame

            # Save at checkpoints
            frame = self.current_frame_index + 1
            if frame in self.heatmap_save_checkpoints:
                if frame <= self.heatmap_save_checkpoints[0]:
                    percentage_label = 25
                elif frame <= self.heatmap_save_checkpoints[1]:
                    percentage_label = 50
                elif frame <= self.heatmap_save_checkpoints[2]:
                    percentage_label = 75
                else:
                    percentage_label = 100

                save_path_ai = temp_dir / f"ai_analytics_heatmap_checkpoint_{percentage_label}.jpg"
                save_path_advanced = temp_dir / f"advanced_analytics_heatmap_checkpoint_{percentage_label}.jpg"

                print(f"[SAVE] AI Heatmap at {percentage_label}% - {save_path_ai}")
                cv2.imwrite(str(save_path_ai), processed_classroom_heatmap_ai)

                print(f"[SAVE] Advanced Heatmap at {percentage_label}% - {save_path_advanced}")
                cv2.imwrite(str(save_path_advanced), processed_classroom_heatmap_advanced)

            self.current_frame_index += 1


    def run(self):
        self.preload_frames()    
        self.finished_inference.emit(True)
        
    def stop(self):
        if self.running:  # Ensure the thread is still running
            self.running = False
            # Wait for the thread to finish if it is not in the process of quitting
            self.quit()  
            self.wait()  # Properly waits for the thread to complete

    def pause(self, status):
        self.paused = status
