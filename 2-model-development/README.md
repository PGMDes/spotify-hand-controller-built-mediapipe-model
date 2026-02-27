# Phase 2: Model Development

## Mục đích
Giai đoạn này tập trung vào việc thiết kế, xây dựng và huấn luyện mô hình machine learning để nhận diện cử chỉ tay. Mô hình sẽ được phát triển tương tự như kiến trúc của MediaPipe.

## Thành phần chính

### 1. Kiến trúc mô hình
Mô hình bao gồm các thành phần sau:

#### Hand Detection Network
- Phát hiện vị trí bàn tay trong ảnh
- Xác định bounding box của bàn tay
- Backbone: MobileNet hoặc các CNN architecture tương tự

#### Hand Landmark Network
- Dự đoán 21 điểm mốc 3D trên bàn tay
- Input: Vùng ảnh chứa bàn tay đã được crop
- Output: Tọa độ (x, y, z) của 21 landmarks

#### Gesture Classification Network
- Phân loại cử chỉ dựa trên landmarks
- Input: Vector 63 chiều (21 landmarks × 3 coordinates)
- Output: Xác suất cho từng gesture class

### 2. Tiền xử lý dữ liệu
- Chuẩn hóa kích thước ảnh
- Data augmentation (rotation, flip, brightness, contrast)
- Tạo train/validation/test splits
- Normalization và feature scaling

### 3. Quá trình huấn luyện
- Thiết lập hyperparameters (learning rate, batch size, epochs)
- Training loop với checkpointing
- Validation sau mỗi epoch
- Early stopping để tránh overfitting
- Learning rate scheduling

### 4. Đánh giá mô hình
- Metrics: Accuracy, Precision, Recall, F1-Score
- Confusion matrix để phân tích lỗi
- Landmark position error (mean/median distance)
- Inference time và FPS
- ROC curves và AUC scores

## Cấu trúc thư mục

```
2-model-development/
├── train.py              # Script huấn luyện mô hình
├── evaluate.py           # Script đánh giá performance
├── utils.py             # Utility functions (loss, metrics, etc.)
└── README.md            # File này

models/
├── checkpoints/         # Lưu trữ checkpoints trong quá trình train
│   └── logs/           # TensorBoard logs
└── saved_models/       # Mô hình đã train xong
    └── best_model.h5   # Best model theo validation metric
```

## Quy trình phát triển

### Bước 1: Thiết kế kiến trúc
- Nghiên cứu các kiến trúc hiện có (MediaPipe, OpenPose)
- Xác định input/output dimensions
- Thiết kế network layers
- Tính toán số lượng parameters

### Bước 2: Tiền xử lý dữ liệu
- Load dữ liệu từ Phase 1
- Implement data pipeline
- Apply augmentation techniques
- Create DataLoader/Generator

### Bước 3: Training
- Initialize model với pretrained weights (transfer learning)
- Setup optimizer và loss functions
- Configure callbacks (checkpoint, early stopping)
- Monitor training metrics

### Bước 4: Evaluation
- Test trên test set
- Phân tích errors
- Visualize predictions
- Generate evaluation reports

### Bước 5: Optimization
- Model compression (pruning, quantization)
- Export sang các format (TensorFlow Lite, ONNX)
- Optimize cho inference speed
- Test trên target hardware

## Chỉ số performance mục tiêu

### Accuracy Targets
- Hand Detection: mAP > 0.95
- Landmark Prediction: Mean pixel error < 5px
- Gesture Classification: Accuracy > 95%

### Speed Targets
- Inference time: < 33ms (30 FPS)
- Model size: < 50MB
- RAM usage: < 200MB

### Robustness
- Hoạt động tốt trong nhiều điều kiện ánh sáng
- Ổn định với các góc nhìn khác nhau
- Xử lý được nhiều kích thước tay

## Tools và frameworks

### Deep Learning Frameworks
- TensorFlow / Keras
- PyTorch
- ONNX Runtime

### Visualization Tools
- TensorBoard cho training metrics
- Matplotlib/Seaborn cho plots
- Confusion matrix visualization

### Experiment Tracking
- Weights & Biases
- MLflow
- TensorBoard

## Best practices

### Training
- Sử dụng version control cho code và configs
- Log tất cả hyperparameters
- Save checkpoints regularly
- Monitor overfitting

### Evaluation
- Sử dụng nhiều metrics khác nhau
- Test trên diverse test set
- Phân tích failure cases
- Compare với baseline models

### Documentation
- Document kiến trúc model rõ ràng
- Ghi chú các quyết định thiết kế
- Version models theo semantic versioning
- Lưu training logs và results

## Lưu ý quan trọng

- Không commit model files (*.h5, *.pt) lên Git
- Sử dụng GPU để training nhanh hơn
- Backup checkpoints thường xuyên
- Test model trên real-world data trước khi deploy
