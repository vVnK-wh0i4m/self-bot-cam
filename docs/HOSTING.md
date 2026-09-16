# 🖥️ Hướng dẫn cài đặt trên Hosting

Hướng dẫn deploy bot lên các nền tảng hosting để chạy 24/7.

---

## 📋 Tổng quan

| Hosting | Giá | Uptime | Độ khó |
|---------|-----|--------|--------|
| [Replit](#replit) | Miễn phí | Tùy | ⭐ Dễ |
| [PythonAnywhere](#pythonanywhere) | Miễn phí | Tùy | ⭐ Dễ |
| [Railway](#railway) | Có free tier | 24/7 | ⭐⭐ Trung bình |
| [Render](#render) | Có free tier | 24/7 | ⭐⭐ Trung bình |
| [VPS](#vps--serverriêng) | Trả phí | 24/7 | ⭐⭐⭐ Khó |
| [Docker](#docker) | Tùy VPS | 24/7 | ⭐⭐⭐ Khó |

---

## Replit (Miễn phí)

### Bước 1: Tạo tài khoản

1. Truy cập https://replit.com
2. Đăng ký tài khoản (dùng GitHub/Google)

### Bước 2: Tạo Repl mới

1. Nhấn **+ Create Repl**
2. Chọn **Python** làm language
3. Đặt tên: `vVnK-bot`
4. Nhấn **Create Repl**

### Bước 3: Upload code

**Cách 1: Clone từ GitHub**
```bash
git clone https://github.com/vVnK-wh0i4m/self-bot-cam.git
```

**Cách 2: Upload file thủ công**
- Nhấn nút **Upload file** trong Replit
- Upload từng file từ máy tính

### Bước 4: Cấu hình Secrets

> ⚠️ **KHÔNG** hardcode token trực tiếp trong code khi dùng hosting!

1. V tab **Secrets** (biểu tượng khóa 🔒 bên trái)
2. Thêm biến môi trường:

| Key | Value | Mô tả |
|-----|-------|-------|
| `TOKEN` | Token Discord của bạn | Token bot |
| `PREFIX` | `.` | Tiền tố lệnh |
| `WEBHOOK_URL` | URL webhook | Webhook thông báo |

### Bước 5: Sửa code đọc Environment Variable

Mở file `nova.py`, tìm và sửa phần đọc config:

```python
# Thêm ở đầu file
import os

# Thay phần đọc config bằng:
token = os.environ.get('TOKEN', '')
prefix = os.environ.get('PREFIX', '.')
WEBHOOK_URL = os.environ.get('WEBHOOK_URL', '')
```

### Bước 6: Chạy bot

- Nhấn nút **Run** ▶️
- Bot sẽ tự động cài đặt thư viện và khởi động

### ⚠️ Lưu ý Replit

- Replit free tier có **giới hạn thời gian chạy** (sleep sau 1 giờ không hoạt động)
- Dùng **UptimeRobot** (https://uptimerobot.com) để ping giữ bot awake
- Hoặc nâng cấp Replit付费 plan

---

## PythonAnywhere (Miễn phí)

### Bước 1: Đăng ký

1. Truy cập https://pythonanywhere.com
2. Đăng ký tài khoản miễn phí

### Bước 2: Upload files

1. Vào **Files** trên dashboard
2. Nhấn **Upload a file**
3. Upload toàn bộ files từ folder `self-bot-cam`

### Bước 3: Cài thư viện

1. Vào **Bash console** (tab bên phải)
2. Chạy:

```bash
cd ~/self-bot-cam
pip3 install -r requirements.txt --user
```

### Bước 4: Chạy bot

```bash
cd ~/self-bot-cam
python3 nova.py
```

### ⚠️ Lưu ý PythonAnywhere

- Free tier chỉ chạy được **1 process** liên tục
- Không hỗ trợ WebSocket (có thể bot bị chậm)
- Nâng cấp paid ($5/tháng) để chạy tốt hơn

---

## Railway (24/7)

### Bước 1: Đăng ký

1. Truy cập https://railway.app
2. Đăng ký bằng GitHub

### Bước 2: Tạo project

1. Nhấn **New Project**
2. Chọn **Deploy from GitHub repo**
3. Chọn repo `self-bot-cam`

### Bước 3: Thêm biến môi trường

1. V tab **Variables**
2. Thêm:

| Variable | Value |
|----------|-------|
| `TOKEN` | Token Discord |
| `PREFIX` | `.` |
| `WEBHOOK_URL` | URL webhook |

### Bước 4: Sửa code

Như hướng dẫn ở [Replit](#bước-5-sửa-code-đọc-environment-variable) - đọc từ environment variable.

### Bước 5: Deploy

- Railway sẽ tự động deploy khi có code mới
- Bot sẽ chạy 24/7

### ⚠️ Lưu ý Railway

- Free tier: **500 giờ/tháng** (đủ cho 1 bot)
- Tự ngủ sau 15 phút không có request
- Nâng cấp paid để không bị giới hạn

---

## Render (24/7)

### Bước 1: Đăng ký

1. Truy cập https://render.com
2. Đăng ký bằng GitHub

### Bước 2: Tạo Background Worker

1. Nhấn **New** → **Background Worker**
2. Connect GitHub repo `self-bot-cam`

### Bước 3: Cấu hình

| Setting | Value |
|---------|-------|
| Name | `vvnk-bot` |
| Runtime | `Python` |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `python nova.py` |

### Bước 4: Thêm Environment Variables

| Key | Value |
|-----|-------|
| `TOKEN` | Token Discord |
| `PREFIX` | `.` |

### ⚠️ Lưu ý Render

- Free tier: **750 giờ/tháng**
- Tự spin down sau 15 phút không hoạt động
- Cold start có thể mất 30-60 giây

---

## VPS / Server riêng

### Ubuntu/Debian

```bash
# 1. Cập nhật hệ thống
sudo apt update && sudo apt upgrade -y

# 2. Cài Python
sudo apt install python3 python3-pip -y

# 3. Clone repo
git clone https://github.com/vVnK-wh0i4m/self-bot-cam.git
cd self-bot-cam

# 4. Cài thư viện
pip3 install -r requirements.txt

# 5. Cài FFmpeg
sudo apt install ffmpeg -y

# 6. Chạy bot (dùng screen để chạy nền)
sudo apt install screen -y
screen -S vvnk-bot
python3 nova.py

# Tách screen: Ctrl+A rồi D
# Quay lại: screen -r vvnk-bot
```

### Sử dụng Systemd (tự khởi động lại)

Tạo file `/etc/systemd/system/vvnk-bot.service`:

```ini
[Unit]
Description=vVnK Discord Self Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/root/self-bot-cam
ExecStart=/usr/bin/python3 nova.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Kích hoạt:

```bash
sudo systemctl daemon-reload
sudo systemctl enable vvnk-bot
sudo systemctl start vvnk-bot

# Xem log
sudo journalctl -u vvnk-bot -f

# Kiểm tra trạng thái
sudo systemctl status vvnk-bot
```

### Quản lý bot

```bash
# Dừng bot
sudo systemctl stop vvnk-bot

# Khởi động lại
sudo systemctl restart vvnk-bot

# Tắt tự khởi động
sudo systemctl disable vvnk-bot
```

---

## Docker

### Tạo Dockerfile

Tạo file `Dockerfile` trong thư mục project:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "nova.py"]
```

### Build và chạy

```bash
# Build image
docker build -t vvnk-bot .

# Chạy container
docker run -d --name vvnk-bot --restart=always vvnk-bot

# Xem log
docker logs -f vvnk-bot

# Dừng container
docker stop vvnk-bot

# Xóa container
docker rm vvnk-bot
```

### Docker Compose

Tạo file `docker-compose.yml`:

```yaml
version: '3.8'

services:
  bot:
    build: .
    container_name: vvnk-bot
    restart: always
    environment:
      - TOKEN=your_token_here
      - PREFIX=.
```

Chạy:

```bash
docker-compose up -d
```

---

## 🔒 Mẹo bảo mật khi dùng Hosting

1. **Dùng Environment Variable:** Không hardcode token trong code
2. **Gitignore:** Đảm bảo `config.json` và `datoken.txt` nằm trong `.gitignore`
3. **Token riêng:** Dùng token tài khoản phụ, không dùng tài khoản chính
4. **Reset token nếu lộ:** Vào https://discord.com/developers/applications để reset

---

> Quay lại [README chính](../README.md) | Trước: [Cài đặt](INSTALL.md) | Tiếp: [Chỉnh sửa](CUSTOMIZE.md)
