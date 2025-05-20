

import numpy as np
from PySide6.QtCore import QThread, Signal

class HeadPostureIdentifier(QThread):
    head_postures_signal = Signal(object)

    def __init__(self, main_window, human_keypoints_list):
        super().__init__()
        self.main_window = main_window
        self.human_keypoints = human_keypoints_list
        self.head_posture_results_list = []
        self._running = True

    def calculate_angle(self, p1, p2):
        dx, dy = p2[0] - p1[0], p2[1] - p1[1]
        return np.degrees(np.arctan2(dy, dx))

    def classify_head_posture(self, nose, eyes_mid, ears_mid, shoulders_mid):
        head_relative_angle = self.calculate_angle(eyes_mid, nose)  # yaw
        head_relative_tilt = self.calculate_angle(nose, ears_mid)   # tilt
        shoulder_tilt = self.calculate_angle(shoulders_mid, ears_mid)
        head_relative_tilt -= shoulder_tilt

        if nose[1] > shoulders_mid[1] + 20 and head_relative_tilt < -15:
            return "FACING DOWNWARDS"
        elif head_relative_angle > 90:
            return "FACING RIGHT"
        elif head_relative_angle < 80:
            return "FACING LEFT"
        
        return "FACING FORWARD"

    def run(self):
        total_frames = len(self.human_keypoints)
        head_posture_results_list = []

        for human_keypoint in self.human_keypoints:
            if self.isInterruptionRequested():
                return
            head_posture_dict = {}

            for track_id, keypoint_set in human_keypoint.items():
                
                # Skip if keypoint_set is missing or empty
                if not isinstance(keypoint_set, (list, np.ndarray)) or len(keypoint_set) == 0:
                    continue

                # Convert to NumPy array for easier processing
                keypoint_set = np.array(keypoint_set)

                # Ensure it has at least 7 keypoints, fill missing ones with zeros
                if keypoint_set.shape[0] < 7:
                    padding = np.zeros((7 - keypoint_set.shape[0], 2))
                    keypoint_set = np.vstack([keypoint_set, padding])

                # Check if all keypoints are zero or NaN (skip only in this case)
                if np.all((keypoint_set == 0) | np.isnan(keypoint_set)):
                    continue
                
                # Extract keypoints
                nose = keypoint_set[0]
                left_eye = keypoint_set[1]
                right_eye = keypoint_set[2]
                left_ear = keypoint_set[3]
                right_ear = keypoint_set[4]
                left_shoulder = keypoint_set[5]
                right_shoulder = keypoint_set[6]

                # Check which are valid
                nose_valid = not np.isnan(nose).any()
                left_eye_valid = not np.isnan(left_eye).any()
                right_eye_valid = not np.isnan(right_eye).any()
                left_ear_valid = not np.isnan(left_ear).any()
                right_ear_valid = not np.isnan(right_ear).any()
                left_shoulder_valid = not np.isnan(left_shoulder).any()
                right_shoulder_valid = not np.isnan(right_shoulder).any()

                # === CASE 1: Only left ear is present
                if left_ear_valid and not (right_ear_valid or nose_valid or left_eye_valid or right_eye_valid):
                    posture = "FACING RIGHT"
                    head_relative_angle = None
                    head_relative_tilt = None

                # === CASE 2: Only right ear is present
                elif right_ear_valid and not (left_ear_valid or nose_valid or left_eye_valid or right_eye_valid):
                    posture = "FACING LEFT"
                    head_relative_angle = None
                    head_relative_tilt = None

                # === CASE 3: Insufficient data for estimation
                elif not (nose_valid and left_eye_valid and right_eye_valid and left_shoulder_valid and right_shoulder_valid):
                    posture = "UNKNOWN"
                    head_relative_angle = None
                    head_relative_tilt = None

                # === CASE 4: Normal case or with estimation
                else:
                    # Estimate missing ears if needed
                    if not left_ear_valid and nose_valid and right_eye_valid:
                        left_ear = nose + (nose - right_eye)
                    if not right_ear_valid and nose_valid and left_eye_valid:
                        right_ear = nose + (nose - left_eye)

                    # Compute midpoints
                    eyes_mid = ((left_eye[0] + right_eye[0]) / 2, (left_eye[1] + right_eye[1]) / 2)
                    ears_mid = ((left_ear[0] + right_ear[0]) / 2, (left_ear[1] + right_ear[1]) / 2)
                    shoulders_mid = ((left_shoulder[0] + right_shoulder[0]) / 2, (left_shoulder[1] + right_shoulder[1]) / 2)

                    # Compute angles
                    head_relative_angle = round(self.calculate_angle(nose, shoulders_mid), 2)
                    head_relative_tilt = round(self.calculate_angle(ears_mid, shoulders_mid), 2)

                    # Classify
                    posture = self.classify_head_posture(nose, eyes_mid, ears_mid, shoulders_mid)

                head_posture_dict[track_id] = {
                    'head_posture': posture,
                    'head_relative_angle': head_relative_angle,
                    'head_relative_tilt': head_relative_tilt
                }

            head_posture_results_list.append(head_posture_dict)

        self.head_postures_signal.emit(head_posture_results_list)

    def stop(self):
        self.requestInterruption()
        self.wait()

class ArmPostureIdentifer(QThread):
    
    arm_postures_list_signal = Signal(object)
    
    def __init__(self, main_window, human_keypoints_list):
        super().__init__()
        self.main_window = main_window
        self.human_keypoints = human_keypoints_list
        self.arm_postures_list = []
        self._running = True

    def calculate_angle(self, a, b, c):
        if np.any(np.isnan(a)) or np.any(np.isnan(b)) or np.any(np.isnan(c)):
            return None
        ba = np.array(a) - np.array(b)
        bc = np.array(c) - np.array(b)
        norm_ba = np.linalg.norm(ba)
        norm_bc = np.linalg.norm(bc)
        if norm_ba == 0 or norm_bc == 0:
            return None
        cosine_angle = np.dot(ba, bc) / (norm_ba * norm_bc)
        angle = np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0)))
        return round(angle, 2)

    def calculate_relative_angle(self, joint, ref_a, ref_b):
        if np.any(np.isnan(joint)) or np.any(np.isnan(ref_a)) or np.any(np.isnan(ref_b)):
            return None
        baseline = np.array(ref_b) - np.array(ref_a)
        vector = np.array(joint) - np.array(ref_a)
        norm_baseline = np.linalg.norm(baseline)
        norm_vector = np.linalg.norm(vector)
        if norm_baseline == 0 or norm_vector == 0:
            return None
        cosine_angle = np.dot(baseline, vector) / (norm_baseline * norm_vector)
        angle = np.degrees(np.arccos(np.clip(cosine_angle, -1.0, 1.0)))
        if joint[1] > ref_a[1]:  # Elbow below shoulder line
            angle = 360 - angle
        return round(angle, 2)

    def classify_arm_posture(self, shoulder_angle, elbow_angle, wrist_missing=False):
        if wrist_missing:
            if shoulder_angle is not None and shoulder_angle > 90:
                return "RAISING ARM"
            return "UNKNOWN"
        
        if shoulder_angle is None or elbow_angle is None:
            return "UNKNOWN"
        
        if (85 <= shoulder_angle <= 150) and (60 <= elbow_angle <= 180):
            return "NEUTRAL (RESTING)"
        elif (150 <= shoulder_angle <= 180) and (140 <= elbow_angle <= 180):
            return "EXTENDING SIDEWARDS"
        elif (shoulder_angle < 40) and (elbow_angle > 140):
            return "NEUTRAL (RESTING)"
        elif (270 <= shoulder_angle <= 350) and (0 <= elbow_angle < 130):
            return "NEUTRAL (RESTING)"
        else:
            return "UNKNOWN"

    def run(self):
        arms_posture_results_list = []

        for human_keypoint in self.human_keypoints:
            if self.isInterruptionRequested():
                return
            
            arms_posture_dict = {}

            for track_id, keypoint_set in human_keypoint.items():
                keypoints = np.array(keypoint_set)
                
                    # Skip if it's empty
                if keypoints.size == 0:
                    continue

                # Pad to at least 11 keypoints if necessary
                if keypoints.shape[0] < 11:
                    padding = np.zeros((11 - keypoints.shape[0], 2))
                    keypoints = np.vstack([keypoints, padding])
                    
                shoulder_r, shoulder_l = keypoints[6], keypoints[5]
                elbow_r, elbow_l = keypoints[8], keypoints[7]
                wrist_r, wrist_l = keypoints[10], keypoints[9]

                # Right arm
                shoulder_angle_r = self.calculate_relative_angle(elbow_r, shoulder_r, shoulder_l)
                elbow_angle_r = self.calculate_angle(wrist_r, elbow_r, shoulder_r) if not np.any(np.isnan(wrist_r)) else None
                right_arm_posture = self.classify_arm_posture(shoulder_angle_r, elbow_angle_r, wrist_missing=np.any(np.isnan(wrist_r)))

                # Left arm
                shoulder_angle_l = self.calculate_relative_angle(elbow_l, shoulder_l, shoulder_r)
                elbow_angle_l = self.calculate_angle(wrist_l, elbow_l, shoulder_l) if not np.any(np.isnan(wrist_l)) else None
                left_arm_posture = self.classify_arm_posture(shoulder_angle_l, elbow_angle_l, wrist_missing=np.any(np.isnan(wrist_l)))

                arms_posture_dict[track_id] = {
                    "right_arm_posture": str("RIGHT ARM "+ right_arm_posture),
                    "left_arm_posture": str("LEFT ARM "+left_arm_posture),
                    "right_shoulder_angle": shoulder_angle_r,
                    "right_elbow_angle": elbow_angle_r,
                    "left_shoulder_angle": shoulder_angle_l,
                    "left_elbow_angle": elbow_angle_l
                }

            arms_posture_results_list.append(arms_posture_dict)

        self.arm_postures_list_signal.emit(arms_posture_results_list)
        
    def stop(self):
        self.requestInterruption()
        self.wait()