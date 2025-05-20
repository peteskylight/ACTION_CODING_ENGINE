import cv2

from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import Qt
from PySide6.QtGui import QImage, QPixmap



from utils import (VideoProcessorThread)
from trackers import (PoseDetection,
                    ActionDetectionThread,
                    HeadPostureIdentifier,
                    ArmPostureIdentifer)

import time

class FrontVideo:
    def __init__(self, main_window):
        self.main_window = main_window
        
        self.human_detect_model = "yolov8x.pt"
        self.human_detect_conf = 0.5
        self.human_pose_model = "yolov8x-pose.pt"
        self.human_pose_conf = 0.5
        self.iou_value = 0.4

        self.returned_frames = []
        self.humanDetectionResults = []
        self.action_results_list = []

        self.humanPoseDetectionResults = None
        self.isImportDone = False
        self.videoHeight = None
        self.videoWidth = None
        self.number_of_frames = 0

        self.video_player_thread = None
        self.action_detection_thread_front = None

        self.directory = None
        self.detection = PoseDetection(humanDetectionModel=self.human_detect_model,
                                                    humanDetectConf= self.human_detect_conf,
                                                    humanPoseModel= self.human_pose_model,
                                                    humanPoseConf= self.human_pose_conf
                                                    )
        self.start_time = None
        self.end_time = None

    #When browse for center video is clicked
    def browse_video(self):
        self.directory, _ = QFileDialog.getOpenFileName(self.main_window, "Select Video File", "", "Video Files (*.mp4 *.avi *.mkv *.mov *.wmv)")
        if self.directory:
            #Reset the analytics button
            self.main_window.activate_analytics(False)
            
            self.returned_frames = []
            self.humanDetectionResults = []
            self.action_results_list = []
            
            self.main_window.video_player_thread_preview = None

            self.main_window.videoDirectory_front.setText(f"{self.directory}")
            
            self.main_window.is_front_video_ready = False
            self.main_window.human_pose_results_front = None
            self.main_window.human_detect_results_front = None
            self.main_window.action_results_list_front = None
            
            self.main_window.import_video_button_front.setEnabled(False)

            self.start_video_processing(self.directory)
            
            

    # Assuming you have an instance of your VideoProcessorThread called 'video_thread'

    def print_time_length(self, start_time, end_time):
        self.start_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(start_time))
        self.end_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(end_time))
        print(f"Processing started at: {self.start_time_str}")
        print(f"Processing ended at: {self.end_time_str}")

        time_difference = end_time - start_time

        # Calculate different time units
        seconds = int(time_difference)
        minutes = seconds // 60
        hours = minutes // 60
        days = hours // 24

        # Format the time difference string
        if days > 0:
            time_length_str = f"{days} days, {hours % 24} hrs, {minutes % 60} mins, {seconds % 60} s"
        elif hours > 0:
            time_length_str = f"{hours} hrs, {minutes % 60} mins, {seconds % 60} s"
        elif minutes > 0:
            time_length_str = f"{minutes} mins, {seconds % 60} s"
        else:
            time_length_str = f"{seconds} s"

        print(f"Processing time: {time_length_str}")
        
        return time_length_str


    def start_video_processing(self, video_path):
        self.main_window.status_label_front.setText("[ PROCESSING VIDEO... PLEASE WAIT ]")

        self.start_time = time.time()
        
        self.front_video_processor = VideoProcessorThread(video_path, resize_frames=False,
                                                    isFront=True,
                                                    human_detection_model=self.human_detect_model,
                                                    human_detection_confidence=self.human_detect_conf,
                                                    human_pose_model=self.human_pose_model,
                                                    human_pose_confidence=self.human_pose_conf,
                                                    main_window=self.main_window,
                                                    camera_angle="-F")

        self.front_video_processor.human_detect_results.connect(self.update_detection_results)
        self.front_video_processor.human_pose_results.connect(self.update_pose_detection_results)
        self.front_video_processor.progress_update.connect(self.update_progress_bar)

        #Start the operation
        self.front_video_processor.start()
        
    def update_detection_results(self, results_list):
        self.humanDetectionResults = results_list
        self.main_window.human_detect_results_front = results_list

        print("HUMAN DETECT RESULTS:", len(results_list))
    
    def update_pose_detection_results(self, pose_results):
        self.humanPoseDetectionResults = pose_results
        self.main_window.human_pose_results_front = pose_results
        self.identify_actions()

        print("POSE RESULTS:", len(pose_results))
    
    def identify_actions(self):
        self.main_window.status_label_front.setText("[ IDENTIFYING BODY POSTURES...]")

        self.action_detection_thread_front = ActionDetectionThread(main_window=self.main_window,
                                                            video_keypoints=self.humanPoseDetectionResults,
                                                            black_frames=self.main_window.front_white_frames_preview,
                                                            video_frames=self.returned_frames,
                                                            detections=self.humanDetectionResults)
        
        self.action_detection_thread_front.detected_actions_list.connect(self.update_action_results)
        self.action_detection_thread_front.progress_update.connect(self.update_progress_bar)  
        self.action_detection_thread_front.start()

    def update_action_results(self, actions):
        self.action_detection_thread_front.stop()
        
        self.action_results_list = actions
        self.main_window.action_results_list_front = actions
        self.main_window.status_label_front.setText("[ POSTURE IDENTIFICATION, DONE! ]")
        self.main_window.is_front_video_ready = True

        self.main_window.import_video_button_front.setEnabled(True)

        cap = cv2.VideoCapture(self.directory)

        #Get the frame count
        frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        #Get the video length
        # Get the frame rate (frames per second)
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Calculate the video length in seconds
        video_length = frame_count / fps
        
        # Convert video length to hours, minutes, and seconds
        hours = int(video_length // 3600)
        minutes = int((video_length % 3600) // 60)
        seconds = int(video_length % 60)
        time_formatted = f"{hours:02}:{minutes:02}:{seconds:02}"

        #self.main_window.front_frame_count.setText(str(frame_count))

        #self.main_window.front_video_length.setText(time_formatted)
        
        
        
        # self.front_video_processor.stop()
        
        # self.action_detection_thread_front.stop()

        
        #Start the head posture detection based on thresholds
        self.detect_head_action_thresholds()
    
    def detect_head_action_thresholds(self):
        
        self.head_posture_identifier  = HeadPostureIdentifier(main_window=self.main_window,
                                                              human_keypoints_list= self.humanPoseDetectionResults)
        self.head_posture_identifier.head_postures_signal.connect(self.update_head_postures_list)
        self.head_posture_identifier.start()
        self.main_window.status_label_front.setText("[ DETECTING HEAD POSTURES... ]")
        
    
    def update_head_postures_list(self, head_postures_list):
        self.main_window.head_postures_list_front = head_postures_list
        self.head_posture_identifier.stop()
        self.head_posture_identifier = None

        self.main_window.status_label_front.setText("[ HEAD POSTURE DETECTION, DONE! ]")

        #Start the arm posture detection based on thresholds
        self.detect_arm_posture_thresholds()
        
    def detect_arm_posture_thresholds(self):
        self.arm_posture_identifier = ArmPostureIdentifer(main_window=self.main_window,
                                                          human_keypoints_list=self.humanPoseDetectionResults)
        
        self.arm_posture_identifier.arm_postures_list_signal.connect(self.update_arm_postures_list)
        self.arm_posture_identifier.start()
        self.main_window.status_label_front.setText("[ DETECTING ARM POSTURES... ]")
        
    
    def update_arm_postures_list(self, arm_posture_list):
        self.main_window.arms_postures_list_front = arm_posture_list
        self.arm_posture_identifier.stop()
        self.arm_posture_identifier = None
        
        print(f"FRONT ACTIONS: {self.action_results_list}")

        self.main_window.status_label_front.setText("[ VIDEO ANALYSIS, DONE! ]")
        
        self.end_time = time.time()
        time_length = self.print_time_length(start_time=self.start_time,
                                   end_time=self.end_time)
        
        self.main_window.time_elapsed_label_front.setText(time_length)
        
        if self.main_window.is_center_video_ready and self.main_window.is_front_video_ready:
            self.main_window.activate_analytics(True)
            
        else:
            self.main_window.activate_analytics(False)
        
    def update_progress_bar(self,value):
        self.main_window.importProgressBar_front.setValue(value)


    #=== FOR UPDATING FRAMES:

    def update_frame(self, front_frame):
        if len(front_frame.shape) == 3:
            front_video_height, front_video_width, _ = front_frame.shape
        else:
            front_video_height, front_video_width = front_frame.shape

        initial_row_height = int(front_video_height * (1/16))  # Bottom 4 rows (adjust as needed)

        bytes_per_line = 3 * front_video_width
        q_img_front = QImage(front_frame.data, front_video_width, front_video_height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        # Set the QImage to the QLabel with aspect ratio maintained and white spaces
        pixmap_front = QPixmap.fromImage(q_img_front)
        scaled_pixmap_front = pixmap_front.scaled(self.main_window.video_preview_label_front.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.main_window.video_preview_label_front.setPixmap(scaled_pixmap_front)
