import cv2
from PySide6.QtCore import QThread, Signal
import numpy as np

from ultralytics import YOLO
import queue
import threading
from PySide6.QtGui import QImage, QPixmap

from pathlib import Path


class VideoUtils:
    
    def __init__(self) -> None:
        pass

    def read_video(self, video_path, resize_frames): #LIST
        cap = cv2.VideoCapture(video_path)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            if resize_frames:
                resized_frame = cv2.resize(frame, (1088, 608))
                frames.append(resized_frame)
            else:
                frames.append(frame)
        cap.release()
        return frames
    #Old Code
    
    def save_video(self, output_video_frames, output_video_path, monitorFrames=False):
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')
        
        out = cv2.VideoWriter(output_video_path, fourcc, 24, (output_video_frames[0].shape[1], output_video_frames[0].shape[0]))
        
        for frame in output_video_frames:
            out.write(frame)
            if monitorFrames:
                cv2.imshow("Monitor Frames", frame)
                cv2.waitKey(1)
        out.release()
    
    def generate_white_frame(self, height, width):
        white_frame = np.ones((height, width, 3), dtype=np.uint8) * 255 # Create a white frame (all pixel values set to 255)
        return white_frame

class WhiteFrameGenerator(QThread):
    progress_update = Signal(object)
    return_white_frames = Signal(object)
    
    def __init__(self, number_of_frames, width, height):
        super().__init__()
        self.number_of_frames = number_of_frames
        self.videoWidth = width
        self.videoHeight = height
        self._running = True
    def run(self):
        white_frames = []
        current_frame = 0
        total_frames_length = self.number_of_frames
        for frame in range(total_frames_length):
            white_frame = np.ones((self.videoHeight, self.videoWidth, 3), dtype=np.uint8) * 0 
            white_frames.append(white_frame)
            current_frame += 1
            progress = int(current_frame/total_frames_length *100)
            
            self.progress_update.emit(progress)
            
            del white_frame
            del progress
            
        self.return_white_frames.emit(white_frames)
        del white_frames
    def stop(self):
        self._running = False
        self.wait()


class VideoProcessorThread(QThread):
    '''
    This class is used to process the video in a thread.
    It will process the video frame by frame and emit signals with the results.
    What I mean with processing is to detect humans and their keypoints frame by frame. 
    Appending each result in the corresponding list.
    Emmits signals with the results.

    Here is the pseudo code:
    1. Read the video
    2. Get the total frames
    3. Loop through the video frames
       (Inside the loop)
        4. Get the frame
        5. Detect humans in the frame
        detected_human = [{Person1: 4 Corners; Person2: 4corners}]

        6. Append the results in the human_detect_results_list - GLOBAL

        7. Detect the keypoints in the frame based on the results of the cropped image in the human_detect_results_list

        8. Append the results in the human_pose_results_list
        
        9. Update the progress
    (Outside the loop)
    10. Emit the signals with the results

    '''
    #Initiate the signals

    human_detect_results = Signal(object)
    human_pose_results = Signal(object)
    progress_update = Signal(object)
    finished_signal = Signal(float, float)

    def __init__(self, video_path,
                 resize_frames = False,
                 isFront = True,
                 human_detection_model = None,
                 human_detection_confidence = 0.5,
                 human_pose_model = None,
                 human_pose_confidence = 0.5,
                 main_window = None,
                 camera_angle = None):

        super().__init__()

        self.isFront = isFront
        self.human_detection_model = YOLO(human_detection_model)  
        self.human_detection_confidence = human_detection_confidence
        self.human_pose_model = YOLO(human_pose_model)
        self.human_pose_confidence = human_pose_confidence
        self.main_window = main_window

        self.human_detect_results_list = []
        self.human_pose_results_list = []

        self.video_path = video_path
        self.resize_frames = resize_frames

        self.initial_row_height = None

        self._running = True
        
        self.camera_angle = camera_angle

    #Mask for front camera
    def create_roi_mask(self, frame, row_height):
        height, width, _ = frame.shape
        mask = np.zeros((height, width), dtype=np.uint8)
        roi = (0, row_height+10, width, height)  # Bottom to middle
        cv2.rectangle(mask, (roi[0], roi[1]), (roi[2], roi[3]), 255, -1)
        cv2.line(img=frame, pt1=(0, row_height), pt2=(frame.shape[1], row_height),color = (0,255,0), thickness=2)
        return mask
    
    def create_roi_mask_center(self, frame, row_height):
        height, width, _ = frame.shape
        mask = np.zeros((height, width), dtype=np.uint8)

        # Define the visible (unmasked) region: from top (0) to `row_height`
        roi_bottom = min(height, row_height)
        cv2.rectangle(mask, (0, 0), (width, roi_bottom), 255, -1)  # White = keep

        # Optional: draw a visual guide line at the cutoff
        cv2.line(frame, (0, roi_bottom), (width, roi_bottom), (0, 255, 0), 2)

        return mask

        
    #Human Detection
    def human_detect(self, frame):
    # Initialize dictionary for tracking students
        student_dict = {}

        # Check if the front camera is being used and apply ROI mask if so
        if self.isFront:
            roi_mask = self.create_roi_mask(frame, self.initial_row_height)
            masked_frame = cv2.bitwise_and(frame, frame, mask=roi_mask)
            input_frame = masked_frame
        else:
            roi_mask = self.create_roi_mask_center(frame, self.initial_row_height)
            masked_frame = cv2.bitwise_and(frame, frame, mask=roi_mask)
            input_frame = masked_frame

        results = self.human_detection_model.track(
                                                    input_frame,
                                                    conf=self.human_detection_confidence,
                                                    persist=True,
                                                    classes=0,
                                                    iou=0.4,
                                                    agnostic_nms=True
                                                )[0]




        id_name_dict = results.names

        for result in results:
            boxes = result.boxes
            for box in boxes:
                if box.id is not None and box.xyxy is not None and box.cls is not None:
                    track_id = int(box.id.tolist()[0])
                    track_result = box.xyxy.tolist()[0]
                    object_cls_id = box.cls.tolist()[0]
                    object_cls_name = id_name_dict.get(object_cls_id, "unknown")

                    if object_cls_name == "person":
                        student_dict[str(str(track_id) + str(self.camera_angle))] = track_result
                else:
                    print("One of the attributes is None:", box.id, box.xyxy, box.cls)
                    continue  # Avoids UnboundLocalError

        return student_dict  # ✅ Always return a dictionary

    
    #Human Pose Detection
    def human_pose_detect(self, frame, human_results):
        keypoints_dict = {}  # Initialize here to store keypoints for all detections in the frame

        for track_id, bbox in human_results.items():
            # Extract the bounding box coordinates
            x1, y1, x2, y2 = map(int, bbox)
            cropped_image = frame[y1:y2, x1:x2]

            try:
                # Perform pose detection on the cropped image
                results = self.human_pose_model(cropped_image, self.human_pose_confidence)
                for result in results:
                    if result.keypoints:
                        keypoints_normalized = np.array(result.keypoints.xyn.cpu().numpy()[0])
                        keypoints_dict[track_id] = keypoints_normalized
                    else:
                        print(f"Error processing track ID {track_id}: {e}")
            except Exception as e:
                print(f"Error processing track ID {track_id}: {e}")
                keypoints_dict[track_id] = None
        
        return keypoints_dict

    def extend_frame_width(self,frame: np.ndarray, extension: int = 300) -> np.ndarray:


        height, width, channels = frame.shape
        
        # Ensure the input frame is 1920x1080
        if width != 1920 or height != 1080:
            raise ValueError("Expected a 1920x1080 frame.")
        
        # Create a new black frame with extended width
        new_width = width + (2 * extension)
        extended_frame = np.zeros((height, new_width, channels), dtype=np.uint8)
        
        # Place the original frame in the center
        extended_frame[:, extension:extension + width] = frame
        
        return extended_frame
    
    #Main function to run in a thread
    def run(self):
        #Get the video
        cap = cv2.VideoCapture(self.video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        current_frame = 0

        #Variables for the human detection model
        
        while self._running:
            ret, retrieved_frame = cap.read() #Get the frame

            
            
            #Safety net if there is no frame anymore
            if not ret:
                break
            
            #Extend the frame
            frame = self.extend_frame_width(frame=retrieved_frame,
                                            extension=300)
            
            #Get the shape of the frame
            height, width, _ = frame.shape

            #Get the initial row height
            if self.isFront:
                self.initial_row_height = int(height * (1/16))  # Bottom 4 rows (adjust as needed)
            else:
                self.initial_row_height = int(height * (180/300))  # Bottom 4 rows (adjust as needed)
            
            human_detect_results = self.human_detect(frame)
            human_pose_detect_results = self.human_pose_detect(frame, human_detect_results)

            self.human_detect_results_list.append(human_detect_results)
            self.human_pose_results_list.append(human_pose_detect_results)

            current_frame += 1
            progress = int(current_frame/total_frames *100)
            self.progress_update.emit(progress)
            
            del frame #Just to delete unnecessary data

        self.human_detect_results.emit(self.human_detect_results_list)
        self.human_pose_results.emit(self.human_pose_results_list)
        

        #Just to delete unnecessary data
        del self.human_detect_results_list
        del self.human_pose_results_list

        cap.release() #Release the video

    def stop(self):
        self._running = False
        self.wait()


