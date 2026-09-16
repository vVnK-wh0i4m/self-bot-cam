# ❓ Câu hỏi thường gặp (FAQ)

---

## 🔧 Cài đặt

### Q: Bot cần Python version nào?

**A:** Python 3.8 trở lên. Kiểm tra bằng lệnh:

```bash
python --version
```

### Q: `pip` không hoạt động?

**A:** Thử dùng:

```bash
python -m pip install -r requirements.txt
```

Hoặc cài từng thư viện:

```bash
python -m pip install discord.py-self
python -m pip install requests
python -m pip install aiohttp
```

### Q: Lỗi `No module named 'discord'`?

**A:** Cài thư viện discord.py-self:

```bash
pip install discord.py-self
```

> ⚠️ Dùng `discord.py-self`, **KHÔNG** dùng `discord.py` thường.

### Q: Lỗi `ffmpeg.exe not found`?

**A:** Tải FFmpeg tại https://ffmpeg.org/download.html và đặt `ffmpeg.exe` vào thư mục `ffmpeg/`.

---

## 🔑 Token và Config

### Q: Token Discord là gì? Lấy ở đâu?

**A:** Token là chuỗi ký tự dùng để xác thực bot.

Cách lấy:
1. Mở Discord trên trình duyệt
2. Nhấn `F12` → Tab **Network**
3. Tìm request đến `discord.com/api`
4. Copy header `Authorization`

> ⚠️ **KHÔNG** chia sẻ token. Nếu lộ, reset ngay tại https://discord.com/developers/applications

### Q: `config.json` báo lỗi?

**A:** Kiểm tra format JSON:

```json
{
    "token": "TOKEN_CỦA_BẠN",
    "prefix": ".",
    "sniper_webhook": "WEBHOOK_URL"
}
```

- Không có dấu phẩy cuối cùng
- Dùng `"` (dấu ngoặc kép), không dùng `'`
- Kiểm tra encoding: UTF-8

### Q: Webhook URL lấy ở đâu?

**A:**
1. Mở Discord → Server Settings → Integrations → Webhooks
2. Nhấn **New Webhook**
3. Đặt tên, chọn kênh
4. Nhấn **Copy Webhook URL**

---

## 🚀 Bot không hoạt động

### Q: Bot không phản hồi lệnh?

**A:** Kiểm tra:
1. Bot đã chạy chưa? (terminal không có lỗi)
2. Token có hợp lệ không?
3. Prefix có đúng không? (mặc định: `.`)
4. Bot có trong server không?

### Q: Bot chạy nhưng không hiện gì?

**A:**
- Kiểm tra terminal có thông báo `vVnK is Online` không
- Thử restart bot: `.restart`
- Kiểm tra lại token

### Q: Lỗi `401 Unauthorized`?

**A:** Token không hợp lệ hoặc đã hết hạn. Reset token tại https://discord.com/developers/applications

### Q: Bot bị disconnect liên tục?

**A:**
- Kiểm tra kết nối internet
- Có thể Discord đang rate limit. Đợi 1-2 phút rồi restart
- Kiểm tra token có bị dùng ở nơi khác không

---

## 💬 Lệnh

### Q: Lệnh không hoạt động?

**A:**
- Kiểm tra prefix (mặc định: `.`)
- Kiểm tra bot có quyền cần thiết không
- Thử `.botinfo` xem bot có chạy không

### Q: Lệnh `.spam` bị lỗi?

**A:**
- Delay phải > 0 (ví dụ: `.spam 2 Hello`)
- Nội dung không được rỗng
- Bot cần quyền **Send Messages** và **Read Message History**

### Q: Lệnh voice không hoạt động?

**A:**
- Bot cần quyền **Connect** và **Speak**
- ID voice channel phải đúng
- File nhạc phải nằm trong thư mục `music/`

### Q: Lệnh NSFW không hoạt động?

**A:**
- Chỉ dùng được trong kênh đã bật NSFW
- Kiểm tra quyền kênh

---

## 🖥️ Hosting

### Q: Bot chạy 24/7 bằng cách nào?

**A:** Dùng hosting:
- [Replit](HOSTING.md#replit) (miễn phí, có giới hạn)
- [Railway](HOSTING.md#railway) (free tier 500h/tháng)
- [VPS](HOSTING.md#vps--serverriêng) (trả phí, ổn định nhất)

### Q: Bot bị ngủ trên Replit?

**A:**
- Dùng UptimeRobot (https://uptimerobot.com) ping mỗi 5 phút
- Hoặc nâng cấp Replit paid plan

### Q: Token bị lộ khi dùng hosting?

**A:**
- Dùng Environment Variable, KHÔNG hardcode
- Reset token ngay: https://discord.com/developers/applications
- Tạo token mới và cập nhật config

---

## 🔧 Chỉnh sửa

### Q: Làm sao đổi tên bot?

**A:** Sửa trong `nova.py`:

```python
__NAME__ = 'TênMới'
```

> Xem chi tiết: [Hướng dẫn chỉnh sửa](CUSTOMIZE.md)

### Q: Làm sao thêm lệnh mới?

**A:** Thêm function trong `nova.py`:

```python
@bot.command()
async def ten_lenh(ctx):
    await ctx.message.delete()
    await ctx.send(f"# __{__NAME__}__\nNội dung")
```

> Xem chi tiết: [Hướng dẫn chỉnh sửa](CUSTOMIZE.md)

### Q: Làm sao đổi prefix?

**A:** Sửa trong `config/config.json`:

```json
{
    "prefix": "!"
}
```

---

## ❓ Vấn đề khác

### Q: Bot có an toàn không?

**A:** Self bot vi phạm ToS Discord. Sử dụng có thể bị khóa tài khoản. Hãy cân nhắc kỹ.

### Q: Bot có hỗ trợ trên điện thoại không?

**A:** Bot chạy trên máy tính/server. Không cần điện thoại.

### Q: Làm sao cập nhật bot?

**A:**

```bash
git pull origin master
```

Rồi restart bot.

### Q: Bot có thể chạy nhiều server không?

**A:** Có. Bot tự động tham gia tất cả server mà nó được invite.

---

> Quay lại [README chính](../README.md) | Trước: [Điều khoản](TERMS.md)
