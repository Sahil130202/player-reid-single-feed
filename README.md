# Player Re-Identification in a Single Feed

## Overview

This project was developed as part of the **Liat.ai AI Intern assignment**. The primary objective is to consistently identify and track soccer players within a 15-second single-camera video clip using object detection and tracking.

## Objective

- Detect soccer players using a pretrained YOLOv11 model.
- Assign consistent and unique IDs to each player.
- Ensure identity preservation even after temporary disappearance.
- Output an annotated video showing bounding boxes and player IDs.

---

## Requirements

### 1. System Dependencies
- Python ≥ 3.10
- Git
- Git LFS (Large File Storage)
- pip (Python package manager)

### 2. Python Dependencies

Install them using:

```bash
pip install -r requirements.txt
```

---

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
│   └── yolov11.pt           # (Excluded in GitHub, managed via Git LFS or provided externally)
├── outputs/
│   └── reid_output.mp4
├── report/
│   └── player_reid_report.md
├── requirements.txt
└── README.md
```

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/Sahil130202/player-reid-single-feed.git
cd player_reid_single_feed
```

### 2. Setup Environment

```bash
python -m venv venv
source venv/bin/activate        # or use venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Add YOLOv11 Model

Place the YOLOv11 model (`yolov11.pt`) in the `models/` directory.  
 This file is excluded from GitHub due to its size (>100MB). Use Git LFS or request access.
https://drive.google.com/file/d/1-5fOSHOSB9UXyP_enOoZNAMScrePVcMD/view
Use this link to download the yolo11.pt file and place it in models/ folder before running

### 4. Run the System

```bash
python run.py
```

The output will be saved in `outputs/reid_output.mp4`.

---

## Key Components

- `detector.py`: Loads YOLOv11 using `torch.hub` and performs player detection.
- `tracker.py`: Tracks players using centroid logic and ID reassignment strategy.
- `visualizer.py`: Draws bounding boxes and player IDs on the video frames.
- `run.py`: Main entry point that ties everything together.
- `config.yaml`: Central location for all paths and thresholds.

---

## Technical Challenges & Solutions

###  GitHub Large File Limit
-  Error: GitHub refused to push `yolov11.pt` due to its 186MB size.
-  Solution: Installed and used [Git LFS](https://git-lfs.github.com/) to handle large file uploads.

###  Player Re-ID Logic Bug
-  Problem: IDs were reassigning when players touched the ball.
-  Solution: Changed to **spatial consistency** tracking using bounding box centroids.


###  Output Debugging
- ✔️ Manually reviewed the 15s video to ensure consistent ID annotation.

---

## Limitations

- Currently uses centroid tracking without re-identification embeddings.
- Accuracy may degrade with occlusion or player overlap.
- Only tested on a 15s single-feed soccer video.

---

## Future Improvements

- Integrate **Deep SORT** or **ByteTrack** for better ID preservation.
- Add appearance descriptors (color histograms, embeddings).
- Generalize to other sports and multi-camera inputs.

---

## Submission Checklist

 Output video `reid_output.mp4`  
 GitHub Repo: [player-reid-single-feed](https://github.com/Sahil130202/player-reid-single-feed)  
 Report `player_reid_report.md`  
 README with full instructions  
 Clean project structure with modular code  
 Large model file excluded via Git LFS

---

## Author

**Sahil Nayak**  
M.Tech in Artificial Intelligence  
GitHub: [Sahil130202](https://github.com/Sahil130202)

---

This documentation is intended to serve both reviewers and collaborators with full clarity and technical transparency.
