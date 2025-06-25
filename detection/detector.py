# detection/detector.py

from ultralytics import YOLO

class PlayerDetector:
    def __init__(self, model_path, conf_thresh=0.4):
        self.model = YOLO(model_path)  # loads YOLOv8/v5/YOLOv11-style .pt model
        self.conf_thresh = conf_thresh

    def detect(self, frame):
        # Run prediction
        results = self.model.predict(source=frame, save=False, verbose=False)[0]

        player_boxes = []
        for box in results.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cls = int(box.cls[0])

            # Optional: class filtering (assumes class 0 is 'player')
            if conf >= self.conf_thresh and cls == 0:
                player_boxes.append([x1, y1, x2, y2, conf])

        return player_boxes
