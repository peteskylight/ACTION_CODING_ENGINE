from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QGraphicsView, QGraphicsScene, 
    QTableWidget, QTableWidgetItem, QPushButton, QLabel, QSizePolicy, 
    QGraphicsProxyWidget, QSlider, QTableWidget

)
from PySide6.QtCharts import QChartView, QChart  
from PySide6.QtGui import QPainter, QPixmap, QImage, QColor, QImage, QPainter
from PySide6.QtCore import Qt, QTimer, Signal, QPoint, QRect, QThread
import numpy as np
from reportlab.lib.pagesizes import landscape, A4, letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from collections import defaultdict
import os
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches

class AI_Analytics_Table_Events_Log(QWidget):
    row_selected = Signal(int)
    

    def __init__(self, main_window, action_results_list_front, action_results_list_center, min_time, max_time):
        super().__init__()
        self.action_results_list_front = action_results_list_front
        self.action_results_list_center = action_results_list_center
        self.main_window = main_window
        self.min_time = min_time
        self.max_time = max_time
        self.TimeLabel = self.main_window.findChild(QLabel, "TimeLabel")

        self.frame_update_interval = 30  # Only update logs every 30 frames
        self.last_updated_frame = -1  # To track when the last update occurred

        # Set up event log tables
        self.main_window.ai_analytics_event_logs_table_1.setHorizontalHeaderLabels(["Person ID", "Action", "Timestamp"])
        self.main_window.ai_analytics_event_logs_table_1.setSortingEnabled(True)

        self.main_window.ai_analytics_event_logs_table_2.setHorizontalHeaderLabels(["Person ID", "Action", "Timestamp"])
        self.main_window.ai_analytics_event_logs_table_2.setSortingEnabled(True)

        self.main_window.ai_analytics_event_logs_table_3.setHorizontalHeaderLabels(["Person ID", "Action", "Timestamp"])
        self.main_window.ai_analytics_event_logs_table_3.setSortingEnabled(True)

        # Slider-based log update
        self.main_window.time_frame_range_slider_ai_analytics_table_event_logs.valueChanged.connect(self.update_logs_periodically)

        # Row double-click behavior
        self.main_window.ai_analytics_event_logs_table_1.cellDoubleClicked.connect(self.on_row_double_clicked)
        self.main_window.ai_analytics_event_logs_table_2.cellDoubleClicked.connect(self.on_row_double_clicked)
        self.main_window.ai_analytics_event_logs_table_3.cellDoubleClicked.connect(self.on_row_double_clicked)

        self.row_selected.connect(self.update_video_position)

    def update_logs_every_n_frames(self, current_frame):
        """Call this method manually from your video loop, passing current frame index."""
        if current_frame - self.last_updated_frame < self.frame_update_interval:
            return  # Don't update yet
        self.last_updated_frame = current_frame
        self.update_logs_periodically(current_frame)

    def format_time(self, seconds):
        hours = int(seconds) // 3600
        minutes = (int(seconds) % 3600) // 60
        secs = int(seconds) % 60
        return f"{hours:02d}:{minutes:02d}:{secs:02d}"
        
    def update_logs_periodically(self, current_frame=None):
        """Update logs based on slider time and video frame."""
        self.action_results_list_front = self.main_window.action_results_list_front
        self.action_results_list_center = self.main_window.action_results_list_center

        value = self.main_window.time_frame_range_slider_ai_analytics_table_event_logs.value()
        min_time, max_time = value if isinstance(value, tuple) else (value, value)

        fps = 20
        self.min_time = min_time / fps
        self.max_time = max_time / fps
        
        self.main_window.TimeLabel.setText(f"{self.format_time(self.min_time)} to {self.format_time(self.max_time)}")
        
        new_logs = []

        # Process front camera frames
        for frame_idx, actions in enumerate(self.action_results_list_front):
            timestamp = frame_idx / fps
            current_time = self.get_current_video_time()
            if timestamp < self.min_time or timestamp > current_time:
                continue
            for person_id, action in actions.items():
                if action and action.lower() != "no action":
                    new_logs.append((person_id, action, timestamp))

        # Process center camera frames
        for frame_idx, actions in enumerate(self.action_results_list_center):
            timestamp = frame_idx / fps
            current_time = self.get_current_video_time()
            if timestamp < self.min_time or timestamp > current_time:
                continue
            for person_id, action in actions.items():
                if action and action.lower() != "no action":
                    new_logs.append((person_id, action, timestamp))

        new_logs.sort(reverse=True, key=lambda log: log[2])
        self.update_logs_from_list(new_logs)

    def update_logs_from_list(self, logs):
        self.main_window.ai_analytics_event_logs_table_1.setRowCount(0)
        self.main_window.ai_analytics_event_logs_table_2.setRowCount(0)
        self.main_window.ai_analytics_event_logs_table_3.setRowCount(0)

        for person_id, action, timestamp in logs:
            if action in ["SITTING", "FACING DOWNWARDS", "FACING FORWARD"]:
                self.add_row(self.main_window.ai_analytics_event_logs_table_1, person_id, action, timestamp)
            elif action in ["FACING LEFT", "FACING RIGHT"]:
                self.add_row(self.main_window.ai_analytics_event_logs_table_2, person_id, action, timestamp)
            elif action in ["STANDING", "RIGHT ARM EXTENDING SIDEWARDS", "LEFT ARM EXTENDING SIDEWARDS"]:
                self.add_row(self.main_window.ai_analytics_event_logs_table_3, person_id, action, timestamp)

    def add_row(self, table, person_id, action, timestamp):
        if timestamp is None or not isinstance(timestamp, (int, float)):
            return
        row_position = table.rowCount()
        table.insertRow(row_position)
        table.setItem(row_position, 0, QTableWidgetItem(f"Person {person_id}"))
        table.setItem(row_position, 1, QTableWidgetItem(action))
        table.setItem(row_position, 2, QTableWidgetItem(f"{timestamp:.2f} s"))

    def on_row_double_clicked(self, row, column):
        sender_table = self.sender()
        if sender_table:
            timestamp_item = sender_table.item(row, 2)
            if timestamp_item:
                time_str = timestamp_item.text().replace(" s", "")
                try:
                    timestamp = float(time_str)
                    self.row_selected.emit(int(timestamp * 20))  # assuming 20 fps
                except ValueError:
                    pass

    def get_current_video_time(self):
        # Replace with actual logic to get current video playback time in seconds
        return self.main_window.current_video_time if hasattr(self.main_window, 'current_video_time') else self.max_time
    
    
    def update_video_position(self, timestamp):
        print(f"Double-clicked row, emitting timestamp {timestamp} seconds")

        timestamp_seconds = float(timestamp)  # Ensure it's a float

        # Get current slider range
        slider_value = self.time_frame_range_slider_ai_analytics_table_event_logs.value()
        print(f"Slider current value: {slider_value}, Type: {type(slider_value)}")

        if isinstance(slider_value, tuple):  # If it's a range slider
            min_time, max_time = slider_value
            print(f"Slider current range: {min_time} - {max_time}")

            # Convert timestamp (seconds) to a frame index
            new_slider_value = int(timestamp_seconds * self.fps)

            # Ensure it stays within valid range
            new_slider_value = max(min_time, min(new_slider_value, max_time))

            # Update only the minimum time of the range slider
            self.time_frame_range_slider_ai_analytics_table_event_logs.setValue((new_slider_value, max_time))
        else:  # If it's a single-value slider
            min_time = self.time_frame_range_slider_ai_analytics_table_event_logs.minimum()
            max_time = self.time_frame_range_slider_ai_analytics_table_event_logs.maximum()

            # Convert timestamp to a valid slider position
            new_slider_value = int(timestamp_seconds * self.fps)

            # Clamp value within valid slider range
            new_slider_value = max(min_time, min(new_slider_value, max_time))

            self.time_frame_range_slider_ai_analytics_table_event_logs.setValue(new_slider_value)  # Set integer value

        print(f"✅ Slider updated to: {self.time_frame_range_slider_ai_analytics_table_event_logs.value()} (converted from {timestamp_seconds} sec)")

# full updated version of Advanced_Analytics_Table_Events_Log
class Advanced_Analytics_Table_Events_Log(QWidget):
    row_selected = Signal(int)

    def __init__(self, main_window, head_postures_front, head_postures_center,
                 arms_postures_front, arms_postures_center, min_time, max_time):
        super().__init__()
        self.main_window = main_window

        self.head_postures_front = head_postures_front
        self.head_postures_center = head_postures_center
        self.arms_postures_front = arms_postures_front
        self.arms_postures_center = arms_postures_center

        self.min_time = min_time
        self.max_time = max_time

        self.TimeLabel = self.main_window.findChild(QLabel, "TimeLabel")
        self.is_playing = False

        self.setWindowTitle("AI Posture Logs")

        self.main_window.advanced_analytics_event_logs_table_1.setHorizontalHeaderLabels(
            ["Person ID", "Posture", "Timestamp", "Angle", "Tilt"]
        )
        self.main_window.advanced_analytics_event_logs_table_2.setHorizontalHeaderLabels(
            ["Person ID", "Posture", "Timestamp", "Angle", "Tilt"]
        )
        self.main_window.advanced_analytics_event_logs_table_3.setHorizontalHeaderLabels(
            ["Person ID", "Posture", "Timestamp", "Shoulder Angle", "Elbow Angle"]
        )

        self.main_window.play_pause_button_advanced_analytics_table_event_logs.clicked.connect(self.toggle_play_pause_logs)
        self.main_window.time_frame_range_slider_advanced_analytics_table_event_logs.valueChanged.connect(self.update_logs_periodically)

        self.main_window.advanced_analytics_event_logs_table_1.cellDoubleClicked.connect(self.on_row_double_clicked)
        self.main_window.advanced_analytics_event_logs_table_2.cellDoubleClicked.connect(self.on_row_double_clicked)
        self.main_window.advanced_analytics_event_logs_table_3.cellDoubleClicked.connect(self.on_row_double_clicked)

        self.row_selected.connect(self.update_video_position)

        self.frame_update_interval = 30  # Only update logs every 30 frames
        self.last_updated_frame = -1  # To track when the last update occurred

    def toggle_play_pause_logs(self):
        self.is_playing = not self.is_playing
        self.update_logs_periodically()

    def add_row(self, table, person_id, action, timestamp, angle=None, tilt=None):
        if timestamp is None or not isinstance(timestamp, (int, float)):
            return
        row_position = table.rowCount()
        table.insertRow(row_position)
        table.setItem(row_position, 0, QTableWidgetItem(f"Person {person_id}"))
        table.setItem(row_position, 1, QTableWidgetItem(str(action)))
        table.setItem(row_position, 2, QTableWidgetItem(f"{timestamp:.2f} s"))

        # Handle angle and tilt or shoulder/elbow depending on table
        if table == self.main_window.advanced_analytics_event_logs_table_3:
            shoulder_str = f"{angle:.1f}°" if angle is not None else "N/A"
            elbow_str = f"{tilt:.1f}°" if tilt is not None else "N/A"
            table.setItem(row_position, 3, QTableWidgetItem(shoulder_str))
            table.setItem(row_position, 4, QTableWidgetItem(elbow_str))
        else:
            angle_str = f"{angle:.1f}°" if angle is not None else "N/A"
            tilt_str = f"{tilt:.1f}°" if tilt is not None else "N/A"
            table.setItem(row_position, 3, QTableWidgetItem(angle_str))
            table.setItem(row_position, 4, QTableWidgetItem(tilt_str))

    def update_logs_from_list(self, logs):
        tables = [
            self.main_window.advanced_analytics_event_logs_table_1,
            self.main_window.advanced_analytics_event_logs_table_2,
            self.main_window.advanced_analytics_event_logs_table_3
        ]

        for table in tables:
            table.setRowCount(0)

        for person_id, posture, timestamp, category, angle, tilt in logs:
            if category == 1:
                self.add_row(self.main_window.advanced_analytics_event_logs_table_1, person_id, posture, timestamp, angle, tilt)
            elif category == 2:
                self.add_row(self.main_window.advanced_analytics_event_logs_table_2, person_id, posture, timestamp, angle, tilt)
            elif category == 3:
                self.add_row(self.main_window.advanced_analytics_event_logs_table_3, person_id, posture, timestamp, angle, tilt)

        for table in tables:
            table.resizeColumnsToContents()


    def update_logs_periodically(self):
        if not self.main_window:
            return

        self.head_postures_front = self.main_window.head_postures_list_front
        self.head_postures_center = self.main_window.head_postures_list_center
        self.arms_postures_front = self.main_window.arms_postures_list_front
        self.arms_postures_center = self.main_window.arms_postures_list_center

        if not self.is_playing:
            return

        value = self.main_window.time_frame_range_slider_advanced_analytics_table_event_logs.value()
        min_time, max_time = value if isinstance(value, tuple) else (value, value)

        fps = 20
        self.min_time = min_time / fps
        self.max_time = max_time / fps

        new_logs = []

        for cam_data in [
            (self.head_postures_front, self.arms_postures_front),
            (self.head_postures_center, self.arms_postures_center)
        ]:
            head_postures, arm_postures = cam_data

            for frame_idx in range(len(head_postures)):
                timestamp = frame_idx / fps
                current_time = self.get_current_video_time()
                if timestamp < self.min_time or timestamp > current_time:
                    continue

                # Head posture logs
                head_frame = head_postures[frame_idx]
                for track_id, info in head_frame.items():
                    posture = info["head_posture"]
                    angle = info["head_relative_angle"]
                    tilt = info["head_relative_tilt"]
                    posture_description = f"{posture}"
                    category = 1 if posture in ["FACING DOWNWARDS", "FACING FORWARD"] else 2
                    new_logs.append((track_id, posture_description, timestamp, category, angle, tilt))

                # Arm posture logs
                arms_frame = arm_postures[frame_idx]
                for track_id, info in arms_frame.items():
                    right_posture = info["right_arm_posture"]
                    left_posture = info["left_arm_posture"]

                    rs = info["right_shoulder_angle"]
                    re = info["right_elbow_angle"]
                    ls = info["left_shoulder_angle"]
                    le = info["left_elbow_angle"]

                    # RIGHT arm
                    if right_posture and right_posture != "NO POSTURE":
                        desc = f"Right Arm: {right_posture}"
                        if right_posture == "NEUTRAL":
                            new_logs.append((track_id, desc, timestamp, 1, rs, re))
                        elif "EXTENDING" in right_posture:
                            new_logs.append((track_id, desc, timestamp, 2, rs, re))
                        else:
                            new_logs.append((track_id, desc, timestamp, 3, rs, re))

                    # LEFT arm
                    if left_posture and left_posture != "NO POSTURE":
                        desc = f"Left Arm: {left_posture}"
                        if left_posture == "NEUTRAL":
                            new_logs.append((track_id, desc, timestamp, 1, ls, le))
                        elif "EXTENDING" in left_posture:
                            new_logs.append((track_id, desc, timestamp, 2, ls, le))
                        else:
                            new_logs.append((track_id, desc, timestamp, 3, ls, le))

        new_logs.sort(reverse=True, key=lambda log: log[2])
        self.update_logs_from_list(new_logs)


    def get_current_video_time(self):
        return self.main_window.current_frame_index / 30.0 if self.main_window.current_frame_index else 0

    def update_logs_every_n_frames(self, current_frame):
        if current_frame - self.last_updated_frame < self.frame_update_interval:
            return
        self.last_updated_frame = current_frame
        self.update_logs_periodically()

    def on_row_double_clicked(self, row, column):
        table = self.sender()
        timestamp_item = table.item(row, 2)
        if timestamp_item:
            timestamp_str = timestamp_item.text().replace(" s", "")
            try:
                timestamp = float(timestamp_str)
                frame = int(timestamp * 20)
                self.row_selected.emit(frame)
            except ValueError:
                pass

    def update_video_position(self, timestamp):
        print(f"Double-clicked row, emitting timestamp {timestamp} seconds")

        timestamp_seconds = float(timestamp)  # Ensure it's a float

        # Get current slider range
        slider_value = self.time_frame_range_slider_advanced_analytics_table_event_logs.value()
        print(f"Slider current value: {slider_value}, Type: {type(slider_value)}")

        if isinstance(slider_value, tuple):  # If it's a range slider
            min_time, max_time = slider_value
            print(f"Slider current range: {min_time} - {max_time}")

            # Convert timestamp (seconds) to a frame index
            new_slider_value = int(timestamp_seconds * self.fps)

            # Ensure it stays within valid range
            new_slider_value = max(min_time, min(new_slider_value, max_time))

            # Update only the minimum time of the range slider
            self.time_frame_range_slider_advanced_analytics_table_event_logs.setValue((new_slider_value, max_time))
        else:  # If it's a single-value slider
            min_time = self.time_frame_range_slider_advanced_analytics_table_event_logs.minimum()
            max_time = self.time_frame_range_slider_advanced_analytics_table_event_logs.maximum()

            # Convert timestamp to a valid slider position
            new_slider_value = int(timestamp_seconds * self.fps)

            # Clamp value within valid slider range
            new_slider_value = max(min_time, min(new_slider_value, max_time))

            self.time_frame_range_slider_advanced_analytics_table_event_logs.setValue(new_slider_value)  # Set integer value

        print(f"✅ Slider updated to: {self.time_frame_range_slider_advanced_analytics_table_event_logs.value()} (converted from {timestamp_seconds} sec)")