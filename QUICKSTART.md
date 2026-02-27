# Hướng Dẫn Nhanh Cho Contributors

## 🚀 Bắt Đầu Trong 5 Phút

### Bước 1: Fork và Clone
```bash
# Fork repo trên GitHub, sau đó:
git clone https://github.com/YOUR_USERNAME/spotify-hand-controller-built-mediapipe-model.git
cd spotify-hand-controller-built-mediapipe-model
```

### Bước 2: Thiết Lập Môi Trường
```bash
# Tạo và kích hoạt virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# hoặc: venv\Scripts\activate  # Windows

# Cài đặt dependencies
pip install -r requirements.txt
```

### Bước 3: Cấu Hình
```bash
# Copy file config mẫu
cp config/config.example.py config/config.py

# Chỉnh sửa config/config.py với Spotify credentials của bạn
# Lấy credentials tại: https://developer.spotify.com/dashboard
```

### Bước 4: Thiết Lập Git
```bash
# Thêm upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/spotify-hand-controller-built-mediapipe-model.git
```

### Bước 5: Test
```bash
# Chạy tests để đảm bảo mọi thứ hoạt động
pytest tests/
```

## 💻 Quy Trình Làm Việc Hàng Ngày

### Trước Khi Bắt Đầu Làm Việc
```bash
# Đồng bộ code mới nhất
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

### Khi Làm Việc
```bash
# Tạo nhánh mới
git checkout -b feature/ten-tinh-nang

# Làm việc, sau đó commit
git add .
git commit -m "feat: mô tả ngắn gọn"

# Push lên fork của bạn
git push origin feature/ten-tinh-nang
```

### Sau Khi Hoàn Thành
1. Truy cập GitHub
2. Tạo Pull Request từ nhánh của bạn
3. Chờ review và phản hồi feedback nếu có

## 📋 Checklist PR

Trước khi submit Pull Request, đảm bảo:

- [ ] Code chạy được không lỗi
- [ ] Tất cả tests đều pass
- [ ] Đã thêm tests cho code mới
- [ ] Commit messages rõ ràng
- [ ] Đã đồng bộ với main mới nhất

## 🎯 Ý Tưởng Cho Người Mới Bắt Đầu

- Sửa typos trong documentation
- Thêm comments cho code
- Viết thêm tests
- Tìm issues được tag `good first issue`
- Cải thiện error messages

## 📚 Tài Liệu Đầy Đủ

Đọc [CONTRIBUTING.md](CONTRIBUTING.md) để biết thêm chi tiết!

## 🤝 Cần Giúp Đỡ?

- Mở Issue để đặt câu hỏi
- Tag maintainer trong comments
- Đọc [docs/README.md](docs/README.md) cho thông tin kỹ thuật

---

## Quick Guide for Contributors (English)

## 🚀 Get Started in 5 Minutes

### Step 1: Fork and Clone
```bash
# Fork repo on GitHub, then:
git clone https://github.com/YOUR_USERNAME/spotify-hand-controller-built-mediapipe-model.git
cd spotify-hand-controller-built-mediapipe-model
```

### Step 2: Setup Environment
```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Configure
```bash
# Copy example config
cp config/config.example.py config/config.py

# Edit config/config.py with your Spotify credentials
# Get credentials at: https://developer.spotify.com/dashboard
```

### Step 4: Setup Git
```bash
# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/spotify-hand-controller-built-mediapipe-model.git
```

### Step 5: Test
```bash
# Run tests to ensure everything works
pytest tests/
```

## 💻 Daily Workflow

### Before Starting Work
```bash
# Sync latest code
git checkout main
git fetch upstream
git merge upstream/main
git push origin main
```

### While Working
```bash
# Create new branch
git checkout -b feature/feature-name

# Work, then commit
git add .
git commit -m "feat: brief description"

# Push to your fork
git push origin feature/feature-name
```

### After Completion
1. Visit GitHub
2. Create Pull Request from your branch
3. Wait for review and respond to feedback if any

## 📋 PR Checklist

Before submitting Pull Request, ensure:

- [ ] Code runs without errors
- [ ] All tests pass
- [ ] Added tests for new code
- [ ] Clear commit messages
- [ ] Synced with latest main

## 🎯 Ideas for Beginners

- Fix typos in documentation
- Add comments to code
- Write more tests
- Find issues tagged `good first issue`
- Improve error messages

## 📚 Full Documentation

Read [CONTRIBUTING.md](CONTRIBUTING.md) for more details!

## 🤝 Need Help?

- Open Issue to ask questions
- Tag maintainer in comments
- Read [docs/README.md](docs/README.md) for technical info
