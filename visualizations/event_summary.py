from collections import deque, Counter
from PySide6.QtWidgets import QTableWidgetItem, QHeaderView
from PySide6.QtCore import Qt

class AI_Analytics_Chunk_Summary_Log:
    def __init__(self, main_window, chunk_size_seconds=2, fps=30, max_chunks=10):
        self.main_window = main_window
        self.fps = fps
        self.table_widget = self.main_window.ai_analytics_event_summary_table
        
        self.min_value = 0
        self.max_value = 0
        
        self.interval_minutes = 0
        self.interval_seconds = 2
        self.chunk_size_in_seconds = chunk_size_seconds
        self.chunk_size = self.chunk_size_in_seconds * fps
        self.max_chunks = max_chunks
        self.frame_counter = 0
        self.chunks = deque(maxlen=max_chunks)
        self.current_chunk_data = []
        self.start_time = 0  # Start time for chunking (in seconds)
        self.main_window.time_frame_range_slider_ai_analytics_table_event_summary.valueChanged.connect(self._update_min_max_value)
        self.main_window.ai_analytics_interval_slider_minutes.valueChanged.connect(self._update_chunk_size_minutes)
        self.main_window.ai_analytics_interval_slider_seconds.valueChanged.connect(self._update_chunk_size_seconds)
        
        
        self._update_total_interval_seconds()
        
        self._initialize_table_headers()
    
    def _initialize_table_headers(self):
        """Initial setup of the table headers and column sizes."""
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Time Range", "AI Summary Log"])
        self.table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.table_widget.horizontalHeader().setStretchLastSection(False)

        # Column width allocation
        total_width = self.table_widget.viewport().width()
        time_col_width = int(total_width * 0.25)
        summary_col_width = total_width - time_col_width

        self.table_widget.setColumnWidth(0, time_col_width)
        self.table_widget.setColumnWidth(1, summary_col_width)

        # Fixed column sizes
        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        header.setSectionResizeMode(1, QHeaderView.Fixed)

        # Disable scrollbars
        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Enable word wrap
        self.table_widget.setWordWrap(True)



    def _update_chunk_size_minutes(self, value):
        self.interval_minutes = value
        self._update_total_interval_seconds()
    
    def _update_chunk_size_seconds(self, value):
        self.interval_seconds = value
        self._update_total_interval_seconds()
    
    def _update_total_interval_seconds(self):
        interval_minutes_to_seconds = self.interval_minutes * 60
        interval_seconds = self.interval_seconds
        
        total_interval_seconds = interval_minutes_to_seconds + interval_seconds
        
        total_interval_seconds_to_fps = total_interval_seconds * self.fps
        
        self.chunk_size = total_interval_seconds_to_fps
        
        self.main_window.interval_time_label.setText(f"{self.interval_minutes} mins {self.interval_seconds} secs")
    
    def _update_min_max_value(self):
        self.min_value, self.max_value = self.main_window.time_frame_range_slider_ai_analytics_table_event_summary.value()
        self._reset_data()
        
    def _update_table(self):
        self.table_widget.setRowCount(len(self.chunks))
        self.table_widget.setWordWrap(True)  # This enables word wrapping at the table level

        for row, (time_range, summary) in enumerate(self.chunks):
            time_item = QTableWidgetItem(time_range)
            time_item.setTextAlignment(Qt.AlignLeft)
            time_item.setFlags(time_item.flags() ^ Qt.ItemIsEditable)
            self.table_widget.setItem(row, 0, time_item)

            summary_item = QTableWidgetItem(summary)
            summary_item.setTextAlignment(Qt.AlignLeft | Qt.AlignTop)
            summary_item.setFlags(summary_item.flags() ^ Qt.ItemIsEditable)
            # Removed summary_item.setWordWrap(True) — not supported
            self.table_widget.setItem(row, 1, summary_item)

            self.table_widget.resizeRowToContents(row)  # Adjust row height based on content


        self._resize_table_height_to_fit()

    def _resize_table_height_to_fit(self):
        """Auto-resize the table widget height to avoid scrollbars and fit content."""
        total_height = self.table_widget.horizontalHeader().height()
        for row in range(self.table_widget.rowCount()    ):
            total_height += self.table_widget.rowHeight(row)
        self.table_widget.setFixedHeight(total_height)


    def _finalize_chunk(self):
        counter = Counter(self.current_chunk_data)
        total = sum(counter.values())

        if total == 0:
            print("⚠️ Finalized chunk but had no data.")
            return  # Avoid inserting empty rows

        # Create summary string
        summary_parts = []
        for posture, count in counter.most_common():
            percent = round((count / total) * 100)
            summary_parts.append(f"{percent}% are {posture}")
        sentence = ", ".join(summary_parts)

        print("✅ Chunk Summary:", sentence)

        # Generate time range (00:00 - 00:05, 00:05 - 00:10, etc.)
        end_time = self.start_time + (self.chunk_size // self.fps)
        start_time_str = self._format_time(self.start_time)
        end_time_str = self._format_time(end_time)
        time_range = f"{start_time_str} - {end_time_str}"

        self.chunks.appendleft((time_range, sentence))
        self._update_table()
        print("📦 Current Chunks:")
        for idx, (time_range, summary) in enumerate(self.chunks):
            print(f"{idx+1}. Time: {time_range} | Summary: {summary}")

    def _format_time(self, time_in_seconds):
        """Format seconds into HH:MM:SS format"""
        minutes, seconds = divmod(time_in_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def update_frame(self,frame_index, postures_dict):
        """Call this every frame with the merged posture data dict"""
        
        self.min_value, self.max_value = self.main_window.time_frame_range_slider_ai_analytics_table_event_summary.value()
        
        if frame_index == self.min_value:
            self._reset_data()
            self.start_time = self.min_value // self.fps
            return
        
        self.frame_counter += 1

        # Add posture values to current chunk
        self.current_chunk_data.extend(postures_dict.values())

        # Check if it's time to finalize the current chunk
        if self.frame_counter >= self.chunk_size:
            self._finalize_chunk()
            self.frame_counter = 0
            self.current_chunk_data = []
            self.start_time += self.chunk_size // self.fps  # Advance start time in seconds

    def _reset_data(self):
        """Reset table data and chunking variables only once when the first valid frame is encountered"""
        self.table_widget.setRowCount(0)  # Clear table content
        self.chunks.clear()  # Clear chunk data
        self.current_chunk_data = []  # Clear current chunk data
        self.frame_counter = 0  # Reset frame counter
        self.start_time = 0  # Reset the starting time
    
    def extract_summary_chunks(self):
        """Returns the chunk summary data in a format suitable for DOCX."""
        return [{'time_range': time_range, 'summary': summary} for time_range, summary in self.chunks]

    
        



class Advanced_Analytics_Chunk_Summary_Log:
    def __init__(self, main_window, chunk_size_seconds=2, fps=30, max_chunks=10):
        self.main_window = main_window
        self.fps = fps
        self.table_widget = self.main_window.advanced_analytics_event_summary_table
        
        self.min_value = 0
        self.max_value = 0

        self.interval_minutes = 0
        self.interval_seconds = 5

        self.chunk_size_in_seconds = chunk_size_seconds
        self.chunk_size = self.chunk_size_in_seconds * fps
        
        self.max_chunks = max_chunks
        self.frame_counter = 0
        self.chunks = deque(maxlen=max_chunks)
        self.current_chunk_data = []
        self.start_time = 0  # in seconds

        self.main_window.time_frame_range_slider_advanced_analytics_table_event_summary.valueChanged.connect(self._update_min_max_value)
        self.main_window.advanced_analytics_interval_slider_minutes.valueChanged.connect(self._update_chunk_size_minutes)
        self.main_window.advanced_analytics_interval_slider_seconds.valueChanged.connect(self._update_chunk_size_seconds)
        
        self._update_total_interval_seconds()
        self._initialize_table_headers()
        

    def _initialize_table_headers(self):
        self.table_widget.setColumnCount(2)
        self.table_widget.setHorizontalHeaderLabels(["Time Range", "Advanced AI Summary"])
        self.table_widget.horizontalHeader().setDefaultAlignment(Qt.AlignCenter)
        self.table_widget.horizontalHeader().setStretchLastSection(False)

        total_width = self.table_widget.viewport().width()
        time_col_width = int(total_width * 0.25)
        summary_col_width = total_width - time_col_width

        self.table_widget.setColumnWidth(0, time_col_width)
        self.table_widget.setColumnWidth(1, summary_col_width)

        header = self.table_widget.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Fixed)
        header.setSectionResizeMode(1, QHeaderView.Fixed)

        self.table_widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.table_widget.setWordWrap(True)

    def _update_chunk_size_minutes(self, value):
        self.interval_minutes = value
        self._update_total_interval_seconds()

    def _update_chunk_size_seconds(self, value):
        self.interval_seconds = value
        self._update_total_interval_seconds()

    def _update_total_interval_seconds(self): 
        total_interval_seconds = (self.interval_minutes * 60) + self.interval_seconds
        self.chunk_size = total_interval_seconds * self.fps
        self.main_window.interval_time_label_advanced_analytics.setText(f"{self.interval_minutes} mins {self.interval_seconds} secs")

    def _update_min_max_value(self):
        self.min_value, self.max_value = self.main_window.time_frame_range_slider_advanced_analytics_table_event_summary.value()
        self._reset_data()

    def _update_table(self):
        self.table_widget.setRowCount(len(self.chunks))
        self.table_widget.setWordWrap(True)

        for row, (time_range, summary) in enumerate(self.chunks):
            time_item = QTableWidgetItem(time_range)
            time_item.setTextAlignment(Qt.AlignLeft)
            time_item.setFlags(time_item.flags() ^ Qt.ItemIsEditable)
            self.table_widget.setItem(row, 0, time_item)

            summary_item = QTableWidgetItem(summary)
            summary_item.setTextAlignment(Qt.AlignLeft | Qt.AlignTop)
            summary_item.setFlags(summary_item.flags() ^ Qt.ItemIsEditable)
            self.table_widget.setItem(row, 1, summary_item)

            self.table_widget.resizeRowToContents(row)

        self._resize_table_height_to_fit()

    def _resize_table_height_to_fit(self):
        total_height = self.table_widget.horizontalHeader().height()
        for row in range(self.table_widget.rowCount()):
            total_height += self.table_widget.rowHeight(row)
        self.table_widget.setFixedHeight(total_height)

    def _finalize_chunk(self):
        counter = Counter(self.current_chunk_data)
        total = sum(counter.values())

        if total == 0:
            print("⚠️ Finalized chunk but had no data.")
            return

        summary_parts = []
        for posture, count in counter.most_common():
            percent = round((count / total) * 100)
            summary_parts.append(f"{percent}% are {posture}")
        sentence = ", ".join(summary_parts)

        print("✅ Advanced Chunk Summary:", sentence)

        end_time = self.start_time + (self.chunk_size // self.fps)
        start_time_str = self._format_time(self.start_time)
        end_time_str = self._format_time(end_time)
        time_range = f"{start_time_str} - {end_time_str}"

        self.chunks.appendleft((time_range, sentence))
        self._update_table()

    def _format_time(self, time_in_seconds):
        minutes, seconds = divmod(time_in_seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

    def update_frame(self, frame_index, head_posture_list_front, head_posture_list_center, arms_posture_list_front, arms_posture_list_center):
        self.min_value, self.max_value = self.main_window.time_frame_range_slider_advanced_analytics_table_event_summary.value()

        if frame_index == self.min_value:
            self._reset_data()
            self.start_time = self.min_value // self.fps
            return

        self.frame_counter += 1

        # Collect all postures from both head and arm posture sources
        for posture_dict in head_posture_list_front + head_posture_list_center:
            for data in posture_dict.values():
                self.current_chunk_data.append(data['head_posture'])

        for arms_dict in arms_posture_list_front + arms_posture_list_center:
            for data in arms_dict.values():
                self.current_chunk_data.append(str("Right Arm " + data['right_arm_posture']))
                self.current_chunk_data.append(str("Left Arm " + data['left_arm_posture']))

        if self.frame_counter >= self.chunk_size:
            self._finalize_chunk()
            self.frame_counter = 0
            self.current_chunk_data = []
            self.start_time += self.chunk_size // self.fps

    def _reset_data(self):
        self.table_widget.setRowCount(0)
        self.chunks.clear()
        self.current_chunk_data = []
        self.frame_counter = 0
        self.start_time = 0
    
    def extract_summary_chunks(self):
        """Returns the chunk summary data in a format suitable for DOCX."""
        return [{'time_range': time_range, 'summary': summary} for time_range, summary in self.chunks]
