import cv2
from PySide6.QtGui import QIcon
from PySide6.QtCore import QThread, Signal, QMetaObject, Qt, Q_ARG
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
import numpy as np
import queue
import threading
from pathlib import Path
import os

cv2.setNumThreads(0)
cv2.ocl.setUseOpenCL(False)

class Video_Detection_Export(QThread):
    '''
    The technique used in playing the video is to preload the frames in a queue and then play them in a loop.
    This is done to ensure that the video is played smoothly without any lagging.
    The technique is called "Frame Buffering WITH Lazy Lodaing
    Producer-Consumer Pattern (Using queue.Queue)
        Producer: The preload_frames() function continuously reads frames in the background and stores them in a queue (queue.Queue).
        Consumer: The run() method fetches preloaded frames from the queue and sends them to the UI for display.
    Advantage: This prevents the UI thread from waiting for frame decoding, making playback smooth.
         Lazy Loading (On-Demand Processing)

    Instead of storing all frames in RAM, we load only the next few frames (maxsize=10 in the queue).
    When a frame is needed, it's already decoded and ready for display.

    '''

    
    frames_signal = Signal(object)
    current_frame_signal = Signal(object)
    current_frame_index_signal = Signal(int)
    status_signal = Signal(object)

    #cv2.setNumThreads(1)  # Disable OpenCV multi-threading to reduce CPU usage

    def __init__(self, center_video_path, front_video_path, main_window, is_advanced_analytics, video_output_directory):
        
        super().__init__()

        self.main_window = main_window
        self.center_video_path = center_video_path
        self.front_video_path = front_video_path

        self.is_advanced_analytics = is_advanced_analytics
        self.video_output_directory = video_output_directory
        
        #Separate captures for each video

        self.center_cap = cv2.VideoCapture(self.center_video_path)
        self.front_cap = cv2.VideoCapture(self.front_video_path)
        
        
        # Get frame size and FPS from the video
        
        self.front_video_fps = self.front_cap.get(cv2.CAP_PROP_FPS)
        self.center_video_fps = self.center_cap.get(cv2.CAP_PROP_FPS)

        # Define the codec and create VideoWriter object
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        
        if self.main_window.ai_analytics_export_radio_button.isChecked():
            self.file_name_option = "AI_Analytics"
        else:
            self.file_name_option = "Advanced_Analytics"
        
        self.front_video_writer = cv2.VideoWriter(os.path.join(self.video_output_directory, f"{str(self.main_window.session_name)}_output_front_{self.file_name_option}.avi"), self.fourcc, self.front_video_fps, (1920, 1080))
        self.center_video_writer = cv2.VideoWriter(os.path.join(self.video_output_directory, f"{str(self.main_window.session_name)}_output_center_{self.file_name_option}.avi"), self.fourcc, self.center_video_fps, (1920, 1080))
        
        #For all
        self.running = True
        self.paused = False

        self.max_size = 10 
        #Keep preloaded frames here

        self.center_video_frame_queue = queue.Queue(maxsize=self.max_size)  
        self.front_video_frame_queue = queue.Queue(maxsize=self.max_size)  

        self.current_center_video_frame_index = 0
        self.current_front_video_frame_index = 0
        self.current_frame_index = 0

        self.target_frame_index = 0 # Set target frame index
        self.preload_thread = threading.Thread(target=self.preload_frames, daemon=True)
        self.preload_thread.start()  # Start background frame loader

        self.skeleton_pairs = [
            (0, 1), (0, 2), (1, 3), (2, 4), (0, 5), (0, 6), (5, 6), 
            (5, 7), (6, 8), (7, 9), (8, 10), (5, 11), (6, 12), (11, 12), 
            (11, 13), (12, 14), (13, 15), (14, 16)
        ]

        self.isFirstFrame =True
        
        self.suspicious_criteria = self.main_window.suspicious_criteria



        
    def write_action_text(self, frame, detections, actions, head_postures_list,
                        arm_postures_list):
        '''
        Draw bounding boxes with action labels on each frame.
        '''

        if self.main_window.advanced_analytics_export_radio_button.isChecked():
            for person_id, bbox in detections.items():
                x, y, w, h = map(int, bbox)  # Ensure coordinates are integers
                
                #action_text = f"Action: {actions.get(person_id, 'Unknown')}"
                
                #Get the details per person
                head_posture_info = head_postures_list.get(person_id, {})
                head_posture_label = head_posture_info.get('head_posture', 'Unknown')
                
                #Get the details per person
                arm_posture_info = arm_postures_list.get(person_id, {})
                left_arm_posture_label = arm_posture_info.get('left_arm_posture', 'Unknown')  
                right_arm_posture_label = arm_posture_info.get('right_arm_posture', 'Unknown')
                
                head_posture = f"Head: {head_posture_label}"
                left_arm_posture = f"Left Arm: {left_arm_posture_label}"
                right_arm_posture = f"Right Arm: {right_arm_posture_label}"
                
                # Ensure text position is within frame bounds
                text_x, text_y = x, max(y - 10, 50)  # Prevent negative y
                
                # Make font size and location relative to bbox width
                
                bbox_width = w - x
                bbox_height = h - y

                font_scale = max(0.5, bbox_width / 300)  # Adjust 200 to control scaling
                thickness = max(1, int(bbox_width / 120))  # Adjust for visibility
                
                #For Head
                head_offset_y = int(bbox_height * 0.05)  # % of bbox height above top
                head_offset_x = int(bbox_width )  # % of bbox height above top
                head_text_position = (x , y - head_offset_y)
                
                #For Left Arm
                left_arm_offset_y = int(bbox_height * 0.15)  # % of bbox height above top
                left_arm_offset_x = int(bbox_width )  # % of bbox height above top
                left_arm_text_position = (x , y - left_arm_offset_y)
                
                #For Right Arm
                right_arm_offset_y = int(bbox_height * 0.25)  # % of bbox height above top
                right_arm_offset_x = int(bbox_width )  # % of bbox height above top
                right_arm_text_position = (x , y - right_arm_offset_y)
                
                #For Head Postures
                cv2.putText(frame, head_posture, head_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 255, 0), thickness)

                
                #For Left Arm Posture
                cv2.putText(frame, left_arm_posture, left_arm_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 255, 0), thickness)

                
                #For Right Arm Postures
                cv2.putText(frame, right_arm_posture, right_arm_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 255, 0), thickness)
        
        else:
            
            for person_id, bbox in detections.items():
                x, y, w, h = map(int, bbox)  # Ensure coordinates are integers
                action_text = f"Action: {actions.get(person_id, 'Unknown')}"
                
                # Ensure text position is within frame bounds
                text_x, text_y = x, max(y - 10, 10)  # Prevent negative y
                
                bbox_width = w - x
                bbox_height = h - y

                font_scale = max(0.5, bbox_width / 250)  # Adjust 200 to control scaling
                thickness = max(1, int(bbox_width/120))  # Adjust for visibility
                offset_y = int(bbox_height * 0.05)  # % of bbox height above top
                text_position = (x, y - offset_y)
                
                #cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame, action_text, text_position, cv2.FONT_HERSHEY_SIMPLEX,font_scale, (0, 255, 0), thickness)

            
        return frame

    def get_colors_actions_from_tracker(self):
        red_actions = self.suspicious_criteria.get('red_actions', [])
        orange_actions = self.suspicious_criteria.get('orange_actions', [])
        green_actions = self.suspicious_criteria.get('green_actions', [])
        min_consistent_frames = self.suspicious_criteria.get('min_consistent_frames', {})
        repetition_thresholds = self.suspicious_criteria.get('repetition_thresholds', {})
        repetition_interval = self.suspicious_criteria.get('repetition_interval', 15)

        # Prepare data sources
        if self.is_advanced_analytics:
            arms_front = self.main_window.arms_postures_list_front
            arms_center = self.main_window.arms_postures_list_center
            head_front = self.main_window.head_postures_list_front
            head_center = self.main_window.head_postures_list_center

            combined_results = []
            for a_f, a_c, h_f, h_c in zip(arms_front, arms_center, head_front, head_center):
                frame_dict = {}
                for track_id, arm_data in {**a_f, **a_c}.items():
                    frame_dict.setdefault(track_id, {}).update(arm_data)
                for track_id, head_data in {**h_f, **h_c}.items():
                    frame_dict.setdefault(track_id, {}).update(head_data)
                combined_results.append(frame_dict)
        else:
            action_results_front = self.main_window.action_results_list_front
            action_results_center = self.main_window.action_results_list_center
            combined_results = [
                {**front, **center}
                for front, center in zip(action_results_front, action_results_center)
            ]

        color_label_map = [{} for _ in combined_results]
        track_histories = {}
        track_counts = {}
        track_last_occurrence = {}

        for frame_idx, frame in enumerate(combined_results):
            for track_id, data in frame.items():
                # Determine the relevant label
                if isinstance(data, dict):
                    label = (
                        data.get('left_arm_posture') or
                        data.get('right_arm_posture') or
                        data.get('head_posture') or
                        'UNKNOWN'
                    )
                else:
                    label = data

                # Initialize tracking structures
                track_histories.setdefault(track_id, [])
                track_counts.setdefault(track_id, {})
                track_last_occurrence.setdefault(track_id, {})

                # Update label history
                track_histories[track_id].append(label)
                consistency_limit = min_consistent_frames.get(label, 1)
                if len(track_histories[track_id]) > consistency_limit:
                    track_histories[track_id].pop(0)

                # Default color and tag
                color = (0, 255, 0)
                tag = ""

                # Repetition-based suspiciousness logic
                if label in repetition_thresholds:
                    last_frame = track_last_occurrence[track_id].get(label, -repetition_interval - 1)
                    if frame_idx - last_frame >= repetition_interval:
                        track_counts[track_id][label] = track_counts[track_id].get(label, 0) + 1
                        track_last_occurrence[track_id][label] = frame_idx

                    rep_count = track_counts[track_id].get(label, 0)
                    max_allowed = repetition_thresholds[label]

                    if rep_count > max_allowed:
                        color = (0, 0, 255)      # Red
                        tag = f"HIGHLY SUSPICIOUS"
                    elif 0 < rep_count <= max_allowed:
                        color = (0, 255, 255)    # Orange
                        tag = f"MODERATELY SUSPICIOUS"
                    else:
                        color = (0, 255, 0)
                        tag = "NON-SUSPICIOUS"
                else:
                    # Consistency-based suspiciousness logic
                    history = track_histories[track_id]
                    is_consistent = (
                        len(history) == consistency_limit and
                        all(h == label for h in history)
                    )

                    if is_consistent:
                        if label in red_actions:
                            color = (0, 0, 255)
                            tag = "HIGHLY SUSPICIOUS"
                        elif label in orange_actions:
                            color = (0, 255, 255)
                            tag = "MODERATELY SUSPICIOUS"
                        elif label in green_actions:
                            color = (0, 255, 0)
                            tag = "NON-SUSPICIOUS"
                        else:
                            color = (0, 255, 0)
                            tag = "NON-SUSPICIOUS"
                    else:
                        color = (0, 255, 0)
                        tag = "NON-SUSPICIOUS"

                color_label_map[frame_idx][track_id] = (color, tag)

        current_idx = int(self.current_frame_index)

        if (
            self.main_window.suspicious_movements_option_export.isChecked()
        ):
            return color_label_map[current_idx] if current_idx < len(color_label_map) else {}
        else:
            if current_idx < len(combined_results):
                return {
                    track_id: ((0, 255, 0), "")  # All green
                    for track_id in combined_results[current_idx].keys()
                }
            else:
                return {}
            
            
    def drawing_bounding_box(self, video_frame, results, colors_actions):

        for track_id, bbox in results.items():
            x1, y1, x2, y2 = bbox
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            bbox_width = x2 - x1
            bbox_height = y2 - y1

            # Font and offset scaling
            font_scale = max(0.5, bbox_width / 300)
            thickness = max(1, int(bbox_width / 150))
            offset_y = int(bbox_height * 0.10)
            offset_x = int(bbox_width * 0.05)
            text_position = (x1, y1 + offset_y)

            # Get color and suspicion label
            color, suspicion_label = colors_actions.get(track_id, ((0, 255, 0), ""))

            label = f"Student ID: {track_id}"
            if suspicion_label:
                label += f" | {suspicion_label}"


            cv2.putText(video_frame, label, text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255,255,255), int(thickness + (thickness * 0.5)))
            cv2.rectangle(video_frame, (x1, y1), (x2, y2), color, 5)

        return video_frame

    
    def drawing_keypoints(self, keypoints_dict, detection, video_frame):
        for track_id in keypoints_dict:
            if track_id in detection:
                keypoints = keypoints_dict[track_id]
                bbox = detection[track_id]
                bbox_x, bbox_y, bbox_w, bbox_h = bbox

                video_cropped_frame = video_frame[int(bbox_y):int(bbox_h), int(bbox_x):int(bbox_w)]

                for keypoint in keypoints:
                    x = int(keypoint[0] * video_cropped_frame.shape[1])
                    y = int(keypoint[1] * video_cropped_frame.shape[0])
                    cv2.circle(video_cropped_frame, (x, y), radius=4, color=(0, 255, 0), thickness=-1)
                    cv2.circle(video_cropped_frame, (x, y), radius=4, color=(0, 255, 0), thickness=-1)

                # Draw skeleton
                for pair in self.skeleton_pairs:
                    if pair[0] < len(keypoints) and pair[1] < len(keypoints):
                        pt1 = keypoints[pair[0]]
                        pt2 = keypoints[pair[1]]
                        #print(f"pt1: {pt1}, pt2: {pt2}")
                        # # Debug statement
                        if isinstance(pt1, np.ndarray) and isinstance(pt2, np.ndarray):
                            x1 = int(pt1[0] * video_cropped_frame.shape[1])
                            y1 = int(pt1[1] * video_cropped_frame.shape[0])
                            x2 = int(pt2[0] * video_cropped_frame.shape[1])
                            y2 = int(pt2[1] * video_cropped_frame.shape[0])
                            
                            if 0.1 <= x1 < video_cropped_frame.shape[1] and 0.1 <= y1 < video_cropped_frame.shape[0] and 0.1 <= x2 < video_cropped_frame.shape[1] and 0.1 <= y2 < video_cropped_frame.shape[0]:
                                cv2.line(video_cropped_frame, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)
                                cv2.line(video_cropped_frame, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)
                        else:
                            print(f"Invalid keypoints for track ID {track_id}: pt1={pt1}, pt2={pt2}")
                    else:
                        print(f"Keypoints array too small for track ID {track_id}: {keypoints}")

                # Place the cropped frame back into the original frame

                video_frame[int(bbox_y):int(bbox_h), int(bbox_x):int(bbox_w)] = video_cropped_frame
        
        return video_frame

    def extend_frame_width(self, frame: np.ndarray, extension: int = 300) -> np.ndarray:

        if len(frame.shape) == 3:
            height, width, channels = frame.shape  # RGB frame
        elif len(frame.shape) == 2:
            height, width = frame.shape  # Grayscale frame
            channels = None
        else:
            raise ValueError("Unexpected frame shape! Only 2D or 3D frames are supported.")

        # Create a new black frame with extended width
        new_width = width + (2 * extension)

        if channels is None:  # Grayscale
            extended_frame = np.zeros((height, new_width), dtype=np.uint8)
            # Place the grayscale frame in the center
            extended_frame[:, extension:extension + width] = frame
        else:  # RGB
            extended_frame = np.zeros((height, new_width, channels), dtype=np.uint8)
            # Place the RGB frame in the center
            extended_frame[:, extension:extension + width, :] = frame

        return extended_frame
    
    def preload_frames(self):
        results = None
        keypoints = None

        front_video_results = self.main_window.human_detect_results_front
        front_video_keypoints = self.main_window.human_pose_results_front
        front_video_actions = self.main_window.action_results_list_front

        center_video_results = self.main_window.human_detect_results_center
        center_video_keypoints = self.main_window.human_pose_results_center
        center_video_actions = self.main_window.action_results_list_center
        
        #Frame Versions

        while self.running:
            if not self.paused and (not self.center_video_frame_queue.full()):
                front_ret, front_frame = self.front_cap.read()
                center_ret, center_frame = self.center_cap.read()
                
                if not front_ret or not center_ret:
                    break
                
                front_frame = self.extend_frame_width(frame=front_frame)
                center_frame = self.extend_frame_width(frame=center_frame)
                
                color_labels = self.get_colors_actions_from_tracker()
                
                #Drawing Bounding Box using Original Processed Frame
                if self.main_window.both_front_and_center_video_button.isChecked() or self.main_window.center_video_only_radio_button.isChecked():
                    if self.main_window.add_bounding_box_check_box.isChecked():
                        center_frame = self.drawing_bounding_box(video_frame=center_frame,
                                                                    results=center_video_results[int(self.current_frame_index)],
                                                                    colors_actions=color_labels)
                        
                    #Drawing Keypoints using Original Processed Frame
                    if self.main_window.add_keypoints_check_box.isChecked():
                        center_frame = self.drawing_keypoints(keypoints_dict=center_video_keypoints[int(self.current_frame_index)],
                                                                    detection=center_video_results[int(self.current_frame_index)],
                                                                    video_frame= center_frame)
                    
                    center_frame = self.write_action_text(frame=center_frame,
                                                                            detections=self.main_window.human_detect_results_center[int(self.current_frame_index)],
                                                                            actions=self.main_window.action_results_list_center[int(self.current_frame_index)],
                                                                            head_postures_list=self.main_window.head_postures_list_center[int(self.current_frame_index)],
                                                                            arm_postures_list=self.main_window.arms_postures_list_center[int(self.current_frame_index)]
                                                                            )
                    
                    
                    
                    
                    

                if self.main_window.both_front_and_center_video_button.isChecked() or self.main_window.front_video_only_radio_button.isChecked():
                    #Drawing Bounding Box using Original Processed Frame
                    if self.main_window.add_bounding_box_check_box.isChecked():
                        front_frame = self.drawing_bounding_box(video_frame=front_frame,
                                                                    results=front_video_results[int(self.current_frame_index)],
                                                                    colors_actions=color_labels)
                    

                    #Drawing Keypoints using Original Processed Frame
                    if self.main_window.add_keypoints_check_box.isChecked():
                        front_frame = self.drawing_keypoints(keypoints_dict=front_video_keypoints[int(self.current_frame_index)],
                                                                    detection=front_video_results[int(self.current_frame_index)],
                                                                    video_frame= front_frame)
                    
                    front_frame = self.write_action_text(frame=front_frame,
                                                                            detections=self.main_window.human_detect_results_front[int(self.current_frame_index)],
                                                                            actions=self.main_window.action_results_list_front[int(self.current_frame_index)],
                                                                            head_postures_list=self.main_window.head_postures_list_front[int(self.current_frame_index)],
                                                                            arm_postures_list=self.main_window.arms_postures_list_front[int(self.current_frame_index)]
                                                                            )
                    
                
                self.front_video_frame_queue.put(front_frame)
                self.center_video_frame_queue.put(center_frame)
                self.current_frame_index += 1
                self.target_frame_index +=1

        self.center_cap.release()
        self.front_cap.release()


    def update_progress_bar(self, percentage):
        QMetaObject.invokeMethod(
            self.main_window.export_progress_bar,
            "setValue",
            Qt.QueuedConnection,
            Q_ARG(int, percentage)
        )

    def run(self):
        '''Main playback loop, sending frames from queue to UI'''
        frames_written = 0
        total_frames = self.main_window.max_frames

        while self.running:
            wrote_frame = False

            if self.main_window.both_front_and_center_video_button.isChecked() or self.main_window.front_video_only_radio_button.isChecked():
                try:
                    front_video_frame = self.front_video_frame_queue.get(timeout=1)
                    if front_video_frame is not None:  # Check if frame is None
                        cropped_front_video_frame = front_video_frame[0:1080, 300:2220]
                        if self.front_video_writer.isOpened():
                            
                            self.front_video_writer.write(cropped_front_video_frame)
                            print("SAVING FRONT VIDEO!!!") #Corrected typo
                            wrote_frame = True
                except queue.Empty:
                    pass

            if self.main_window.both_front_and_center_video_button.isChecked() or self.main_window.center_video_only_radio_button.isChecked():
                try:
                    center_video_frame = self.center_video_frame_queue.get(timeout=1)
                    if center_video_frame is not None: # Check if frame is None
                        cropped_center_video_frame = center_video_frame[0:1080, 300:2220]
                        if self.center_video_writer.isOpened():
                            print("SAVING CENTER VIDEO!!!") #Corrected typo
                            self.center_video_writer.write(cropped_center_video_frame)
                            wrote_frame = True
                except queue.Empty:
                    pass

            if wrote_frame:
                frames_written += 1
                percentage = int((frames_written / total_frames) * 100)
                self.update_progress_bar(percentage)
                
        self.front_video_writer.release()
        self.center_video_writer.release()
        self.center_cap.release()
        self.front_cap.release()
        self.status_signal.emit(True)

        
        # self.running = False
        # self.stop()
        

    def stop(self):
        '''Stops video playback and terminates threads.'''
        self.running = False  # Stop preload loop
        self.quit()
        self.wait()
        if self.preload_thread.is_alive():
            self.preload_thread.join()  # Ensure the thread exits cleanly

        self.center_cap.release()
        self.front_cap.release()


    def pause(self, status):
        self.paused = status
