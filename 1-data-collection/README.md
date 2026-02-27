# Phase 1: Data Collection

## Mục đích
Giai đoạn này tập trung vào việc thu thập và chuẩn bị dữ liệu để huấn luyện mô hình nhận diện cử chỉ tay. Đây là bước đầu tiên và quan trọng nhất trong quy trình machine learning.

## Nhiệm vụ chính

### 1. Thu thập dữ liệu thô
- Sử dụng webcam để ghi lại các cử chỉ tay khác nhau
- Lưu trữ dữ liệu dạng ảnh hoặc video vào thư mục `../data/raw/`
- Đảm bảo đa dạng về điều kiện ánh sáng, góc nhìn, và đối tượng

### 2. Gán nhãn và chú thích dữ liệu
- Xác định các điểm mốc (landmarks) trên bàn tay
- Gán nhãn cho từng cử chỉ (gesture classes)
- Lưu trữ thông tin chú thích vào `../data/annotations/`

### 3. Kiểm tra chất lượng dữ liệu
- Xác minh tính đầy đủ của dataset
- Loại bỏ dữ liệu nhiễu hoặc không hợp lệ
- Đảm bảo cân bằng giữa các classes

## Cấu trúc dữ liệu

```
data/
├── raw/                    # Dữ liệu thô chưa xử lý
│   ├── gesture_1/         # Ảnh cho cử chỉ 1
│   ├── gesture_2/         # Ảnh cho cử chỉ 2
│   └── ...
├── annotations/           # File chú thích landmarks và labels
│   ├── gesture_1.json
│   ├── gesture_2.json
│   └── ...
└── processed/            # Dữ liệu đã được tiền xử lý
```

## Nguồn dữ liệu

### Thu thập tự động
- Sử dụng camera để ghi lại cử chỉ của người dùng
- Tự động chụp ảnh theo khoảng thời gian định trước
- Lưu trữ metadata (timestamp, điều kiện chụp)

### Dataset từ nguồn bên ngoài
- Sử dụng dataset công khai từ Kaggle hoặc các nguồn khác
- Tham khảo `../data/kaggle_data_link.md` để biết thêm chi tiết
- Đảm bảo tuân thủ license và điều khoản sử dụng

## Yêu cầu về dữ liệu

### Chất lượng
- Độ phân giải tối thiểu: 640x480 pixels
- Format: JPG, PNG hoặc video MP4
- Ánh sáng đầy đủ, bàn tay nằm trong khung hình
- Tránh nhiễu hoặc che khuất

### Số lượng
- Tối thiểu 500 mẫu cho mỗi cử chỉ
- Khuyến nghị 1000+ mẫu để đạt độ chính xác cao
- Đa dạng về người thực hiện và điều kiện

### Đa dạng
- Nhiều góc nhìn khác nhau (chính diện, nghiêng, từ trên xuống)
- Các điều kiện ánh sáng khác nhau (sáng mạnh, yếu, tự nhiên)
- Nhiều người khác nhau (kích thước tay, màu da khác nhau)
- Các background khác nhau

## Lưu ý quan trọng

- Đảm bảo tuân thủ quyền riêng tư khi thu thập dữ liệu
- Lưu trữ dữ liệu an toàn và có backup
- Document rõ ràng cách thức thu thập và tiêu chí
- Không commit dữ liệu lớn lên Git repository
