import os
import cv2
from PySide6.QtCore import QThread, Signal
from docxtpl import DocxTemplate, InlineImage
from docx.shared import Inches, Cm
from pathlib import Path
from datetime import date, time, datetime
from visualizations import Advanced_Analytics_Chunk_Summary_Log, AI_Analytics_Chunk_Summary_Log
from collections import deque
from docx2pdf import convert
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox


class DocxGenerationThread(QThread):
    finished = Signal(str)  # Signal to notify when done
    
    def __init__(self, main_window, directory):
        super().__init__() 
        self.main_window = main_window
        self.directory = directory

    
    def extract_summary_chunks(self, summary_log_class):
        chunks_data = []
        chunks = getattr(summary_log_class, "chunks", [])

        for time_range, summary in chunks:
            chunk_dict = {
                "time_range": time_range,
                "summary": summary
            }
            chunks_data.append(chunk_dict)


        return chunks_data
    
    def get_video_length(self, video_path):

        # Open the video file
        cap = cv2.VideoCapture(video_path)

        # Get the total number of frames
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        # Get the frame rate (fps)
        fps = cap.get(cv2.CAP_PROP_FPS)

        # Compute the duration in seconds
        duration_seconds = total_frames / fps

        # Convert to hours, minutes, seconds
        hours = int(duration_seconds // 3600)
        minutes = int((duration_seconds % 3600) // 60)
        seconds = int(duration_seconds % 60)

        cap.release()

        # Return formatted string
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    
    def run(self):
        try:
            self.main_window.update_export_progress_bar(0)
            script_dir = Path(__file__).parent
            docx_path = script_dir.parent / "assets" / "Output_Template_Thesis.docx"
            template_path = docx_path
            print("Resolved template path:", template_path)

            if not os.path.exists(template_path):
                print("❌ Template file not found! Check path above.")
                self.finished.emit("Error: Template file not found")
                return

            doc = DocxTemplate(template_path)
            assets_dir = script_dir.parent / "visualizations" / "temp"

            ai_summary_chunks = self.extract_summary_chunks(self.main_window.AI_Analytics_Event_Summary)
            adv_summary_chunks = self.extract_summary_chunks(self.main_window.Advanced_Analytics_Event_Summary)

            front_video_length = self.get_video_length(str(self.main_window.videoDirectory_front.text()))
            center_video_length = self.get_video_length(str(self.main_window.videoDirectory_center.text()))
            
            self.main_window.time_exported = str(datetime.today().strftime('%m/%d/%Y'))

            context = {
                "Session_Name": self.main_window.session_name,
                "Analytics_ID": "A12345",
                "Date_Downloaded": str(datetime.today().strftime('%m/%d/%Y')),
                "Time_Downloaded": str(datetime.now().strftime('%I:%M:%S %p')),
                "File_Name": f"{self.main_window.session_name}_ACE_Output_Document.docx",
                "AI_Front_File_Path": str(self.main_window.videoDirectory_center.text()),
                "AI_Front_File_Size": str(round(os.path.getsize(str(self.main_window.videoDirectory_front.text())) / (1024 * 1024), 2)) + " MB",
                "AI_Front_Video_Length": front_video_length,
                "AI_Center_File_Path": str(self.main_window.videoDirectory_center.text()),
                "AI_Center_File_Size": str(round(os.path.getsize(str(self.main_window.videoDirectory_center.text())) / (1024 * 1024), 2)) + " MB",
                "AI_Center_Video_Length": center_video_length,
                "AI_Analytics_Chunk_Summary_Log": ai_summary_chunks,
                "Advanced_Analytics_Chunk_Summary_Log": adv_summary_chunks,
                "AI_Front_File_Path": self.main_window.videoDirectory_front.text(),
            }

            line_graph_image_paths = {
                "LineGraph_All_Actions_AI": os.path.join(assets_dir, "All_Actions_AI_Analytics.jpg"),
                "LineGraph_ExtendingRight_Actions_AI": os.path.join(assets_dir, "RIGHT_ARM_EXTENDING_SIDEWARDS_AI_Analytics.jpg"),
                "LineGraph_ExtendingLeft_Actions_AI": os.path.join(assets_dir, "LEFT_ARM_EXTENDING_SIDEWARDS_AI_Analytics.jpg"),
                "LineGraph_Sitting_Actions_AI": os.path.join(assets_dir, "SITTING_AI_Analytics.jpg"),
                "LineGraph_Standing_Actions_AI": os.path.join(assets_dir, "STANDING_AI_Analytics.jpg"),
                "LineGraph_Facing_Left_AI": os.path.join(assets_dir, "FACING_LEFT_AI_Analytics.jpg"),
                "LineGraph_Facing_Right_AI": os.path.join(assets_dir, "FACING_RIGHT_AI_Analytics.jpg"),
                "LineGraph_Facing_Downward_AI": os.path.join(assets_dir, "FACING_DOWNWARDS_AI_Analytics.jpg"),
                "LineGraph_Facing_Forward_AI": os.path.join(assets_dir, "FACING_FORWARD_AI_Analytics.jpg"),
                "LineGraph_All_Actions_Advanced": os.path.join(assets_dir, "All_Actions_Advanced_Analytics.jpg"),
                "LineGraph_ExtendingRight_Actions_Advanced": os.path.join(assets_dir, "RIGHT_ARM_EXTENDING_SIDEWARDS_Advanced_Analytics.jpg"),
                "LineGraph_ExtendingLeft_Actions_Advanced": os.path.join(assets_dir, "LEFT_ARM_EXTENDING_SIDEWARDS_Advanced_Analytics.jpg"),
                "LineGraph_Sitting_Actions_Advanced": os.path.join(assets_dir, "SITTING_Advanced_Analytics.jpg"),
                "LineGraph_Standing_Actions_Advanced": os.path.join(assets_dir, "STANDING_Advanced_Analytics.jpg"),
                "LineGraph_Facing_Left_Advanced": os.path.join(assets_dir, "FACING_LEFT_Advanced_Analytics.jpg"),
                "LineGraph_Facing_Right_Advanced": os.path.join(assets_dir, "FACING_RIGHT_Advanced_Analytics.jpg"),
                "LineGraph_Facing_Downward_Advanced": os.path.join(assets_dir, "FACING_DOWNWARDS_Advanced_Analytics.jpg"),
                "LineGraph_Facing_Forward_Advanced": os.path.join(assets_dir, "FACING_FORWARD_Advanced_Analytics.jpg"),
                "LineGraph_RightArmResting_Actions_Advanced": os.path.join(assets_dir, "RIGHT_ARM_NEUTRAL_(RESTING)_Advanced_Analytics.jpg"),
                "LineGraph_RightArmUnknown_Actions_Advanced": os.path.join(assets_dir, "RIGHT_ARM_UNKNOWN_Advanced_Analytics.jpg"),
                "LineGraph_LeftArmResting_Actions_Advanced": os.path.join(assets_dir, "LEFT_ARM_NEUTRAL_(RESTING)_Advanced_Analytics.jpg"),
                "LineGraph_LeftArmUnknown_Actions_Advanced": os.path.join(assets_dir, "LEFT_ARM_UNKNOWN_Advanced_Analytics.jpg"),
                
            }

            heatmap_image_paths = {
                "Heatmap_All_Actions_AI_Analytics_25": os.path.join(assets_dir, "ai_analytics_heatmap_checkpoint_25.jpg"),
                "Heatmap_All_Actions_AI_Analytics_50": os.path.join(assets_dir, "ai_analytics_heatmap_checkpoint_50.jpg"),
                "Heatmap_All_Actions_AI_Analytics_75": os.path.join(assets_dir, "ai_analytics_heatmap_checkpoint_75.jpg"),
                "Heatmap_All_Actions_AI_Analytics_100": os.path.join(assets_dir, "ai_analytics_heatmap_checkpoint_100.jpg"),
                "Heatmap_All_Actions_Advanced_Analytics_25": os.path.join(assets_dir, "advanced_analytics_heatmap_checkpoint_25.jpg"),
                "Heatmap_All_Actions_Advanced_Analytics_50": os.path.join(assets_dir, "advanced_analytics_heatmap_checkpoint_50.jpg"),
                "Heatmap_All_Actions_Advanced_Analytics_75": os.path.join(assets_dir, "advanced_analytics_heatmap_checkpoint_75.jpg"),
                "Heatmap_All_Actions_Advanced_Analytics_100": os.path.join(assets_dir, "advanced_analytics_heatmap_checkpoint_100.jpg")
            }

            all_images = {**line_graph_image_paths, **heatmap_image_paths}
            total_images = len(all_images)
            progress_start = 10
            progress_end = 90
            progress_step = (progress_end - progress_start) / total_images
            current_progress = progress_start

            for key, path in all_images.items():
                if os.path.exists(path):
                    if "LineGraph" in key:
                        context[key] = InlineImage(doc, path, width=Cm(17.75), height=Cm(4.25))
                    else:
                        context[key] = InlineImage(doc, path, width=Cm(9.99), height=Cm(7.5))
                else:
                    context[key] = "Image not found"

                current_progress += progress_step
                self.main_window.update_export_progress_bar(int(current_progress // 5) * 5)  # Round down to nearest 5

            doc.render(context)
            output_docx_path = os.path.join(self.directory, f"{self.main_window.session_name}_ACE_Output_Document.docx")
            doc.save(output_docx_path)

            self.main_window.update_export_progress_bar(95)

            output_pdf_path = os.path.join(self.directory, f"{self.main_window.session_name}_ACE_Output_Document.pdf")
            
            
            try:
                convert(output_docx_path, output_pdf_path)

                if os.path.exists(output_pdf_path):  # ✅ Only remove if PDF was actually created
                    os.remove(output_docx_path)
                    self.main_window.update_export_progress_bar(100)
                else:
                    raise Exception("PDF file was not created after conversion.")
            except Exception as e:
                print(f"PDF conversion failed: {e}")




            self.finished.emit(output_pdf_path)

        except Exception as e:
            self.finished.emit(f"Error: {str(e)}")

    def stop(self):
        # Wait for the thread to finish if it is not in the process of quitting
        self.quit()  
        self.wait()  