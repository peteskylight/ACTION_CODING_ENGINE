from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis
from PySide6.QtWidgets import QGraphicsScene, QSizePolicy, QVBoxLayout, QPushButton, QWidget,QFileDialog, QApplication
from PySide6.QtGui import QPainter, QFont, QColor
from PySide6.QtCore import Qt, QBuffer, QByteArray
import pandas as pd
import os
import time
from pathlib import Path

class AI_Analytics_Line_Chart_Visualization: 
    '''
    AUTHOR: JOHN BENNETT GONZALES & PETER JUSTIN DATINGALING
    '''
    def __init__(self, main_window, action_results_list_front, action_results_list_center, min_time, max_time):
        self.action_results_list_front = action_results_list_front
        self.action_results_list_center = action_results_list_center
        self.min_time = min_time
        self.max_time = max_time
        self.main_window = main_window

        self.action_labels = [
            'LEFT ARM EXTENDING SIDEWARDS', 'RIGHT ARM EXTENDING SIDEWARDS', 'FACING DOWNWARDS',
            "FACING FORWARD", 'FACING LEFT', 'FACING RIGHT', 'SITTING', 'STANDING', 
            'TOTAL # of HUMANS DETECTED',
            'HIGHLY SUSPICIOUS', 'MODERATELY SUSPICIOUS', 'NON-SUSPICIOUS'
        ]
        self.active_actions = set(self.action_labels)

        self.chart = QChart()
        legend = self.chart.legend()
        for marker in legend.markers():
            marker.setShape(QLegendMarker.LegendMarkerShapeRectangle)

        self.chart.setTitle("Actions Over Time")
        self.chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)

        self.series_dict = {label: QLineSeries() for label in self.action_labels}
        for label, series in self.series_dict.items():
            series.setName(label)
            self.chart.addSeries(series)

        for label in ['HIGHLY SUSPICIOUS', 'MODERATELY SUSPICIOUS', 'NON-SUSPICIOUS']:
            self.series_dict[label].setColor(
                QColor(255, 0, 0) if label == 'HIGHLY SUSPICIOUS' 
                else QColor(255, 165, 0) if label == 'MODERATELY SUSPICIOUS' 
                else QColor(0, 255, 0)
            )

        self.axis_x = QValueAxis()
        self.axis_x.setTitleText("Time (seconds)")
        self.axis_x.setLabelFormat("%.1f")
        self.axis_x.setRange(self.min_time / 30.0, self.max_time / 30.0)
        self.axis_x.setTickCount(min(10, (self.max_time - self.min_time) // 30 + 1))
        font = QFont()
        font.setPointSize(12)
        self.axis_x.setLabelsFont(font)
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)

        for series in self.series_dict.values():
            series.attachAxis(self.axis_x)

        self.axis_y = QValueAxis()
        self.axis_y.setTitleText("Students")
        self.axis_y.setRange(0, 45)
        self.axis_y.setTickCount(6)
        self.axis_y.setLabelFormat("%d")
        self.axis_y.setLabelsFont(QFont("Arial", 10))
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)

        for series in self.series_dict.values():
            series.attachAxis(self.axis_y)

        self.scene = QGraphicsScene()
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.chart_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        graphics_view_size = self.main_window.ai_analytics_line_chart.size()
        self.chart_view.setMinimumSize(graphics_view_size)
        self.chart_view.setMaximumSize(graphics_view_size)

        self.scene.addWidget(self.chart_view)
        self.main_window.ai_analytics_line_chart.setScene(self.scene)

        self.main_window.ai_analytics_line_chart.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_window.ai_analytics_line_chart.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.chart_view.fitInView(self.chart_view.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.chart.legend().setFont(QFont("Arial", 10))
        self.chart.legend().setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.axis_x.setLabelsAngle(0)
        self.axis_x.setLabelsFont(QFont("Arial", 10))
        self.axis_x.setTickCount(min(6, (self.max_time - self.min_time) // 30 + 1))

        self.axis_y.setLabelsFont(QFont("Arial", 10))
        self.axis_y.setTickCount(6)

        self.main_window.time_frame_range_slider_ai_analytics_line_graph.valueChanged.connect(self.update_chart)
        self.main_window.ai_analytics_line_graph_combo_box.addItems(["ALL ACTIONS"] + self.action_labels)
        self.main_window.ai_analytics_line_graph_combo_box.selectionChanged.connect(self.filter_chart_by_actions)
        self.main_window.time_frame_range_slider_ai_analytics_line_graph.sliderReleased.connect(self.get_colors_all_frames)

        # Connect checkboxes to re-filter chart when toggled
        self.main_window.identify_suspicious_check_box_line_graph_ai_analytics.stateChanged.connect(self.filter_chart_by_actions_checkbox)
        self.main_window.identify_suspicious_check_box_line_graph_advanced_analytics.stateChanged.connect(self.filter_chart_by_actions_checkbox)

        self.color_label_map = None
        self.color_counts_per_frame = None

        self.get_colors_all_frames()
        self.populate_chart()

    def get_colors_all_frames(self):
        self.color_label_map, self.color_counts_per_frame = self.main_window.get_colors_actions_from_tracker_all_frames(is_advanced_analytics=False)

    def filter_chart_by_actions(self, selected_action: str):
        suspicious_filter = self.is_suspicious_filter_active()
        
        if suspicious_filter:
            allowed_labels = {"HIGHLY SUSPICIOUS", "MODERATELY SUSPICIOUS", "NON-SUSPICIOUS"}
        else:
            allowed_labels = set(self.action_labels)

        if selected_action == "ALL ACTIONS":
            self.active_actions = allowed_labels
        else:
            selected_actions = {action.strip() for action in selected_action.split(",")}
            self.active_actions = selected_actions & allowed_labels

        self.populate_chart()


    def filter_chart_by_actions_checkbox(self):
        current_selection = self.main_window.ai_analytics_line_graph_combo_box.currentText()
        self.filter_chart_by_actions(current_selection)


    def is_suspicious_filter_active(self):
        return (
            self.main_window.identify_suspicious_check_box_line_graph_ai_analytics.isChecked()
            or self.main_window.identify_suspicious_check_box_line_graph_advanced_analytics.isChecked()
        )

    def populate_chart(self):
        # Remove all series from chart to avoid duplicates
        
        for series in self.series_dict.values():
            if series is not None:
                self.chart.removeSeries(series)

        # Clear all series and set them invisible
        for series in self.series_dict.values():
            series.clear()
            series.setVisible(False)

        total_humans_overall = 0
        valid_frame_count = 0

        for frame_index in range(self.min_time, self.max_time + 1):
            time_value = frame_index / 30.0
            combined_counts = {label: 0 for label in self.action_labels}
            total_humans = 0
            highly_suspicious = 0
            moderately_suspicious = 0
            non_suspicious = 0

            # Front view
            if frame_index < len(self.action_results_list_front):
                front_actions = list(self.action_results_list_front[frame_index].values())
                front_detections = list(self.main_window.human_detect_results_front[frame_index].values())
                total_humans += len(front_detections)
                for action in front_actions:
                    if action in combined_counts:
                        combined_counts[action] += 1

            # Center view
            if frame_index < len(self.action_results_list_center):
                center_actions = list(self.action_results_list_center[frame_index].values())
                center_detections = list(self.main_window.human_detect_results_center[frame_index].values())
                total_humans += len(center_detections)
                for action in center_actions:
                    if action in combined_counts:
                        combined_counts[action] += 1

            combined_counts["TOTAL # of HUMANS DETECTED"] = total_humans
            total_humans_overall += total_humans
            valid_frame_count += 1

            if frame_index < len(self.color_counts_per_frame):
                counts = self.color_counts_per_frame[frame_index]
                highly_suspicious = counts.get("red", 0)
                moderately_suspicious = counts.get("orange", 0)
                non_suspicious = counts.get("green", 0)

            combined_counts["HIGHLY SUSPICIOUS"] = highly_suspicious
            combined_counts["MODERATELY SUSPICIOUS"] = moderately_suspicious
            combined_counts["NON-SUSPICIOUS"] = non_suspicious

            for label in self.series_dict:
                if label in self.active_actions:
                    self.series_dict[label].append(time_value, combined_counts.get(label, 0))


        # Re-add and show only the selected series
        for label in self.active_actions:
            if label in self.series_dict:
                self.chart.addSeries(self.series_dict[label])
                self.series_dict[label].attachAxis(self.axis_x)
                self.series_dict[label].attachAxis(self.axis_y)
                self.series_dict[label].setVisible(True)

        if valid_frame_count > 0:
            average_humans = total_humans_overall / valid_frame_count
            print(f"📊 Average humans detected per frame: {average_humans:.2f}")
        else:
            print("⚠️ No valid frames processed.")

    def update_chart(self):
        self.min_time, self.max_time = self.main_window.time_frame_range_slider_ai_analytics_line_graph.value()
        self.populate_chart()

        self.chart.removeAxis(self.axis_x)
        self.axis_x = QValueAxis()
        self.axis_x.setTitleText("Time (seconds)")
        self.axis_x.setLabelFormat("%.1f")
        self.axis_x.setRange(self.min_time / 30.0, self.max_time / 30.0)
        self.axis_x.setTickCount(min(10, (self.max_time - self.min_time) // 30 + 1))
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)

        for series in self.series_dict.values():
            series.attachAxis(self.axis_x)

        self.chart.update()

    def toggle_action(self, action, checked):
        if checked:
            self.active_actions.add(action)
        else:
            self.active_actions.discard(action)
        self.populate_chart()


    def export_to_excel(self):
        data = []
        for frame_index in range(self.min_time, self.max_time + 1):
            time_value = frame_index / 30.0
            frame_data = {"Time (s)": time_value}

            if frame_index < len(self.action_results_list_front):
                for track_id, action in self.action_results_list_front[frame_index].items():
                    frame_data[f"Front_Cam_Person_{track_id}"] = action

            if frame_index < len(self.action_results_list_center):
                for track_id, action in self.action_results_list_center[frame_index].items():
                    frame_data[f"Center_Cam_Person_{track_id}"] = action

            data.append(frame_data)

        df = pd.DataFrame(data)
        file_path, _ = QFileDialog.getSaveFileName(None, "Save Excel File", "", "Excel Files (*.xlsx)")
        if file_path:
            df.to_excel(file_path, index=False)

    def export_to_jpeg(self):
        script_dir = Path(__file__).parent
        temp_dir = script_dir / "temp"
        temp_dir.mkdir(parents=True, exist_ok=True)

        print(f"Temp directory path: {temp_dir}")

        original_active_actions = self.active_actions.copy()

        def save_pixmap_to_file(pixmap, filepath):
            if pixmap.isNull():
                print(f"❌ Failed to capture pixmap for {filepath}")
                return

            buffer = QBuffer()
            buffer.open(QBuffer.ReadWrite)

            if pixmap.save(buffer, "JPG"):
                data = buffer.data()
                if data:
                    with open(filepath, "wb") as f:
                        f.write(data)
                        f.flush()
                        os.fsync(f.fileno())
                    if os.path.exists(filepath):
                        print(f"✅ Confirmed: {filepath} exists!")
                else:
                    print(f"❌ Buffer is empty for {filepath}")
            else:
                print(f"❌ pixmap.save() failed for {filepath}")

            buffer.close()

        for action in self.action_labels:
            self.active_actions = {action}
            self.populate_chart()
            self.chart.update()
            QApplication.processEvents()
            time.sleep(0.5)

            pixmap = self.chart_view.grab()
            action_filename = f"{action.replace(' ', '_')}_AI_Analytics.jpg"
            action_path = os.path.join(temp_dir, action_filename)
            save_pixmap_to_file(pixmap, action_path)

        self.active_actions = set(self.action_labels)
        self.populate_chart()
        self.chart.update()
        QApplication.processEvents()
        time.sleep(0.5)

        pixmap = self.chart_view.grab()
        all_actions_path = os.path.join(temp_dir, "All_Actions_AI_Analytics.jpg")
        save_pixmap_to_file(pixmap, all_actions_path)

        self.active_actions = original_active_actions
        self.populate_chart()
        self.chart.update()
        QApplication.processEvents()

        print(f"📁 Charts saved in: {temp_dir}")




class Advanced_Analytics_Line_Chart_Visualization:
    """
    AUTHOR: JOHN BENNETT GONZALES
    """

    def __init__(self, main_window, head_posture_list_front, head_posture_list_center, arm_posture_list_front,
                 arm_posture_list_center, min_time, max_time):
        self.head_posture_list_front = head_posture_list_front
        self.head_posture_list_center = head_posture_list_center
        self.arm_posture_list_front = arm_posture_list_front
        self.arm_posture_list_center = arm_posture_list_center
        self.min_time = min_time
        self.max_time = max_time
        self.main_window = main_window

        # Define posture labels
        self.head_postures = ['FACING DOWNWARDS', 'FACING LEFT', 'FACING RIGHT', "FACING FORWARD"]
        self.left_arm_postures = ["NEUTRAL (RESTING)", "EXTENDING SIDEWARDS", "UNKNOWN"]
        self.right_arm_postures = ["NEUTRAL (RESTING)", "EXTENDING SIDEWARDS", "UNKNOWN"]

        self.action_labels = self.head_postures + \
                             [f"LEFT ARM {p.upper()}" for p in self.left_arm_postures] + \
                             [f"RIGHT ARM {p.upper()}" for p in self.right_arm_postures] + \
                             ["TOTAL # of HUMANS DETECTED", "HIGHLY SUSPICIOUS", "MODERATELY SUSPICIOUS", "NON-SUSPICIOUS"]

        self.active_actions = set(self.action_labels)

        self.chart = QChart()
        self.chart.setTitle("Head and Arm Postures Over Time")
        self.chart.setAnimationOptions(QChart.AnimationOption.AllAnimations)

        self.series_dict = {label: QLineSeries(name=label) for label in self.action_labels}
        for series in self.series_dict.values():
            self.chart.addSeries(series)

        self.axis_x = QValueAxis()
        self.axis_x.setTitleText("Time (seconds)")
        self.axis_x.setLabelFormat("%.1f")
        self.axis_x.setRange(self.min_time / 30.0, self.max_time / 30.0)
        self.axis_x.setTickCount(min(10, (self.max_time - self.min_time) // 30 + 1))
        self.chart.addAxis(self.axis_x, Qt.AlignmentFlag.AlignBottom)

        self.axis_y = QValueAxis()
        self.axis_y.setTitleText("Students")
        self.axis_y.setRange(0, 45)
        self.axis_y.setTickCount(9)
        self.axis_y.setLabelFormat("%d")
        self.chart.addAxis(self.axis_y, Qt.AlignmentFlag.AlignLeft)

        for series in self.series_dict.values():
            series.attachAxis(self.axis_x)
            series.attachAxis(self.axis_y)

        self.scene = QGraphicsScene()
        self.chart_view = QChartView(self.chart)
        self.chart_view.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.chart_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        graphics_view_size = self.main_window.advanced_analytics_line_chart.size()
        self.chart_view.setMinimumSize(graphics_view_size)
        self.chart_view.setMaximumSize(graphics_view_size)

        self.scene.addWidget(self.chart_view)
        self.main_window.advanced_analytics_line_chart.setScene(self.scene)
        self.main_window.advanced_analytics_line_chart.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.main_window.advanced_analytics_line_chart.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.chart_view.fitInView(self.chart_view.sceneRect(), Qt.AspectRatioMode.KeepAspectRatio)

        self.chart.legend().setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.chart.legend().setFont(QFont("Arial", 10))
        self.chart.legend().setLayoutDirection(Qt.LayoutDirection.LeftToRight)

        self.axis_x.setLabelsFont(QFont("Arial", 10))
        self.axis_x.setLabelsAngle(0)
        self.axis_y.setLabelsFont(QFont("Arial", 10))
        self.axis_y.setTickCount(6)

        # Connect UI
        self.main_window.time_frame_range_slider_advanced_analytics_line_graph.valueChanged.connect(self.update_chart)
        self.main_window.advanced_analytics_actions_combo_box.addItems(["ALL ACTIONS"] + self.action_labels)
        self.main_window.advanced_analytics_actions_combo_box.currentTextChanged.connect(self.filter_chart_by_actions)
        self.main_window.time_frame_range_slider_advanced_analytics_line_graph.sliderReleased.connect(self.get_colors_all_frames)
        self.main_window.identify_suspicious_check_box_line_graph_advanced_analytics.stateChanged.connect(self.on_checkbox_changed)

        self.color_label_map = None
        self.color_counts_per_frame = None

        self.get_colors_all_frames()
        self.populate_chart()

    def get_colors_all_frames(self):
        self.color_label_map, self.color_counts_per_frame = self.main_window.get_colors_actions_from_tracker_all_frames(is_advanced_analytics=True)

    def is_suspicious_filter_active(self):
        return self.main_window.identify_suspicious_check_box_line_graph_advanced_analytics.isChecked()

    def populate_chart(self):
        for series in self.series_dict.values():
            self.chart.removeSeries(series)
            series.clear()
            series.setVisible(False)

        for frame_index in range(self.min_time, self.max_time + 1):
            time_value = frame_index / 30.0
            combined_counts = {label: 0 for label in self.action_labels}
            total_humans = 0

            if frame_index < len(self.head_posture_list_front):
                total_humans += len(self.main_window.human_detect_results_front[frame_index])
                for posture_data in self.head_posture_list_front[frame_index].values():
                    posture = posture_data['head_posture']
                    if posture in combined_counts:
                        combined_counts[posture] += 1

            if frame_index < len(self.head_posture_list_center):
                total_humans += len(self.main_window.human_detect_results_center[frame_index])
                for posture_data in self.head_posture_list_center[frame_index].values():
                    posture = posture_data['head_posture']
                    if posture in combined_counts:
                        combined_counts[posture] += 1

            if frame_index < len(self.arm_posture_list_front):
                for posture_data in self.arm_posture_list_front[frame_index].values():
                    right_label = f"RIGHT ARM {posture_data['right_arm_posture']}"
                    left_label = f"LEFT ARM {posture_data['left_arm_posture']}"
                    if right_label in combined_counts:
                        combined_counts[right_label] += 1
                    if left_label in combined_counts:
                        combined_counts[left_label] += 1

            if frame_index < len(self.arm_posture_list_center):
                for posture_data in self.arm_posture_list_center[frame_index].values():
                    right_label = f"RIGHT ARM {posture_data['right_arm_posture']}"
                    left_label = f"LEFT ARM {posture_data['left_arm_posture']}"
                    if right_label in combined_counts:
                        combined_counts[right_label] += 1
                    if left_label in combined_counts:
                        combined_counts[left_label] += 1

            combined_counts["TOTAL # of HUMANS DETECTED"] = total_humans

            if self.color_counts_per_frame and frame_index < len(self.color_counts_per_frame):
                frame_colors = self.color_counts_per_frame[frame_index]
                combined_counts["HIGHLY SUSPICIOUS"] = frame_colors.get("red", 0)
                combined_counts["MODERATELY SUSPICIOUS"] = frame_colors.get("orange", 0)
                combined_counts["NON-SUSPICIOUS"] = frame_colors.get("green", 0)

            for label in self.active_actions:
                if label in self.series_dict:
                    self.series_dict[label].append(time_value, combined_counts.get(label, 0))

        for label, series in self.series_dict.items():
            if label in self.active_actions:
                self.chart.addSeries(series)
                series.attachAxis(self.axis_x)
                series.attachAxis(self.axis_y)
                series.setVisible(True)


    def filter_chart_by_actions(self, selected_action: str):
        if self.is_suspicious_filter_active():
            self.active_actions = {"HIGHLY SUSPICIOUS", "MODERATELY SUSPICIOUS", "NON-SUSPICIOUS"}
        elif selected_action == "ALL ACTIONS":
            self.active_actions = set(self.action_labels)
        else:
            selected_actions = [action.strip().upper() for action in selected_action.split(",")]
            self.active_actions = set(selected_actions) if selected_actions else set(self.action_labels)
        self.populate_chart()

    def on_checkbox_changed(self):
        selected_action = self.main_window.advanced_analytics_actions_combo_box.currentText()
        self.filter_chart_by_actions(selected_action)

    def update_chart(self):
        self.min_time, self.max_time = self.main_window.time_frame_range_slider_advanced_analytics_line_graph.value()
        self.axis_x.setRange(self.min_time / 30.0, self.max_time / 30.0)
        self.populate_chart()

    def toggle_action(self, action, checked):
        if checked:
            self.active_actions.add(action)
        else:
            self.active_actions.discard(action)
        self.populate_chart()

    def export_to_excel(self):
        data = []
        for frame_index in range(self.min_time, self.max_time + 1):
            time_value = frame_index / 30.0  # Convert frame index to seconds
            frame_data = {"Time (s)": time_value}

            if frame_index < len(self.action_results_list_front):
                for track_id, action in self.action_results_list_front[frame_index].items():
                    frame_data[f"Front_Cam_Person_{track_id}"] = action

            if frame_index < len(self.action_results_list_center):
                for track_id, action in self.action_results_list_center[frame_index].items():
                    frame_data[f"Center_Cam_Person_{track_id}"] = action

            data.append(frame_data)

        # Convert to DataFrame
        df = pd.DataFrame(data)

        # Save to Excel file
        file_path, _ = QFileDialog.getSaveFileName(None, "Save Excel File", "", "Excel Files (*.xlsx)")
        if file_path:
            df.to_excel(file_path, index=False)

    def export_to_jpeg(self):
        # Ask user for save directory
        # Get the directory where the currently running script (main.py) is located
        script_dir = Path(__file__).parent

        # Create the "temp" folder inside the script directory
        temp_dir = script_dir / "temp"
        temp_dir.mkdir(parents=True, exist_ok=True)

        print(f"Temp directory path: {temp_dir}")

        if not temp_dir:  # User canceled
            print("Export canceled.")
            return

        original_active_actions = self.active_actions.copy()  # Save the original state

        def save_pixmap_to_file(pixmap, filepath):
            if pixmap.isNull():
                print(f"❌ Failed to capture pixmap for {filepath}")
                return

            buffer = QBuffer()
            buffer.open(QBuffer.ReadWrite)

            if pixmap.save(buffer, "JPG"):
                data = buffer.data()
                if data:
                    with open(filepath, "wb") as f:
                        f.write(data)
                        f.flush()
                        os.fsync(f.fileno())

                    if os.path.exists(filepath):
                        print(f"✅ Confirmed: {filepath} exists!")
                    else:
                        print(f"❌ File not found after saving: {filepath}")

                else:
                    print(f"❌ Buffer is empty for {filepath}")
            else:
                print(f"❌ pixmap.save() failed for {filepath}")

            buffer.close()

        # Export separate charts for each action
        for action in self.action_labels:
            self.active_actions = {action}  # Enable only one action
            self.populate_chart()
            self.chart.update()
            QApplication.processEvents()  # Force UI update

            # 🕒 **New: Delay to allow the UI to fully render**
            time.sleep(0.5)

            pixmap = self.chart_view.grab()
            action_filename = f"{action.replace(' ', '_')}_Advanced_Analytics.jpg"
            action_path = os.path.join(temp_dir, action_filename)
            save_pixmap_to_file(pixmap, action_path)

        # Export a chart with all actions
        self.active_actions = set(self.action_labels)  # Enable all actions
        self.populate_chart()
        self.chart.update()
        QApplication.processEvents()

        time.sleep(0.5)  # 🕒 **Ensure chart rendering before capture**

        pixmap = self.chart_view.grab()
        all_actions_path = os.path.join(temp_dir, "All_Actions.jpg")
        save_pixmap_to_file(pixmap, all_actions_path)

        # Restore original active actions
        self.active_actions = original_active_actions
        self.populate_chart()
        self.chart.update()
        QApplication.processEvents()

        print(f"📁 Charts saved in: {temp_dir}")