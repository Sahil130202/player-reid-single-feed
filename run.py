import cv2
import yaml
from detection.detector import PlayerDetector
from tracking.tracker import PlayerTracker
from utils.visualizer import draw_boxes

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

video_path = config["video_path"]
output_path = config["output_video_path"]
frame_stride = config["frame_stride"]

# Initialize detection and tracking
detector = PlayerDetector(config["model_path"], config["detection_conf_thresh"])
tracker = PlayerTracker()

# Open video
cap = cv2.VideoCapture(video_path)
fps = cap.get(cv2.CAP_PROP_FPS)
w, h = int(cap.get(3)), int(cap.get(4))
out = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (w, h))

frame_id = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    if frame_id % frame_stride == 0:
        boxes = detector.detect(frame)
        tracked_players = tracker.update(boxes, frame)
        vis_frame = draw_boxes(frame.copy(), tracked_players)
        out.write(vis_frame)

    frame_id += 1

cap.release()
out.release()
print(f"✅ Output saved to {output_path}")
