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

class CenterVideo:
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
        
        self.action_detection_thread_center = None

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
            
            #Reset the analytics buttons
            self.main_window.activate_analytics(False)
            
            self.returned_frames = []
            self.humanDetectionResults = []
            self.action_results_list = []
            self.main_window.videoDirectory_center.setText(f"{self.directory}")
            self.start_video_processing(self.directory)
            self.main_window.is_center_video_ready = False

            self.main_window.video_player_thread_preview = None
            self.main_window.human_pose_results_center = None
            self.main_window.human_detect_results_center = None
            self.main_window.action_results_list_center = None
            self.main_window.import_video_button_center.setEnabled(False)
    
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
        self.main_window.status_label_center.setText("[ PROCESSING VIDEO... PLEASE WAIT ]")

        self.start_time = time.time()
        self.video_processor = VideoProcessorThread(video_path, resize_frames=False,
                                                    isFront=False,
                                                    human_detection_model=self.human_detect_model,
                                                    human_detection_confidence=self.human_detect_conf,
                                                    human_pose_model=self.human_pose_model,
                                                    human_pose_confidence=self.human_pose_conf,
                                                    main_window=self.main_window,
                                                    camera_angle="-C")
        
        self.video_processor.human_detect_results.connect(self.update_detection_results)
        self.video_processor.human_pose_results.connect(self.update_pose_detection_results)
        self.video_processor.progress_update.connect(self.update_progress_bar)

        #Start the operation
        self.video_processor.start()
        
    def update_detection_results(self, results_list):
        self.humanDetectionResults = results_list
        self.main_window.human_detect_results_center = results_list
        
    def update_pose_detection_results(self, pose_results):
        self.humanPoseDetectionResults = pose_results
        self.main_window.human_pose_results_center = pose_results
        self.identify_actions()
    
    def identify_actions(self):
        self.main_window.status_label_center.setText("[ IDENTIFYING BODY POSTURES...]")

        self.action_detection_thread_center = ActionDetectionThread(main_window=self.main_window,
                                                            video_keypoints=self.humanPoseDetectionResults,
                                                            black_frames=self.main_window.center_white_frames_preview,
                                                            video_frames=self.returned_frames,
                                                            detections=self.humanDetectionResults)
        
        self.action_detection_thread_center.detected_actions_list.connect(self.update_action_results)
        self.action_detection_thread_center.progress_update.connect(self.update_progress_bar)  
        self.action_detection_thread_center.start()

    def update_action_results(self, actions):
        self.action_detection_thread_center.stop()
        
        self.action_results_list = actions
        self.main_window.action_results_list_center = actions
        self.main_window.status_label_center.setText("[ POSTURE IDENTIFICATION, DONE! ]")
        
        self.main_window.is_center_video_ready = True
        
        self.main_window.import_video_button_center.setEnabled(True)

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

        self.video_processor = None
        
        self.detect_head_action_thresholds()
    
    def detect_head_action_thresholds(self):
        self.head_posture_identifier  = HeadPostureIdentifier(main_window=self.main_window,
                                                              human_keypoints_list= self.humanPoseDetectionResults)
        self.head_posture_identifier.head_postures_signal.connect(self.update_head_postures_list)
        self.head_posture_identifier.start()

        self.main_window.status_label_center.setText("[ DETECTING HEAD POSTURES... ]")
    
    def update_head_postures_list(self, head_postures_list):
        self.main_window.head_postures_list_center = head_postures_list
        self.head_posture_identifier.stop()
        self.head_posture_identifier = None

        self.main_window.status_label_center.setText("[ HEAD POSTURE DETECTION, DONE! ]")
        #Start the arm posture detection based on thresholds
        self.detect_arm_posture_thresholds()


    def detect_arm_posture_thresholds(self):
        self.arm_posture_identifier = ArmPostureIdentifer(main_window=self.main_window,
                                                          human_keypoints_list=self.humanPoseDetectionResults)
        
        self.arm_posture_identifier.arm_postures_list_signal.connect(self.update_arm_postures_list)

        self.arm_posture_identifier.start()
        self.main_window.status_label_center.setText("[ DETECTING ARM POSTURES... ]")
    
    def update_arm_postures_list(self, arm_posture_list):
        self.main_window.arms_postures_list_center = arm_posture_list
        self.arm_posture_identifier.stop()
        self.arm_posture_identifier = None

        self.main_window.status_label_center.setText("[ VIDEO ANALYSIS, DONE! ]")
        
        self.end_time = time.time()
        time_length = self.print_time_length(start_time=self.start_time,
                                   end_time=self.end_time)
        
        self.main_window.time_elapsed_label_center.setText(time_length)
        
        if self.main_window.is_center_video_ready and self.main_window.is_front_video_ready:
            self.main_window.activate_analytics(True)
            
            
        else:
            self.main_window.activate_analytics(False)
        

    def update_progress_bar(self,value):
        self.main_window.importProgressBar_center.setValue(value)

    # def closeEvent(self, event):
    #     if self.video_processor._running():
    #         self.video_processor.quit()
    #         self.video_processor.wait()
    #     event.accept()
    

    #=== FOR UPDATING FRAMES:

    def update_frame(self, center_frame):
        if len(center_frame.shape) == 3:
            center_video_height, center_video_width, _ = center_frame.shape
        else:
            center_video_height, center_video_width = center_frame.shape

        bytes_per_line = 3 * center_video_width
        q_img_center = QImage(center_frame.data, center_video_width, center_video_height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        # Set the QImage to the QLabel with aspect ratio maintained and white spaces
        pixmap_center = QPixmap.fromImage(q_img_center)
        scaled_pixmap_center = pixmap_center.scaled(self.main_window.video_preview_label_center.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.main_window.video_preview_label_center.setPixmap(scaled_pixmap_center)


    def cleanup_thread(self):
        """Called when the thread finishes to release memory."""
        self.video_player_thread.deleteLater()
