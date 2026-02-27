# Tài Liệu Dự Án / Project Documentation

## Mục Lục / Table of Contents

1. [Architecture / Kiến Trúc](#architecture)
2. [API Documentation / Tài Liệu API](#api-documentation)
3. [Training Guide / Hướng Dẫn Training](#training-guide)
4. [Deployment / Triển Khai](#deployment)
5. [Troubleshooting / Xử Lý Sự Cố](#troubleshooting)

---

## Architecture

### System Overview / Tổng Quan Hệ Thống

```
┌─────────────────┐
│   Camera Input  │
│   (Webcam)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  MediaPipe      │
│  Hand Detection │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Gesture        │
│  Recognition    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Gesture to     │
│  Action Mapping │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Spotify API    │
│  Controller     │
└─────────────────┘
```

### Components / Các Thành Phần

#### 1. Hand Detector (`src/hand_detector.py`)
- Sử dụng MediaPipe để phát hiện và tracking tay
- Extract landmarks của bàn tay
- Tính toán các features từ landmarks

#### 2. Gesture Mapping (`src/gesture_mapping.py`)
- Map gestures thành actions
- Quản lý gesture configurations
- Xử lý gesture events

#### 3. Spotify Controller (`src/spotify_controller.py`)
- Tích hợp với Spotify API
- Thực hiện các actions (play, pause, next, previous, volume)
- Xử lý authentication

---

## API Documentation

### HandDetector Class

```python
class HandDetector:
    def __init__(self, min_detection_confidence=0.7, min_tracking_confidence=0.5):
        """
        Initialize hand detector.
        
        Args:
            min_detection_confidence: Minimum confidence for initial detection
            min_tracking_confidence: Minimum confidence for tracking
        """
        
    def detect(self, frame):
        """
        Detect hands in frame.
        
        Args:
            frame: numpy array, input image (BGR format)
            
        Returns:
            dict: {
                'detected': bool,
                'landmarks': list of hand landmarks,
                'handedness': 'Left' or 'Right',
                'gesture': detected gesture name
            }
        """
```

### SpotifyController Class

```python
class SpotifyController:
    def __init__(self, client_id, client_secret, redirect_uri):
        """
        Initialize Spotify controller.
        
        Args:
            client_id: Spotify API client ID
            client_secret: Spotify API client secret
            redirect_uri: OAuth redirect URI
        """
        
    def play(self):
        """Start playback."""
        
    def pause(self):
        """Pause playback."""
        
    def next_track(self):
        """Skip to next track."""
        
    def previous_track(self):
        """Go to previous track."""
        
    def set_volume(self, volume_percent):
        """
        Set playback volume.
        
        Args:
            volume_percent: int (0-100)
        """
```

---

## Training Guide

### Data Collection / Thu Thập Dữ Liệu

1. **Capture gestures:**
   ```bash
   python scripts/collect_data.py --gesture thumbs_up --samples 1000
   ```

2. **Organize data:**
   ```
   data/raw/
   ├── thumbs_up/
   ├── thumbs_down/
   ├── swipe_left/
   ├── swipe_right/
   └── ...
   ```

### Training / Huấn Luyện

```bash
# Train model
python training/train.py --epochs 100 --batch_size 32

# Evaluate model
python training/evaluate.py --model_path models/saved_models/latest.h5
```

### Model Architecture / Kiến Trúc Model

```python
# Example custom model structure
Input (21 landmarks x 3 coordinates = 63 features)
    ↓
Dense(128, activation='relu')
    ↓
Dropout(0.3)
    ↓
Dense(64, activation='relu')
    ↓
Dropout(0.3)
    ↓
Dense(num_classes, activation='softmax')
```

---

## Deployment

### Local Deployment

```bash
# Run application
python src/main.py
```

### Docker Deployment (Future)

```dockerfile
# Dockerfile example
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "src/main.py"]
```

---

## Troubleshooting

### Common Issues / Các Vấn Đề Thường Gặp

#### 1. Camera không hoạt động / Camera not working

```python
# Try different camera IDs
camera_id = 0  # Try 0, 1, 2, etc.
```

#### 2. Spotify authentication fails

- Kiểm tra credentials trong `config/config.py`
- Đảm bảo redirect URI khớp với Spotify Dashboard
- Kiểm tra internet connection

#### 3. Low detection accuracy

- Cải thiện lighting conditions
- Điều chỉnh `min_detection_confidence`
- Train custom model với data của bạn

#### 4. High latency

- Giảm frame resolution
- Tăng `min_tracking_confidence`
- Sử dụng GPU nếu có

### Performance Tuning / Tối Ưu Hiệu Suất

```python
# Example configuration for better performance
config = {
    'frame_width': 640,  # Lower resolution = faster
    'frame_height': 480,
    'min_detection_confidence': 0.7,
    'min_tracking_confidence': 0.6,
    'max_num_hands': 1  # Detect only 1 hand
}
```

---

## Additional Resources / Tài Nguyên Bổ Sung

- [MediaPipe Documentation](https://mediapipe.dev/)
- [Spotipy Documentation](https://spotipy.readthedocs.io/)
- [OpenCV Documentation](https://docs.opencv.org/)

---

## FAQ

**Q: Tôi có cần Spotify Premium không? / Do I need Spotify Premium?**
A: Có, cần Premium để sử dụng playback control API / Yes, Premium is required for playback control API.

**Q: Gestures nào được hỗ trợ? / What gestures are supported?**
A: Xem file `src/gesture_mapping.py` hoặc README chính / See `src/gesture_mapping.py` or main README.

**Q: Làm sao thêm gestures mới? / How to add new gestures?**
A: 
1. Thu thập training data cho gesture
2. Train model hoặc thêm rule-based detection
3. Update `gesture_mapping.py`
4. Test và submit PR

**Q: Dự án này có hoạt động trên Raspberry Pi không? / Does this work on Raspberry Pi?**
A: Có thể, nhưng có thể cần tối ưu performance / Possible, but may need performance optimization.
