# 🔧 Hướng dẫn chỉnh sửa

Hướng dẫn tùy chỉnh và chỉnh sửa bot theo ý muốn.

---

## 📝 Đổi tên bot

Tìm trong file `nova.py`:

```python
# Dòng ~84: Đổi tên hiển thị trong code
__NAME__ = 'vVnK'

# Dòng ~256: Đổi tên hiển thị trong menu
    ✨ vVnK ✨

# Dòng ~83: Đổi version
version = '5.0.5'
```

---

## 🔄 Đổi prefix (tiền tố lệnh)

**Cách 1: Sửa trong config.json**

```json
{
    "prefix": "!"
}
```

**Cách 2: Sửa trong nova.py**

```python
# Dòng ~51
bot = commands.Bot(command_prefix='!', self_bot=True)
```

Ví dụ: prefix `!` → lệnh: `!menu`, `!spam`, `!botinfo`

---

## ➕ Thêm lệnh mới

Thêm function trong file `nova.py`:

```python
@bot.command()
async def ten_lenh(ctx, *, args=None):
    """Mô tả lệnh"""
    await ctx.message.delete()
    await ctx.send(f"# __{__NAME__}__\nNội dung phản hồi")
```

### Ví dụ: Lệnh gửi tin nhắn

```python
@bot.command()
async def hello(ctx):
    await ctx.message.delete()
    await ctx.send(f"# __{__NAME__}__\nXin chào {ctx.author.mention}! 👋")
```

### Ví dụ: Lệnh với tham số

```python
@bot.command()
async def say(ctx, *, text):
    await ctx.message.delete()
    await ctx.send(f"# __{__NAME__}__\n{text}")
```

### Ví dụ: Lệnh embed

```python
@bot.command()
async def info(ctx):
    await ctx.message.delete()
    embed = discord.Embed(
        title="Thông tin",
        description="Đây là bot vVnK",
        color=0x00ff00
    )
    embed.add_field(name="Prefix", value=prefix)
    embed.add_field(name="Version", value=version)
    await ctx.send(embed=embed)
```

---

## 🎭 Thay đổi Auto React

Trong file `nova.py`, tìm function `on_message`:

```python
@bot.event
async def on_message(message):
    if message.author == bot.user and auto_react_enabled:
        reactions = {
            'ngu': '🤣',        # Thay từ và emoji
            'oc cac': '🤣',     # Thêm bao nhiêu tùy ý
            'hello': '👋',
            'troll': '😈',
        }
        for word, emoji in reactions.items():
            if message.content.lower() == word:
                await message.add_reaction(emoji)
```

---

## ⚙️ Bật/Tắt tính năng

Trong file `nova.py`, tìm và thay đổi:

```python
# Nitro Sniper (dòng ~77)
nitro_sniper = True    # Bật
nitro_sniper = False   # Tắt

# Auto React (dòng ~75)
auto_react_enabled = True    # Bật
auto_react_enabled = False   # Tắt

# Sound Notification (dòng ~79)
sound_notification = True    # Bật
sound_notification = False   # Tắt

# Webhook Notification (dòng ~80)
webhooknotification = True    # Bật
webhooknotification = False   # Tắt
```

---

## 📝 Chỉnh sửa Cycle Status

File `cogs/cycstatus.txt` chứa danh sách status tự động chuyển:

```
Playing vVnK Bot
discord.gg/vVnK
Đang online 24/7
Hello world!
```

Mỗi dòng = 1 status, bot sẽ tự chuyển mỗi 30 giây.

---

## 📝 Chỉnh sửa tin nhắn nháy

File `cogs/nhay.txt` chứa danh sách tin nhắn spam:

```
DẬY
ALO
DẬY
```

Mỗi dòng = 1 tin nhắn, bot sẽ spam tuần tự.

---

## 🔗 Thay đổi Webhook

Trong `config/config.json`:

```json
{
    "sniper_webhook": "URL_WEBHOOK_MỚI"
}
```

Hoặc trong `nova.py`, tìm:

```python
WEBHOOK_URL = config['sniper_webhook']
```

---

## 🎵 Thêm nhạc phát voice

Đặt file nhạc (`.mp3`, `.wav`, `.ogg`) vào thư mục `music/`.

Sử dụng lệnh:

```
.xanhac [id_voice_channel] [ten_file.mp3]
```

Ví dụ:

```
.xanhac 123456789 music.mp3
```

---

## 🛡️ Thêm từ tự động react

Trong `nova.py`, tìm `on_message` event và thêm:

```python
reactions = {
    'ngu': '🤣',
    'oc cac': '🤣',
    'Thêm từ mới': 'emoji_mới',
    'hello': '👋',
    'love': '❤️',
    'fire': '🔥',
}
```

---

## 📊 Thay đổi delay mặc định

Trong `nova.py`:

```python
# Delay giữa các lần thay đổi status (dòng ~81)
changing_time = 10  # giây

# Delay spam voice
await asyncio.sleep(2)  # giây

# Delay cycle status
@tasks.loop(seconds=30)  # mỗi 30 giây
```

---

## 🎨 Đổi màu Embed

Khi gửi embed, thay đổi color:

```python
# Màu hex
color=0x00ff00   # Xanh lá
color=0xff0000   # Đỏ
color=0x0000ff   # Xanh dương
color=0xffff00   # Vàng
color=0xff00ff   # Tím

# Hoặc dùng discord.Color
color=discord.Color.green()
color=discord.Color.red()
color=discord.Color.blue()
```

---

## ⚠️ Lưu ý khi chỉnh sửa

1. **Sao lưu trước:** Luôn copy file trước khi sửa
2. **_indent đúng:** Python rất quan trọng indentation
3. **Kiểm tra syntax:** Chạy `python -m py_compile nova.py` để kiểm tra lỗi
4. **Không xóa `bot.run(token)`:** Dòng cuối cùng trong nova.py
5. **restart bot:** Sau khi sửa, cần restart bot để áp dụng

---

> Quay lại [README chính](../README.md) | Trước: [Hosting](HOSTING.md) | Tiếp: [Commands](COMMANDS.md)
