import cv2

from PySide6.QtGui import QIcon
from PySide6.QtCore import QThread, Signal
import numpy as np
import queue
import threading
from pathlib import Path
from collections import defaultdict

cv2.setNumThreads(0)
cv2.ocl.setUseOpenCL(False)

class VideoPlayerThread(QThread):
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

    #cv2.setNumThreads(1)  # Disable OpenCV multi-threading to reduce CPU usage

    def __init__(self, center_video_path, front_video_path, main_window, slider, has_actions, keypoints_check_box_front, bounding_box_check_point_front,
                 keypoints_check_box_center, bounding_box_check_point_center, is_advanced_analytics):
        
        super().__init__()

        self.main_window = main_window
        self.slider = slider
        self.center_video_path = center_video_path
        self.front_video_path = front_video_path
        self.has_actions = has_actions
        self.keypoints_check_box_front = keypoints_check_box_front
        self.keypoints_check_box_center = keypoints_check_box_center
        self.bounding_box_check_point_front = bounding_box_check_point_front
        self.bounding_box_check_point_center = bounding_box_check_point_center
        self.is_advanced_analytics = is_advanced_analytics
        
        #Separate captures for each video

        self.center_cap = cv2.VideoCapture(self.center_video_path)
        self.front_cap = cv2.VideoCapture(self.front_video_path)

        #For all
        self.running = True
        self.paused = False

        self.max_size = 10
        #Keep preloaded frames here

        self.center_video_frame_queue = queue.Queue(maxsize=self.max_size)  
        self.center_video_black_frame_queue = queue.Queue(maxsize=self.max_size) 
        self.front_video_frame_queue = queue.Queue(maxsize=self.max_size)  
        self.front_video_black_frame_queue = queue.Queue(maxsize=self.max_size)  

        self.current_center_video_frame_index = 0
        self.current_front_video_frame_index = 0
        self.current_frame_index = 0

        self.target_frame_index = 0 # Set target frame index
        self.preload_thread = threading.Thread(target=self.preload_frames, daemon=True)
        

        self.skeleton_pairs = [
            (0, 1), (0, 2), (1, 3), (2, 4), (0, 5), (0, 6), (5, 6), 
            (5, 7), (6, 8), (7, 9), (8, 10), (5, 11), (6, 12), (11, 12), 
            (11, 13), (12, 14), (13, 15), (14, 16)
        ]

        self.isFirstFrame =True
        
        
        # One-time initialization outside the loop
        self.action_tracker = defaultdict(lambda: {
            'current_action': None,
            'streak': 0,
            'total_count': 0,
            'last_frame_seen': -1,
            'is_suspicious': False
        })

        # Define suspicious behavior criteria — you can later make this dynamic using your PySide6 table
        self.suspicious_criteria = self.main_window.suspicious_criteria

    
    def update_action_status(self, current_frame_number, frame_action_dict, criteria):
        for track_id, action in frame_action_dict.items():
            tracker = self.action_tracker[track_id]

            if action == criteria['action_name']:
                if tracker['current_action'] == action:
                    tracker['streak'] += 1
                else:
                    tracker['current_action'] = action
                    tracker['streak'] = 1

                tracker['total_count'] += 1
            else:
                tracker['current_action'] = action
                tracker['streak'] = 1 if action else 0

            # Check if criteria is met
            if (tracker['total_count'] >= criteria['frequency'] and 
                tracker['streak'] >= criteria['interval_frequency']):
                tracker['is_suspicious'] = True
            else:
                tracker['is_suspicious'] = False

    def get_colors_actions_from_tracker(self):
        red_actions = self.suspicious_criteria.get('red_actions', [])
        orange_actions = self.suspicious_criteria.get('orange_actions', [])
        green_actions = self.suspicious_criteria.get('green_actions', [])
        min_consistent_frames = self.suspicious_criteria.get('min_consistent_frames', {})
        repetition_thresholds = self.suspicious_criteria.get('repetition_thresholds', {})
        repetition_interval = self.suspicious_criteria.get('repetition_interval', 15)

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
                track_histories.setdefault(track_id, {})
                track_counts.setdefault(track_id, {})
                track_last_occurrence.setdefault(track_id, {})

                if isinstance(data, dict) and self.is_advanced_analytics:
                    labels = [
                        data.get('left_arm_posture'),
                        data.get('right_arm_posture'),
                        data.get('head_posture')
                    ]
                    labels = [label for label in labels if label]
                else:
                    labels = [data if isinstance(data, str) else 'UNKNOWN']

                color_counts = {'green': 0, 'orange': 0, 'red': 0}
                for label in labels:
                    # History tracking per label
                    track_histories[track_id].setdefault(label, [])
                    history = track_histories[track_id][label]
                    history.append(label)
                    consistency_limit = min_consistent_frames.get(label, 1)
                    if len(history) > consistency_limit:
                        history.pop(0)

                    is_consistent = len(history) == consistency_limit and all(h == label for h in history)

                    if label in repetition_thresholds:
                        last_frame = track_last_occurrence[track_id].get(label, -repetition_interval - 1)
                        if frame_idx - last_frame >= repetition_interval:
                            track_counts[track_id][label] = track_counts[track_id].get(label, 0) + 1
                            track_last_occurrence[track_id][label] = frame_idx

                        rep_count = track_counts[track_id].get(label, 0)
                        max_allowed = repetition_thresholds[label]

                        if rep_count > max_allowed:
                            color_counts['red'] += 1
                        elif 0 < rep_count <= max_allowed:
                            color_counts['orange'] += 1
                        else:
                            color_counts['green'] += 1
                    else:
                        if is_consistent:
                            if label in red_actions:
                                color_counts['red'] += 1
                            elif label in orange_actions:
                                color_counts['orange'] += 1
                            elif label in green_actions:
                                color_counts['green'] += 1
                            else:
                                color_counts['green'] += 1
                        else:
                            color_counts['green'] += 1

                # Determine majority or priority
                if color_counts['red'] >= 2 or (color_counts['red'] == 1 and color_counts['orange'] == 1 and color_counts['green'] == 1):
                    color = (0, 0, 255)
                    tag = "HIGHLY SUSPICIOUS"
                elif color_counts['orange'] >= 2:
                    color = (0, 255, 255)
                    tag = "MODERATELY SUSPICIOUS"
                elif color_counts['green'] >= 2:
                    color = (0, 255, 0)
                    tag = "NON-SUSPICIOUS"
                else:
                    if color_counts['red']:
                        color = (0, 0, 255)
                        tag = "HIGHLY SUSPICIOUS"
                    elif color_counts['orange']:
                        color = (0, 255, 255)
                        tag = "MODERATELY SUSPICIOUS"
                    else:
                        color = (0, 255, 0)
                        tag = "NON-SUSPICIOUS"

                color_label_map[frame_idx][track_id] = (color, tag)

        current_idx = int(self.current_frame_index)

        if (
            self.main_window.identify_suspicious_check_box_line_graph_advanced_analytics.isChecked() or
            self.main_window.identify_suspicious_check_box_line_graph_ai_analytics.isChecked()
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



    def write_action_text(self, frame, black_frame, detections, actions, head_postures_list,
                        arm_postures_list):
        '''
        Draw bounding boxes with action labels on each frame.
        '''
        if self.has_actions:
            if self.is_advanced_analytics:
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
                    cv2.putText(frame, head_posture, head_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255,255,255), int(thickness + (thickness * 0.5)))
                    cv2.putText(black_frame, head_posture, head_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (0, 255, 0), int(thickness + (thickness * 0.5)))
                    
                    #For Left Arm Posture
                    cv2.putText(frame, left_arm_posture, left_arm_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255,255,255), int(thickness + (thickness * 0.5)))
                    cv2.putText(black_frame, left_arm_posture, left_arm_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255,255,255), int(thickness + (thickness * 0.5)))
                    
                    #For Right Arm Postures
                    cv2.putText(frame, right_arm_posture, right_arm_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255,255,255), int(thickness + (thickness * 0.5)))
                    cv2.putText(black_frame, right_arm_posture, right_arm_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255,255,255), int(thickness + (thickness * 0.5)))

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
                    cv2.putText(frame, action_text, text_position, cv2.FONT_HERSHEY_SIMPLEX,font_scale, (255, 255, 255), int(thickness + (thickness * 0.5)))
                    cv2.putText(black_frame, action_text, text_position, cv2.FONT_HERSHEY_SIMPLEX,font_scale, (255, 255, 255), int(thickness + (thickness * 0.5)))
                
            return frame, black_frame
    
    def drawing_bounding_box(self, video_frame, results, colors_actions):
        black_frame = np.zeros((1080, 2520, 3), dtype=np.uint8)

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

            # Draw on both frames
            for frame in (video_frame, black_frame):
                cv2.putText(frame, label, text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255,255,255), int(thickness + (thickness * 0.5)))
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 5)

        return video_frame, black_frame
  
    def drawing_keypoints(self, keypoints_dict, detection, black_frame, video_frame):
        for track_id in keypoints_dict:
            if track_id in detection:
                keypoints = keypoints_dict[track_id]
                bbox = detection[track_id]
                bbox_x, bbox_y, bbox_w, bbox_h = bbox

                cropped_frame = black_frame[int(bbox_y):int(bbox_h), int(bbox_x):int(bbox_w)]
                video_cropped_frame = video_frame[int(bbox_y):int(bbox_h), int(bbox_x):int(bbox_w)]

                for keypoint in keypoints:
                    x = int(keypoint[0] * cropped_frame.shape[1])
                    y = int(keypoint[1] * cropped_frame.shape[0])
                    cv2.circle(cropped_frame, (x, y), radius=4, color=(0, 255, 0), thickness=-1)
                    cv2.circle(video_cropped_frame, (x, y), radius=4, color=(0, 255, 0), thickness=-1)

                # Draw skeleton
                for pair in self.skeleton_pairs:
                    if pair[0] < len(keypoints) and pair[1] < len(keypoints):
                        pt1 = keypoints[pair[0]]
                        pt2 = keypoints[pair[1]]
                        #print(f"pt1: {pt1}, pt2: {pt2}")
                        # # Debug statement
                        if isinstance(pt1, np.ndarray) and isinstance(pt2, np.ndarray):
                            x1 = int(pt1[0] * cropped_frame.shape[1])
                            y1 = int(pt1[1] * cropped_frame.shape[0])
                            x2 = int(pt2[0] * cropped_frame.shape[1])
                            y2 = int(pt2[1] * cropped_frame.shape[0])
                            
                            if 0.1 <= x1 < cropped_frame.shape[1] and 0.1 <= y1 < cropped_frame.shape[0] and 0.1 <= x2 < cropped_frame.shape[1] and 0.1 <= y2 < cropped_frame.shape[0]:
                                cv2.line(cropped_frame, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)
                                cv2.line(video_cropped_frame, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)
                        else:
                            print(f"Invalid keypoints for track ID {track_id}: pt1={pt1}, pt2={pt2}")
                    else:
                        print(f"Keypoints array too small for track ID {track_id}: {keypoints}")

                # Place the cropped frame back into the original frame

                black_frame[int(bbox_y):int(bbox_h), int(bbox_x):int(bbox_w)] = cropped_frame
                video_frame[int(bbox_y):int(bbox_h), int(bbox_x):int(bbox_w)] = video_cropped_frame
        
        return video_frame, black_frame

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
    
    def merge_action_dicts(self, action_dict_front, action_dict_center):
        merged = {}

        all_track_ids = set(action_dict_front) | set(action_dict_center)

        for track_id in all_track_ids:
            action_front = action_dict_front.get(track_id)
            action_center = action_dict_center.get(track_id)

            if action_center and action_center != "None":
                merged[track_id] = action_center
            elif action_front and action_front != "None":
                merged[track_id] = action_front
            else:
                merged[track_id] = "None"

        return merged


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
                front_ret, retrieved_front_frame = self.front_cap.read()
                center_ret, retrieved_center_frame = self.center_cap.read()

                #CHECKLIST IF THERE IS STILL A FRAME BEFORE PROCEEDING
                if (not front_ret) or (not center_ret):
                    self.center_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Restart video if it ends
                    self.front_cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                    self.current_frame_index = 0
                    self.target_frame_index = 0 
                    continue

                front_frame = self.extend_frame_width(frame=retrieved_front_frame,
                                                      extension=300)
                
                center_frame = self.extend_frame_width(frame=retrieved_center_frame,
                                                       extension=300)
                # Draw bounding boxes and keypoints only for the current frame index


                min_value, max_value = self.slider.value()

                #Make sure that the videos are starting based on the set range sliders
                if self.isFirstFrame:
                    self.center_cap.set(cv2.CAP_PROP_POS_FRAMES, min_value)
                    self.front_cap.set(cv2.CAP_PROP_POS_FRAMES, min_value)
                    self.current_frame_index = min_value
                    self.target_frame_index = min_value
                    self.isFirstFrame = False

                if (not front_ret) or (self.current_frame_index > (max_value-1)):
                    self.center_cap.set(cv2.CAP_PROP_POS_FRAMES, min_value)  # Restart video if it ends
                    self.front_cap.set(cv2.CAP_PROP_POS_FRAMES, min_value)

                    self.isFirstFrame = True

                    self.current_frame_index = min_value
                    self.target_frame_index = min_value
                    continue

                if self.current_frame_index == self.target_frame_index:  # Draw only for target frame index #
                    
                    center_video_black_frame = np.zeros((1080, 2520, 3), dtype=np.uint8)
                    front_video_black_frame = np.zeros((1080, 2520, 3), dtype=np.uint8)
                    
                    
                    #Merge actions
                    # merged_action_frame_dict = self.merge_action_dicts(front_video_results[int(self.current_frame_index)], center_video_results[int(self.current_frame_index)])
                    
                    # self.update_action_status(self.current_frame_index, merged_action_frame_dict, self.suspicious_criteria)
                    

                    colors_actions = self.get_colors_actions_from_tracker()
                    
                    #Drawing Bounding Box using Original Processed Frame
                    if self.bounding_box_check_point_center.isChecked():
                        center_frame, center_video_black_frame = self.drawing_bounding_box(video_frame=center_frame,
                                                                    results=center_video_results[int(self.current_frame_index)], 
                                                                    colors_actions=colors_actions)
                    
                    
                    #Drawing Keypoints using Original Processed Frame
                    if self.keypoints_check_box_center.isChecked():
                        center_frame, center_video_black_frame = self.drawing_keypoints(keypoints_dict=center_video_keypoints[int(self.current_frame_index)],
                                                                    detection=center_video_results[int(self.current_frame_index)],
                                                                    black_frame= center_video_black_frame,
                                                                    video_frame= center_frame)


                    #Drawing Bounding Box using Original Processed Frame
                    if self.bounding_box_check_point_front.isChecked():
                        front_frame, front_video_black_frame = self.drawing_bounding_box(video_frame=front_frame,
                                                                    results=front_video_results[int(self.current_frame_index)],
                                                                    colors_actions=colors_actions)
                    

                    #Drawing Keypoints using Original Processed Frame
                    if self.keypoints_check_box_front.isChecked():
                        front_frame, front_video_black_frame = self.drawing_keypoints(keypoints_dict=front_video_keypoints[int(self.current_frame_index)],
                                                                    detection=front_video_results[int(self.current_frame_index)],
                                                                    black_frame= front_video_black_frame,
                                                                    video_frame= front_frame)
                    
                    if self.has_actions and self.bounding_box_check_point_front.isChecked():
                        front_frame, front_video_black_frame = self.write_action_text(frame=front_frame,
                                                                                        black_frame=front_video_black_frame,
                                                                                        detections=self.main_window.human_detect_results_front[int(self.current_frame_index)],
                                                                                        actions=self.main_window.action_results_list_front[int(self.current_frame_index)],
                                                                                        head_postures_list=self.main_window.head_postures_list_front[int(self.current_frame_index)],
                                                                                        arm_postures_list=self.main_window.arms_postures_list_front[int(self.current_frame_index)]
                                                                                        )

                    if self.has_actions and self.bounding_box_check_point_center.isChecked():       
                        center_frame, center_video_black_frame = self.write_action_text(frame=center_frame,
                                                                                    black_frame=center_video_black_frame,
                                                                                    detections=self.main_window.human_detect_results_center[int(self.current_frame_index)],
                                                                                    actions=self.main_window.action_results_list_center[int(self.current_frame_index)],
                                                                                    head_postures_list=self.main_window.head_postures_list_center[int(self.current_frame_index)],
                                                                                    arm_postures_list=self.main_window.arms_postures_list_center[int(self.current_frame_index)]
                                                                                    )

                else:
                    # If not the target frame, skip drawing\
                    center_frame = center_frame  # Just pass the frame unchanged
                    center_video_black_frame = center_video_black_frame  # Just pass the black_frame unchanged
                    front_frame = front_frame
                    front_video_black_frame = front_video_black_frame

                
                # Store the frame with the drawn bounding box and keypoints
                
                if center_frame is not None and center_video_black_frame is not None:
                    self.center_video_frame_queue.put(center_frame)
                    self.center_video_black_frame_queue.put(center_video_black_frame)

                if front_frame is not None and front_video_black_frame is not None:
                    self.front_video_frame_queue.put(front_frame)
                    self.front_video_black_frame_queue.put(front_video_black_frame)

                self.current_frame_index += 1
                self.target_frame_index +=1

        self.center_cap.release()
        self.front_cap.release()

    def run(self):
        self.preload_thread.start()  # Start background frame loader
        '''Main playback loop, sending frames from queue to UI'''
        while self.running:
            if not self.paused and not self.center_video_frame_queue.empty():
                
                center_video_frame = self.center_video_frame_queue.get()  # Get frame from queue
                center_black_frame = self.center_video_black_frame_queue.get()

                front_video_frame = self.front_video_frame_queue.get()  # Get frame from queue
                front_black_frame = self.front_video_black_frame_queue.get()
                
                self.frames_signal.emit([center_video_frame, front_video_frame, center_black_frame, front_black_frame])  # Send frame to UI
                self.current_frame_signal.emit(int(self.current_frame_index)-30)
                self.current_frame_index_signal.emit(int(self.current_frame_index))
                cv2.waitKey(1000//33)  # Play at ~30 FPS

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


class VideoPlayer_With_Heatmap_Thread(QThread):

    frames_signal = Signal(object)
    #cv2.setNumThreads(1)  # Disable OpenCV multi-threading to reduce CPU usage

    def __init__(self, center_video_path, front_video_path, main_window, slider, button, is_advanced_analytics,
                 keypoints_check_box_front, bounding_box_check_point_front, keypoints_check_box_center,
                 bounding_box_check_point_center):
        super().__init__()
        self.main_window = main_window
        self.slider = slider
        self.center_video_path = center_video_path
        self.front_video_path = front_video_path
        self.button = button
        self.is_advanced_analytics = is_advanced_analytics

        self.filtered_bboxes_front = self.main_window.filtered_action_results_bboxes_front
        self.filtered_bboxes_center = self.main_window.filtered_action_results_bboxes_center

        self.minimum_value = None
        self.maximum_value = None
        
        self.keypoints_check_box_front = keypoints_check_box_front
        self.keypoints_check_box_center = keypoints_check_box_center
        self.bounding_box_check_point_front = bounding_box_check_point_front
        self.bounding_box_check_point_center = bounding_box_check_point_center
        
        #Separate captures for each video

        self.center_cap = cv2.VideoCapture(self.center_video_path)
        self.front_cap = cv2.VideoCapture(self.front_video_path)

        #For all
        self.running = True
        self.paused = False

        self.max_size = 30

        #Keep preloaded frames here

        self.classroom_heatmap_frames_queue = queue.Queue(maxsize=self.max_size)

        self.original_center_video_frame_queue = queue.Queue(maxsize=self.max_size)  
        self.center_video_frame_queue = queue.Queue(maxsize=self.max_size)  
        self.center_video_black_frame_queue = queue.Queue(maxsize=self.max_size) 

        self.original_front_video_frame_queue = queue.Queue(maxsize=self.max_size)  
        self.front_video_frame_queue = queue.Queue(maxsize=self.max_size)  
        self.front_video_black_frame_queue = queue.Queue(maxsize=self.max_size)  

        self.current_center_video_frame_index = 0
        self.current_front_video_frame_index = 0
        self.current_frame_index = 0

        self.target_frame_index = 0 # Set target frame index
        self.preload_thread = threading.Thread(target=self.preload_frames, daemon=True)
        self.preload_thread.start()  # Start background frame loader

        #For getting the seatplan image hehe
        
        
        self.script_dir = Path(__file__).parent  # Get script's folder
        self.image_path = self.script_dir.parent / "assets" / "SEAT_PLAN.png"
        self.seat_plan_picture = cv2.imread(self.image_path)
        self.seat_plan_picture_previous_frame = None
        
        script_dir_2 = Path(__file__).parent  # Get script's folder
        image_path_2 = script_dir_2.parent / "assets" / "SEAT_PLAN_SUSPICIONS.png"
        self.seat_plan_picture_suspicious = cv2.imread(image_path_2)
        
        self.isFirstFrame =True

        self.skeleton_pairs = [
            (0, 1), (0, 2), (1, 3), (2, 4), (0, 5), (0, 6), (5, 6), 
            (5, 7), (6, 8), (7, 9), (8, 10), (5, 11), (6, 12), (11, 12), 
            (11, 13), (12, 14), (13, 15), (14, 16)
        ]

        # Define 4 corresponding points from the center video frame to the heatmap

        self.src_pts_center = np.array([
                            [668,193],  # Top-left
                            [1843,194],  # Top-right
                            [197,638],  # Bottom-left
                            [2348,649]   # Bottom-right
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
                            [478,97],  # Top-left
                            [2168,63],  # Top-right
                            [6,965],  # Bottom-left
                            [2491,973]   # Bottom-right
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
        self.center_video_black_frame = np.zeros((1080, 2520, 3), dtype=np.uint8)
        self.front_video_black_frame = np.zeros((1080, 2520, 3), dtype=np.uint8)
        self.suspicious_criteria = self.main_window.suspicious_criteria
        
        self.label_color_map = {
                                    "Highly Suspicious": (255, 0, 0),
                                    "Moderately Suspicious": (255, 165, 0),
                                    "Non-Suspicious": (0, 255, 0),
                                    "UNKNOWN": (255, 255, 255)
                                }




    def write_action_text(self, frame, black_frame, detections, actions, head_postures_list,
                        arm_postures_list):
        '''
        Draw bounding boxes with action labels on each frame.
        '''

        if self.is_advanced_analytics:
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
                cv2.putText(frame, head_posture, head_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), int(thickness + (thickness * 0.5)))
                cv2.putText(black_frame, head_posture, head_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), int(thickness + (thickness * 0.5)))
                
                #For Left Arm Posture
                cv2.putText(frame, left_arm_posture, left_arm_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 0), int(thickness + (thickness * 0.5)))
                cv2.putText(black_frame, left_arm_posture, left_arm_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), int(thickness + (thickness * 0.5)))
                
                #For Right Arm Postures
                cv2.putText(frame, right_arm_posture, right_arm_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), int(thickness + (thickness * 0.5)))
                cv2.putText(black_frame, right_arm_posture, right_arm_text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255, 255, 255), int(thickness + (thickness * 0.5)))

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
                cv2.putText(frame, action_text, text_position, cv2.FONT_HERSHEY_SIMPLEX,font_scale, (255,255,255), int(thickness + (thickness * 0.5)))
                cv2.putText(black_frame, action_text, text_position, cv2.FONT_HERSHEY_SIMPLEX,font_scale, (255, 255, 255), int(thickness + (thickness * 0.5)))
            
        return frame, black_frame


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
                        tag = f"HIGHLY SUSPICIOUS {rep_count}x"
                    elif 0 < rep_count <= max_allowed:
                        color = (0, 255, 255)    # Orange
                        tag = f"LIMITED {rep_count}x"
                    else:
                        color = (0, 255, 0)
                        tag = ""
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
                            tag = "TO REVIEW"
                        elif label in green_actions:
                            color = (0, 255, 0)
                            tag = ""
                        else:
                            color = (0, 255, 0)
                            tag = ""
                    else:
                        color = (0, 255, 0)
                        tag = ""

                color_label_map[frame_idx][track_id] = (color, tag)

        current_idx = int(self.current_frame_index)

        if (
            self.main_window.identify_suspicious_check_box_heatmap_advanced_analytics.isChecked() or
            self.main_window.identify_suspicious_check_box_heatmap_ai_analytics.isChecked()
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
        black_frame = np.zeros((1080, 2520, 3), dtype=np.uint8)

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

            # Draw on both frames
            for frame in (video_frame, black_frame):
                cv2.putText(frame, label, text_position, cv2.FONT_HERSHEY_SIMPLEX, font_scale, (255,255,255), int(thickness + (thickness * 0.5)))
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 5)

        return video_frame, black_frame
    
    def drawing_keypoints(self, keypoints_dict, detection, black_frame, video_frame):
        for track_id in keypoints_dict:
            if track_id in detection:
                keypoints = keypoints_dict[track_id]
                bbox = detection[track_id]
                bbox_x, bbox_y, bbox_w, bbox_h = bbox

                cropped_frame = black_frame[int(bbox_y):int(bbox_h), int(bbox_x):int(bbox_w)]
                video_cropped_frame = video_frame[int(bbox_y):int(bbox_h), int(bbox_x):int(bbox_w)]

                for keypoint in keypoints:
                    x = int(keypoint[0] * cropped_frame.shape[1])
                    y = int(keypoint[1] * cropped_frame.shape[0])
                    cv2.circle(cropped_frame, (x, y), radius=4, color=(0, 255, 0), thickness=-1)
                    cv2.circle(video_cropped_frame, (x, y), radius=4, color=(0, 255, 0), thickness=-1)

                # Draw skeleton
                for pair in self.skeleton_pairs:
                    if pair[0] < len(keypoints) and pair[1] < len(keypoints):
                        pt1 = keypoints[pair[0]]
                        pt2 = keypoints[pair[1]]
                        #print(f"pt1: {pt1}, pt2: {pt2}")
                        # # Debug statement
                        if isinstance(pt1, np.ndarray) and isinstance(pt2, np.ndarray):
                            x1 = int(pt1[0] * cropped_frame.shape[1])
                            y1 = int(pt1[1] * cropped_frame.shape[0])
                            x2 = int(pt2[0] * cropped_frame.shape[1])
                            y2 = int(pt2[1] * cropped_frame.shape[0])
                            
                            if 0.1 <= x1 < cropped_frame.shape[1] and 0.1 <= y1 < cropped_frame.shape[0] and 0.1 <= x2 < cropped_frame.shape[1] and 0.1 <= y2 < cropped_frame.shape[0]:
                                cv2.line(cropped_frame, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)
                                cv2.line(video_cropped_frame, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)
                        else:
                            print(f"Invalid keypoints for track ID {track_id}: pt1={pt1}, pt2={pt2}")
                    else:
                        print(f"Keypoints array too small for track ID {track_id}: {keypoints}")

                # Place the cropped frame back into the original frame

                black_frame[int(bbox_y):int(bbox_h), int(bbox_x):int(bbox_w)] = cropped_frame
                video_frame[int(bbox_y):int(bbox_h), int(bbox_x):int(bbox_w)] = video_cropped_frame
        
        return video_frame, black_frame
    
     #Helper Method
    def draw_heat_circle(self, bbox, label, homography_matrix, radius, custom_color=None):
        color = custom_color if custom_color else self.action_colors.get(label, (255, 255, 255))
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

    
    # Main Heatmap Drawing Function
    def drawing_classroom_heatmap(self, frame, results_front, results_center, 
                            actions_front=None, actions_center=None,
                            head_posture_front=None, head_posture_center=None,
                            arm_posture_front=None, arm_posture_center=None):
        """
        Draws a heatmap with action-specific gradient circles or suspiciousness-based colors.
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
        
        # 🔹 Get suspiciousness-based color labels if checkbox is checked
        use_suspicious_mode = self.main_window.identify_suspicious_check_box_heatmap_ai_analytics.isChecked() or self.main_window.identify_suspicious_check_box_heatmap_advanced_analytics.isChecked()
        
        
        if self.isFirstFrame:
            self.heatmap_image = self.seat_plan_picture.copy()
            self.isFirstFrame = False
        else:
            self.heatmap_image = frame.copy()

        radius = 50

        

        
        suspicious_colors = self.get_colors_actions_from_tracker() if use_suspicious_mode else {}

        # 🔹 Process both camera results
        for camera_label, data in label_map.items():
            results = data["results"]
            actions = data[selected_label_type]
            homography_matrix = data["homography"]

            if not results or not actions:
                continue

            for track_id, bbox in results.items():
                if not isinstance(bbox, (list, tuple)) or len(bbox) != 4:
                    continue

                action = actions.get(track_id, "UNKNOWN")

                if isinstance(action, dict):  # For arm_posture with left/right
                    for arm_side, label in action.items():
                        custom_color = suspicious_colors.get(track_id, (self.action_colors.get(label, (255, 255, 255)), ""))[0] if use_suspicious_mode else None
                        self.draw_heat_circle(bbox, label, homography_matrix, radius, custom_color)
                else:
                    custom_color = suspicious_colors.get(track_id, (self.action_colors.get(action, (255, 255, 255)), ""))[0] if use_suspicious_mode else None
                    self.draw_heat_circle(bbox, action, homography_matrix, radius, custom_color)

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
        # Ensure color is a tuple of 3 elements
        if isinstance(color, (list, np.ndarray)):
            color = tuple(color)
        elif isinstance(color, int):
            color = (color, color, color)  # Assume grayscale if int is given

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

    def extend_frame_width(self,frame: np.ndarray, extension: int = 300) -> np.ndarray:
        height, width, channels = frame.shape
        

        if width != 1920 or height != 1080:
            raise ValueError("Expected a 1920x1080 frame.")
        

        new_width = width + (2 * extension)
        extended_frame = np.zeros((height, new_width, channels), dtype=np.uint8)
        

        extended_frame[:, extension:extension + width] = frame
        
        return extended_frame

    def preload_frames(self):

        front_video_keypoints = self.main_window.human_pose_results_front
        center_video_keypoints = self.main_window.human_pose_results_center
        
        front_video_results = self.main_window.filtered_action_results_bboxes_front
        center_video_results = self.main_window.filtered_action_results_bboxes_center
        
        front_video_actions = self.main_window.filtered_action_results_list_front
        center_video_actions = self.main_window.filtered_action_results_list_center
        
        front_video_head_postures = self.main_window.filtered_head_postures_list_front
        center_video_head_postures = self.main_window.filtered_head_postures_list_center
        
        front_video_arm_postures = self.main_window.filtered_arms_postures_list_front
        center_video_arm_postures = self.main_window.filtered_arms_postures_list_center
        
        min_value, max_value = self.slider.value()
        
        self.minimum_value, self.maximum_value = min_value, max_value
        
        """
        Background thread to keep decoding frames ahead of playback
        """
        
        while self.running:
            if not self.paused and (not self.center_video_frame_queue.full()):
                front_ret, retrieved_front_frame = self.front_cap.read()
                center_ret, retrieved_center_frame = self.center_cap.read()

                min_value, max_value = self.slider.value()
                center_video_black_frame = np.zeros((1080, 2520, 3), dtype=np.uint8)
                front_video_black_frame = np.zeros((1080, 2520, 3), dtype=np.uint8)
                
                # 🔹 Get suspiciousness-based color labels if checkbox is checked
                use_suspicious_mode = self.main_window.identify_suspicious_check_box_heatmap_ai_analytics.isChecked() or self.main_window.identify_suspicious_check_box_heatmap_advanced_analytics.isChecked()
                
                if use_suspicious_mode:
                    self.seat_plan_picture = self.seat_plan_picture_suspicious
                else:
                    self.seat_plan_picture = cv2.imread(self.image_path)
                
                #Make sure that the videos are starting based on the set range sliders
                if self.isFirstFrame:
                    self.center_cap.set(cv2.CAP_PROP_POS_FRAMES, min_value)
                    self.front_cap.set(cv2.CAP_PROP_POS_FRAMES, min_value)
                    self.isFirstFrame = False
                    self.seat_plan_picture_previous_frame = self.seat_plan_picture.copy()
                    self.current_frame_index = min_value
                    self.target_frame_index = min_value

                if (not front_ret) or (not center_ret) or (self.current_frame_index > (max_value-1)):
                    self.center_cap.set(cv2.CAP_PROP_POS_FRAMES, min_value)  # Restart video if it ends
                    self.front_cap.set(cv2.CAP_PROP_POS_FRAMES, min_value)

                    self.seat_plan_picture_previous_frame = self.seat_plan_picture.copy()
                    self.isFirstFrame = True

                    self.current_frame_index = min_value
                    self.target_frame_index = min_value
                    continue
                
                
                # Draw bounding boxes and keypoints only for the current frame index
                front_frame = self.extend_frame_width(frame=retrieved_front_frame,
                                                      extension=300)
                
                center_frame = self.extend_frame_width(frame=retrieved_center_frame,
                                                       extension=300)
                
                
                
                if self.current_frame_index == self.target_frame_index:  # Draw only for target frame index #
                    
                    color_actions = self.get_colors_actions_from_tracker()
                    
                    if self.bounding_box_check_point_center.isChecked():
                        center_frame, center_video_black_frame = self.drawing_bounding_box(video_frame=center_frame,
                                                                    results=self.main_window.filtered_action_results_bboxes_center[int(self.current_frame_index)],
                                                                    colors_actions=color_actions)
                        
                        if self.is_advanced_analytics:
                            center_frame, center_video_black_frame = self.write_action_text(frame=center_frame,
                                                                                            black_frame=center_video_black_frame,
                                                                                            detections=self.main_window.filtered_action_results_bboxes_center[int(self.current_frame_index)],
                                                                                            actions=None,
                                                                                            head_postures_list=self.main_window.filtered_head_postures_list_center[int(self.current_frame_index)],
                                                                                            arm_postures_list=self.main_window.filtered_arms_postures_list_center[int(self.current_frame_index)]
                                                                                            )
                        else:
                            center_frame, center_video_black_frame = self.write_action_text(frame=center_frame,
                                                                                            black_frame=center_video_black_frame,
                                                                                            detections=self.main_window.filtered_action_results_bboxes_center[int(self.current_frame_index)],
                                                                                            actions=self.main_window.filtered_action_results_list_center[int(self.current_frame_index)],
                                                                                            head_postures_list=None,
                                                                                            arm_postures_list=None
                                                                                            )
                        
                    if self.keypoints_check_box_center.isChecked():
                        center_frame, center_video_black_frame = self.drawing_keypoints(keypoints_dict=center_video_keypoints[int(self.current_frame_index)],
                                                                    detection=center_video_results[int(self.current_frame_index)],
                                                                    black_frame=center_video_black_frame,
                                                                    video_frame=center_frame)
                    
                    if self.bounding_box_check_point_front.isChecked():
                        front_frame, front_video_black_frame = self.drawing_bounding_box(video_frame=front_frame,
                                                                    results=self.main_window.filtered_action_results_bboxes_front[int(self.current_frame_index)],
                                                                    colors_actions=color_actions)
                        
                        if self.is_advanced_analytics:
                            front_frame, front_video_black_frame = self.write_action_text(frame=front_frame,
                                                                                        black_frame=front_video_black_frame,
                                                                                        detections=self.main_window.filtered_action_results_bboxes_front[int(self.current_frame_index)],
                                                                                        actions=None,
                                                                                        head_postures_list=front_video_head_postures[int(self.current_frame_index)],
                                                                                        arm_postures_list=front_video_arm_postures[int(self.current_frame_index)])
                        else:
                            front_frame, front_video_black_frame = self.write_action_text(frame=front_frame,
                                                                                        black_frame=front_video_black_frame,
                                                                                        detections=self.main_window.filtered_action_results_bboxes_front[int(self.current_frame_index)],
                                                                                        actions=front_video_actions[int(self.current_frame_index)],
                                                                                        head_postures_list=None,
                                                                                        arm_postures_list=None)
                    
                        
                    if self.keypoints_check_box_front.isChecked():
                        front_frame, front_video_black_frame = self.drawing_keypoints(keypoints_dict=front_video_keypoints[int(self.current_frame_index)],
                                                                    detection=front_video_results[int(self.current_frame_index)],
                                                                    black_frame=front_video_black_frame,
                                                                    video_frame=front_frame)
                    
                    heatmap_frame_threshold = int(self.main_window.max_frames * 0.025) #PLot every 5% of the video
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
                        if self.isFirstFrame:
                            self.classroom_heatmap_frames_queue.put(self.seat_plan_picture)
                        else:
                            self.classroom_heatmap_frames_queue.put(self.seat_plan_picture_previous_frame)

                else:
                    # If not the target frame, skip drawing
                    self.center_cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame_index)
                    self.front_cap.set(cv2.CAP_PROP_POS_FRAMES, self.current_frame_index)
                    self.current_frame_index = self.target_frame_index
                
                print(self.main_window.filtered_arms_postures_list_front[int(self.current_frame_index)])
                
                # Store the frame with the drawn bounding box and keypoints
                if center_frame is not None and center_video_black_frame is not None:
                    self.center_video_frame_queue.put(center_frame)
                    self.center_video_black_frame_queue.put(center_video_black_frame)

                if front_frame is not None and front_video_black_frame is not None:
                    self.front_video_frame_queue.put(front_frame)
                    self.front_video_black_frame_queue.put(front_video_black_frame)

                self.current_frame_index += 1
                self.target_frame_index +=1

    def run(self):
        '''
        Main playback loop, sending frames from queue to UI
        '''
        while self.running:
            if not self.paused and not self.center_video_frame_queue.empty():
                center_video_frame = self.center_video_frame_queue.get()  # Get frame from queue
                center_black_frame = self.center_video_black_frame_queue.get()

                front_video_frame = self.front_video_frame_queue.get()  # Get frame from queue
                front_black_frame = self.front_video_black_frame_queue.get()

                classroom_heatmap = self.classroom_heatmap_frames_queue.get()

                self.frames_signal.emit([classroom_heatmap,
                                         front_black_frame, center_black_frame,
                                         front_video_frame, center_video_frame])  # Send frameS to UI displayer/updater

    def stop(self):
        self.running = False
        self.quit()
        self.wait()

    def pause(self, status):
        self.paused = status

            
