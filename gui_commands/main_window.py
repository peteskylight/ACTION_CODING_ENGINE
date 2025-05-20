import sys
import cv2
import os
import re
import numpy as np
import psutil
import GPUtil

from PySide6.QtWidgets import (QApplication,
                                QMainWindow,
                                QVBoxLayout,
                                QFileDialog,
                                QMessageBox,
                                QTableWidgetItem,
                                QWidget,
                                QButtonGroup,
                                QComboBox,
                                QLabel,
                                QDialog,
                                QLineEdit,
                                QDialogButtonBox,
                                QHBoxLayout
                                )
from PySide6.QtCore import QRect, QCoreApplication, QMetaObject, QTimer, QTime, Qt, QDate
from PySide6.QtGui import QImage, QPixmap, QFont, QIcon
from PySide6.QtCore import QTimer, QPropertyAnimation, QThread
from PySide6.QtGui import QEnterEvent
from PySide6.QtWidgets import QGraphicsOpacityEffect
from visualizations import Advanced_Analytics_Line_Chart_Visualization
from superqt import QRangeSlider

from ultralytics import YOLO

from pathlib import Path

from utils.drawing_utils import DrawingUtils

from utils import (Tools,
                   VideoUtils,
                   ThreadManager,
                   HeatmapView,
                   DocxGenerationThread,
                   EmailSendingWorker)

from trackers import PoseDetection

from gui_codes import Ui_MainWindow

from gui_commands import (CenterVideo,
                          FrontVideo,
                          CreateDataset,
                          AnalyticsTab,
                          AdvancedAnalyticsTab)

from visualizations import (AI_Analytics_Line_Chart_Visualization,
                            Advanced_Analytics_Line_Chart_Visualization,
                            AI_Analytics_Table_Events_Log,
                            Advanced_Analytics_Table_Events_Log,
                            AI_Analytics_Chunk_Summary_Log,
                            Advanced_Analytics_Chunk_Summary_Log,
                            Export_Heatmap_Image_Thread)

import copy

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        
        self.setupUi(self)
        
        '''
        GLOBAL VARIABLES INSTANCES
        '''
        self.FrontVideo = FrontVideo(main_window=self)
        self.CreateDataset = CreateDataset(main_window=self)
        self.AnalyticsTab = AnalyticsTab(main_window=self)
        self.AdvancedAnalyticsTab = AdvancedAnalyticsTab(main_window=self)
        self.CenterVideo = CenterVideo(main_window=self)
        
        self.fps = 20

        self.drawing_utils = DrawingUtils()
        self.tools_utils = Tools()
        self.video_utils = VideoUtils()
        self.ThreadManager = ThreadManager(main_window=self)

        # Load Seat Plan Image (for resetting heatmap)
        
        script_dir = Path(__file__).parent
        image_path = script_dir.parent / "assets" / "SEAT_PLAN.png"
        self.seat_plan_picture = cv2.imread(str(image_path))


        #IS PLAY/PAUSE BUTTON RUNNING?
        self.isAlreadyRunning = [False] * 10
        self.isRunningAndPaused = [False] * 10

                    # 0 - FOR PREVIEW
                    # 1 - FOR AI ANALYTICS - HEATMAP
                    # 2 - FOR AI ANALYTICS - LINE GRAPH
                    # 3 - FOR AI ANALYTICS - TABLE LOGS
                    # 4 - FOR ADVANCED ANALYTICS - HEATMAP
                    # 5 - FOR ADVANCED ANALYTICS - LINE GRAPH
                    # 6 - FOR ADVANCED ANALYTICS - TABLE LOGS

        
        
        #Set Default Panel: HOME - 0
        self.stackedPanels.setCurrentIndex(0)

        '''
        Connecting buttons to redirect to the stacked panels
        PANEL INDEX:
        HOME - 1
        CREATE DATASET - 2
        AI_ANALYTICS - 3
        IMPORT - 4
        ADVANCED_ANALYTICS - 5
        '''

        #============ FOR NAVIGATION FRAME PANE ========
        self.Home_button.clicked.connect(self.showHomePanel)
        self.Import_button.clicked.connect(self.showImportVideoPanel)
        self.sessionName_line_edit.returnPressed.connect(self.showImportVideoPanel) #Trigger when the etner button is pressed
        self.AI_analytics_button.clicked.connect(self.showAiAnalyticsPanel)
        self.Advanced_analytics_button.clicked.connect(self.showAdvancedAnalyticsPanel)
        self.Tutorial_button.clicked.connect(self.showTutorialPanel)
        self.Export_file_button.clicked.connect(self.showExportDataPanel)

        self.actionNew_Project.triggered.connect(self.showHomePanel)
        self.actionImport_Video.triggered.connect(self.showImportVideoPanel)
        self.actionAI_Analytics_Results.triggered.connect(self.showAiAnalyticsPanel)
        self.actionAdvanced_Analytics_Results.triggered.connect(self.showAdvancedAnalyticsPanel)
        self.actionTutorial.triggered.connect(self.showTutorialPanel)
        self.actionExport_Data_Analytics_Results.triggered.connect(self.showExportDataPanel)
        self.actionExit_Application.triggered.connect(self.confirm_exit)

        #============ FOR  PLAY AND PAUSE BUTTONS ===========
        '''
        Designed for managing thread. Assigning index on each button for thread calling.
        Each button/number has their own thread.

        THREADS ASSIGNMENT:
        # 0 - FOR PREVIEW
        # 1 - FOR AI ANALYTICS - HEATMAP
        # 2 - FOR AI ANALYTICS - LINE GRAPH
        # 3 - FOR AI ANALYTICS - TABLE LOGS
        # 4 - FOR ADVANCED ANALYTICS - HEATMAP
        # 5 - FOR ADVANCED ANALYTICS - LINE GRAPH
        # 6 - FOR ADVANCED ANALYTICS - TABLE LOGS
        
        '''
        #For preview after importing
        self.play_pause_button_video_preview.clicked.connect(self.play_and_pause_preview)
        
        # self.front_preview_video_keypoints_check_box.clicked.connect(self.disable_dark_mode_front)
        # self.front_preview_video_bounding_box_check_box.clicked.connect(self.disable_dark_mode_front)
        
        # self.center_preview_video_keypoints_check_box.clicked.connect(self.disable_dark_mode_center)
        # self.center_preview_video_bounding_box_check_box.clicked.connect(self.disable_dark_mode_center)
        
        #For AI Analytics
        self.play_pause_button_ai_analytics_heatmap.clicked.connect(self.play_and_pause_ai_analytics_heatmap)
        self.play_pause_button__ai_analytics_line_graph.clicked.connect(self.play_and_pause_ai_analytics_line_graph)
        self.play_pause_button_ai_analytics_table_event_logs.clicked.connect(self.play_and_pause_ai_analytics_table_logs)
        self.ai_analytics_event_summary_play_pause_button.clicked.connect(self.play_and_pause_ai_analytics_event_summary)
        

        #For Advanced Analytics
        self.play_pause_button_advanced_analytics_heatmap.clicked.connect(self.play_and_pause_advanced_analytics_heatmap)
        self.play_pause_button_advanced_analytics_line_graph.clicked.connect(self.play_and_pause_advanced_analytics_line_graph)
        self.play_pause_button_advanced_analytics_table_event_logs.clicked.connect(self.play_and_pause_advanced_analytics_table_logs)
        self.advanced_analytics_event_summary_play_pause_button.clicked.connect(self.play_and_pause_advanced_analytics_event_summary)
        
        #============ FOR VIEW TAB MENU ========
        self.actionCreate_Dataset.triggered.connect(self.showCreateDatasetPanel)
        self.actionCalibrate_Camera.triggered.connect(self.showCameraCalibrationPanel)
        self.actionAbout_Us_Panel.triggered.connect(self.showAboutUsPanel)
        
        #For confirming exit
        self.Exit_button.clicked.connect(self.confirm_exit)

        '''
        IMPORTING TAB CODE SECTION
        '''
        self.videoWidth = None
        self.videoHeight = None
        
        #============ FOR IMPORTING VIDEO TAB ===========
        
        #Create INSTANCES\
        self.human_detect_model = YOLO("yolov8x.pt")
        self.human_pose_model = YOLO("yolov8x-pose.pt")
        self.human_detect_conf = 0.5
        self.human_pose_conf = 0.5
        
        self.human_pose_detection = PoseDetection(humanDetectionModel="yolov8x.pt",
                                                  humanDetectConf=self.human_detect_conf,
                                                  humanPoseModel="yolov8x-pose.pt",
                                                  humanPoseConf=self.human_pose_conf)
        
        self.human_detect_results_front = []
        self.human_detect_results_center = []
        
        self.human_pose_results_front = []
        self.human_pose_results_center = []
        
        self.selected_human_detect_results_front = []
        self.selected_human_detect_results_center = []
        
        self.action_results_list_front = None
        self.action_results_list_center = None
        
        self.selected_action_results_list_front = None
        self.selected_action_results_list_center = None

        self.filtered_action_results_bboxes_front = None
        self.filtered_action_results_bboxes_center = None

        self.filtered_action_results_list_front = None
        self.filtered_action_results_list_center = None
        
        self.filtered_head_postures_list_front = None
        self.filtered_head_postures_list_center = None

        self.filtered_arms_postures_list_front = None
        self.filtered_arms_postures_list_center = None

        self.head_postures_list_front = None
        self.head_postures_list_center = None
        
        self.arms_postures_list_front = None
        self.arms_postures_list_center = None

        self.center_white_frames_preview = None
        self.front_white_frames_preview = None

        self.is_center_video_ready = False
        self.is_front_video_ready = False
        
        self.session_name = None

        self.frame_processing_value = None

        self.video_player_thread_preview = None
        self.video_player_thread_analytics = None
        self.video_player_thread_advanced_analytics = None
        
        self.import_video_button_center.clicked.connect(self.CenterVideo.browse_video)

        

        self.import_video_button_front.clicked.connect(self.FrontVideo.browse_video)

        #=====GET FOOTAGE ANALYTICS
        self.are_videos_ready = False
        self.whole_classroom_height = 1080
        self.center_video_height = 700
        self.front_starting_y = 0
        self.center_starting_y = 0

        #self.analyze_video_button.clicked.connect(self.switch_to_analytics_tab)

        # self.play_pause_button_analytics.clicked.connect(self.toggle_play_pause_analytics)


        #Adjust this according to video but meh. This is just the default. Just check the specs of the cam. Default naman sya all the times
        self.center_video_interval = 1000//30 #30 fps
        self.front_video_interval = 1000//30 #30 fps

        self.clock_interval = 1000  # 1 second interval for clock
        self.toggle_record_label_interval = 750

        self.center_video_counter = 0
        self.front_video_counter = 0
        self.cropped_center_video_counter = 0
        self.cropped_front_video_counter = 0

        
        self.clock_counter = 0
        self.toggle_record_label_counter = 0
        self.toggle_import_indicator = 0
        self.center_video_frame_counter = 0        
        self.front_video_frame_counter = 0

        self.cropped_center_video_frame_counter = 0
        self.cropped_front_video_frame_counter = 0

        self.time_range_start_time = 0
        self.time_range_end_time = 0
        
        self.current_frame_index = 0
        
        #TIME FRAME CONTAINERS FOR ADVANCED ANALYTICS

        self.time_frame_slider_import_preview = QRangeSlider(Qt.Horizontal)
        self.time_frame_slider_import_preview.setMinimum(0)  # Example duration
        self.time_frame_slider_import_preview.setMaximum(100)  # Example duration
        self.time_frame_slider_import_preview.setValue((20, 80))  # Default selected range
        self.time_frame_slider_import_preview.setFixedHeight(40)
        
        self.time_frame_range_slider_advanced_analytics_heatmap = QRangeSlider(Qt.Horizontal)
        self.time_frame_range_slider_advanced_analytics_heatmap.setMinimum(0)  # Example duration
        self.time_frame_range_slider_advanced_analytics_heatmap.setMaximum(100)  # Example duration
        self.time_frame_range_slider_advanced_analytics_heatmap.setValue((20, 80))  # Default selected range
        self.time_frame_range_slider_advanced_analytics_heatmap.setFixedHeight(40)

        self.time_frame_range_slider_advanced_analytics_line_graph = QRangeSlider(Qt.Horizontal)
        self.time_frame_range_slider_advanced_analytics_line_graph.setMinimum(0)  # Example duration
        self.time_frame_range_slider_advanced_analytics_line_graph.setMaximum(100)  # Example duration
        self.time_frame_range_slider_advanced_analytics_line_graph.setValue((20, 80))  # Default selected range
        self.time_frame_range_slider_advanced_analytics_line_graph.setFixedHeight(40)

        self.time_frame_range_slider_advanced_analytics_table_event_logs = QRangeSlider(Qt.Horizontal)
        self.time_frame_range_slider_advanced_analytics_table_event_logs.setMinimum(0)  # Example duration
        self.time_frame_range_slider_advanced_analytics_table_event_logs.setMaximum(100)  # Example duration
        self.time_frame_range_slider_advanced_analytics_table_event_logs.setValue((20, 80))  # Default selected range
        self.time_frame_range_slider_advanced_analytics_table_event_logs.setFixedHeight(40)
        
        self.time_frame_range_slider_advanced_analytics_table_event_summary = QRangeSlider(Qt.Horizontal)
        self.time_frame_range_slider_advanced_analytics_table_event_summary.setMinimum(0)  # Example duration
        self.time_frame_range_slider_advanced_analytics_table_event_summary.setMaximum(100)  # Example duration
        self.time_frame_range_slider_advanced_analytics_table_event_summary.setValue((20, 80))  # Default selected range
        self.time_frame_range_slider_advanced_analytics_table_event_summary.setFixedHeight(40)

        # Replace placeholder with actual QRangeSlider
        layout_adv_analytics_heatmap = QVBoxLayout(self.time_frame_container_import_preview)
        layout_adv_analytics_heatmap.addWidget(self.time_frame_slider_import_preview)
        
        layout_adv_analytics_heatmap = QVBoxLayout(self.time_frame_container_heatmap_advanced_analytics)
        layout_adv_analytics_heatmap.addWidget(self.time_frame_range_slider_advanced_analytics_heatmap)

        layout_adv_analytics_line_graph = QVBoxLayout(self.time_frame_container_line_graph_advanced_analytics)
        layout_adv_analytics_line_graph.addWidget(self.time_frame_range_slider_advanced_analytics_line_graph)

        layout_adv_analytics_table_event_logs = QVBoxLayout(self.time_frame_container_table_event_logs_advanced_analytics)
        layout_adv_analytics_table_event_logs.addWidget(self.time_frame_range_slider_advanced_analytics_table_event_logs)
        
        layout_ai_analytics_table_event_logs = QVBoxLayout(self.time_frame_container_table_event_summary_advanced_analytics)
        layout_ai_analytics_table_event_logs.addWidget(self.time_frame_range_slider_advanced_analytics_table_event_summary)

        
        #TIME FRAME CONTAINERS FOR AI ANALYTICS

        self.time_frame_range_slider_ai_analytics_heatmap = QRangeSlider(Qt.Horizontal)
        self.time_frame_range_slider_ai_analytics_heatmap.setMinimum(0)  # Example duration
        self.time_frame_range_slider_ai_analytics_heatmap.setMaximum(100)  # Example duration
        self.time_frame_range_slider_ai_analytics_heatmap.setValue((20, 80))  # Default selected range
        self.time_frame_range_slider_ai_analytics_heatmap.setFixedHeight(40)

        self.time_frame_range_slider_ai_analytics_line_graph = QRangeSlider(Qt.Horizontal)
        self.time_frame_range_slider_ai_analytics_line_graph.setMinimum(0)  # Example duration
        self.time_frame_range_slider_ai_analytics_line_graph.setMaximum(100)  # Example duration
        self.time_frame_range_slider_ai_analytics_line_graph.setValue((20, 80))  # Default selected range
        self.time_frame_range_slider_ai_analytics_line_graph.setFixedHeight(40)

        self.time_frame_range_slider_ai_analytics_table_event_logs = QRangeSlider(Qt.Horizontal)
        self.time_frame_range_slider_ai_analytics_table_event_logs.setMinimum(0)  # Example duration
        self.time_frame_range_slider_ai_analytics_table_event_logs.setMaximum(100)  # Example duration
        self.time_frame_range_slider_ai_analytics_table_event_logs.setValue((20, 80))  # Default selected range
        self.time_frame_range_slider_ai_analytics_table_event_logs.setFixedHeight(40)
        
        self.time_frame_range_slider_ai_analytics_table_event_summary = QRangeSlider(Qt.Horizontal)
        self.time_frame_range_slider_ai_analytics_table_event_summary.setMinimum(0)  # Example duration
        self.time_frame_range_slider_ai_analytics_table_event_summary.setMaximum(100)  # Example duration
        self.time_frame_range_slider_ai_analytics_table_event_summary.setValue((20, 80))  # Default selected range
        self.time_frame_range_slider_ai_analytics_table_event_summary.setFixedHeight(40)

        #CONNECT THE SLIDERS FOR IT TO BE RESPONSIVE TO THE DISPLAY
        self.time_frame_slider_import_preview.sliderReleased.connect(self.reset_video_playing_to_start)
        self.time_frame_range_slider_advanced_analytics_heatmap.sliderReleased.connect(self.reset_video_playing_to_start)
        self.time_frame_range_slider_advanced_analytics_line_graph.sliderReleased.connect(self.reset_video_playing_to_start)
        self.time_frame_range_slider_advanced_analytics_table_event_logs.sliderReleased.connect(self.reset_video_playing_to_start)
        self.time_frame_range_slider_advanced_analytics_table_event_summary.sliderReleased.connect(self.reset_video_playing_to_start)
        
        self.time_frame_range_slider_ai_analytics_heatmap.sliderReleased.connect(self.reset_video_playing_to_start)
        self.time_frame_range_slider_ai_analytics_line_graph.sliderReleased.connect(self.reset_video_playing_to_start)
        self.time_frame_range_slider_ai_analytics_table_event_logs.sliderReleased.connect(self.reset_video_playing_to_start)
        self.time_frame_range_slider_ai_analytics_table_event_summary.sliderReleased.connect(self.reset_video_playing_to_start)
        
        
        # Replace placeholder with actual QRangeSlider
        layout_ai_analytics_heatmap = QVBoxLayout(self.time_frame_container_heatmap_ai_analytics)
        layout_ai_analytics_heatmap.addWidget(self.time_frame_range_slider_ai_analytics_heatmap)

        layout_ai_analytics_line_graph = QVBoxLayout(self.time_frame_container_line_graph_ai_analytics)
        layout_ai_analytics_line_graph.addWidget(self.time_frame_range_slider_ai_analytics_line_graph)

        layout_ai_analytics_table_event_logs = QVBoxLayout(self.time_frame_container_table_event_logs_ai_analytics)
        layout_ai_analytics_table_event_logs.addWidget(self.time_frame_range_slider_ai_analytics_table_event_logs)
        
        layout_ai_analytics_table_event_logs = QVBoxLayout(self.time_frame_container_table_event_summary_ai_analytics)
        layout_ai_analytics_table_event_logs.addWidget(self.time_frame_range_slider_ai_analytics_table_event_summary)
        

        #============ FOR HOME TAB =================
        self.start_button.clicked.connect(self.showImportVideoPanel)

        self.AI_Analytics_Line_Chart_Visualization = None
        self.AI_Analytics_Table_Event_Logs = None
        self.AI_Analytics_Event_Summary = None
        self.Advanced_Analytics_Event_Summary = None

        
        #============= HEATMAP COLORS =====================
        self.action_colors = {
                            'LEFT ARM EXTENDING SIDEWARDS': (255, 99, 71),   # Tomato Red
                            'LEFT ARM NEUTRAL (RESTING)': (34, 139, 34),     # Forest Green
                            'LEFT ARM UNKNOWN': (138, 43, 226),              # Blue Violet
                            'RIGHT ARM EXTENDING SIDEWARDS': (255, 140, 0),   # Dark Orange
                            'RIGHT ARM NEUTRAL (RESTING)': (70, 130, 180),   # Steel Blue
                            'RIGHT ARM UNKNOWN': (32, 178, 170),             # Light Sea Green
                            'FACING DOWNWARDS': (255, 223, 0),                # Bright Yellow
                            'FACING FORWARD': (0, 206, 209),                 # Dark Turquoise
                            'FACING LEFT': (255, 105, 180),                  # Hot Pink
                            'FACING RIGHT': (186, 85, 211),                  # Medium Orchid
                            'SITTING': (205, 133, 63),                       # Peru
                            'STANDING': (169, 169, 169),                     # Dark Gray
                            'UNKNOWN': (192, 192, 192),                      # Silver
                            }


        self.identify_suspicious_check_box_line_graph_ai_analytics.clicked.connect(self.toggle_suspicious)
        
        #============ FOR AI ANALYTICS TAB =================
        self.play_icon = QIcon(":/icons/play-256.png")   # Play icon from resources
        self.pause_icon = QIcon(":/icons/pause-256.png") # Pause icon from resources
        
        #self.view_ai_analytics_button.clicked.connect(self.switch_ai_analytics_inner_panel)
        self.ai_analytics_visualization_combo_box.currentTextChanged.connect(self.switch_ai_analytics_inner_panel)

        self.view_button_ai_analytics_heatmap.clicked.connect(self.heatmap_update_selected_action_ai_analytics)
        
        

        #============ FOR ADVANCED ANALYTICS ===============
        
        self.stacked_panels_arrangement = [2,0,1]
        self.advanced_analytics_visualization_combo_box.currentTextChanged.connect(self.switch_page_advanced_analytics)
        
        self.advanced_analytics_table_event_logger = None
        
        # self.heatmap_graphics_view_advanced_analytics: HeatmapView = self.findChild(HeatmapView, "heatmap_advanced_analytics_graphics_view")
        
        self.view_button_advanced_analytics_heatmap.clicked.connect(self.heatmap_update_selected_action_advanced_analytics)
                                                                                                                                    
        
        # self.suspicious_criteria = {
        #                             'red_actions': ['LEFT ARM EXTENDING SIDEWARDS', 'RIGHT ARM EXTENDING SIDEWARDS'],
        #                             'orange_actions': ['RIGHT ARM UNKNOWN', 'LEFT ARM UNKNOWN', 'FACING DOWN', 'SITTING'],
        #                             'green_actions': ['STANDING'],
        #                             'min_consistent_frames': {
        #                                 'FACING DOWNWARDS': 30,
        #                                 'FACING FORWARD':30,
        #                                 'FACING LEFT': 30,
        #                                 'FACING RIGHT': 30,
        #                                 'LEFT ARM EXTENDING SIDEWARDS': 30,
        #                                 'RIGHT ARM EXTENDING SIDEWARDS': 30,
        #                                 'SITTING': 30,
        #                                 'STANDING': 30
        #                                 },
                                     
        #                             'repetition_thresholds': {
        #                                 'LEFT ARM EXTENDING SIDEWARDS': 2,
        #                                 'RIGHT ARM EXTENDING SIDEWARDS': 3
        #                             },
        #                             'repetition_interval': 15
        #                         }

        
        self.suspicious_criteria = {
                                        'red_actions': [],
                                        'orange_actions': [],
                                        'green_actions': [],
                                        'min_consistent_frames': {},
                                        'repetition_thresholds': {},
                                        'repetition_interval': 15
                                    }
        
        self.suspicious_criteria_empty = {
                                        'red_actions': [],
                                        'orange_actions': [],
                                        'green_actions': [],
                                        'min_consistent_frames': {},
                                        'repetition_thresholds': {},
                                        'repetition_interval': 15
                                    }
        
        self.default_criteria = {
                                    'red_actions': ['LEFT ARM EXTENDING SIDEWARDS', 'RIGHT ARM EXTENDING SIDEWARDS'],
                                    'orange_actions': ['RIGHT ARM UNKNOWN', 'LEFT ARM UNKNOWN'],
                                    'green_actions': ['STANDING', 'SITTING', 'FACING DOWN'],
                                    'min_consistent_frames': {
                                        'FACING DOWNWARDS': 30,               # 1 sec – considered normal
                                        'FACING FORWARD': 30,                 # 1 sec – normal
                                        'FACING LEFT': 150,                   # ≥5 sec for red suspicion
                                        'FACING RIGHT': 150,                  # ≥5 sec for red suspicion
                                        'LEFT ARM EXTENDING SIDEWARDS': 30,   # 1 sec – base threshold
                                        'RIGHT ARM EXTENDING SIDEWARDS': 30,
                                        'SITTING': 30,                        # Always green – kept minimal
                                        'STANDING': 90                        # >3 sec may be red depending on context
                                    },
                                    'repetition_thresholds': {
                                        'LEFT ARM EXTENDING SIDEWARDS': 3,    # >2 times = red
                                        'RIGHT ARM EXTENDING SIDEWARDS': 3
                                    },
                                    'repetition_interval': 15                # Remains unchanged (may be used for tracking frequency)
                                }

                                        
        
        
        self.suspicion_level_mapping = {
                                            "HIGHLY SUSPICIOUS": "red_actions",
                                            "MODERATELY SUSPICIOUS": "orange_actions",
                                            "NON-SUSPICIOUS": "green_actions"
                                        }
        self.all_actions = [
                                "LEFT ARM EXTENDING SIDEWARDS", "RIGHT ARM EXTENDING SIDEWARDS",
                                "RIGHT ARM UNKNOWN", "LEFT ARM UNKNOWN", "FACING DOWN",
                                "SITTING", "STANDING", "FACING FORWARD", "FACING LEFT", "FACING RIGHT"
                            ]

        for action in self.all_actions:
            self.actions_suspicion_level_combo_box.addItem(action)
            self.actions_length_combo_box.addItem(action)
            self.actions_repitiion_length_combo_box.addItem(action)


        #================= CALIBRATING SUSPICIOUSNESS ========================
        
        self.add_action_suspicion_level_button.clicked.connect(self.add_action_suspicion_level)
        self.add_action_length_button.clicked.connect(self.add_action_length)
        self.add_action_repitition_length_button.clicked.connect(self.add_repetition_length)
        self.reset_tables_button.clicked.connect(self.reset_tables)
        self.clear_tables_button.clicked.connect(self.clear_tables)
        
        
        #============ FOR GENERATING REPORTS TAB ===========
        # self.generate_report_to_docx_button.clicked.connect(self.generate_data_to_docx)
        # self.generate_data_detections_button.clicked.connect(self.generate_detections_video)
        
        self.generate_document_report.clicked.connect(self.generate_data_and_media)
        
        self.send_to_email_button.clicked.connect(self.open_email_dialog)
        
        self.time_exported = None
        
        self.chosen_directory = None
        
        # self.export_media_button.clicked.connect(self.generate_media)

        self.add_bounding_box_check_box.clicked.connect(self.update_add_bounding_box_status)
        self.add_keypoints_check_box.clicked.connect(self.update_add_keypoints_status)
        
        self.document_export_combo_box.currentTextChanged.connect(self.update_media_options)
        
        self.max_frames = 0

        #============ FOR CREATE DATASET TAB ============
        #Disable Maximize Button
        
        self.setWindowFlag(Qt.WindowMaximizeButtonHint, False)

        self.closeCamera.clicked.connect(self.CreateDataset.stop_camera)
        self.openCamera.clicked.connect(self.CreateDataset.start_camera)
        self.browseButton.clicked.connect(self.browse_button_functions)
        self.refresh_button.clicked.connect(lambda: self.CreateDataset.scan_directory(self.directoryLineEdit.text()))
        self.add_action_button.clicked.connect(self.CreateDataset.add_folder)
        self.delete_action_button.clicked.connect(self.CreateDataset.delete_folder)
        self.recording_button.clicked.connect(self.toggle_button)
        self.refresh_action_list.clicked.connect(self.CreateDataset.showActionsToTable)
        self.CreateDataset.populate_camera_combo_box()

        # Slider Value Change
        self.interval_slider.valueChanged.connect(self.updateIntervalLabel)
        self.sequence_slider.valueChanged.connect(self.updateSequenceLabel)
        
        # Set Column Names
        self.action_table.setHorizontalHeaderLabels(["Actions", "# of Recordings"])
        
        # Center the window on the screen
        self.center()
        
        #Set the date:
        current_date = QDate.currentDate().toString()
        
        self.day_label.setText(f"{current_date}")\
        
        self.actions_list = np.array(['FACING DOWNWARDS', 'FACING FORWARD', 'FACING LEFT', 'FACING RIGHT', 'LEFT ARM EXTENDING SIDEWARDS', 'RIGHT ARM EXTENDING SIDEWARDS', 'SITTING', 'STANDING'])

        '''
        CAMERA ANGLES:
        0 - Front
        1 - Center
        2 - Both Front & Center
        '''
        
        self.camera_angle = 0
        '''
        DETECTION TYPES:
        0 - Ai Analytics
        1 - Advanced Analytics
        '''
        self.detection_type = 0 
        
        '''
        THIS IS FOR BUBBLE MESSAGE AFTER PROCESSING
        '''
        # Bubble Message (QLabel)
        self.bubble_label = QLabel("Video Processing Completed!\n\n\n\n\n\n< You may now view the action data\nanalytics here!\n\n\n\n\n\n\n\n< EXPORT option is also available!", self)
        self.bubble_label.setGeometry(180, 110, 275, 290)  # Position beside button
        self.bubble_label.setStyleSheet(
            """
            QLabel {
                background: lightblue;
                color: black;
                font-size: 14px;
                font-family: 'NSimSun';
                padding: 10px 15px;
                border-radius: 15px;
                border: 2px solid #0078D7;
            }
            """
        )
        self.bubble_label.setFont(QFont("NSimSun", 12))
        self.bubble_label.setVisible(False)

        # Opacity Effect
        self.opacity_effect = QGraphicsOpacityEffect()
        self.bubble_label.setGraphicsEffect(self.opacity_effect)
        self.opacity_effect.setOpacity(0)

        # Fade Animation
        self.animation = QPropertyAnimation(self.opacity_effect, b"opacity")
        self.animation.setDuration(500)  # 500ms fade in/out
        
        self.add_keypoints_drawing = "No"
        self.add_bounding_box_drawing = "No"
        
        self.reset_tables()

        # Timer for auto fade-out
        self.fade_timer = QTimer()
        self.fade_timer.timeout.connect(self.fade_out_bubble)

        # Event filter for hover effect
        self.bubble_label.installEventFilter(self)

        self.timer = QTimer(self) #TIMER FOR ALL!!!
        self.timer.timeout.connect(self.update_all_with_timers) #=======Update all and just have conditional statements
        self.timer.start(10) 
        
    #FOR STACK PANELS IN MAIN WINDOW
    def showHomePanel(self): #FOR SHOWING HOME PANEL
        self.ThreadManager.stop_current_thread()
        self.stackedPanels.setCurrentIndex(0)

        self.actionNew_Project.setEnabled(False)
        self.actionAI_Analytics_Results.setEnabled(False)
        self.actionAdvanced_Analytics_Results.setEnabled(False)
        self.actionImport_Video.setEnabled(False)
        self.actionExport_Data_Analytics_Results.setEnabled(False)

    def all_summary_chunks(self):
        if self.AI_Analytics_Event_Summary is not None and self.Advanced_Analytics_Event_Summary is not None:
            merged_postures = {}
            for frame_index in range(0, self.max_frames):
                if self.action_results_list_front:
                    merged_postures.update(self.action_results_list_front[frame_index])  # or [-1] for last

                if self.action_results_list_center:
                    merged_postures.update(self.action_results_list_center[frame_index])  # or [-1]
                    
                self.AI_Analytics_Event_Summary.update_frame(frame_index=frame_index,
                                                                postures_dict=merged_postures)

                self.Advanced_Analytics_Event_Summary.update_frame(frame_index=frame_index,
                                                                head_posture_list_front=self.head_postures_list_front,
                                                                head_posture_list_center=self.head_postures_list_center,
                                                                arms_posture_list_front=self.arms_postures_list_front,
                                                                arms_posture_list_center=self.arms_postures_list_center
                                                                )
            
        
        
    def update_current_frame_index(self, frame_index):
        self.current_frame_index = frame_index
        self.update_movement_quantities_ai_analytics_line_chart(current_index=frame_index)
        
        self.update_movement_quantities_advanced_analytics_line_chart(current_index=frame_index)
        
        if self.AI_Analytics_Table_Event_Logs is not None:
            self.AI_Analytics_Table_Event_Logs.update_logs_every_n_frames(current_frame=frame_index)
            
        if self.advanced_analytics_table_event_logger is not None:
            self.advanced_analytics_table_event_logger.update_logs_every_n_frames(current_frame=frame_index)
        
        if self.AI_Analytics_Event_Summary is not None and (self.ai_analytics_event_summary_play_pause_button.text() == "PAUSE PREVIEW"):
            print("ATTEMPT TO UPDATE FRAME")
            
            # Merge front and center for the current frame
            merged_postures = {}

            if self.action_results_list_front:
                merged_postures.update(self.action_results_list_front[frame_index])  # or [-1] for last

            if self.action_results_list_center:
                merged_postures.update(self.action_results_list_center[frame_index])  # or [-1]
            

            # Call the logger's update function
            self.AI_Analytics_Event_Summary.update_frame(frame_index=frame_index,
                                                         postures_dict=merged_postures)
        
        if self.Advanced_Analytics_Event_Summary is not None and (self.advanced_analytics_event_summary_play_pause_button.text() == "PAUSE PREVIEW"):
            self.Advanced_Analytics_Event_Summary.update_frame(frame_index=frame_index,
                                                               head_posture_list_front=self.head_postures_list_front,
                                                               head_posture_list_center=self.head_postures_list_center,
                                                               arms_posture_list_front=self.arms_postures_list_front,
                                                               arms_posture_list_center=self.arms_postures_list_center
                                                               )
        


    def showAiAnalyticsPanel(self):
        self.ThreadManager.stop_current_thread()
        self.reset_video_playing_boolean()
        
        self.identify_suspicious_check_box_heatmap_advanced_analytics.setChecked(False)
        self.identify_suspicious_check_box_line_graph_advanced_analytics.setChecked(False)

        #self.activate_analytics(activation=True)
        self.play_pause_button_video_preview.setText("PLAY PREVIEW")
        
        self.stackedPanels.setCurrentIndex(2)

    def get_colors_actions_from_tracker_all_frames(self, is_advanced_analytics):
        red_actions = self.suspicious_criteria.get('red_actions', [])
        orange_actions = self.suspicious_criteria.get('orange_actions', [])
        green_actions = self.suspicious_criteria.get('green_actions', [])
        min_consistent_frames_dict = self.suspicious_criteria.get('min_consistent_frames', {})
        repetition_thresholds = self.suspicious_criteria.get('repetition_thresholds', {})
        repetition_interval = self.suspicious_criteria.get('repetition_interval', 15)

        if is_advanced_analytics:
            arms_front = self.arms_postures_list_front
            arms_center = self.arms_postures_list_center
            head_front = self.head_postures_list_front
            head_center = self.head_postures_list_center

            combined_results = []
            for a_f, a_c, h_f, h_c in zip(arms_front, arms_center, head_front, head_center):
                frame_dict = {}
                for track_id, arm_data in {**a_f, **a_c}.items():
                    frame_dict.setdefault(track_id, {}).update(arm_data)
                for track_id, head_data in {**h_f, **h_c}.items():
                    frame_dict.setdefault(track_id, {}).update(head_data)
                combined_results.append(frame_dict)
        else:
            action_results_front = self.action_results_list_front
            action_results_center = self.action_results_list_center
            combined_results = [
                {**front, **center}
                for front, center in zip(action_results_front, action_results_center)
            ]

        color_label_map = [{} for _ in combined_results]
        color_counts_per_frame = []
        track_histories = {}

        for frame_idx, frame in enumerate(combined_results):
            color_counts = {'green': 0, 'orange': 0, 'red': 0}

            for track_id, data in frame.items():
                # Determine the relevant label
                if isinstance(data, dict):
                    label = data.get('left_arm_posture') or data.get('right_arm_posture') or data.get('head_posture') or 'UNKNOWN'
                else:
                    label = data

                # Get per-action min_consistent_frames value
                min_consistent_frames = min_consistent_frames_dict.get(label, 30)

                # Initialize trackers
                track_histories.setdefault(track_id, [])

                # Update label history
                track_histories[track_id].append(label)
                if len(track_histories[track_id]) > min_consistent_frames:
                    track_histories[track_id].pop(0)

                # Default
                color = (0, 255, 0)
                tag = ""

                # Handle repetition-based logic if action is being tracked for repetition
                if label in repetition_thresholds:
                    history = track_histories[track_id]
                    count_in_window = history.count(label)
                    max_allowed = repetition_thresholds[label]

                    if count_in_window > max_allowed:
                        color = (0, 0, 255)  # Red
                        tag = "HIGHLY SUSPICIOUS"
                    elif 0 < count_in_window <= max_allowed:
                        color = (0, 255, 255)  # Orange
                        tag = "MODERATELY SUSPICIOUS"
                    else:
                        color = (0, 255, 0)
                        tag = "NON-SUSPICIOUS"


                else:
                    # Fallback to consistency-based color coding
                    history = track_histories[track_id]
                    is_consistent = (
                        len(history) == min_consistent_frames and
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

                # Count color
                if color == (0, 255, 0):
                    color_counts['green'] += 1
                elif color == (0, 255, 255):
                    color_counts['orange'] += 1
                elif color == (0, 0, 255):
                    color_counts['red'] += 1

            color_counts_per_frame.append(color_counts)

        if self.identify_suspicious_check_box_line_graph_advanced_analytics.isChecked() or self.identify_suspicious_check_box_line_graph_ai_analytics.isChecked():
            return color_label_map, color_counts_per_frame
        else:
            fallback = []
            fallback_counts = []
            for frame in combined_results:
                fallback.append({
                    track_id: ((0, 255, 0), "") for track_id in frame.keys()
                })
                fallback_counts.append({'green': len(frame), 'orange': 0, 'red': 0})
            return fallback, fallback_counts



    def showAdvancedAnalyticsPanel(self):
        self.ThreadManager.stop_current_thread()
        self.reset_video_playing_boolean()
        self.identify_suspicious_check_box_heatmap_ai_analytics.setChecked(False)
        self.identify_suspicious_check_box_line_graph_ai_analytics.setChecked(False)

        # from visualizations import Advanced_Analytics_Line_Chart_Visualization

        self.stackedPanels.setCurrentIndex(3)
    
    def showTutorialPanel(self):
        self.ThreadManager.stop_current_thread()
        self.reset_video_playing_boolean()
        
        self.stackedPanels.setCurrentIndex(5)
    
    def showExportDataPanel(self):
        self.ThreadManager.stop_current_thread()
        self.reset_video_playing_boolean()
        
        self.stackedPanels.setCurrentIndex(4)
    
    def showImportVideoPanel(self):
        self.ThreadManager.stop_current_thread()
        self.reset_video_playing_boolean()

        retrieve_session_name = self.sessionName_line_edit.text().strip()
        
        if re.fullmatch(r"[A-Za-z0-9 ]{5,}", retrieve_session_name):
            
            
            self.session_name = self.sessionName_line_edit.text()
            
        else:
            QMessageBox.information(self, "Invalid", "Session name must be at least 5 characters long and contain only letters, numbers, and spaces.")
            return

        self.Import_button.setEnabled(True)
        self.actionNew_Project.setEnabled(True)
        self.session_name_label.setText(str(self.session_name))
        self.stackedPanels.setCurrentIndex(1)

    def showCreateDatasetPanel(self):
        self.stackedPanels.setCurrentIndex(6)
    
    def showCameraCalibrationPanel(self):
        self.stackedPanels.setCurrentIndex(7)
        
        
    def showAboutUsPanel(self):
        self.stackedPanels.setCurrentIndex(8)
        
    #======= FOR SHOWING INNER PANEL IN AI ANALYTICS PANEL ==============
    
    def stop_all_video_player_threads(self):

        self.ThreadManager.stop_current_thread()
        self.reset_video_playing_boolean()


    def switch_ai_analytics_inner_panel(self):
        """Change the stacked widget page based on the selected combo box option."""

        selected_option = int(self.ai_analytics_visualization_combo_box.currentIndex())  # Get selected text

        print("SELECTED OPTION:", selected_option)
        # Map options to stacked widget indexes
        if selected_option == 0:
            self.stacked_panels_ai_analytics.setCurrentIndex(0)
            self.ai_analytics_label.setText("AI VISUALIZATIONS - HEATMAP")
        
        if selected_option == 1:
            self.stacked_panels_ai_analytics.setCurrentIndex(1)  
            self.ai_analytics_label.setText("AI VISUALIZATIONS - LINE GRAPH")
            
        if selected_option == 2:
            self.stacked_panels_ai_analytics.setCurrentIndex(2)  # 
            self.ai_analytics_label.setText("AI VISUALIZATIONS - EVENT LOGS")
        
        if selected_option == 3:
            self.stacked_panels_ai_analytics.setCurrentIndex(3)  # 
            self.ai_analytics_label.setText("AI VISUALIZATIONS - EVENT SUMMARY")
            
    def confirm_exit(self):
        reply = QMessageBox.question(
            self, "Exit Confirmation", "Are you sure you want to exit?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            QApplication.quit()  # Properly closes the application

    def update_all_with_timers(self):

        
        self.clock_counter += self.timer.interval()
        self.toggle_record_label_counter += self.timer.interval()
                

        if self.clock_counter >= self.clock_interval:
            self.CreateDataset.update_usage()
            self.CreateDataset.update_time()
            self.clock_counter = 0

        if self.toggle_record_label_counter >= self.toggle_record_label_interval:
            self.toggleLabelVisibility()
            self.toggle_record_label_counter = 0
        
    
    def center(self):
        '''
        This centers the appearance of the window on the screen.
        '''
        # Get the screen geometry
        screen = QApplication.primaryScreen()
        screen_geometry = screen.availableGeometry()
        # Get the window geometry
        window_geometry = self.frameGeometry()
        # Move the window to the center of the screen
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    #THIS IS FOR CREATE DATASET
    '''
    THIS AREA NEEDS MAINTENANCE!!!
    '''
    def browse_button_functions(self):
        self.CreateDataset.open_file_explorer()
        self.CreateDataset.showActionsToTable()

    def startBlinking(self):
        self.status_label.setStyleSheet("""
                QLabel {
                    color: rgb(0, 255, 0);
                }
            """)
        self.status_label.setVisible(True) # Ensure the label is visible when starting
    
    def stopBlinking(self):
        self.status_label.setStyleSheet("""
                QLabel {
                    color: rgb(0, 255, 0);
                }
            """)
        self.blink_timer.stop()
        self.status_label.setText("NOT RECORDING")
        self.status_label.setVisible(True)
        
    def toggleLabelVisibility(self):
        self.status_label.setVisible(not self.status_label.isVisible())
        
    def updateIntervalLabel(self, value):
        self.interval_label.setText(str(value))
        
    def updateSequenceLabel(self, value):
        self.sequence_label.setText(str(value))
    

    def toggle_button(self):
        if self.recording_button.text() == "START\nRECORDING":
            self.recording_button.setText("STOP\nRECORDING")
            self.recording_button.setStyleSheet("""
                QPushButton {
                    background-color: rgb(170, 0, 0);
                    border-radius: 15px; /* Adjust the radius as needed */
                    color: black; /* Set the text color */
                    border: 1px solid black; /* Optional: Add a border */
                }
            """)
            self.status_label.setText("RECORDING")
            self.startBlinking()
            
        else:
            self.recording_button.setText("START\nRECORDING")
            self.recording_button.setStyleSheet("""
                QPushButton {
                    background-color: rgb(170, 255, 127);
                    border-radius: 15px; /* Adjust the radius as needed */
                    color: black; /* Set the text color */
                    border: 1px solid black; /* Optional: Add a border */
                }
            """)
            self.status_label.setText("NOT RECORDING")
    
    
    #template for warning message boxes:
    def show_warning_message(self, status_title, message):
        # Create and show a warning message box
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Warning)
        msg_box.setWindowTitle(status_title)
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.Ok)
        msg_box.exec()

    '''
    THIS AREA IS FOR VIDEO PLAYER THREAD MANAGEMENT
    '''

    def set_bool_default(self):
        for value in self.isAlreadyRunning:
            value = False

    def play_and_pause_preview(self):
        self.priority_video_player_preview_thread(target_panel = 0,
                                                  has_heatmap = False)

    
    def play_and_pause_ai_analytics_heatmap(self):
        
        
        self.priority_video_player_preview_thread(target_panel = 1,
                                                  has_heatmap = True)
        
    
    def play_and_pause_ai_analytics_line_graph(self):
        self.AI_Analytics_Line_Chart_Visualization.get_colors_all_frames = self.get_colors_actions_from_tracker_all_frames(is_advanced_analytics=False)
        self.AI_Analytics_Line_Chart_Visualization.populate_chart()
        self.priority_video_player_preview_thread(target_panel = 2,
                                                  has_heatmap = False)
    
    def play_and_pause_ai_analytics_table_logs(self):
        self.priority_video_player_preview_thread(target_panel = 3,
                                                  has_heatmap = False)
    
    def play_and_pause_advanced_analytics_heatmap(self):

        self.priority_video_player_preview_thread(target_panel = 4,
                                                  has_heatmap = True)
        
    
    def play_and_pause_advanced_analytics_line_graph(self):
        self.AI_Analytics_Line_Chart_Visualization.get_colors_all_frames = self.get_colors_actions_from_tracker_all_frames(is_advanced_analytics=True)
        self.priority_video_player_preview_thread(target_panel = 5,
                                                  has_heatmap = False)
    
    def play_and_pause_advanced_analytics_table_logs(self):
        self.priority_video_player_preview_thread(target_panel = 6,
                                                  has_heatmap = False)
    
    def play_and_pause_ai_analytics_event_summary(self):
        self.priority_video_player_preview_thread(target_panel=7,
                                                  has_heatmap=False)
        
    def play_and_pause_advanced_analytics_event_summary(self):
        self.priority_video_player_preview_thread(target_panel=8,
                                                  has_heatmap=False)
        
    def priority_video_player_preview_thread(self, target_panel, has_heatmap):
        '''
        ---THIS IS FOR VIDEO THREAD PREVIEW---

        PANELS/FRAMES ASSIGNMENT:
        # 0 - FOR PREVIEW
        # 1 - FOR AI ANALYTICS - HEATMAP
        # 2 - FOR AI ANALYTICS - LINE GRAPH
        # 3 - FOR AI ANALYTICS - TABLE LOGS
        # 4 - FOR ADVANCED ANALYTICS - HEATMAP
        # 5 - FOR ADVANCED ANALYTICS - LINE GRAPH
        # 6 - FOR ADVANCED ANALYTICS - TABLE LOGS
        # 7 - FOR AI ANALYTICS - EVENT SUMMARY
        # 8 - FOR ADVANCED ANALYTICS - EVENT SUMMARY
                        
        '''
        #Where to get the video
        center_video_directory = self.videoDirectory_center.text()
        front_video_directory = self.videoDirectory_front.text()
        
        if not self.isAlreadyRunning[target_panel]:
            if has_heatmap:
                self.ThreadManager.start_video_player_with_heatmap_thread(center_video_path = center_video_directory,
                                                front_video_path = front_video_directory,
                                                target_panel = target_panel)
            else:
                self.ThreadManager.start_video_player_thread(center_video_path = center_video_directory,
                                                front_video_path = front_video_directory,
                                                target_panel = target_panel)
            #RESET VALUES
            self.set_bool_default()

            #Reassign the value for one time policy
            self.isAlreadyRunning[target_panel] = not self.isAlreadyRunning[target_panel]

            # self.play_pause_button_video_preview.setText("PAUSE PREVIEW")
            # self.play_pause_button_video_preview.setIcon(self.pause_icon)
            #Avoid browsing while threads are running
            self.import_video_button_front.setEnabled(False)
            self.import_video_button_center.setEnabled(False)
            
        else:
            if self.isRunningAndPaused[target_panel]:
                #Avoid browsing while threads are running
                self.import_video_button_front.setEnabled(False)
                self.import_video_button_center.setEnabled(False)
                self.ThreadManager.pause_continue_current_video_player_thread()
            else:
                #Avoid browsing while threads are running
                self.import_video_button_front.setEnabled(True)
                self.import_video_button_center.setEnabled(True)
                
                self.ThreadManager.pause_continue_current_video_player_thread()
            
            #FOR TOGGLING THE VALUES IN ISPAUSED LIST
            self.isRunningAndPaused[target_panel] = not self.isRunningAndPaused[target_panel]
    
    def update_frame_for_advanced_analytics(self, frame_list):
        if frame_list is not None:
            center_frame = frame_list[0]
            front_frame = frame_list[1]
            heatmap_frame = frame_list[2]

            self.AnalyticsTab.update_frame_for_center_video_label(frame = center_frame,
                                                                  center_starting_y=self.center_starting_y,
                                                                  front_starting_y=self.center_video_height)
            
            self.AnalyticsTab.update_frame_for_front_video_label(frame=front_frame,
                                                                 starting_y=self.front_starting_y,
                                                                 whole_classroom_height=self.whole_classroom_height
                                                                 )

            self.AnalyticsTab.update_heatmap(frame=heatmap_frame)

    '''
    THIS AREA IS FOR VIDEO PLAYER THREAD
    '''
    def update_frame_for_preview(self, frame_list):
        '''
        This function is for updating the picture on the frames.
        More like key component to show frames and to look like a video

        '''
        if frame_list is not None:
            
            center_frame = frame_list[0]
            front_frame = frame_list[1]

            '''
            THIS AREA IS FOR CENTER FRAME
            '''
            # Convert the frame from BGR to RGB
            #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            '''
            THIS AREA IS FOR CENTER FRAME
            '''
            self.CenterVideo.update_frame(center_frame=center_frame)
            '''
            THIS AREA IS FOR FRONT FRAME
            '''
            self.FrontVideo.update_frame(front_frame=front_frame)

    '''
    THIS AREA IS FOR VIDEO PLAYER THREAD
    '''

    def activate_analytics(self, activation):

        if activation:
            front_video_directory = self.videoDirectory_front.text()
            center_video_directory = self.videoDirectory_center.text()
            
            front_cap = cv2.VideoCapture(front_video_directory)
            center_cap = cv2.VideoCapture(center_video_directory)

            front_video_frame_count = int(front_cap.get(cv2.CAP_PROP_FRAME_COUNT))

            center_video_frame_count = int(center_cap.get(cv2.CAP_PROP_FRAME_COUNT))

            if front_video_frame_count > center_video_frame_count:

                self.show_bubble_message()
                
                #For Preview
                self.time_frame_slider_import_preview.setMaximum(int(len(self.human_pose_results_center)-1))
                
                #AI ANALYTICS TIME RANGE SLIDERS
                self.time_frame_range_slider_ai_analytics_heatmap.setMaximum(int(len(self.human_pose_results_center)-1))
                self.time_frame_range_slider_ai_analytics_line_graph.setMaximum(int(len(self.human_pose_results_center)-1))
                self.time_frame_range_slider_ai_analytics_line_graph.setValue((0, int(len(self.human_pose_results_front)-1)))
                self.time_frame_range_slider_ai_analytics_table_event_logs.setMaximum(int(len(self.human_pose_results_center)-1))
                self.time_frame_range_slider_ai_analytics_table_event_summary.setMaximum(int(len(self.human_pose_results_center)-1))
                
                self.time_frame_range_slider_ai_analytics_table_event_summary.setValue((0, int(len(self.human_pose_results_front)-1)))

                #ADVANCED ANALYTICS TIME RANGE SLIDERS
                self.time_frame_range_slider_advanced_analytics_heatmap.setMaximum(int(len(self.human_pose_results_center)-1))
                self.time_frame_range_slider_advanced_analytics_line_graph.setMaximum(int(len(self.human_pose_results_center)-1))
                self.time_frame_range_slider_advanced_analytics_line_graph.setValue((0, int(len(self.human_pose_results_front)-1)))
                self.time_frame_range_slider_advanced_analytics_table_event_logs.setMaximum(int(len(self.human_pose_results_center)-1))
                self.time_frame_range_slider_advanced_analytics_table_event_summary.setMaximum(int(len(self.human_pose_results_center)-1))
                
                self.time_frame_range_slider_advanced_analytics_table_event_summary.setValue((0, int(len(self.human_pose_results_front)-1)))
                
                self.max_frames = int(len(self.human_pose_results_center))
                
                
            else:
                
                
                self.time_frame_slider_import_preview.setMaximum(int(len(self.human_pose_results_front)-1))
                
                self.time_frame_range_slider_ai_analytics_heatmap.setMaximum(int(len(self.human_pose_results_front)-1))
                self.time_frame_range_slider_ai_analytics_line_graph.setMaximum(int(len(self.human_pose_results_front)-1))
                self.time_frame_range_slider_ai_analytics_line_graph.setValue((0, int(len(self.human_pose_results_front)-1)))
                self.time_frame_range_slider_ai_analytics_table_event_logs.setMaximum(int(len(self.human_pose_results_center)-1))
                self.time_frame_range_slider_ai_analytics_table_event_summary.setMaximum(int(len(self.human_pose_results_center)-1))

                #ADVANCED ANALYTICS TIME RANGE SLIDERS
                self.time_frame_range_slider_advanced_analytics_heatmap.setMaximum(int(len(self.human_pose_results_front)-1))
                self.time_frame_range_slider_advanced_analytics_line_graph.setMaximum(int(len(self.human_pose_results_front)-1))
                self.time_frame_range_slider_advanced_analytics_line_graph.setValue((0, int(len(self.human_pose_results_front)-1)))
                
                self.time_frame_range_slider_advanced_analytics_table_event_logs.setMaximum(int(len(self.human_pose_results_front)-1))
                self.time_frame_range_slider_advanced_analytics_table_event_summary.setMaximum(int(len(self.human_pose_results_front)-1))

                self.max_frames = int(len(self.human_pose_results_front))

            
            
            '''
            Initialize AI Analytics Features
            '''
            min_value, max_value = self.time_frame_range_slider_ai_analytics_line_graph.value()  
            
            self.time_frame_range_slider_ai_analytics_heatmap.setValue((min_value, max_value))
            self.time_frame_range_slider_ai_analytics_line_graph.setValue((min_value, max_value))
            self.time_frame_range_slider_ai_analytics_table_event_logs.setValue((min_value, max_value))
            self.time_frame_range_slider_ai_analytics_table_event_summary.setValue((min_value, max_value))
            

            # Integrate chart into QGraphicsView instead of a separate window

            self.AI_Analytics_Line_Chart_Visualization = AI_Analytics_Line_Chart_Visualization(main_window=self,
                                                        action_results_list_front=self.action_results_list_front,
                                                        action_results_list_center=self.action_results_list_center,
                                                        min_time=min_value,
                                                        max_time=max_value)

            self.AI_Analytics_Table_Event_Logs = AI_Analytics_Table_Events_Log(main_window=self,
                                                action_results_list_center=None,
                                                action_results_list_front=None,
                                                min_time=None,
                                                max_time=None)
            
            self.AI_Analytics_Event_Summary = AI_Analytics_Chunk_Summary_Log(main_window=self,
                                                                            fps=30,
                                                                            chunk_size_seconds=1,
                                                                            max_chunks=10)

            self.time_frame_range_slider_ai_analytics_table_event_logs.valueChanged.connect(self.AI_Analytics_Table_Event_Logs.update_logs_periodically)

            '''
            Initialize Advanced Analytics Features
            '''
            min_value, max_value = self.time_frame_range_slider_advanced_analytics_line_graph.value()
            
            self.time_frame_range_slider_advanced_analytics_heatmap.setValue((min_value, max_value))
            self.time_frame_range_slider_advanced_analytics_line_graph.setValue((min_value, max_value))
            self.time_frame_range_slider_advanced_analytics_table_event_logs.setValue((min_value, max_value))
            self.time_frame_range_slider_advanced_analytics_table_event_summary.setValue((min_value, max_value))

            self.advanced_analytics_line_chart_visualization = Advanced_Analytics_Line_Chart_Visualization(main_window=self,
                                                                                head_posture_list_front=self.head_postures_list_front,
                                                                                head_posture_list_center= self.head_postures_list_center,
                                                                                arm_posture_list_front=self.arms_postures_list_front,
                                                                                arm_posture_list_center=self.arms_postures_list_center,
                                                                                min_time=min_value,
                                                                                max_time=max_value)

            self.advanced_analytics_table_event_logger = Advanced_Analytics_Table_Events_Log(main_window=self,
                                                                                            head_postures_front=self.head_postures_list_front,
                                                                                            head_postures_center= self.head_postures_list_center,
                                                                                            arms_postures_front=self.arms_postures_list_front,
                                                                                            arms_postures_center=self.arms_postures_list_center,
                                                                                            min_time=min_value,
                                                                                            max_time=max_value)
            
            self.Advanced_Analytics_Event_Summary = Advanced_Analytics_Chunk_Summary_Log(main_window=self,
                                                                                        fps=30,
                                                                                        chunk_size_seconds=1,
                                                                                        max_chunks=10)


            
        self.heatmap_update_selected_action_advanced_analytics()
        self.heatmap_update_selected_action_ai_analytics()

        if activation:
            self.status_label_front.setText("[VIDEO PREPROCESSING COMPLETED!]")
            self.status_label_center.setText("[VIDEO PREPROCESSING COMPLETED!]")
        
        self.play_pause_button_video_preview.setEnabled(activation)
        self.Import_button.setEnabled(activation)

        #For Menu Bar
        self.actionAI_Analytics_Results.setEnabled(activation)
        self.actionAdvanced_Analytics_Results.setEnabled(activation)
        self.actionExport_Data_Analytics_Results.setEnabled(activation)

        self.AI_analytics_button.setEnabled(activation)
        self.Advanced_analytics_button.setEnabled(activation)
        self.Export_file_button.setEnabled(activation)
        
    def reenable_recording_button(self):
        self.recording_window_button.setDisabled(False)

    def switch_page_advanced_analytics(self):
        
        if self.ThreadManager is not None:
            self.ThreadManager.stop_current_thread()
            self.reset_video_playing_boolean()
        
        self.reset_video_playing_boolean()
        index = self.advanced_analytics_visualization_combo_box.currentIndex()
        self.stacked_advanced_analytics.setCurrentIndex(int(index))

    def switch_page_ai_analytics(self):
        if self.ThreadManager is not None:
            self.ThreadManager.stop_current_thread()
            self.reset_video_playing_boolean()
            
        self.reset_video_playing_boolean()
        index = self.ai_analytics_visualization_combo_box.currentIndex()
        self.stacked_panels_ai_analytics.setCurrentIndex(index)


    '''
    THIS IS FOR BUBBLE MESSAGE NOTIF AFTER VIDEO PROCESSING
    '''
    def show_bubble_message(self):
        """Show the bubble, cancel existing fade-out, and reset its state"""
        # If bubble is currently visible, make it disappear first
        if self.bubble_label.isVisible():
            self.fade_out_bubble(immediate=True)

        # Now show bubble with fade-in
        self.bubble_label.setVisible(True)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

        # Auto fade-out after 5 seconds if not hovered
        self.fade_timer.start(5000)

    def fade_out_bubble(self, immediate=False):
        """Fade out the bubble message immediately or smoothly"""
        if immediate:
            self.animation.stop()
            self.opacity_effect.setOpacity(0)
            self.bubble_label.setVisible(False)
        else:
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.start()
            self.animation.finished.connect(lambda: self.bubble_label.setVisible(False))

    def eventFilter(self, obj, event):
        """Handle hover effects"""
        if obj == self.bubble_label:
            if event.type() == QEnterEvent.Enter:
                # Stop auto fade-out & set full opacity immediately
                self.animation.stop()
                self.opacity_effect.setOpacity(1)
                self.fade_timer.stop()
            elif event.type() == QEnterEvent.Leave:
                # Immediately hide bubble on hover-out
                self.fade_out_bubble(immediate=True)
        return super().eventFilter(obj, event)
    
    from PySide6.QtWidgets import QFileDialog, QMessageBox

    def generate_data_to_docx(self):
        # Prompt user to select folder
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Select Folder Destination"
        )

        # If no folder selected, stop execution
        if not folder_path:
            QMessageBox.warning(self, "No Folder Selected", "Please select a destination folder.")
            return

        self.chosen_directory = folder_path
        
        # Create AI Analytics Images (Line Chart)
        self.AI_Analytics_Line_Chart_Visualization.export_to_jpeg()

        # Create Advanced Analytics Images (Line Chart)
        self.advanced_analytics_line_chart_visualization.export_to_jpeg()

        # Create Heatmaps
        self.heatmap_images_generator = self.ThreadManager.generate_heatmap_image()

        # Generate DOCX file in selected folder
        self.generate_docx_thread = DocxGenerationThread(main_window=self, directory=folder_path)
        self.generate_docx_thread.finished.connect(self.on_docx_generation_complete)
        self.generate_docx_thread.start()


    def on_docx_generation_complete(self, result):
        if result.startswith("Error"):
            QMessageBox.information(self, "Error", f"Failed to generate PDF file:\n{result}")
            print(f"Failed to generate PDF: {result}")
        else:
            QMessageBox.information(self, "Error", f"PDF file generated successfully:\n{result}")
            print(f"PDF file generated successfully: {result}")
    
    

    def heatmap_update_selected_action_ai_analytics(self):
        """
        Handles action selection change and resets the heatmap instantly.
        """
        #RESET THE VIDEO TO PLAY FROM THE START AGAIN
        self.reset_video_playing_to_start()
        
        # Reset heatmap
        self.heatmap_ai_analytics_label.clear()
        
        selected_action = self.heatmap_actions_ai_analytics_combo_box.currentText()

        print(f"[DEBUG] Selected action changed to: {selected_action}. Resetting heatmap...")

        if selected_action == "ALL ACTIONS":
            print("[STATUS] RETURNING ALL ACTION RESULTS")
            self.ThreadManager.filtered_bboxes_front = self.human_detect_results_front
            self.ThreadManager.filtered_bboxes_center = self.human_detect_results_center

            self.filtered_action_results_bboxes_front = self.human_detect_results_front
            self.filtered_action_results_bboxes_center = self.human_detect_results_center

            self.filtered_action_results_list_front = self.action_results_list_front
            self.filtered_action_results_list_center = self.action_results_list_center

            self.filtered_head_postures_list_front = self.head_postures_list_front
            self.filtered_head_postures_list_center = self.head_postures_list_center

            self.filtered_arms_postures_list_front = self.arms_postures_list_front
            self.filtered_arms_postures_list_center = self.arms_postures_list_center

            return

        

        # Ensure required data exists
        if not hasattr(self, 'action_results_list_front') or not hasattr(self, 'action_results_list_center'):
            print("[ERROR] Missing action detection results!")
            return

        # Extract filtered bounding boxes based on the selected action
        filtered_bboxes_front, filtered_bboxes_center = self.get_filtered_bboxes_ai_analytics(
            selected_action=selected_action,
            action_results_list_front=self.action_results_list_front,
            action_results_list_center=self.action_results_list_center,
        )

        self.filtered_action_results_bboxes_front = filtered_bboxes_front
        self.filtered_action_results_bboxes_center = filtered_bboxes_center

        # Also filter action results list (not just bboxes)
        selected_action_lower = selected_action.strip().lower()
        self.filtered_action_results_list_front = [
            {tid: act for tid, act in frame.items() if act.lower() == selected_action_lower}
            for frame in self.action_results_list_front
        ]

        self.filtered_action_results_list_center = [
            {tid: act for tid, act in frame.items() if act.lower() == selected_action_lower}
            for frame in self.action_results_list_center
        ]

    def get_filtered_bboxes_ai_analytics(self, selected_action, action_results_list_front, action_results_list_center):
        """Filters bounding boxes based on the selected action, returns only matching track IDs per frame."""

        human_detect_results_front = self.human_detect_results_front
        human_detect_results_center = self.human_detect_results_center

        filtered_bboxes_front = [dict() for _ in action_results_list_front]
        filtered_bboxes_center = [dict() for _ in action_results_list_center]

        selected_action = selected_action.strip().lower()

        for i, actions in enumerate(action_results_list_front):
            for track_id, action in actions.items():
                if action.lower() == selected_action:
                    if 0 <= i < len(human_detect_results_front):
                        if track_id in human_detect_results_front[i]:
                            filtered_bboxes_front[i][track_id] = human_detect_results_front[i][track_id]

        for i, actions in enumerate(action_results_list_center):
            for track_id, action in actions.items():
                if action.lower() == selected_action:
                    if 0 <= i < len(human_detect_results_center):
                        if track_id in human_detect_results_center[i]:
                            filtered_bboxes_center[i][track_id] = human_detect_results_center[i][track_id]

        return filtered_bboxes_front, filtered_bboxes_center


    def heatmap_update_selected_action_advanced_analytics(self):
        """
        Handles action selection change and resets the heatmap instantly based on head or arm postures.
        """
        selected_action = self.heatmap_actions_advanced_analytics_combo_box.currentText()

        print(f"[DEBUG] Selected action changed to: {selected_action}. Resetting heatmap...")

        if selected_action == "ALL ACTIONS":
            print("[STATUS] RETURNING ALL ACTION RESULTS")

            self.ThreadManager.filtered_bboxes_front = self.human_detect_results_front
            self.ThreadManager.filtered_bboxes_center = self.human_detect_results_center

            self.filtered_action_results_bboxes_front = self.human_detect_results_front
            self.filtered_action_results_bboxes_center = self.human_detect_results_center

            self.filtered_head_postures_list_front = self.head_postures_list_front
            self.filtered_head_postures_list_center = self.head_postures_list_center

            self.filtered_arms_postures_list_front = self.arms_postures_list_front
            self.filtered_arms_postures_list_center = self.arms_postures_list_center

            return

        #RESET THE VIDEO TO PLAY FROM THE START AGAIN
        self.reset_video_playing_to_start()

        # Reset heatmap
        self.heatmap_ai_analytics_label.clear()

        # Validate required data
        if not all(hasattr(self, attr) for attr in [
            'human_detect_results_front',
            'human_detect_results_center',
            'head_postures_list_front',
            'head_postures_list_center',
            'arms_postures_list_front',
            'arms_postures_list_center'
        ]):
            print("[ERROR] Missing required posture or detection data!")
            return

        # Perform filtering using advanced method
        (filtered_bboxes_front, filtered_bboxes_center, filtered_head_postures_list_front,
         filtered_head_postures_list_center, filtered_arms_postures_list_front,
         filtered_arms_postures_list_center) = self.get_filtered_bboxes_advanced_analytics(
                                                                                            selected_action=selected_action,
                                                                                            head_postures_list_front=self.head_postures_list_front,
                                                                                            head_postures_list_center=self.head_postures_list_center,
                                                                                            arms_postures_list_front=self.arms_postures_list_front,
                                                                                            arms_postures_list_center=self.arms_postures_list_center
                                                                                        )
         
        # Store filtered results
        self.ThreadManager.filtered_bboxes_front = filtered_bboxes_front
        self.ThreadManager.filtered_bboxes_center = filtered_bboxes_center

        self.filtered_action_results_bboxes_front = filtered_bboxes_front
        self.filtered_action_results_bboxes_center = filtered_bboxes_center

        self.filtered_head_postures_list_front = filtered_head_postures_list_front
        self.filtered_head_postures_list_center = filtered_head_postures_list_center

        self.filtered_arms_postures_list_front = filtered_arms_postures_list_front
        self.filtered_arms_postures_list_center = filtered_arms_postures_list_center

    def get_filtered_bboxes_advanced_analytics(
                                            self, selected_action,
                                            head_postures_list_front, head_postures_list_center,
                                            arms_postures_list_front,arms_postures_list_center
                                        ):
        """Filters bounding boxes based on selected head or arm posture action."""

        human_detect_results_front = self.human_detect_results_front
        human_detect_results_center = self.human_detect_results_center

        # Initialize blank bbox containers
        filtered_bboxes_front = [dict() for _ in human_detect_results_front]
        filtered_bboxes_center = [dict() for _ in human_detect_results_center]

        # Also prepare filtered posture info to return
        filtered_head_postures_front = [dict() for _ in head_postures_list_front]
        filtered_head_postures_center = [dict() for _ in head_postures_list_center]
        filtered_arm_postures_front = [dict() for _ in arms_postures_list_front]
        filtered_arm_postures_center = [dict() for _ in arms_postures_list_center]

        selected_action = selected_action.strip().lower()

        if selected_action.startswith("facing"):
            # Filter by head posture
            for i, frame_postures in enumerate(head_postures_list_front):
                for track_id, data in frame_postures.items():
                    if data['head_posture'].lower() == selected_action:
                        if track_id in human_detect_results_front[i]:
                            filtered_bboxes_front[i][track_id] = human_detect_results_front[i][track_id]
                            filtered_head_postures_front[i][track_id] = data

            for i, frame_postures in enumerate(head_postures_list_center):
                for track_id, data in frame_postures.items():
                    if data['head_posture'].lower() == selected_action:
                        if track_id in human_detect_results_center[i]:
                            filtered_bboxes_center[i][track_id] = human_detect_results_center[i][track_id]
                            filtered_head_postures_center[i][track_id] = data

        else:
            # Determine if we're filtering left or right arm
            if selected_action.startswith("left arm"):
                target_key = "left_arm_posture"
            else:
                target_key = "right_arm_posture"

            # Filter by arm posture
            for i, frame_postures in enumerate(arms_postures_list_front):
                for track_id, data in frame_postures.items():
                    if data[target_key].lower() == selected_action:
                        if track_id in human_detect_results_front[i]:
                            filtered_bboxes_front[i][track_id] = human_detect_results_front[i][track_id]
                            filtered_arm_postures_front[i][track_id] = data

            for i, frame_postures in enumerate(arms_postures_list_center):
                for track_id, data in frame_postures.items():
                    if data[target_key].lower() == selected_action:
                        if track_id in human_detect_results_center[i]:
                            filtered_bboxes_center[i][track_id] = human_detect_results_center[i][track_id]
                            filtered_arm_postures_center[i][track_id] = data

        return (
            filtered_bboxes_front,
            filtered_bboxes_center,
            filtered_head_postures_front,
            filtered_head_postures_center,
            filtered_arm_postures_front,
            filtered_arm_postures_center
        )

    # def disable_dark_mode_front(self):
        
    #     self.front_preview_video_dark_mode_check_box.setChecked(self.front_preview_video_keypoints_check_box.isChecked() or self.front_preview_video_bounding_box_check_box.isChecked())
    #     self.front_preview_video_dark_mode_check_box.setEnabled(self.front_preview_video_keypoints_check_box.isChecked() or self.front_preview_video_bounding_box_check_box.isChecked())
    
    def disable_dark_mode_center(self):

        self.center_preview_video_dark_mode_check_box.setChecked(self.center_preview_video_keypoints_check_box.isChecked() or self.center_preview_video_bounding_box_check_box.isChecked())
        self.center_preview_video_dark_mode_check_box.setEnabled(self.center_preview_video_keypoints_check_box.isChecked() or self.center_preview_video_bounding_box_check_box.isChecked())

    def reset_video_playing_to_start(self):
        if self.ThreadManager.current_thread is not None:
            self.ThreadManager.current_thread.isFirstFrame = True
            
    def reset_video_playing_boolean(self):
        self.isRunningAndPaused = [False] * 10
        self.isAlreadyRunning = [False] * 10
    
    def update_movement_quantities_ai_analytics_line_chart(self, current_index):
        
        if (current_index % 2) == 0:
            combined = {}
            # Process front view
            for track_id, action in self.action_results_list_front[current_index].items():
                unique_track_id = f"front_{track_id}"  # Unique ID for front view
                combined[unique_track_id] = action

            # Process center view
            for track_id, action in self.action_results_list_center[current_index].items():
                unique_track_id = f"center_{track_id}"  # Unique ID for center view
                combined[unique_track_id] = action

            # Count occurrences of each action
            action_list = [
                'LEFT ARM EXTENDING SIDEWARDS', 'RIGHT ARM EXTENDING SIDEWARDS',
                'FACING DOWNWARDS', 'FACING FORWARD', 'FACING LEFT', 'FACING RIGHT',
                'SITTING', 'STANDING'
            ]
            counts = {action: 0 for action in action_list}

            for action in combined.values():
                if action in counts:
                    counts[action] += 1


            # Update label texts
            self.ai_analytics_count_left_arm_extending_sidewards.setText(str(counts['LEFT ARM EXTENDING SIDEWARDS']))
            self.ai_analytics_count_right_arm_extending_sidewards.setText(str(counts['RIGHT ARM EXTENDING SIDEWARDS']))
            self.ai_analytics_count_facing_downwards.setText(str(counts['FACING DOWNWARDS']))
            self.ai_analytics_count_facing_forward.setText(str(counts['FACING FORWARD']))
            self.ai_analytics_count_facing_left.setText(str(counts['FACING LEFT']))
            self.ai_analytics_count_facing_right.setText(str(counts['FACING RIGHT']))
            self.ai_analytics_count_sitting.setText(str(counts['SITTING']))
            self.ai_analytics_count_standing.setText(str(counts['STANDING']))

            # Update student count
            self.ai_analytics_count_students.setText(str(len(combined)))
            
    def update_movement_quantities_advanced_analytics_line_chart(self, current_index):
        if (current_index % 7) == 0:
            combined_head = {}
            combined_arm = {}

            # Combine front and center view - HEAD POSTURES
            for track_id, head_data in self.head_postures_list_front[current_index].items():
                unique_track_id = f"front_{track_id}"
                combined_head[unique_track_id] = head_data

            for track_id, head_data in self.head_postures_list_center[current_index].items():
                unique_track_id = f"center_{track_id}"
                combined_head[unique_track_id] = head_data

            # Combine front and center view - ARM POSTURES
            for track_id, arm_data in self.arms_postures_list_front[current_index].items():
                unique_track_id = f"front_{track_id}"
                combined_arm[unique_track_id] = arm_data

            for track_id, arm_data in self.arms_postures_list_center[current_index].items():
                unique_track_id = f"center_{track_id}"
                combined_arm[unique_track_id] = arm_data

            # Initialize counts
            head_counts = {
                'FACING FORWARD': 0,
                'FACING RIGHT': 0,
                'FACING LEFT': 0,
                'FACING DOWNWARDS': 0,
                'FACING UNKNOWN': 0
            }

            left_arm_counts = {
                'NEUTRAL': 0,
                'EXTENDING SIDEWARDS': 0,
                'UNKNOWN': 0
            }

            right_arm_counts = {
                'NEUTRAL': 0,
                'EXTENDING SIDEWARDS': 0,
                'UNKNOWN': 0
            }

            # Count head postures
            for data in combined_head.values():
                posture = data.get("head_posture", "FACING UNKNOWN")
                if posture in head_counts:
                    head_counts[posture] += 1

            # Count arm postures
            for data in combined_arm.values():
                left_posture = data.get("left_arm_posture", "UNKNOWN")
                right_posture = data.get("right_arm_posture", "UNKNOWN")
                
                if left_posture in left_arm_counts:
                    left_arm_counts[left_posture] += 1
                if right_posture in right_arm_counts:
                    right_arm_counts[right_posture] += 1

            # Update labels for head postures
            self.advanced_analytics_count_facing_forward.setText(str(head_counts['FACING FORWARD']))
            self.advanced_analytics_count_facing_right.setText(str(head_counts['FACING RIGHT']))
            self.advanced_analytics_count_facing_left.setText(str(head_counts['FACING LEFT']))
            self.advanced_analytics_count_facing_downwards.setText(str(head_counts['FACING DOWNWARDS']))

            # Update labels for left arm postures
            self.advanced_analytics_count_left_arm_extending_sidewards.setText(str(left_arm_counts['EXTENDING SIDEWARDS']))
            self.advanced_analytics_count_left_arm_neutral.setText(str(left_arm_counts['NEUTRAL']))
            self.advanced_analytics_count_left_arm_unknown.setText(str(left_arm_counts['UNKNOWN']))

            # Update labels for right arm postures
            self.advanced_analytics_count_right_arm_extending_sidewards.setText(str(right_arm_counts['EXTENDING SIDEWARDS']))
            self.advanced_analytics_count_right_arm_neutral.setText(str(right_arm_counts['NEUTRAL']))
            self.advanced_analytics_count_right_arm_unknown.setText(str(right_arm_counts['UNKNOWN']))

            # Update total student count
            self.advanced_analytics_count_students.setText(str(len(combined_head)))
    
    def generate_detections_video(self):
        
        reply = QMessageBox.question(
            self,
            "Confirm Action",
            f"Do you want to proceed to export detections video?\nDrawings\nBounding Box: {self.add_bounding_box_drawing}\nDrawing Keypoints: {self.add_keypoints_drawing}",
            QMessageBox.No | QMessageBox.Yes 
        )

        if reply == QMessageBox.No:
            return
        
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Select Folder Destination"
        )
        
        if folder_path is not None:
            
            center_video_directory = self.videoDirectory_center.text()
            front_video_directory = self.videoDirectory_front.text()
            
            if self.advanced_analytics_export_radio_button.isChecked():
                self.ThreadManager.generate_detection_video(center_video_path=center_video_directory,
                                                            front_video_path=front_video_directory,
                                                            is_advanced_analytics=True,
                                                            directory=folder_path)
            else:
                self.ThreadManager.generate_detection_video(center_video_path=center_video_directory,
                                                            front_video_path=front_video_directory,
                                                            is_advanced_analytics=False,
                                                            directory=folder_path)
    
    def generate_heatmap_video(self):
        reply = QMessageBox.question(
            self,
            "Confirm Action",
            f"Do you want to proceed to export heatmap video?",
            QMessageBox.No | QMessageBox.Yes 
        )

        if reply == QMessageBox.No:
            return
        
        folder_path = QFileDialog.getExistingDirectory(
            self,
            "Select Folder Destination"
        )
        
        if folder_path is not None:
            
            center_video_directory = self.videoDirectory_center.text()
            front_video_directory = self.videoDirectory_front.text()
            
            if self.advanced_analytics_export_radio_button.isChecked():
                self.ThreadManager.generate_heatmap_video(front_video_path=front_video_directory,
                                                          center_video_path=center_video_directory,
                                                          directory=folder_path,
                                                          is_advanced_analytics=True)
            else:
                self.ThreadManager.generate_heatmap_video(front_video_path=front_video_directory,
                                                          center_video_path=center_video_directory,
                                                          directory=folder_path,
                                                          is_advanced_analytics=False)
                
    
    def update_add_keypoints_status(self):
        if self.add_keypoints_check_box.isChecked():
            self.add_keypoints_drawing = "Yes"
        else:
            self.add_keypoints_drawing = "No"
    
    def update_add_bounding_box_status(self):
        if self.add_bounding_box_check_box.isChecked():
            self.add_bounding_box_drawing = "Yes"
        else:
            self.add_bounding_box_drawing = "No"
    
    def generate_data_and_media(self):
        chosen_document = int(self.document_export_combo_box.currentIndex())
        
        if chosen_document == 0:
            print("GENERATING DOCX FILE")
            self.send_to_email_button.setEnabled(True)
            self.all_summary_chunks()
            self.generate_data_to_docx()
        elif chosen_document == 1:
            print("GENERATING DETECTION VIDEO")
            self.generate_detections_video()
        
        elif chosen_document == 2:
            print("GENERATING HEATMAP VIDEO")    
            self.generate_heatmap_video()
        return

    
    def update_media_options(self):
        chosen_media = int(self.document_export_combo_box.currentIndex())
        enable_setting = True
        
        if chosen_media == 1: #For Detections Video Only
            enable_setting = True
        else:
            enable_setting = False
        
        self.media_settings_frame.setEnabled(enable_setting)
        self.add_keypoints_check_box.setEnabled(enable_setting)
        self.add_bounding_box_check_box.setEnabled(enable_setting)
        self.camera_angles_group_frame.setEnabled(enable_setting)
        
    
    # def generate_heatmap_image(self):
    #     center_video_directory = self.videoDirectory_center.text()
    #     front_video_directory = self.videoDirectory_front.text()
        
    #     self.heatmap_image_generator = Export_Heatmap_Image_Thread(front_video_path=front_video_directory,
    #                                                                center_video_path=center_video_directory,
    #                                                                main_window=self)
        
    #     self.heatmap_image_generator.finished_inference.connect(self.heatmap_image_generator.stop)
    #     self.heatmap_image_generator.start()
    
    def update_export_progress_bar(self, progress_value):
        self.export_progress_bar.setValue(progress_value)
        return

    def send_email(self, recipient):
        if not self.chosen_directory:
            QMessageBox.information(
                self,
                "Export Required",
                "Please export the DOCX file first before proceeding."
            )
            return

        attachment_directory = os.path.join(self.chosen_directory, f"{self.session_name}_ACE_Output_Document.pdf")

        # Create the QThread
        self.email_thread = QThread()
        
        # Create the worker and move to the thread
        self.email_worker = EmailSendingWorker(
            receipient=recipient,
            session_name=self.session_name,
            attachment_directory=attachment_directory,
            front_video_directory=self.videoDirectory_front.text(),
            center_video_directory=self.videoDirectory_center.text(),
            time_exported=self.time_exported
        )
        self.email_worker.moveToThread(self.email_thread)

        # Connect signals
        self.email_thread.started.connect(self.email_worker.run)
        self.email_worker.finished.connect(self.email_thread.quit)
        self.email_worker.finished.connect(self.email_worker.deleteLater)
        self.email_thread.finished.connect(self.email_thread.deleteLater)

        self.email_worker.error.connect(self.handle_email_error)
        self.email_worker.finished.connect(self.handle_email_success)

        # Start the thread
        self.email_thread.start()

    def handle_email_error(self, error_msg):
        QMessageBox.critical(self, "Email Error", f"Failed to send email:\n{error_msg}")

    def handle_email_success(self):
        QMessageBox.information(self, "Email Sent", "The report has been successfully sent.")
    
    def open_email_dialog(self):
        dialog = EmailDialog()
        
        if dialog.exec() == QDialog.Accepted:
            email = dialog.get_email()
            if email:
                self.send_email(recipient=email)
    
    def add_action_suspicion_level(self):
        action = self.actions_suspicion_level_combo_box.currentText()
        level_ui = self.suspicion_level_combo_box.currentText()
        key = self.suspicion_level_mapping.get(level_ui)

        if action and key:
            if action not in self.suspicious_criteria[key]:
                self.suspicious_criteria[key].append(action)
                self.action_suspicion_level_table.insertRow(self.action_suspicion_level_table.rowCount())
                self.action_suspicion_level_table.setItem(self.action_suspicion_level_table.rowCount() - 1, 0, QTableWidgetItem(action))
                self.action_suspicion_level_table.setItem(self.action_suspicion_level_table.rowCount() - 1, 1, QTableWidgetItem(level_ui))
                self.actions_suspicion_level_combo_box.removeItem(self.actions_suspicion_level_combo_box.currentIndex())
                self.action_suspicion_level_table.resizeColumnsToContents()

            # ✅ Print confirmation
            print(f"[Added] '{action}' classified as '{level_ui}' (-> {key})")
        print(f"SUSPICIOUS CRITERIA: {self.suspicious_criteria}")    

    def add_action_length(self):
        action = self.actions_length_combo_box.currentText()
        value = self.action_length_line_edit.text()

        try:
            seconds = float(value)
            frames = int(seconds * 30)  # Convert seconds to frames (30 FPS)

            if action:
                # Update internal criteria with frame value
                self.suspicious_criteria['min_consistent_frames'][action] = frames

                # Insert row into the table
                row = self.action_length_table.rowCount()
                self.action_length_table.insertRow(row)
                self.action_length_table.setItem(row, 0, QTableWidgetItem(action))
                self.action_length_table.setItem(row, 1, QTableWidgetItem(f"{seconds:.2f} sec ({frames} frames)"))

                # Remove action from dropdown and resize
                self.actions_length_combo_box.removeItem(self.actions_length_combo_box.currentIndex())
                self.action_length_table.resizeColumnsToContents()

                # Debug print
                print(f"[Added] Action '{action}' set to {frames} frames ({seconds:.2f} sec)")
                print(f"SUSPICIOUS CRITERIA: {self.suspicious_criteria}")

        except ValueError:
            print("[Error] Invalid input. Please enter a numeric value for seconds.")

    

    def add_repetition_length(self):
        action = self.actions_repitiion_length_combo_box.currentText()
        value = self.action_repitition_length_line_edit.text()

        try:
            seconds = float(value)
            frames = int(seconds * 30)  # Convert seconds to frames (30 FPS)

            if action:
                self.suspicious_criteria['repetition_thresholds'][action] = frames
                self.action_repitition_length_table.insertRow(self.action_repitition_length_table.rowCount())
                self.action_repitition_length_table.setItem(self.action_repitition_length_table.rowCount() - 1, 0, QTableWidgetItem(action))
                self.action_repitition_length_table.setItem(self.action_repitition_length_table.rowCount() - 1, 1, QTableWidgetItem(f"{seconds:.2f} sec ({frames} frames)"))
                self.actions_repitiion_length_combo_box.removeItem(self.actions_repitiion_length_combo_box.currentIndex())
                self.action_repitition_length_table.resizeColumnsToContents()

                print(f"[Added] Repetition threshold for '{action}' set to {frames} frames ({seconds:.2f} sec)")
                print(f"SUSPICIOUS CRITERIA: {self.suspicious_criteria}")

        except ValueError:
            print("[Error] Invalid input. Please enter a numeric value for seconds.")
    

    def reset_tables(self):
        import copy
        self.suspicious_criteria = copy.deepcopy(self.default_criteria)

        # Clear tables visually
        self.action_suspicion_level_table.setRowCount(0)
        self.action_length_table.setRowCount(0)
        self.action_repitition_length_table.setRowCount(0)

        # Repopulate combo boxes
        self.actions_suspicion_level_combo_box.clear()
        self.actions_length_combo_box.clear()
        self.actions_repitiion_length_combo_box.clear()

        # Build a complete set of actions
        all_actions = set(
            self.default_criteria['red_actions'] +
            self.default_criteria['orange_actions'] +
            self.default_criteria['green_actions'] +
            list(self.default_criteria['min_consistent_frames'].keys()) +
            list(self.default_criteria['repetition_thresholds'].keys())
        )

        for action in sorted(all_actions):
            self.actions_suspicion_level_combo_box.addItem(action)
            self.actions_length_combo_box.addItem(action)
            self.actions_repitiion_length_combo_box.addItem(action)

        # ✅ Populate action_suspicion_level_table
        for action in self.default_criteria['red_actions']:
            row = self.action_suspicion_level_table.rowCount()
            self.action_suspicion_level_table.insertRow(row)
            self.action_suspicion_level_table.setItem(row, 0, QTableWidgetItem(action))
            self.action_suspicion_level_table.setItem(row, 1, QTableWidgetItem("HIGHLY SUSPICIOUS"))

        for action in self.default_criteria['orange_actions']:
            row = self.action_suspicion_level_table.rowCount()
            self.action_suspicion_level_table.insertRow(row)
            self.action_suspicion_level_table.setItem(row, 0, QTableWidgetItem(action))
            self.action_suspicion_level_table.setItem(row, 1, QTableWidgetItem("MODERATELY SUSPICIOUS"))

        for action in self.default_criteria['green_actions']:
            row = self.action_suspicion_level_table.rowCount()
            self.action_suspicion_level_table.insertRow(row)
            self.action_suspicion_level_table.setItem(row, 0, QTableWidgetItem(action))
            self.action_suspicion_level_table.setItem(row, 1, QTableWidgetItem("NON-SUSPICIOUS"))

        # ✅ Populate action_length_table
        for action, length in self.default_criteria['min_consistent_frames'].items():
            row = self.action_length_table.rowCount()
            self.action_length_table.insertRow(row)
            self.action_length_table.setItem(row, 0, QTableWidgetItem(action))
            self.action_length_table.setItem(row, 1, QTableWidgetItem(str(length)))

        # ✅ Populate action_repitition_length_table
        for action, threshold in self.default_criteria['repetition_thresholds'].items():
            row = self.action_repitition_length_table.rowCount()
            self.action_repitition_length_table.insertRow(row)
            self.action_repitition_length_table.setItem(row, 0, QTableWidgetItem(action))
            self.action_repitition_length_table.setItem(row, 1, QTableWidgetItem(str(threshold)))

        print("[Reset] Default suspicious criteria loaded into tables.")
        print(f"SUSPICIOUS CRITERIA: {self.suspicious_criteria}")
    
    def clear_tables(self):
        # Clear table widgets
        self.action_suspicion_level_table.setRowCount(0)
        self.action_length_table.setRowCount(0)
        self.action_repitition_length_table.setRowCount(0)

        # Clear combo boxes
        self.actions_suspicion_level_combo_box.clear()
        self.actions_length_combo_box.clear()
        self.actions_repitiion_length_combo_box.clear()

        # Reset suspicious_criteria to an empty structure
        self.suspicious_criteria = {
            'red_actions': [],
            'orange_actions': [],
            'green_actions': [],
            'min_consistent_frames': {},
            'repetition_thresholds': {},
            'repetition_interval': 15  # You can also set this to None or 0 if needed
        }

        print("[Clear] All tables cleared and suspicious criteria emptied.")
        print(f"SUSPICIOUS CRITERIA: {self.suspicious_criteria}")
    
    def toggle_suspicious(self):
        if self.identify_suspicious_check_box_line_graph_ai_analytics.isChecked():
            self.reset_video_playing_to_start()
            


class EmailDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enter Email")

        main_layout = QVBoxLayout()
        main_layout.addWidget(QLabel("Please enter your email:"))

        # Horizontal layout for email input + domain
        email_layout = QHBoxLayout()
        self.email_input = QLineEdit()
        domain_label = QLabel("@g.batstate-u.edu.ph")
        email_layout.addWidget(self.email_input)
        email_layout.addWidget(domain_label)

        main_layout.addLayout(email_layout)

        # OK / Cancel buttons
        buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        main_layout.addWidget(buttons)

        self.setLayout(main_layout)

    def get_email(self):
        return str(str(self.email_input.text()) + str("@g.batstate-u.edu.ph"))
    
    
    