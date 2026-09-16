<div align="center">

# ✨ vVnK - Discord Self Bot ✨

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Discord.py](https://img.shields.io/badge/Discord.py--self-2.0%2B-purple?logo=discord&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-5.0.5-orange)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

**Discord Self Bot đa năng với đầy đủ tính năng spam, quản lý, giải trí và nhiều hơn nữa.**

[🚀 Bắt đầu](#-cài-đặt-nhanh) • [📖 Tài liệu](#-tài-liệu) • [💬 Commands](docs/COMMANDS.md) • [📜 Điều khoản](docs/TERMS.md)

</div>

---

## ⚠️ Cảnh báo

> **Self bot vi phạm Discord Terms of Service (ToS).** Sử dụng có thể dẫn đến tài khoản bị **khóa vĩnh viễn**. Tác giả **không chịu trách nhiệm** về bất kỳ hậu quả nào. Hãy cân nhắc kỹ trước khi sử dụng.

---

## 📸 Tính năng chính

| Danh mục | Tính năng |
|----------|-----------|
| 👤 **Tài khoản** | Cycle status, AFK, token check, Nitro sniper |
| 🏰 **Server** | Kick, ban, nuke, clone channel/role/emoji |
| 🎤 **Voice** | Phát nhạc, treo voice đa token, spam join/leave |
| 💬 **Spam** | Spam nội dung, webhook, đa token, mass react |
| 🎮 **Giải trí** | Rizz, roast, cat, rainbow role, NSFW |
| 🔧 **Tiện ích** | IP lookup, Instagram, avatar, banner, math |

---

## 🚀 Cài đặt nhanh

```bash
# 1. Clone repo
git clone https://github.com/vVnK-wh0i4m/self-bot-cam.git
cd self-bot-cam

# 2. Chạy file cài đặt (tự động cài thư viện + chạy bot)
python index.py
```

> Chi tiết hơn: [Hướng dẫn cài đặt](docs/INSTALL.md)

---

## 📚 Tài liệu

| File | Nội dung |
|------|----------|
| [📥 Cài đặt](docs/INSTALL.md) | Hướng dẫn cài đặt trên máy tính |
| [🖥️ Hosting](docs/HOSTING.md) | Cài đặt trên Replit, Railway, VPS, Docker |
| [🔧 Chỉnh sửa](docs/CUSTOMIZE.md) | Cách sửa code, đổi tên, thêm lệnh |
| [💬 Commands](docs/COMMANDS.md) | Danh sách tất cả lệnh |
| [📜 Điều khoản](docs/TERMS.md) | Bản quyền MIT và điều khoản sử dụng |
| [❓ FAQ](docs/FAQ.md) | Câu hỏi thường gặp |

---

## 📁 Cấu trúc dự án

```
self-bot-cam/
├── config/
│   └── config.json          # Cấu hình bot
├── cogs/
│   ├── cycstatus.txt         # Danh sách cycle status
│   └── nhay.txt              # Danh sách tin nhắn nháy
├── ffmpeg/
│   └── ffmpeg.exe            # FFmpeg (phát nhạc)
├── music/                    # Thư mục nhạc
├── datoken.txt               # Danh sách token đa token
├── index.py                  # File cài đặt & khởi động
├── nova.py                   # Code chính bot
├── requirements.txt          # Danh sách thư viện
├── docs/                     # Tài liệu chi tiết
└── README.md                 # Trang chính
```

---

## ⚡ Cấu hình nhanh

Mở `config/config.json`:

```json
{
    "token": "TOKEN_CỦA_BẠN",
    "prefix": ".",
    "sniper_webhook": "WEBHOOK_URL"
}
```

| Trường | Mô tả |
|--------|-------|
| `token` | Token tài khoản Discord (bắt buộc) |
| `prefix` | Tiền tố lệnh (mặc định: `.`) |
| `sniper_webhook` | Webhook thông báo Nitro (không bắt buộc) |

---

## 💡 Cách dùng nhanh

```
.menu        → Bảng điều khiển
.botinfo     → Thông tin bot
.spam 2 Xin chào  → Spam mỗi 2 giây
.vcjoin [id] → Vào voice channel
.afk Đang bận  → Bật chế độ AFK
```

> Xem tất cả: [Danh sách lệnh](docs/COMMANDS.md)

---

<div align="center">

**⭐ Star repo nếu thấy hữu ích! ⭐**

Made with ❤️ by vVnK

</div>
