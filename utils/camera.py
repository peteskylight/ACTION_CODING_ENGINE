import cv2
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import numpy as np
from PySide6.QtCore import QTimer, Qt
from PySide6.QtGui import QImage, QPixmap

from trackers.pose_detection import PoseDetection
from utils.drawing_utils import DrawingUtils
from utils.tools import Tools
from utils.cvfpscalc import CvFpsCalc

class CameraFeed:
    def __init__(self, label, white_frame_label, main_window):
        self.pose_detection = PoseDetection(humanDetectionModel='yolov8x.pt',
                                            humanDetectConf=0.4,
                                            humanPoseModel='yolov8x-pose.pt',
                                            humanPoseConf=0.4
                                            )
        
        self.getFPS = CvFpsCalc(buffer_len=10)
        self.drawing_utils = DrawingUtils()
        self.tools_utils = Tools()
        
        self.isRecording = False
        self.folder_count = 0
        self.frame_count = 0
        self.countdown = 0
        
        self.label = label
        self.white_frame_label = white_frame_label
        self.main_window = main_window
        self.cap = None
        self.timer = QTimer()
        
        self.timer.timeout.connect(self.update_frame)
        
        # For internal countdown tracking
        self.last_countdown_update = 0

    def start_camera(self, index):
        self.cap = cv2.VideoCapture(index) #<--- yung index ay yung link
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 0) 
        self.timer.start(10)  # One timer handles both frame and countdown

    def update_frame(self):
        ret, output_frame = self.cap.read()
        color = 255
        
        if not ret:
            return
        
        returned_frame, normalized_keypoints, bbox = self.pose_detection.getHumanPoseKeypoints(frame=output_frame)
        
        # Visualizations
        if self.main_window.showCameraLandmarksChkBox.isChecked():
            self.drawing_utils.drawPoseLandmarks(frame=returned_frame, keypoints=normalized_keypoints)
        
        if self.main_window.showCameraBoundingBoxChkBox.isChecked():
            self.drawing_utils.draw_bounding_box(frame=returned_frame, box=bbox)
        
        if self.main_window.show_skeleton_camera.isChecked():
            self.drawing_utils.draw_keypoints_and_skeleton(frame=returned_frame, keypoints=normalized_keypoints)

        processed_frame = returned_frame
        
        if self.main_window.darkMode_whiteframe.isChecked():
            color = 0
        white_frame = color * np.ones_like(processed_frame)

        self.drawing_utils.drawPoseLandmarks(frame=white_frame, keypoints=normalized_keypoints)

        if self.main_window.show_whiteframe_boundingbox.isChecked():
            self.drawing_utils.draw_bounding_box(frame=white_frame, box=bbox)
        
        if self.main_window.show_skeleton_white_frame.isChecked():
            self.drawing_utils.draw_keypoints_and_skeleton(frame=white_frame, keypoints=normalized_keypoints)
        
        # Logging
        if self.main_window.recording_button.text() == "STOP\nRECORDING":
            if self.main_window.status_label.text() == "RECORDING":
                chosen_directory = self.main_window.directoryLineEdit.text()
                chosen_action = self.main_window.action_comboBox.currentText()
                destination_directory = os.path.join(chosen_directory, chosen_action)
                
                self.folder_count = self.tools_utils.count_folders(directory=destination_directory)
                
                if not os.path.isdir(os.path.join(destination_directory, str(self.folder_count))):
                    os.mkdir(os.path.join(destination_directory, str(self.folder_count)))
                
                self.record_and_save_keypoints(normalized_keypoints=normalized_keypoints, frame_num=self.frame_count)
                self.frame_count += 1

                if self.frame_count % int(self.main_window.sequence_slider.value()) == 0:
                    self.main_window.status_label.setText("NOT RECORDING")
                    self.frame_count = 0
                    self.folder_count += 1
                    os.mkdir(os.path.join(destination_directory, str(self.folder_count)))
                    self.countdown = int(self.main_window.interval_slider.value())  # Reset countdown
                    self.last_countdown_update = cv2.getTickCount()

            if self.countdown == 0:
                self.main_window.status_label.setText("RECORDING")
        
        elif self.main_window.recording_button.text() == "START\nRECORDING":
            self.frame_count = 0
        
        # Countdown timer logic inside frame updates
        if self.countdown > 0:
            current_tick = cv2.getTickCount()
            elapsed_time = (current_tick - self.last_countdown_update) / cv2.getTickFrequency()
            if elapsed_time >= 0.02:
                self.countdown -= 1
                self.last_countdown_update = current_tick

        # Display countdown text
        if self.countdown > 0:
            countdown_text = f"{self.countdown}"
            text_size = cv2.getTextSize(countdown_text, cv2.FONT_HERSHEY_SIMPLEX, 3, 5)[0]
            text_x = (processed_frame.shape[1] - text_size[0]) // 2
            text_y = (processed_frame.shape[0] + text_size[1]) // 2
            cv2.putText(processed_frame, countdown_text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 5, (255, 255, 255), 10, cv2.LINE_AA)

        # Show in QLabel
        height, width, channel = processed_frame.shape
        bytes_per_line = 3 * width
        q_img = QImage(processed_frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        pixmap = QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(self.label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.label.setPixmap(scaled_pixmap)

        white_q_img = QImage(white_frame.data, width, height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        white_pixmap = QPixmap.fromImage(white_q_img)
        scaled_white_pixmap = white_pixmap.scaled(self.white_frame_label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        self.white_frame_label.setPixmap(scaled_white_pixmap)

        fps = self.getFPS.get()
        self.main_window.fps_label.setText(str(fps))

    def stop_camera(self):
        self.timer.stop()
        if self.cap is not None:
            self.cap.release()

        # Clear labels
        self.main_window.camera_feed.clear()
        self.main_window.camera_feed.setText("Camera stopped. No feed available.")
        self.main_window.camera_feed.setAlignment(Qt.AlignCenter)
        
        self.main_window.white_frame_feed.clear()
        self.main_window.white_frame_feed.setText("White frame stopped. No feed available.")
        self.main_window.white_frame_feed.setAlignment(Qt.AlignCenter)

    def record_and_save_keypoints(self, normalized_keypoints, frame_num):
        flattenedList = normalized_keypoints.flatten()
        chosen_directory = self.main_window.directoryLineEdit.text()
        chosen_action = self.main_window.action_comboBox.currentText()
        destination_directory = os.path.join(chosen_directory, chosen_action)
        no_of_sequences = self.main_window.sequence_slider.value()
        
        if not os.path.isdir(destination_directory):
            QMessageBox.critical(self.main_window, "Error", "The specified directory does not exist. Check the chosen directory.")
            self.main_window.toggle_button()
            return
        
        final_destination_directory = os.path.join(destination_directory, str(self.folder_count))
        npy_path = os.path.join(final_destination_directory, str(frame_num))
        np.save(npy_path, flattenedList)
