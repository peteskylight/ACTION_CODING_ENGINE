import cv2



from visualizations import (Video_Detection_Export, Export_Heatmap_Video_Thread, Export_Heatmap_Image_Thread)

from PySide6.QtCore import Qt

from PySide6.QtGui import QImage, QPixmap, QIcon

from PySide6.QtWidgets import QApplication, QMessageBox

from PySide6.QtCharts import QLegendMarker



class ThreadManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.current_thread = None
        self.target_panel = None
        self.current_index = None
        self.filtered_bboxes_front = None
        self.filtered_bboxes_center = None
        self.selected_action = None
        
        self.play_pause_button = None
        self.play_icon = QIcon(":/icons/play-256.png")   # Play icon from resources
        self.pause_icon = QIcon(":/icons/pause-256.png") # Pause icon from resources
        
    def start_video_player_thread(self, center_video_path, front_video_path, target_panel):
        # Stop any existing thread first
        
        self.stop_current_thread()
        
        from utils import VideoPlayerThread
        
        self.has_actions = True
        
        self.target_panel = target_panel
        
        slider = None
        
        is_advanced_analytics = True
        
        keypoints_checkbox_front = None
        bounding_box_check_box_front = None
        keypoints_checkbox_center = None
        bounding_box_check_box_center = None
        

        # ASSIGN WHICH SLIDER
        # 0 - FOR PREVIEW
        # 1 - FOR AI ANALYTICS - HEATMAP
        # 2 - FOR AI ANALYTICS - LINE GRAPH
        # 3 - FOR AI ANALYTICS - TABLE LOGS
        # 4 - FOR ADVANCED ANALYTICS - HEATMAP
        # 5 - FOR ADVANCED ANALYTICS - LINE GRAPH
        # 6 - FOR ADVANCED ANALYTICS - TABLE LOGS

        if target_panel == 0:
            slider = self.main_window.time_frame_slider_import_preview
            self.has_actions = False
            self.play_pause_button = self.main_window.play_pause_button_video_preview
            
            print("BEFORE CHECKING COMPONENTS")
            keypoints_checkbox_front = self.main_window.front_preview_video_keypoints_check_box
            bounding_box_check_box_front = self.main_window.front_preview_video_bounding_box_check_box
            keypoints_checkbox_center = self.main_window.center_preview_video_keypoints_check_box
            bounding_box_check_box_center = self.main_window.center_preview_video_bounding_box_check_box
            print("CHECKING COMPONENTS DONE")

        elif target_panel == 2:
            slider = self.main_window.time_frame_range_slider_ai_analytics_line_graph
            self.has_actions = True
            is_advanced_analytics = False
            self.play_pause_button = self.main_window.play_pause_button__ai_analytics_line_graph
            
            keypoints_checkbox_front = self.main_window.front_preview_video_keypoints_ai_analytics_line_graph_check_box
            bounding_box_check_box_front = self.main_window.front_preview_video_bounding_box_ai_analytics_line_graph_check_box
            keypoints_checkbox_center = self.main_window.center_preview_video_keypoints_ai_analytics_line_graph_check_box
            bounding_box_check_box_center = self.main_window.center_preview_video_bounding_box_ai_analytics_line_graph_check_box
            
        elif target_panel == 3:
            slider = self.main_window.time_frame_range_slider_ai_analytics_table_event_logs
            self.has_actions = True
            is_advanced_analytics = False
            self.play_pause_button = self.main_window.play_pause_button_ai_analytics_table_event_logs
            
            keypoints_checkbox_front = self.main_window.front_preview_video_keypoints_ai_analytics_event_logs_check_box
            bounding_box_check_box_front = self.main_window.front_preview_video_bounding_box_ai_analytics_event_logs_check_box
            keypoints_checkbox_center = self.main_window.center_preview_video_keypoints_ai_analytics_event_logs_check_box
            bounding_box_check_box_center = self.main_window.center_preview_video_bounding_box_ai_analytics_event_logs_check_box
            
        elif target_panel == 5:
            slider = self.main_window.time_frame_range_slider_advanced_analytics_line_graph
            self.has_actions = True
            is_advanced_analytics = True
            self.play_pause_button = self.main_window.play_pause_button_advanced_analytics_line_graph
            
            keypoints_checkbox_front = self.main_window.front_preview_video_keypoints_advanced_analytics_line_chart_check_box
            bounding_box_check_box_front = self.main_window.front_preview_video_bounding_box_advanced_analytics_line_chart_check_box
            keypoints_checkbox_center = self.main_window.center_preview_video_keypoints_advanced_analytics_line_chart_check_box
            bounding_box_check_box_center = self.main_window.center_preview_video_bounding_box_advanced_analytics_line_chart_check_box
            
        elif target_panel == 6:
            slider = self.main_window.time_frame_range_slider_advanced_analytics_table_event_logs
            self.has_actions = True
            is_advanced_analytics = True
            self.play_pause_button = self.main_window.play_pause_button_advanced_analytics_table_event_logs
            
            keypoints_checkbox_front = self.main_window.front_preview_video_keypoints_advanced_analytics_event_logs_check_box
            bounding_box_check_box_front = self.main_window.front_preview_video_bounding_box_advanced_analytics_event_logs_check_box
            keypoints_checkbox_center = self.main_window.center_preview_video_keypoints_advanced_analytics_event_logs_check_box
            bounding_box_check_box_center = self.main_window.center_preview_video_bounding_box_advanced_analytics_event_logs_check_box
        
        elif target_panel == 7:
            slider = self.main_window.time_frame_range_slider_ai_analytics_table_event_summary
            self.has_actions = True
            is_advanced_analytics = False
            self.play_pause_button = self.main_window.ai_analytics_event_summary_play_pause_button
            
            keypoints_checkbox_front = self.main_window.front_preview_video_keypoints_ai_analytics_event_summary_check_box
            bounding_box_check_box_front = self.main_window.front_preview_video_bounding_box_ai_analytics_event_summary_check_box
            keypoints_checkbox_center = self.main_window.center_preview_video_keypoints_ai_analytics_event_summary_check_box
            bounding_box_check_box_center = self.main_window.center_preview_video_bounding_box_ai_analytics_event_summary_check_box
        
        elif target_panel == 8:
            slider = self.main_window.time_frame_range_slider_advanced_analytics_table_event_summary
            self.has_actions = True
            is_advanced_analytics = True
            self.play_pause_button = self.main_window.advanced_analytics_event_summary_play_pause_button
            
            keypoints_checkbox_front = self.main_window.front_preview_video_keypoints_advanced_analytics_event_summary_check_box
            bounding_box_check_box_front = self.main_window.front_preview_video_bounding_box_advanced_analytics_event_summary_check_box
            keypoints_checkbox_center = self.main_window.center_preview_video_keypoints_advanced_analytics_event_summary_check_box
            bounding_box_check_box_center = self.main_window.center_preview_video_bounding_box_advanced_analytics_event_summary_check_box
            
        print("BEFORE VIDEO PLAYER THREAD INSTANCE")
        self.current_thread = VideoPlayerThread(center_video_path=center_video_path, front_video_path=front_video_path,
                                                main_window=self.main_window, slider=slider, has_actions=self.has_actions,
                                                keypoints_check_box_front=keypoints_checkbox_front,
                                                bounding_box_check_point_front=bounding_box_check_box_front,
                                                keypoints_check_box_center=keypoints_checkbox_center,
                                                bounding_box_check_point_center=bounding_box_check_box_center,
                                                is_advanced_analytics=is_advanced_analytics)
        
        self.current_thread.frames_signal.connect(self._update_panel)
        self.current_thread.current_frame_signal.connect(self.update_current_index)
        self.current_thread.current_frame_index_signal.connect(self.main_window.update_current_frame_index)
        self.current_thread.start()

    def start_video_player_with_heatmap_thread(self, center_video_path, front_video_path, target_panel):
        
        self.stop_current_thread()
        
        from utils import VideoPlayer_With_Heatmap_Thread
        
        self.target_panel = target_panel
        self.button = None
        
        keypoints_checkbox_front = None
        bounding_box_check_box_front = None
        keypoints_checkbox_center = None
        bounding_box_check_box_center = None
        

        # ASSIGN WHICH SLIDER
        # 0 - FOR PREVIEW
        # 1 - FOR AI ANALYTICS - HEATMAP
        # 2 - FOR AI ANALYTICS - LINE GRAPH
        # 3 - FOR AI ANALYTICS - TABLE LOGS
        # 4 - FOR ADVANCED ANALYTICS - HEATMAP
        # 5 - FOR ADVANCED ANALYTICS - LINE GRAPH
        # 6 - FOR ADVANCED ANALYTICS - TABLE LOGS

        if target_panel == 0:
            slider = self.main_window.time_frame_slider_import_preview
        
        elif target_panel == 1:
            slider = self.main_window.time_frame_range_slider_ai_analytics_heatmap
            button = self.main_window.play_pause_button_ai_analytics_heatmap
            self.play_pause_button = self.main_window.play_pause_button_ai_analytics_heatmap
            keypoints_checkbox_front = self.main_window.keypoints_check_box_ai_analytics_front
            bounding_box_check_box_front = self.main_window.bounding_box_check_box_ai_analytics_front
            keypoints_checkbox_center = self.main_window.keypoints_check_box_ai_analytics_center
            bounding_box_check_box_center = self.main_window.bounding_box_check_box_ai_analytics_center
            
            self.main_window.heatmap_update_selected_action_ai_analytics()
            
            # Create and start a new thread
            self.current_thread = VideoPlayer_With_Heatmap_Thread(center_video_path=center_video_path,
                                                                front_video_path=front_video_path,
                                                                main_window=self.main_window,
                                                                slider=slider,
                                                                button=button,
                                                                is_advanced_analytics=False,
                                                                keypoints_check_box_front=keypoints_checkbox_front,
                                                                keypoints_check_box_center=keypoints_checkbox_center,
                                                                bounding_box_check_point_front=bounding_box_check_box_front,
                                                                bounding_box_check_point_center=bounding_box_check_box_center)
        
        elif target_panel == 4:
            slider = self.main_window.time_frame_range_slider_advanced_analytics_heatmap
            button = self.main_window.play_pause_button_advanced_analytics_heatmap 
            self.main_window.heatmap_update_selected_action_advanced_analytics()
            self.play_pause_button = self.main_window.play_pause_button_advanced_analytics_heatmap
            keypoints_checkbox_front = self.main_window.keypoints_check_box_advanced_analytics_front
            bounding_box_check_box_front = self.main_window.bounding_box_check_box_advanced_analytics_front
            keypoints_checkbox_center = self.main_window.keypoints_check_box_advanced_analytics_center
            bounding_box_check_box_center = self.main_window.bounding_box_check_box_advanced_analytics_center
            
            # Create and start a new thread
            self.current_thread = VideoPlayer_With_Heatmap_Thread(center_video_path=center_video_path,
                                                            front_video_path=front_video_path,
                                                            main_window=self.main_window,
                                                            slider=slider,
                                                            button=button,
                                                            is_advanced_analytics=True,
                                                            keypoints_check_box_front=keypoints_checkbox_front,
                                                            keypoints_check_box_center=keypoints_checkbox_center,
                                                            bounding_box_check_point_front=bounding_box_check_box_front,
                                                            bounding_box_check_point_center=bounding_box_check_box_center)


        self.current_thread.filtered_bboxes_front = self.main_window.filtered_action_results_bboxes_front
        self.current_thread.filtered_bboxes_center = self.main_window.filtered_action_results_bboxes_center

        self.current_thread.frames_signal.connect(self._update_panel)
        self.current_thread.start()
    
    def generate_detection_video(self,center_video_path, front_video_path,is_advanced_analytics, directory):
        self.stop_current_thread()

        self.current_thread = Video_Detection_Export(main_window=self.main_window,
                                                     front_video_path=front_video_path,
                                                     center_video_path=center_video_path,
                                                     is_advanced_analytics=is_advanced_analytics,
                                                     video_output_directory=directory)
        self.current_thread.status_signal.connect(self.video_generated_notice)
        self.current_thread.start()    
    
    def video_generated_notice(self):
        
        self.destroy_current_thread()   
        QMessageBox.information(self.main_window, "Export Video", "Detection Video exported successfully!")                              
    
    def generate_heatmap_video(self,center_video_path, front_video_path,is_advanced_analytics, directory):
        self.stop_current_thread()
    
        self.current_thread = Export_Heatmap_Video_Thread(main_window=self.main_window,
                                                          front_video_path=front_video_path,
                                                          center_video_path=center_video_path,
                                                          is_advanced_analytics=is_advanced_analytics,
                                                          directory=directory)
        self.current_thread.finished_inference.connect(self.destroy_current_thread)
        self.current_thread.start()
    
    def generate_heatmap_image(self):
        center_video_directory = self.main_window.videoDirectory_center.text()
        front_video_directory = self.main_window.videoDirectory_front.text()
        
        self.heatmap_image_generator = Export_Heatmap_Image_Thread(front_video_path=front_video_directory,
                                                                   center_video_path=center_video_directory,
                                                                   main_window=self.main_window)
        
        self.heatmap_image_generator.finished_inference.connect(self.destroy_current_thread)
        self.heatmap_image_generator.start()
    
    def destroy_current_thread(self, status):
        if status:
            self.current_thread.stop()
            self.current_thread = None
    
    def pause_continue_current_video_player_thread(self):
        if self.current_thread is not None and self.current_thread.isRunning():
            self.current_thread.pause(not self.current_thread.paused)
        
        if self.current_thread is not None:
            if not self.current_thread.paused:
                self.play_pause_button.setIcon(self.pause_icon)
                self.play_pause_button.setText("PAUSE PREVIEW")
            else:
                self.play_pause_button.setIcon(self.play_icon)
                self.play_pause_button.setText("PLAY PREVIEW")
            
    def stop_current_thread(self):
        if self.current_thread is not None and self.current_thread.isRunning():
            self.current_thread.stop()
            self.current_thread = None

    def _update_panel(self, frames):

        if self.target_panel == 0:
            self.update_frame_for_preview(frame_list = frames)

        elif self.target_panel == 1:
            self.update_frame_for_ai_analytics_heatmap(frame_list = frames)

        elif self.target_panel == 2:
            self.update_frame_for_ai_analytics_line_graph(frame_list = frames)
        
        elif self.target_panel == 3:
            self.update_frame_for_ai_analytics_table_event_logs(frame_list = frames)
        
        elif self.target_panel == 4:
            self.update_frame_for_advance_analytics_heatmap(frame_list = frames)
        
        elif self.target_panel == 5:
            self.update_frame_for_advanced_analytics_line_graph(frame_list = frames)
        
        elif self.target_panel == 6:
            self.update_frame_for_advanced_analytics_event_logs_table(frame_list = frames)
         
        elif self.target_panel == 7:
            self.update_frame_for_ai_analytics_event_summary_table(frame_list = frames)
        
        elif self.target_panel == 8:
            self.update_frame_for_advanced_analytics_event_summary_table(frame_list = frames)
         

    def update_frame_for_preview(self, frame_list):
        '''
        This function is for updating the picture on the frames.
        More like key component to show frames and to look like a video

        Also to move the frame haha
        '''

        if frame_list is not None:
            
            center_frame = frame_list[0]
            front_frame = frame_list[1]
            center_black_frame = frame_list[2]
            front_black_frame = frame_list[3]
            
            '''
            THIS AREA IS FOR CENTER FRAME
            '''
            if self.main_window.center_preview_video_dark_mode_check_box.isChecked():
                self.update_video_preview_center(frame=center_black_frame, label=self.main_window.video_preview_label_center)
            else:
                self.update_video_preview_center(frame=center_frame, label=self.main_window.video_preview_label_center)
        
            '''
            THIS AREA IS FOR FRONT FRAME
            '''
            
            if self.main_window.front_preview_video_dark_mode_check_box.isChecked():
                self.update_video_preview(frame=front_black_frame, label=self.main_window.video_preview_label_front)
            
            else:
                self.update_video_preview(frame=front_frame, label=self.main_window.video_preview_label_front)

    def update_frame_for_ai_analytics_heatmap(self, frame_list):
        '''
        This function is for updating the picture on the frames.
        More like key component to show frames and to look like a video
        '''
        if frame_list is not None:
            classroom_heatmap = frame_list[0]
            front_black_frame = frame_list[1]
            center_black_frame = frame_list[2]
            front_video_frame = frame_list[3]
            center_video_frame = frame_list[4]

            '''THIS AREA IS FOR CENTER FRAME'''
            if self.main_window.dark_mode_check_box_ai_analytics_center.isChecked():
                self.update_video_center(frame=center_black_frame, label=self.main_window.video_preview_label_ai_analytics_center)
            else:
                self.update_video_center(frame=center_video_frame, label=self.main_window.video_preview_label_ai_analytics_center)
            
            '''THIS AREA IS FOR FRONT FRAME'''
            if self.main_window.dark_mode_check_box_ai_analytics_front.isChecked():
                self.update_video_preview(frame=front_black_frame, label=self.main_window.video_preview_label_ai_analytics_front)
            else:
                self.update_video_preview(frame=front_video_frame, label=self.main_window.video_preview_label_ai_analytics_front)

            '''---AREA FOR HEATMAP TO BE UPDATED HERE---'''

            self.update_heatmap_preview(frame=classroom_heatmap, label=self.main_window.heatmap_ai_analytics_label)

    def update_frame_for_ai_analytics_line_graph(self, frame_list):
        '''
        This function is for updating the picture on the frames.
        More like key component to show frames and to look like a video

        Also to move the frame haha
        '''

        if frame_list is not None:
            
            center_frame = frame_list[0]
            front_frame = frame_list[1]

            '''
            THIS AREA IS FOR CENTER FRAME
            '''
            self.update_video_center(frame=center_frame, label=self.main_window.ai_analytics_preview_center)
        
            '''
            THIS AREA IS FOR FRONT FRAME
            '''
            self.update_video_preview(frame=front_frame, label=self.main_window.ai_analytics_preview_front)

            # self.update_line_frame_position(current_frame_index=self.current_index,
            #                                 frame_component=self.main_window.vertical_line_frame,
            #                                 time_range_slider=self.main_window.time_frame_range_slider_ai_analytics_line_graph)

    def update_frame_for_ai_analytics_table_event_logs(self, frame_list):
        '''
        This function is for updating the picture on the frames.
        More like key component to show frames and to look like a video

        Also to move the frame haha
        '''
        if frame_list is not None:
            
            center_frame = frame_list[0]
            front_frame = frame_list[1]

            '''
            THIS AREA IS FOR CENTER FRAME
            '''
            self.update_video_center(frame=center_frame, label=self.main_window.ai_analytics_table_event_logs_preview_center)
        
            '''THIS AREA IS FOR FRONT FRAME'''
            self.update_video_preview(frame=front_frame, label=self.main_window.ai_analytics_table_event_logs_preview_front)
            
    def update_frame_for_advance_analytics_heatmap(self, frame_list):

        '''
        This function is for updating the picture on the frames.
        More like key component to show frames and to look like a video
        '''
        if frame_list is not None:
            classroom_heatmap = frame_list[0]
            front_black_frame = frame_list[1]
            center_black_frame = frame_list[2]
            front_video_frame = frame_list[3]
            center_video_frame = frame_list[4]


            if self.main_window.dark_mode_check_box_advanced_analytics_center.isChecked():
                self.update_video_center(frame=center_black_frame, label=self.main_window.advanced_analytics_heatmap_preview_center)
            else:
                self.update_video_center(frame=center_video_frame, label=self.main_window.advanced_analytics_heatmap_preview_center)
            
            '''THIS AREA IS FOR FRONT FRAME'''
            if self.main_window.dark_mode_check_box_advanced_analytics_front.isChecked():
                self.update_video_preview(frame=front_black_frame, label=self.main_window.advanced_analytics_heatmap_preview_front)
            else:
                self.update_video_preview(frame=front_video_frame, label=self.main_window.advanced_analytics_heatmap_preview_front)

            '''---AREA FOR HEATMAP TO BE UPDATED HERE---'''
            self.update_heatmap_preview(frame=classroom_heatmap, label=self.main_window.heatmap_advanced_analytics_label)

    def update_frame_for_advanced_analytics_line_graph(self, frame_list):
        '''
        This function is for updating the picture on the frames.
        More like key component to show frames and to look like a video

        Also to move the frame haha
        '''

        if frame_list is not None:
            
            center_frame = frame_list[0]
            front_frame = frame_list[1]

            '''
            THIS AREA IS FOR CENTER FRAME
            '''
            self.update_video_center(frame=center_frame, label=self.main_window.adv_analytics_preview_line_graph_center)
        
            '''
            THIS AREA IS FOR FRONT FRAME
            '''
            self.update_video_preview(frame=front_frame, label=self.main_window.adv_analytics_preview_line_graph_front)

    def update_frame_for_advanced_analytics_event_logs_table(self, frame_list):

        if frame_list is not None:
            
            center_frame = frame_list[0]
            front_frame = frame_list[1]

            self.update_video_center(frame=center_frame, label=self.main_window.adv_analytics_preview_event_logs_table_center)
            self.update_video_preview(frame=front_frame, label=self.main_window.adv_analytics_preview_event_logs_table_front)

    def update_frame_for_ai_analytics_event_summary_table(self, frame_list):

        if frame_list is not None:
            
            center_frame = frame_list[0]
            front_frame = frame_list[1]

            self.update_video_center(frame=center_frame, label=self.main_window.ai_analytics_chunk_summary_preview_center)
            self.update_video_preview(frame=front_frame, label=self.main_window.ai_analytics_chunk_summary_preview_front)
            
    def update_frame_for_advanced_analytics_event_summary_table(self, frame_list):

        if frame_list is not None:
            
            center_frame = frame_list[0]
            front_frame = frame_list[1]

            self.update_video_center(frame=center_frame, label=self.main_window.advanced_analytics_chunk_summary_preview_center)
            self.update_video_preview(frame=front_frame, label=self.main_window.advanced_analytics_chunk_summary_preview_front)

    def update_video_preview(self, frame, label):
        if len(frame.shape) == 3:
            video_height, video_width, _ = frame.shape
        else:
            video_height, video_width = frame.shape

        # initial_row_height = int(video_height * (1 / 16))  # Bottom 4 rows (adjust as needed)

        # cv2.line(img=frame, pt1=(0, initial_row_height), pt2=(video_width, initial_row_height), color=(0, 255, 0), thickness=2)

        bytes_per_line = 3 * video_width
        q_img = QImage(frame.data, video_width, video_height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        pixmap = QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
        
        label.setPixmap(scaled_pixmap)
        
    def update_video_center(self, frame, label, crop_bottom=250):
        # Step 1: Crop side black bars (assume 2520x1080 input, crop to 1920x1080)
        if frame.shape[1] == 2520:
            start_x = (frame.shape[1] - 1920) // 2 
            frame = frame[:, start_x:start_x + 1920]

        # Step 2: Crop the bottom portion of the frame
        frame = frame[:frame.shape[0] - crop_bottom, :]

        # Step 3: Ensure the frame is C-contiguous
        frame = frame.copy()

        video_height, video_width = frame.shape[:2]
        bytes_per_line = 3 * video_width

        q_img = QImage(frame.data, video_width, video_height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        label.setPixmap(scaled_pixmap)

    def update_video_preview_center(self, frame, label):
        # Step 1: Crop side black bars (assume 2520x1080 input, crop to 1920x1080)
        if frame.shape[1] == 2520:
            start_x = (frame.shape[1] - 1920) // 2 
            frame = frame[:, start_x:start_x + 1920]

        # Step 3: Ensure the frame is C-contiguous
        frame = frame.copy()

        video_height, video_width = frame.shape[:2]
        bytes_per_line = 3 * video_width

        q_img = QImage(frame.data, video_width, video_height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()
        pixmap = QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(label.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)

        label.setPixmap(scaled_pixmap)



    def update_heatmap_preview(self, frame, label):
        if len(frame.shape) == 3:
            video_height, video_width, _ = frame.shape
        else:
            video_height, video_width = frame.shape

        # initial_row_height = int(video_height * (1 / 16))  # Bottom 4 rows (adjust as needed)

        # cv2.line(img=frame, pt1=(0, initial_row_height), pt2=(video_width, initial_row_height), color=(0, 255, 0), thickness=2)

        bytes_per_line = 3 * video_width
        q_img = QImage(frame.data, video_width, video_height, bytes_per_line, QImage.Format_RGB888).rgbSwapped()

        pixmap = QPixmap.fromImage(q_img)
        scaled_pixmap = pixmap.scaled(label.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        
        label.setPixmap(scaled_pixmap)

    def update_line_frame_position(self, current_frame_index, frame_component, time_range_slider):
        """Move the vertical line (`QFrame`) according to the video frame position."""

        # Get the width of the chart only, not the whole graphics view
        chart_width = 1100
        chart_beginning = 260

        # Calculate relative position within the graph
        #Get any slider with the parameter
        init_min_frame, init_max_frame = time_range_slider.value()
        max_frame = init_max_frame-init_min_frame
        min_frame = 0
        relative_x = int(((current_frame_index - min_frame) / float(max_frame - min_frame)) * chart_width)

        print("Relative Initial X: ", relative_x)
        # Ensure the position is within bounds
        relative_x = max(chart_beginning, min(relative_x, chart_width - frame_component.width()))
        print("Relative Processed X: ", relative_x)


    def update_current_index(self, current_index):
        self.current_index = current_index
        
    