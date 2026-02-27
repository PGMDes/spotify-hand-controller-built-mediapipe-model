# Hand Gesture Recognition Model

Một pipeline machine learning hoàn chỉnh để xây dựng mô hình nhận diện cử chỉ tay tùy chỉnh (tương tự MediaPipe) và ứng dụng để điều khiển Spotify.

A complete machine learning pipeline for building a custom hand detection and gesture recognition model (similar to MediaPipe) and applying it to control Spotify playback.

## Mục tiêu dự án

Dự án này minh họa quy trình ML workflow đầy đủ từ A đến Z:

1. **Phase 1 - Data Collection**: Thu thập dữ liệu cử chỉ tay
2. **Phase 2 - Model Development**: Xây dựng và huấn luyện mô hình
3. **Phase 3 - Application**: Triển khai mô hình vào ứng dụng thực tế

## Cấu trúc dự án

## Cấu trúc dự án

```
spotify-hand-controller-built-mediapipe-model/
│
├── 1-data-collection/         # Phase 1: Thu thập dữ liệu
│   └── README.md             # Hướng dẫn thu thập và annotation
│
├── data/                      # Lưu trữ dataset
│   ├── raw/                  # Dữ liệu thô chưa xử lý
│   ├── processed/            # Dữ liệu đã tiền xử lý
│   ├── annotations/          # File chú thích landmarks
│   └── kaggle_data_link.md   # Links tới external datasets
│
├── 2-model-development/       # Phase 2: Phát triển mô hình
│   ├── train.py              # Script huấn luyện
│   ├── evaluate.py           # Script đánh giá
│   ├── utils.py              # Utility functions
│   └── README.md             # Hướng dẫn training
│
├── models/                    # Lưu trữ models
│   ├── saved_models/         # Models đã train xong
│   └── checkpoints/          # Training checkpoints
│
├── 3-application/             # Phase 3: Ứng dụng thực tế
│   ├── main.py               # Entry point
│   ├── hand_detector.py      # Hand detection module
│   ├── spotify_controller.py # Spotify API integration
│   ├── gesture_mapping.py    # Gesture mapping logic
│   ├── utils.py              # Helper functions
│   └── README.md             # Hướng dẫn sử dụng
│
├── notebooks/                 # Jupyter notebooks cho research
│
├── tests/                     # Unit và integration tests
│   ├── test_hand_detector.py
│   └── test_spotify_controller.py
│
├── config/                    # Configuration files
│   ├── config.py             # Main config (không commit)
│   └── config.example.py     # Template config
│
├── assets/                    # Images, diagrams, media files
│
├── docs/                      # Documentation bổ sung
│   └── README.md
│
├── .github/                   # GitHub templates
│   ├── ISSUE_TEMPLATE/
│   └── PULL_REQUEST_TEMPLATE.md
│
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
├── README.md                 # File này
├── CODE_OF_CONDUCT.md        # Quy tắc ứng xử
├── CONTRIBUTING.md           # Hướng dẫn đóng góp
└── QUICKSTART.md             # Quick start guide
```

## Quy trình làm việc

### Phase 1: Thu thập dữ liệu
```bash
cd 1-data-collection
# Đọc README.md để hiểu cách thu thập và annotation dữ liệu
# Implement các scripts theo nhu cầu của bạn
```

**Mục tiêu**: Thu thập dataset cho các cử chỉ tay khác nhau

**Output**: Dữ liệu raw và annotations trong thư mục `data/`

### Phase 2: Phát triển mô hình
```bash
cd 2-model-development
# Đọc README.md để hiểu kiến trúc mô hình
# Implement training pipeline
python train.py               # Khi đã implement
python evaluate.py            # Đánh giá model
```

**Mục tiêu**: Xây dựng và train model nhận diện cử chỉ tay

**Output**: Trained model trong `models/saved_models/`

### Phase 3: Ứng dụng
```bash
cd 3-application
# Đọc README.md để hiểu cách tích hợp
# Setup Spotify API credentials
python main.py               # Khi đã implement
```

**Mục tiêu**: Sử dụng model để điều khiển Spotify

**Output**: Ứng dụng real-time gesture control

## Yêu cầu hệ thống

### Phần cứng
- Webcam (tích hợp hoặc external)
- CPU: Intel i5/AMD Ryzen 5 trở lên
- RAM: 8GB minimum, 16GB khuyến nghị
- GPU: Khuyến nghị có NVIDIA GPU cho training (không bắt buộc)

### Phần mềm
- Python 3.8 hoặc cao hơn
- pip hoặc conda
- Git
- Spotify Premium account (cho Phase 3)

## Cài đặt

### 1. Clone repository
```bash
git clone https://github.com/YOUR_USERNAME/spotify-hand-controller-built-mediapipe-model.git
cd spotify-hand-controller-built-mediapipe-model
```

### 2. Tạo virtual environment
```bash
python -m venv venv

# Kích hoạt environment
# Trên macOS/Linux:
source venv/bin/activate
# Trên Windows:
venv\Scripts\activate
```

### 3. Cài đặt dependencies
```bash
pip install -r requirements.txt
```

### 4. Cấu hình (cho Phase 3)
```bash
cp config/config.example.py config/config.py
# Chỉnh sửa config.py với Spotify API credentials
```

## Spotify API Setup

Để sử dụng Phase 3, bạn cần Spotify API credentials:

1. Truy cập [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)
2. Tạo ứng dụng mới
3. Lấy Client ID và Client Secret
4. Thêm redirect URI: `http://localhost:8888/callback`
5. Cập nhật thông tin trong `config/config.py`

## Gesture Mappings

Các cử chỉ mặc định và actions tương ứng:

| Cử chỉ | Hành động Spotify |
|--------|-------------------|
| Open Palm | Play/Pause |
| Fist | Stop |
| Thumbs Up | Tăng volume |
| Peace Sign | Next track |
| Pointing | Previous track |
| Swipe Left | Tua lùi |
| Swipe Right | Tua tới |

*Có thể tùy chỉnh trong Phase 3*

## Kiến trúc mô hình

Mô hình bao gồm 3 components chính:

### 1. Hand Detection Network
- Detect vị trí bàn tay trong frame
- Output: Bounding box coordinates

### 2. Hand Landmark Network
- Predict 21 điểm mốc 3D trên bàn tay
- Output: (x, y, z) coordinates cho mỗi landmark

### 3. Gesture Classification Network
- Phân loại cử chỉ từ landmarks
- Output: Gesture class và confidence score

## Performance Targets

### Accuracy
- Hand Detection: mAP > 0.95
- Landmark Prediction: Mean error < 5 pixels
- Gesture Classification: Accuracy > 95%

### Speed
- Inference time: < 33ms (>30 FPS)
- Model size: < 50MB
- Latency: < 100ms end-to-end

## Documentation

Mỗi phase có documentation chi tiết:

- [Phase 1: Data Collection Guide](1-data-collection/README.md)
- [Phase 2: Model Development Guide](2-model-development/README.md)
- [Phase 3: Application Guide](3-application/README.md)
- [Contributing Guide](CONTRIBUTING.md)

## Testing

Chạy tests để verify implementation:

```bash
# Chạy tất cả tests
pytest tests/

# Chạy specific test file
pytest tests/test_hand_detector.py
pytest tests/test_spotify_controller.py

# Chạy với coverage report
pytest --cov=. tests/
```

## Use Cases

Ngoài Spotify control, mô hình này có thể ứng dụng cho:

- Điều khiển presentations
- Sign language recognition
- Gaming controls
- Smart home device control
- Accessibility applications
- Virtual reality interactions
- Interactive art installations

## Roadmap

### Version 1.0 (Current)
- [x] Project structure initialization
- [x] Documentation framework
- [ ] Data collection implementation
- [ ] Model architecture implementation
- [ ] Training pipeline
- [ ] Spotify integration

### Version 2.0 (Future)
- [ ] Support multiple gesture sets
- [ ] Multi-hand detection
- [ ] Integration with other music services
- [ ] Mobile application
- [ ] Cloud deployment options
- [ ] Pre-trained models

## Contributing

Chúng tôi hoan nghênh mọi đóng góp từ cộng đồng!

### Getting Started

1. Fork repository này trên GitHub
2. Clone về máy local
3. Tạo branch mới cho feature/fix của bạn
4. Commit changes với clear messages
5. Push lên fork của bạn
6. Tạo Pull Request

### Guidelines

- Đọc [CONTRIBUTING.md](CONTRIBUTING.md) để biết quy trình chi tiết
- Tuân thủ [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)

### Areas to Contribute

- Implement data collection scripts
- Develop model architecture
- Add unit tests
- Improve documentation
- Report bugs
- Suggest features

## License

MIT License - Xem file LICENSE để biết chi tiết

## Acknowledgments

- Inspired by MediaPipe hand tracking
- Spotify Web API
- Open source computer vision community

## Contact và Support

- Issues: [GitHub Issues](https://github.com/YOUR_USERNAME/spotify-hand-controller-built-mediapipe-model/issues)
- Discussions: [GitHub Discussions](https://github.com/YOUR_USERNAME/spotify-hand-controller-built-mediapipe-model/discussions)
- Documentation: [docs/](docs/)

## Project Status

**Status**: In Development

Dự án đang trong giai đoạn phát triển. Cấu trúc và documentation đã được setup. Implementation code sẽ được bổ sung trong các phase tiếp theo.

---

**Lưu ý**: Đây là project framework. Code implementation sẽ được phát triển theo từng phase dựa trên nhu cầu nghiên cứu và phát triển cụ thể.
