# Hand Gesture Recognition Model

A complete machine learning pipeline for building a custom hand detection and gesture recognition model (similar to MediaPipe) and applying it to control Spotify playback.

## 🎯 Project Goals

This project demonstrates the full ML workflow:
1. **Data Collection**: Gather hand gesture data from webcam
2. **Model Development**: Build and train a custom hand detection model
3. **Model Training**: Train the model on collected data
4. **Application**: Deploy the model in a real-world application (Spotify controller)

## 📁 Project Structure

```
hand-gesture-model/
│
├── 1-data-collection/         # Phase 1: Data Collection
│   ├── collect_data.py       # Collect hand gesture images
│   ├── annotate_data.py      # Annotate data with landmarks
│   └── README.md             # Data collection guide
│
├── data/                      # Dataset storage
│   ├── raw/                  # Raw collected images
│   ├── processed/            # Preprocessed data ready for training
│   ├── annotations/          # Annotated landmark data
│   └── kaggle_data_link.md   # External dataset links
│
├── 2-model-development/       # Phase 2: Model Building & Training
│   ├── model_architecture.py # Neural network architecture
│   ├── train.py              # Model training script
│   ├── evaluate.py           # Model evaluation script
│   ├── data_preprocessing.py # Data preprocessing utilities
│   └── README.md             # Model development guide
│
├── models/                    # Trained models
│   ├── saved_models/         # Final trained models
│   └── checkpoints/          # Training checkpoints
│
├── 3-application/             # Phase 3: Real-world Application
│   ├── main.py               # Main application entry point
│   ├── hand_detector.py      # Hand detection using trained model
│   ├── spotify_controller.py # Spotify API integration
│   ├── gesture_mapping.py    # Gesture to action mapping
│   ├── utils.py              # Application utilities
│   └── README.md             # Application usage guide
│
├── notebooks/                 # Jupyter notebooks for experimentation
│
├── tests/                     # Unit tests
│   ├── test_hand_detector.py
│   └── test_spotify_controller.py
│
├── config/                    # Configuration files
│   ├── config.py             # Main configuration
│   └── config.example.py     # Example configuration
│
├── assets/                    # Images, icons, and other assets
│
├── docs/                      # Additional documentation
│
├── requirements.txt           # Python dependencies
└── README.md                 # This file
```

## 🚀 Quick Start

### Phase 1: Data Collection
```bash
cd 1-data-collection
python collect_data.py      # Collect hand gesture images
python annotate_data.py     # Annotate with landmarks
```

### Phase 2: Model Development
```bash
cd 2-model-development
python data_preprocessing.py   # Preprocess data
python train.py               # Train the model
python evaluate.py            # Evaluate performance
```

### Phase 3: Application
```bash
cd 3-application
python main.py               # Run Spotify controller
```

See individual README files in each phase directory for detailed instructions.

## 📋 Prerequisites

- Python 3.8+
- Webcam for data collection and real-time detection
- Spotify Premium account (for Phase 3 application)
- GPU recommended for faster training (optional)

## 🔧 Installation

1. **Clone the repository**
```bash
git clone <repository-url>
cd spotify-hand-controller-built-mediapipe-model
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure Spotify API** (for Phase 3)
```bash
cp config/config.example.py config/config.py
# Edit config/config.py with your Spotify API credentials
```

Get Spotify API credentials:
- Go to [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
- Create a new app
- Copy Client ID and Client Secret to config.py

## 📚 Complete Workflow

### Phase 1: Data Collection
Collect your own hand gesture dataset:

```bash
cd 1-data-collection

# Step 1: Collect images
python collect_data.py
# Follow on-screen instructions to record gestures

# Step 2: Annotate landmarks
python annotate_data.py
# Extracts hand landmarks using MediaPipe
```

**Output**: Annotated data in `data/annotations/`

### Phase 2: Model Development & Training
Build and train your custom model:

```bash
cd 2-model-development

# Step 1: Preprocess data
python data_preprocessing.py
# Creates train/val/test splits with augmentation

# Step 2: Train model
python train.py --epochs 100 --batch-size 32

# Step 3: Evaluate model
python evaluate.py --model-path ../models/saved_models/best_model.h5
```

**Output**: Trained model in `models/saved_models/`

### Phase 3: Application (Spotify Controller)
Use your trained model to control Spotify:

```bash
cd 3-application

# Run the application
python main.py --model-path ../models/saved_models/best_model.h5
```

**Default Gesture Mappings**:
- 🖐️ **Open Palm**: Play/Pause
- ✊ **Fist**: Stop
- 👍 **Thumbs Up**: Volume Up
- ✌️ **Peace Sign**: Next Track
- 👈 **Pointing**: Previous Track
- ← **Swipe Left**: Seek Backward
- → **Swipe Right**: Seek Forward

Customize mappings in [3-application/gesture_mapping.py](3-application/gesture_mapping.py)

## 🎓 Learning Path

This project is designed to teach the complete ML pipeline:

1. **Data Engineering**: Learn data collection, annotation, and preprocessing
2. **Model Architecture**: Understand CNN architectures for computer vision
3. **Training Pipeline**: Implement training loops, checkpointing, and evaluation
4. **Model Deployment**: Deploy ML models in real-time applications
5. **API Integration**: Integrate with external APIs (Spotify)

## 🧪 Testing

Run tests to verify components:

```bash
# Test all components
pytest tests/

# Test specific component
pytest tests/test_hand_detector.py
pytest tests/test_spotify_controller.py
```

## 📊 Model Architecture

Our custom model is inspired by MediaPipe and consists of:

1. **Hand Detection Network**: Locates hands in images using MobileNetV2 backbone
2. **Landmark Prediction Network**: Predicts 21 3D hand landmarks
3. **Gesture Classification Network**: Classifies gestures from landmarks

See [2-model-development/model_architecture.py](2-model-development/model_architecture.py) for details.

## 🎯 Performance Targets

- **Hand Detection**: mAP > 0.95
- **Landmark Accuracy**: Mean error < 5 pixels
- **Gesture Classification**: Accuracy > 95%
- **Inference Speed**: > 30 FPS on CPU

## 📖 Documentation

Detailed documentation for each phase:
- [Phase 1: Data Collection Guide](1-data-collection/README.md)
- [Phase 2: Model Development Guide](2-model-development/README.md)
- [Phase 3: Application Guide](3-application/README.md)

## 🤝 Use Cases

Beyond Spotify control, this model can be applied to:
- Gesture-based presentation control
- Sign language recognition
- Gaming control
- Smart home device control
- Accessibility applications

## Contributing

Chúng tôi hoan nghênh mọi đóng góp! / We welcome all contributions!

### Bắt Đầu Nhanh / Quick Start

1. **Fork** repository này
2. **Clone** về máy của bạn
3. Tạo **virtual environment** và cài đặt dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   pip install -r requirements.txt
   ```
4. Copy `config/config.example.py` sang `config/config.py` và cấu hình Spotify API
5. Tạo **branch mới** cho feature của bạn
6. Thực hiện thay đổi và **commit**
7. **Push** lên fork của bạn
8. Tạo **Pull Request**

### Hướng Dẫn Chi Tiết / Detailed Guide

Đọc hướng dẫn đầy đủ tại [CONTRIBUTING.md](CONTRIBUTING.md) để biết:
- Quy trình phát triển chi tiết
- Code style guidelines
- Cách viết tests
- Quy ước commit messages
- Cách đồng bộ với repository gốc

### Ý Tưởng Đóng Góp / Contribution Ideas

- 🎯 Thêm gestures mới
- 🐛 Sửa bugs trong Issues
- 📖 Cải thiện documentation
- ✅ Viết thêm tests
- ⚡ Cải thiện performance

## License

MIT License

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/) for hand detection
- [Spotipy](https://spotipy.readthedocs.io/) for Spotify API integration
