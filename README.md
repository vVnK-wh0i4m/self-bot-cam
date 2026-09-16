# vVnK - Discord Self Bot

Discord Self Bot với đầy đủ tính năng, được xây dựng bằng Python và thư viện `discord.py-self`.

---

## Mục lục

- [Giới thiệu](#giới-thiệu)
- [Tính năng](#tính-năng)
- [Yêu cầu hệ thống](#yêu-cầu-hệ-thống)
- [Cài đặt](#cài-đặt)
- [Cấu hình](#cấu-hình)
- [Hướng dẫn sử dụng](#hướng-dẫn-sử-dụng)
- [Danh sách lệnh](#danh-sách-lệnh)
- [Cảnh báo](#cảnh-báo)

---

## Giới thiệu

vVnK là một Discord Self Bot được phát triển nhằm mục đích giải trí và quản lý tài khoản Discord cá nhân. Bot cung cấp nhiều tính năng từ quản lý tin nhắn, voice channel, cho đến các lệnh giải trí và spam.

> **Lưu ý:** Self Bot vi phạm Discord Terms of Service. Hãy cân nhắc kỹ trước khi sử dụng. Tôi không chịu trách nhiệm về bất kỳ hậu quả nào.

---

## Tính năng

### Quản lý tài khoản
- Tự động thay đổi trạng thái (cycle status)
- Đặt trạng thái tùy chỉnh
- Đóng tất cả tin nhắn trực tiếp (DM)
- Xóa tất cả bạn bè
- Kiểm tra thông tin token
- Kiểm tra Nitro promo

### Quản lý server
- Kick / Ban / Unban thành viên
- Xóa tất cả role
- Sao chép channel từ server khác
- Sao chép role từ server khác
- Sao chép emoji
- Nuke server (xóa và tạo lại channel)

### Voice Channel
- Vào / rời voice channel
- Phát nhạc trong voice channel
- Treo voice đa token
- Spam join/leave voice
- Ngắt kết nối buộc người dùng khác

### Tin nhắn và Spam
- Spam nội dung với độ trễ tùy chỉnh
- Spam từ file văn bản
- Spam qua webhook
- Spam đa token
- Phản hồi hàng loạt (mass react)
- Xóa tin nhắn hàng loạt
- Xóa chat bằng tin nhắn trống

### Tiện ích
- Xem avatar và banner của người dùng
- Xem thông tin server
- Xem thông tin bot
- Tra cứu IP
- Kiểm tra tài khoản Instagram
- Máy tính đơn giản
- Tự động phản ứng tin nhắn
- Chế độ AFK

### Giải trí
- Lệnh rizz (tán tỉnh)
- Lệnh roast (chế giễu)
- Ảnh mèo ngẫu nhiên
- Lệnh NSFW (chỉ dùng trong kênh NSFW)
- Rainbow role (role 7 màu)
- PornHub Comment troll

### Nitro Sniper
- Tự động claim Nitro gift link
- Thông báo qua webhook khi claim thành công

---

## Yêu cầu hệ thống

- **Hệ điều hành:** Windows / Linux / macOS
- **Python:** 3.8 trở lên
- **FFmpeg:** Cần thiết cho tính năng phát nhạc (đặt `ffmpeg.exe` trong thư mục `ffmpeg/`)

---

## Cài đặt

### 1. Clone repository

```bash
git clone https://github.com/vVnK-wh0i4m/self-bot-cam.git
cd self-bot-cam
```

### 2. Cài đặt thư viện

Chạy file `index.py` để tự động cài đặt tất cả thư viện cần thiết:

```bash
python index.py
```

Hoặc cài đặt thủ công từ file `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Cài đặt FFmpeg

- Tải FFmpeg từ: https://ffmpeg.org/download.html
- Đặt file `ffmpeg.exe` vào thư mục `ffmpeg/`

---

## Cấu hình

### File cấu hình: `config/config.json`

```json
{
    "token": "TOKEN_CỦA_BẠN",
    "prefix": ".",
    "sniper_webhook": "WEBHOOK_URL"
}
```

| Trường | Mô tả |
|--------|--------|
| `token` | Token của tài khoản Discord (self bot) |
| `prefix` | Tiền tố lệnh (mặc định: `.`) |
| `sniper_webhook` | URL webhook để nhận thông báo Nitro sniper |

### Token

Để lấy token tài khoản Discord:
1. Mở Discord trên trình duyệt
2. Nhấn `F12` để mở Developer Tools
3. Vào tab `Network`
4. Tìm bất kỳ request nào đến `discord.com/api`
5. Tìm header `Authorization` - đó chính là token của bạn

> **CẢNH BÁO:** KHÔNG BAO GIỜ chia sẻ token của bạn với bất kỳ ai. Token cho phép truy cập hoàn toàn vào tài khoản của bạn.

---

## Hướng dẫn sử dụng

### Khởi động bot

```bash
python index.py
```

Hoặc chạy trực tiếp file chính:

```bash
python nova.py
```

### Các lệnh cơ bản

Sử dụng prefix đã cấu hình (mặc định là `.`) trước mỗi lệnh.

Ví dụ:
- `.menu` - Hiển thị bảng điều khiển
- `.botinfo` - Xem thông tin bot
- `.spam 2 Hello World` - Spam "Hello World" mỗi 2 giây

---

## Danh sách lệnh

### Lệnh chính

| Lệnh | Mô tả |
|-------|--------|
| `.menu` | Hiển thị bảng điều khiển chính |
| `.botinfo` | Xem thông tin chi tiết về bot |
| `.tienich` | Danh sách tiện ích |
| `.troll` | Danh sách lệnh giải trí |
| `.raid` | Danh sách lệnh spam/raid |
| `.quanly` | Danh sách lệnh quản lý |
| `.shutdown` | Tắt bot |
| `.restart` / `.reboot` | Khởi động lại bot |

### Quản lý tài khoản

| Lệnh | Mô tả |
|-------|--------|
| `.tokencheck [token]` | Kiểm tra thông tin token |
| `.checkpromo [link]` | Kiểm tra Nitro promo |
| `.closealldms` | Đóng tất cả DM |
| `.delfriends` | Xóa tất cả bạn bè |
| `.afk [lý_do]` | Bật chế độ AFK |
| `.unafk` | Tắt chế độ AFK |

### Trạng thái

| Lệnh | Mô tả |
|-------|--------|
| `.cyclestatus` | Bật/tắt tự động thay đổi status |
| `.setstatus [nội_dung]` | Đặt trạng thái tùy chỉnh |
| `.addstatus [nội_dung]` | Thêm status vào danh sách cycle |
| `.clearstatus` | Xóa tất cả status |

### RPC (Rich Presence)

| Lệnh | Mô tả |
|-------|--------|
| `.rpc playing [tên_game]` | Hiển thị đang chơi game |
| `.rpc streaming [tên_game]` | Hiển thị đang stream |
| `.rpc listening [nội_dung]` | Hiển thị đang nghe |
| `.rpc watching [nội_dung]` | Hiển thị đang xem |
| `.stoprpc` | Dừng RPC |

### Voice Channel

| Lệnh | Mô tả |
|-------|--------|
| `.vcjoin [id] [M] [D] [C]` | Vào voice channel (M=mute, D=deafen, C=camera) |
| `.vcleave` | Rời voice channel |
| `.xanhac [id] [file] [D] [C]` | Phát nhạc trong voice |
| `.tokenvc [id]` | Treo voice đa token |
| `.tokenleave` | Dừng treo voice đa token |
| `.vcspam [id]` | Spam join/leave voice |
| `.stopvcspam` | Dừng spam voice |
| `.forcedisconnect [user]` | Ngắt kết nối buộc user khỏi voice |
| `.stopforcedisconnect` | Dừng forced disconnect |

### Spam và Tin nhắn

| Lệnh | Mô tả |
|-------|--------|
| `.spam [delay] [nội_dung]` | Spam nội dung với độ trễ |
| `.stopspam` | Dừng spam |
| `.nhay [delay]` | Spam từ file nhay.txt |
| `.stopnhay` | Dừng nháy |
| `.webhook [url] [nội_dung]` | Spam qua webhook |
| `.stopwebhook` | Dừng spam webhook |
| `.tokenspam [delay] [nội_dung]` | Spam đa token |
| `.tokentreodu [delay] [file]` | Treo đú đa token |
| `.stoptokenspam` | Dừng spam đa token |
| `.stoptreodu` | Dừng treo đú |
| `.massreact [số] [emoji]` | Thêm reaction hàng loạt |
| `.clear [số]` | Xóa tin nhắn |
| `.hackclear` | Xóa chat bằng tin nhắn trống |
| `.setngon [file]` | Đặt file tin nhắn cho tokenspam |

### Quản lý Server

| Lệnh | Mô tả |
|-------|--------|
| `.kick [user]` | Kick thành viên |
| `.ban [user]` | Ban thành viên |
| `.unban [id]` | Unban thành viên |
| `.nuke [tên] [nội_dung]` | Xóa và tạo lại server |
| `.bomb` | Xóa tất cả channel |
| `.deleteallroles` | Xóa tất cả role |
| `.clone_channels [id_cũ] [id_mới]` | Sao chép channel |
| `.clone_roles [id_cũ] [id_mới]` | Sao chép role |
| `.cloneemoji [emoji]` | Sao chép emoji |
| `.autoreact [on/off]` | Bật/tắt tự động phản ứng |

### Thông tin

| Lệnh | Mô tả |
|-------|--------|
| `.botinfo` | Thông tin bot |
| `.serverinfo` | Thông tin server |
| `.avatar [user]` | Xem avatar |
| `.banner [user]` | Xem banner |
| `.iplookup [ip]` | Tra cứu IP |
| `.insta [tên]` | Kiểm tra Instagram |
| `.math [phép_tính]` | Máy tính |
| `.tokencheck [token]` | Kiểm tra token |

### Giải trí

| Lệnh | Mô tả |
|-------|--------|
| `.rizz [user]` | Tán tỉnh |
| `.roast [user]` | Chế giễu |
| `.cat` | Ảnh mèo ngẫu nhiên |
| `.rainbowrole [@role]` | Role 7 màu |
| `.phcomment [user] [nội_dung]` | PornHub Comment |
| `.succac` | Lệnh giải trí |
| `.nsfw [loại]` | Lệnh NSFW (anal, hanal, 4k, gif, pussy, boobs, ass, hboobs, thighs) |

---

## Cấu trúc thư mục

```
self-bot-cam/
├── config/
│   └── config.json          # File cấu hình
├── cogs/
│   ├── cycstatus.txt         # Danh sách status cycle
│   └── nhay.txt              # Danh sách tin nhắn nháy
├── ffmpeg/
│   └── ffmpeg.exe            # FFmpeg (tự tải)
├── music/                    # Thư mục nhạc
├── trash/                    # Thư mục tạm
├── datoken.txt               # Danh sách token đa token
├── du.txt                    # File nội dung
├── ngon.txt                  # File nội dung
├── index.py                  # File cài đặt và khởi động
├── nova.py                   # File chính chứa toàn bộ code bot
├── readfirst.txt             # Hướng dẫn nhanh
├── requirements.txt          # Danh sách thư viện
└── README.md                 # Tài liệu hướng dẫn
```

---

## Yêu cầu thư viện

Xem file `requirements.txt` để biết danh sách đầy đủ. Một số thư viện chính:

- `discord.py-self` - Thư viện Discord cho self bot
- `aiohttp` - HTTP client bất đồng bộ
- `requests` - HTTP client
- `psutil` - Quản lý tiến trình
- `instaloader` - Truy cập Instagram
- `pytz` - Xử lý múi giờ
- `python-dateutil` - Xử lý ngày tháng
- `colour` - Xử lý màu sắc
- `pynacl` - Mã hóa âm thanh
- `protobuf` - Protocol Buffers

---

## Cảnh báo

1. **Self Bot vi phạm Discord ToS:** Sử dụng self bot có thể dẫn đến việc tài khoản bị khóa vĩnh viễn. Hãy cân nhắc kỹ trước khi sử dụng.

2. **Bảo mật token:** KHÔNG bao giờ chia sẻ token của bạn. Nếu token bị lộ, hãy reset ngay lập tức tại Discord Developer Portal.

3. **Sử dụng có trách nhiệm:** Tác giả không chịu trách nhiệm về任何hậu quả phát sinh từ việc sử dụng bot này. Hãy sử dụng một cách có trách nhiệm và tuân thủ pháp luật.

4. **备份dữ liệu:** Trước khi sử dụng các lệnh quản lý server (nuke, bomb, deleteallroles...), hãy đảm bảo bạn đã sao lưu dữ liệu quan trọng.

---

## Tác giả

- **vVnK** - [GitHub](https://github.com/vVnK-wh0i4m)

---

## Giấy phép

Dự án này chỉ dành cho mục đích giáo dục và giải trí. Tác giả không khuyến khích sử dụng vi phạm ToS của Discord.
