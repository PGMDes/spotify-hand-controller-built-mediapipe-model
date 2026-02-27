# Data Collection Phase

## Overview
This phase involves collecting hand gesture data to train our custom hand detection model (similar to MediaPipe).

## Steps

### 1. Setup Data Collection Environment
Ensure you have the required dependencies installed:
```bash
pip install opencv-python mediapipe numpy
```

### 2. Collect Raw Data
Run the data collection script to capture hand gestures:
```bash
python collect_data.py
```

This script will:
- Open your webcam
- Allow you to record different hand gestures
- Save images/videos to `../data/raw/`

### 3. Annotate Data
After collecting raw data, annotate the hand landmarks:
```bash
python annotate_data.py
```

This will:
- Load raw images/videos
- Extract hand landmarks
- Save annotations to `../data/annotations/`

### 4. Validate Dataset
Check the collected dataset quality:
```bash
python validate_dataset.py
```

## Dataset Format
- **Raw data**: Images or videos in `../data/raw/`
- **Annotations**: JSON files with hand landmark coordinates in `../data/annotations/`
- **Processed**: Cleaned and augmented data in `../data/processed/`

## External Datasets
You can also use external datasets from Kaggle. See `../data/kaggle_data_link.md` for more information.

## Tips
- Collect data with various lighting conditions
- Include different hand sizes and skin tones
- Record gestures from multiple angles
- Aim for at least 1000+ images per gesture class
