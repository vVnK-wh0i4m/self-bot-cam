<div align="center">

# ✨ vVnK - Discord Self Bot ✨

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Discord.py](https://img.shields.io/badge/Discord.py--self-2.0%2B-purple?logo=discord&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![Version](https://img.shields.io/badge/Version-5.0.5-orange)

**Discord Self Bot đa năng với đầy đủ tính năng spam, quản lý, giải trí và nhiều hơn nữa.**

</div>

---

## ⚠️ Cảnh báo quan trọng

> **Self bot vi phạm Discord Terms of Service (ToS).** Sử dụng self bot có thể dẫn đến việc tài khoản bị **khóa vĩnh viễn**. Tác giả **không chịu trách nhiệm** về bất kỳ hậu quả nào phát sinh từ việc sử dụng bot này. Hãy cân nhắc kỹ trước khi sử dụng.

---

## 📋 Mục lục

- [Giới thiệu](#-giới-thiệu)
- [Tính năng](#-tính-năng)
- [Yêu cầu hệ thống](#-yêu-cầu-hệ-thống)
- [Cài đặt trên máy tính](#-cài-đặt-trên-máy-tính)
- [Cài đặt trên hosting](#-cài-đặt-trên-hosting)
- [Cấu hình](#-cấu-hình)
- [Hướng dẫn chỉnh sửa](#-hướng-dẫn-chỉnh-sửa)
- [Danh sách lệnh](#-danh-sách-lệnh)
- [Cấu trúc thư mục](#-cấu-trúc-thư-mục)
- [Bản quyền và điều khoản sử dụng](#-bản-quyền-và-điều-khoản-sử-dụng)
- [Hỗ trợ](#-hỗ-trợ)

---

## 🌟 Giới thiệu

vVnK là Discord Self Bot được xây dựng bằng Python và thư viện `discord.py-self`. Bot cung cấp bộ tính năng đa dạng bao gồm:

- Quản lý tài khoản và trạng thái
- Quản lý server (kick, ban, nuke, clone)
- Voice channel (phát nhạc, spam join/leave)
- Spam tin nhắn (đa token, webhook)
- Nitro Sniper tự động
- Lệnh giải trí (rizz, roast, NSFW)
- Tra cứu thông tin (IP, Instagram)

---

## 🚀 Tính năng

### 👤 Quản lý tài khoản
| Tính năng | Mô tả |
|-----------|--------|
| Cycle Status | Tự động thay đổi trạng thái theo danh sách |
| Set Status | Đặt trạng thái tùy chỉnh |
| AFK Mode | Chế độ AFK tự động phản hồi |
| Close All DMs | Đóng tất cả tin nhắn trực tiếp |
| Delete Friends | Xóa tất cả bạn bè |
| Token Check | Kiểm tra thông tin chi tiết token |
| Nitro Promo Check | Kiểm tra link promo Nitro |

### 🏰 Quản lý server
| Tính năng | Mô tả |
|-----------|--------|
| Kick / Ban / Unban | Quản lý thành viên |
| Nuke Server | Xóa và tạo lại toàn bộ channel |
| Bomb | Xóa tất cả channel |
| Delete All Roles | Xóa tất cả role |
| Clone Channels | Sao chép channel từ server khác |
| Clone Roles | Sao chép role từ server khác |
| Clone Emoji | Sao chép emoji từ server khác |

### 🎤 Voice Channel
| Tính năng | Mô tả |
|-----------|--------|
| VC Join / Leave | Vào và rời voice channel |
| Phát nhạc | Phát file nhạc trong voice |
| Token VC | Treo voice đa token |
| VC Spam | Spam join/leave voice |
| Forced Disconnect | Ngắt kết nối buộc user khác |

### 💬 Spam & Tin nhắn
| Tính năng | Mô tả |
|-----------|--------|
| Spam | Spam nội dung với độ trễ tùy chỉnh |
| Nhay | Spam từ file `nhay.txt` |
| Webhook Spam | Spam qua webhook |
| Token Spam | Spam đa token |
| Mass React | Thêm reaction hàng loạt |
| Clear Messages | Xóa tin nhắn hàng loạt |

### 🎮 Giải trí
| Tính năng | Mô tả |
|-----------|--------|
| Rizz | Lời tán tỉnh ngẫu nhiên |
| Roast | Lời chế giễu |
| Cat | Ảnh mèo ngẫu nhiên |
| Rainbow Role | Role 7 màu |
| PH Comment | PornHub Comment troll |
| NSFW | Các lệnh ảnh NSFW |

### 🎯 Tiện ích
| Tính năng | Mô tả |
|-----------|--------|
| Avatar / Banner | Xem ảnh đại diện và banner |
| Server Info | Xem thông tin server |
| Bot Info | Xem thông tin bot |
| IP Lookup | Tra cứu địa chỉ IP |
| Instagram | Xem thông tin tài khoản IG |
| Math | Máy tính đơn giản |
| Nitro Sniper | Tự động claim Nitro gift |

---

## 💻 Yêu cầu hệ thống

### Máy tính cá nhân
| Thành phần | Yêu cầu |
|------------|----------|
| Hệ điều hành | Windows 10+, macOS, Linux |
| Python | 3.8 trở lên |
| RAM | Tối thiểu 512MB |
| Ổ cứng | 500MB trống |
| Mạng | Kết nối internet ổn định |

### Hosting
| Thành phần | Yêu cầu |
|------------|----------|
| Python | 3.8 trở lên |
| RAM | Tối thiểu 512MB |
| Ổ cứng | 1GB trống |
| uptime | 24/7 (khuyến nghị) |

---

## 📥 Cài đặt trên máy tính

### Bước 1: Clone repository

```bash
git clone https://github.com/vVnK-wh0i4m/self-bot-cam.git
cd self-bot-cam
```

### Bước 2: Cài đặt thư viện

**Cách 1: Dùng file tự động cài đặt**
```bash
python index.py
```

**Cách 2: Dùng pip thủ công**
```bash
pip install -r requirements.txt
```

### Bước 3: Cài đặt FFmpeg (cho tính năng phát nhạc)

1. Tải FFmpeg tại: https://ffmpeg.org/download.html
2. Giải nén file `ffmpeg.exe` vào thư mục `ffmpeg/`
3. Cấu trúc: `self-bot-cam/ffmpeg/ffmpeg.exe`

### Bước 4: Cấu hình

Mở file `config/config.json` và điền thông tin:

```json
{
    "token": "TOKEN_CỦA_BẠN",
    "prefix": ".",
    "sniper_webhook": "WEBHOOK_URL"
}
```

### Bước 5: Chạy bot

```bash
python nova.py
```

Hoặc dùng file khởi động (tự động cài đặt + chạy):

```bash
python index.py
```

---

## 🖥️ Cài đặt trên hosting

### Phương án 1: Python Hosting (推荐)

Các hosting hỗ trợ Python phổ biến:
- **Replit** (https://replit.com) - Miễn phí
- **PythonAnywhere** (https://pythonanywhere.com) - Miễn phí
- **Railway** (https://railway.app) - Có free tier
- **Render** (https://render.com) - Có free tier
- **Koyeb** (https://koyeb.com) - Có free tier

#### Hướng dẫn trên Replit

1. **Tạo tài khoản** tại https://replit.com

2. **Tạo Repl mới:**
   - Nhấn **+ Create Repl**
   - Chọn language: **Python**
   - Đặt tên: `vVnK-bot`

3. **Upload code:**
   - Clone repo vào Replit hoặc upload file thủ công
   - File chính: `nova.py`

4. **Cấu hình secrets:**
   - V tab **Secrets** (icon khóa 🔒)
   - Thêm biến:
     - Key: `TOKEN` → Value: token Discord của bạn
     - Key: `PREFIX` → Value: `.` (hoặc prefix bạn muốn)

5. **Sửa code để đọc từ environment:**

   Thay vì đọc file config, sửa `nova.py`:

   ```python
   import os

   token = os.environ.get('TOKEN', '')
   prefix = os.environ.get('PREFIX', '.')
   WEBHOOK_URL = os.environ.get('WEBHOOK_URL', '')
   ```

6. **Chạy bot:**
   - Nhấn **Run** ▶️
   - Bot sẽ tự động cài đặt và khởi động

#### Hướng dẫn trên PythonAnywhere

1. **Đăng ký tài khoản** tại https://pythonanywhere.com

2. **Upload files:**
   - Vào **Files** → Upload file từ máy tính
   - Upload toàn bộ folder `self-bot-cam`

3. **Cài đặt thư viện:**
   - Vào **Bash console**
   - Chạy:
   ```bash
   cd ~/self-bot-cam
   pip install -r requirements.txt --user
   ```

4. **Tạo Console:**
   - Vào **Consoles** → Start a new console: **Bash**
   - Chạy:
   ```bash
   cd ~/self-bot-cam
   python nova.py
   ```

#### Hướng dẫn trên Railway

1. **Đăng ký** tại https://railway.app

2. **Tạo project mới:**
   - Nhấn **New Project**
   - Chọn **Deploy from GitHub repo`
   - Chọn repo `self-bot-cam`

3. **Thêm biến môi trường:**
   - V tab **Variables**
   - Thêm:
     - `TOKEN` = token Discord
     - `PREFIX` = `.`

4. **Sửa code** để đọc environment variable (như hướng dẫn Replit ở trên)

5. **Deploy:**
   - Railway sẽ tự động deploy khi có code mới
   - Bot sẽ chạy 24/7

### Phương án 2: VPS / Server riêng

#### Trên Ubuntu/Debian

```bash
# Cập nhật hệ thống
sudo apt update && sudo apt upgrade -y

# Cài Python và pip
sudo apt install python3 python3-pip -y

# Clone repo
git clone https://github.com/vVnK-wh0i4m/self-bot-cam.git
cd self-bot-cam

# Cài thư viện
pip3 install -r requirements.txt

# Cài FFmpeg
sudo apt install ffmpeg -y

# Chạy bot với screen (chạy nền)
screen -S vvnk-bot
python3 nova.py

# Tách screen: nhấn Ctrl+A rồi D
# Quay lại screen: screen -r vvnk-bot
```

#### Sử dụng systemd (tự khởi động lại khi crash)

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
```

### Phương án 3: Docker

Tạo file `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "nova.py"]
```

Build và chạy:

```bash
docker build -t vvnk-bot .
docker run -d --name vvnk-bot --restart=always vvnk-bot
```

---

## ⚙️ Cấu hình

### File `config/config.json`

```json
{
    "token": "TOKEN_CỦA_BẠN",
    "prefix": ".",
    "sniper_webhook": "https://discord.com/api/webhooks/xxx/xxx"
}
```

| Trường | Kiểu | Mô tả | Mặc định |
|--------|------|-------|----------|
| `token` | string | Token tài khoản Discord | Bắt buộc |
| `prefix` | string | Tiền tố lệnh | `.` |
| `sniper_webhook` | string | Webhook nhận thông báo Nitro | Không bắt buộc |

### File `cogs/cycstatus.txt`

Danh sách status tự động chuyển (mỗi dòng 1 status):

```
Playing vVnK Bot
discord.gg/vVnK
Đang online 24/7
```

### File `cogs/nhay.txt`

Danh sách tin nhắn nháy (mỗi dòng 1 tin nhắn):

```
DẬY
ALO
DẬY
```

### File `datoken.txt`

Danh sách token cho tính năng đa token (mỗi dòng 1 token):

```
token1
token2
token3
```

---

## 🔧 Hướng dẫn chỉnh sửa

### Đổi tên bot

Tìm và thay đổi trong file `nova.py`:

```python
# Dòng ~84
__NAME__ = 'vVnK'  # Đổi thành tên bạn muốn

# Dòng ~256 (menu)
✨ vVnK ✨  # Đổi thành tên hiển thị

# Dòng ~83
version = '5.0.5'  # Đổi version
```

### Đổi prefix (tiền tố lệnh)

Trong file `nova.py`, dòng ~51:

```python
bot = commands.Bot(command_prefix=prefix, self_bot=True)
```

Hoặc thay đổi trong `config/config.json`:

```json
{
    "prefix": "!"
}
```

### Thêm lệnh mới

Thêm function mới trong `nova.py`:

```python
@bot.command()
async def ten_lenh(ctx, *, args=None):
    await ctx.message.delete()
    await ctx.send(f"# __{__NAME__}__\nNội dung phản hồi")
```

### Thay đổi auto react

Trong file `nova.py`, tìm `on_message` event:

```python
reactions = {
    'ngu': '🤣',    # Thay đổi từ và emoji
    'oc cac': '🤣',  # Thêm bao nhiêu tùy ý
}
```

### Tắt/mở tính năng Nitro Sniper

Trong file `nova.py`:

```python
nitro_sniper = True   # Bật
nitro_sniper = False  # Tắt
```

### Đổi webhook thông báo

Trong `config/config.json`:

```json
{
    "sniper_webhook": "URL_WEBHOOK_MỚI"
}
```

### Thêm lệnh NSFW mới

```python
@nsfw.command()
async def ten_anh(ctx):
    await ctx.message.delete()
    if ctx.channel.is_nsfw():
        async with aiohttp.ClientSession() as session:
            async with session.get("https://nekobot.xyz/api/image?type=TEN_LOAI") as response:
                json_data = await response.json()
                await ctx.channel.send(json_data["message"])
    else:
        await ctx.send(f"# __{__NAME__}__\n:x: | Chỉ sử dụng trong kênh NSFW!")
```

---

## 📖 Danh sách lệnh

### 🔹 Lệnh chính

| Lệnh | Aliases | Mô tả |
|-------|---------|--------|
| `.menu` | - | Hiển thị bảng điều khiển |
| `.botinfo` | - | Thông tin bot |
| `.serverinfo` | - | Thông tin server |
| `.shutdown` | - | Tắt bot |
| `.restart` | `.reboot` | Khởi động lại bot |

### 🔹 Quản lý tài khoản

| Lệnh | Mô tả |
|-------|--------|
| `.tokencheck [token]` | Kiểm tra token |
| `.checkpromo [link]` | Kiểm tra Nitro promo |
| `.closealldms` | Đóng tất cả DM |
| `.delfriends` | Xóa tất cả bạn bè |
| `.afk [lý_do]` | Bật AFK |
| `.unafk` | Tắt AFK |

### 🔹 Trạng thái

| Lệnh | Mô tả |
|-------|--------|
| `.cyclestatus` | Bật/tắt cycle status |
| `.setstatus [nội_dung]` | Đặt status |
| `.addstatus [nội_dung]` | Thêm status vào danh sách |
| `.clearstatus` | Xóa tất cả status |

### 🔹 RPC (Rich Presence)

| Lệnh | Mô tả |
|-------|--------|
| `.rpc playing [tên]` | Đang chơi game |
| `.rpc streaming [tên]` | Đang stream |
| `.rpc listening [nội_dung]` | Đang nghe |
| `.rpc watching [nội_dung]` | Đang xem |
| `.stoprpc` | Dừng RPC |

### 🔹 Voice Channel

| Lệnh | Mô tả |
|-------|--------|
| `.vcjoin [id] [M] [D] [C]` | Vào voice (M=mute, D=deafen, C=camera) |
| `.vcleave` | Rời voice |
| `.xanhac [id] [file] [D] [C]` | Phát nhạc |
| `.tokenvc [id]` | Treo voice đa token |
| `.tokenleave` | Dừng treo voice |
| `.vcspam [id]` | Spam join/leave |
| `.stopvcspam` | Dừng spam voice |
| `.forcedisconnect [@user]` | Ngắt user khỏi voice |
| `.stopforcedisconnect` | Dừng forced disconnect |

### 🔹 Spam & Tin nhắn

| Lệnh | Mô tả |
|-------|--------|
| `.spam [delay] [nội_dung]` | Spam với độ trễ |
| `.stopspam` | Dừng spam |
| `.nhay [delay]` | Spam từ nhay.txt |
| `.stopnhay` | Dừng nháy |
| `.webhook [url] [nội_dung]` | Spam webhook |
| `.stopwebhook` | Dừng webhook spam |
| `.tokenspam [delay] [nội_dung]` | Spam đa token |
| `.stoptokenspam` | Dừng token spam |
| `.tokentreodu [delay] [file]` | Treo đú đa token |
| `.stoptreodu` | Dừng treo đú |
| `.massreact [số] [emoji]` | Reaction hàng loạt |
| `.clear [số]` | Xóa tin nhắn |
| `.hackclear` | Xóa chat bằng tin nhắn trống |
| `.setngon [file]` | Đặt file cho tokenspam |

### 🔹 Quản lý Server

| Lệnh | Mô tả |
|-------|--------|
| `.kick [@user]` | Kick thành viên |
| `.ban [@user]` | Ban thành viên |
| `.unban [id]` | Unban |
| `.nuke [tên] [nội_dung]` | Nuke server |
| `.bomb` | Xóa tất cả channel |
| `.deleteallroles` | Xóa tất cả role |
| `.clone_channels [id_cũ] [id_mới]` | Clone channel |
| `.clone_roles [id_cũ] [id_mới]` | Clone role |
| `.cloneemoji [emoji]` | Clone emoji |
| `.autoreact [on/off]` | Auto react |

### 🔹 Tiện ích

| Lệnh | Mô tả |
|-------|--------|
| `.avatar [@user]` | Xem avatar |
| `.banner [@user]` | Xem banner |
| `.iplookup [ip]` | Tra cứu IP |
| `.insta [tên]` | Kiểm tra Instagram |
| `.math [phép_tính]` | Máy tính |

### 🔹 Giải trí

| Lệnh | Mô tả |
|-------|--------|
| `.rizz [@user]` | Tán tỉnh |
| `.roast [@user]` | Chế giễu |
| `.cat` | Ảnh mèo |
| `.rainbowrole [@role]` | Role 7 màu |
| `.phcomment [@user] [nội_dung]` | PH Comment |
| `.succac` | Lệnh giải trí |
| `.nsfw [loại]` | NSFW (anal, hanal, 4k, gif, pussy, boobs, ass, hboobs, thighs) |

---

## 📁 Cấu trúc thư mục

```
self-bot-cam/
├── config/
│   └── config.json          # Cấu hình bot
├── cogs/
│   ├── cycstatus.txt         # Danh sách cycle status
│   └── nhay.txt              # Danh sách tin nhắn nháy
├── ffmpeg/
│   └── ffmpeg.exe            # FFmpeg (cần cho phát nhạc)
├── music/                    # Thư mục nhạc
├── trash/                    # Thư mục tạm
├── datoken.txt               # Danh sách token đa token
├── du.txt                    # Nội dung
├── ngon.txt                  # Nội dung
├── index.py                  # File cài đặt & khởi động
├── nova.py                   # Code chính bot
├── readfirst.txt             # Hướng dẫn nhanh
├── requirements.txt          # Danh sách thư viện
├── .gitignore                # Git ignore
└── README.md                 # Tài liệu
```

---

## 📜 Bản quyền và điều khoản sử dụng

### Bản quyền

```
MIT License

Copyright (c) 2025 vVnK

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Điều khoản sử dụng

1. **Mục đích sử dụng:**
   - Dự án này được cung cấp cho mục đích **giáo dục và nghiên cứu**.
   - Tác giả **không khuyến khích** sử dụng cho mục đích vi phạm ToS của Discord.

2. **Trách nhiệm người dùng:**
   - Người dùng **chịu toàn bộ trách nhiệm** khi sử dụng bot này.
   - Tác giả **không chịu trách nhiệm** về bất kỳ thiệt hại nào, bao gồm nhưng không giới hạn: mất tài khoản, khóa tài khoản, thiệt hại dữ liệu.

3. **Hành vi bị cấm:**
   - Sử dụng bot để **quấy rối, spam** người dùng khác.
   - Sử dụng bot để **vi phạm pháp luật** hoặc ToS của Discord.
   - **Chia sẻ lại** token của người dùng khác.
   - Sử dụng bot cho mục đích **gian lận, lừa đảo**.

4. **Bảo mật:**
   - **KHÔNG BAO GIỜ** chia sẻ token của bạn với bất kỳ ai.
   - **KHÔNG BAO GIỜ** commit token vào repository công khai.
   - Token cho phép truy cập **hoàn toàn** vào tài khoản Discord của bạn.

5. **Miễn trách:**
   - Dự án được cung cấp theo nguyên tắc **"AS IS"** (không bảo hành).
   - Tác giả không đảm bảo bot hoạt động liên tục, không lỗi.
   - Người dùng tự chịu rủi ro khi sử dụng.

6. **Tuân thủ luật pháp:**
   - Người dùng phải tuân thủ pháp luật tại quốc gia của mình.
   - Không sử dụng bot để vi phạm quyền riêng tư của người khác.

---

## 🛡️ Mẹo bảo mật

1. **Không commit token:** Đảm bảo file `config.json` và `datoken.txt` nằm trong `.gitignore`

2. **Sử dụng environment variable:** Trên hosting, dùng biến môi trường thay vì hardcode token

3. **Reset token nếu lộ:** Nếu token bị lộ, reset ngay tại https://discord.com/developers/applications

4. **Không chia sẻ config:** Không chia sẻ file `config/config.json` với người khác

5. **Sử dụng token riêng:** Không dùng token của tài khoản chính, nên dùng tài khoản phụ

---

## ❓ FAQ

**Q: Bot có an toàn không?**
A: Self bot vi phạm Discord ToS. Sử dụng có thể dẫn đến khóa tài khoản. Hãy cân nhắc kỹ.

**Q: Tại sao bot không hoạt động?**
A: Kiểm tra:
- Token có hợp lệ không
- Python version >= 3.8
- Đã cài đủ thư viện chưa
- File config.json đúng format chưa

**Q: Làm sao để bot chạy 24/7?**
A: Sử dụng hosting (Replit, Railway, VPS) thay vì chạy trên máy tính cá nhân.

**Q: Token bị lộ thì làm sao?**
A: Vào https://discord.com/developers/applications → chọn app → Reset token.

**Q: Bot có hỗ trợ Discord trên điện thoại không?**
A: Bot chạy trên máy tính/server, không cần điện thoại.

---

## 📞 Hỗ trợ

- **GitHub Issues:** https://github.com/vVnK-wh0i4m/self-bot-cam/issues
- **Author:** vVnK-wh0i4m

---

<div align="center">

**⭐ Star repo nếu thấy hữu ích! ⭐**

Made with ❤️ by vVnK

</div>
