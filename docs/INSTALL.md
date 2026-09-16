# 📥 Hướng dẫn cài đặt trên máy tính

## 📋 Yêu cầu hệ thống

| Thành phần | Yêu cầu |
|------------|----------|
| Hệ điều hành | Windows 10+, macOS, Linux |
| Python | 3.8 trở lên |
| RAM | Tối thiểu 512MB |
| Ổ cứng | 500MB trống |
| Mạng | Kết nối internet ổn định |

---

## 🚀 Cài đặt

### Bước 1: Clone repository

```bash
git clone https://github.com/vVnK-wh0i4m/self-bot-cam.git
cd self-bot-cam
```

### Bước 2: Cài đặt thư viện

**Cách 1: Dùng file tự động (khuyến nghị)**

```bash
python index.py
```

File này sẽ tự động:
- Cài tất cả thư viện cần thiết
- Chạy bot

**Cách 2: Cài thủ công**

```bash
pip install -r requirements.txt
```

Sau đó chạy bot:

```bash
python nova.py
```

### Bước 3: Cài FFmpeg (cho tính năng phát nhạc)

1. Tải FFmpeg tại: https://ffmpeg.org/download.html
2. Giải nén `ffmpeg.exe` vào thư mục `ffmpeg/`
3. Cấu trúc cuối cùng:

```
self-bot-cam/
└── ffmpeg/
    └── ffmpeg.exe
```

### Bước 4: Cấu hình

Mở file `config/config.json` và điền thông tin:

```json
{
    "token": "TOKEN_CỦA_BẠN",
    "prefix": ".",
    "sniper_webhook": "WEBHOOK_URL"
}
```

#### Cách lấy Token Discord

> ⚠️ **CẢNH BÁO:** KHÔNG BAO GIỜ chia sẻ token. Token cho phép truy cập hoàn toàn vào tài khoản.

1. Mở Discord trên trình duyệt (https://discord.com/app)
2. Nhấn `F12` để mở Developer Tools
3. Vào tab **Network**
4. Tìm bất kỳ request nào đến `discord.com/api`
5. Tìm header `Authorization` → đó là token

#### Cách lấy Webhook URL

1. Mở Discord → chọn server
2. Vào **Cài đặt** → **integrations** → **Webhooks**
3. Nhấn **New Webhook**
4. Đặt tên, chọn kênh
5. Nhấn **Copy Webhook URL**

### Bước 5: Chạy bot

```bash
python nova.py
```

Hoặc dùng file khởi động (cài đặt + chạy):

```bash
python index.py
```

---

## ✅ Kiểm tra bot hoạt động

Sau khi chạy, terminal sẽ hiển thị:

```
==================================================
      vVnK is Online
==================================================
👤 Bot Name: Tên_bot#1234
🆔 Bot ID: 123456789
🔧 Prefix: .
📌 Version: 5.0.5
🌐 Servers: 1
==================================================
```

Mở Discord, nhập `.menu` để kiểm tra bot phản hồi.

---

## 🔧 Cài đặt thủ công (chi tiết)

Nếu `pip install -r requirements.txt` không hoạt động, cài từng thư viện:

```bash
pip install discord.py-self
pip install requests
pip install pynacl
pip install python-dateutil
pip install instaloader
pip install psutil
pip install pytz
pip install protobuf==3.20.3
pip install colour
pip install aiohttp
```

---

## ⚠️ Xử lý lỗi thường gặp

### Lỗi: `Python was not found`

→ Cài Python từ https://www.python.org/downloads/
→ Đánh dấu **"Add Python to PATH"** khi cài

### Lỗi: `pip is not recognized`

→ Chạy: `python -m pip install -r requirements.txt`

### Lỗi: `No module named 'discord'`

→ Chạy: `pip install discord.py-self`

### Lỗi: `ffmpeg.exe not found`

→ Tải FFmpeg và đặt vào thư mục `ffmpeg/`

---

> Quay lại [README chính](../README.md) | Tiếp theo: [Hướng dẫn Hosting](HOSTING.md)
