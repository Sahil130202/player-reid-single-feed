# Player Re-Identification in a Single Feed

## Project Overview

This project is developed as part of the Liat.ai AI Intern assignment. The goal is to track and re-identify soccer players in a short video captured from a single camera feed. The system should consistently assign and maintain player identities throughout the video, even if a player temporarily leaves the frame.

## Objective

* Detect soccer players in a 15-second video clip using a YOLOv11 model.
* Assign unique IDs to each player.
* Ensure IDs remain consistent as players move, interact, and re-enter the frame.
* Output a video annotated with bounding boxes and player IDs.

## Input

* Video file: `15sec_input_720p.mp4`
* Pre-trained YOLOv11 model: `yolov11.pt`

## Output

* Annotated video with bounding boxes and consistent player IDs: `reid_output.mp4`

## Folder Structure

```
player_reid_single_feed/
├── run.py
├── config/
│   └── config.yaml
├── detection/
│   └── detector.py
├── tracking/
│   └── tracker.py
├── utils/
│   ├── visualizer.py
│   └── helpers.py
├── data/
│   └── 15sec_input_720p.mp4
├── models/
│   └── yolov11.pt
├── outputs/
│   └── reid_output.mp4
├── report/
│   └── player_reid_report.md
├── requirements.txt
└── README.md
```

## Components

### 1. `run.py`

Main script to load video, run detection and tracking, and save the annotated output.

### 2. `config/config.yaml`

Stores configurable parameters such as paths, detection thresholds, and frame stride.

### 3. `detection/detector.py`

Wraps the YOLOv11 model using the `ultralytics` library to perform object detection on each frame.

### 4. `tracking/tracker.py`

Implements a basic centroid-based tracking algorithm that assigns and maintains player IDs based on spatial proximity.

### 5. `utils/visualizer.py`

Draws bounding boxes and player IDs on each frame using OpenCV.

### 6. `requirements.txt`

Specifies required Python packages.

### 7. `README.md`

Instructions for setting up, running, and understanding the project.

### 8. `report/player_reid_report.md`

Technical report explaining the methodology, challenges, and outcomes.

## Methodology

1. Load and preprocess the input video.
2. Detect players in each frame using YOLOv11.
3. Track players across frames using a centroid-matching logic with missed frame tolerance.
4. Annotate each frame with bounding boxes and assigned player IDs.
5. Write the annotated frames into an output video.

## Evaluation

* Manual inspection of the video showed that:

  * Multiple players are detected and assigned distinct IDs.
  * IDs remain consistent even when players move or interact.
  * Players retain their IDs upon temporary disappearance and re-entry.

## Tools & Technologies

* Python 3.11
* PyTorch
* Ultralytics YOLO
* OpenCV
* SciPy, NumPy, YAML

## Future Improvements

* Integrate Deep SORT for better long-term tracking and occlusion handling.
* Use appearance-based features for re-identification.
* Support multi-camera input and fusion.

## Authors

Sahil Nayak
M.Tech in Artificial Intelligence
GitHub: \[YourGitHub]
LinkedIn: \[YourLinkedIn]

---

This documentation is designed to help reviewers at Liat.ai and any future collaborators understand the structure, functionality, and motivation behind the player re-identification system.
