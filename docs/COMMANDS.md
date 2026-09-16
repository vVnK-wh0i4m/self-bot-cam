# 💬 Danh sách lệnh

Tất cả lệnh của vVnK Bot. Prefix mặc định: `.`

---

## 🔹 Lệnh chính

| Lệnh | Aliases | Mô tả | Ví dụ |
|-------|---------|-------|-------|
| `.menu` | - | Hiển thị bảng điều khiển | `.menu` |
| `.botinfo` | - | Thông tin chi tiết bot | `.botinfo` |
| `.serverinfo` | - | Thông tin server | `.serverinfo` |
| `.shutdown` | - | Tắt bot | `.shutdown` |
| `.restart` | `.reboot` | Khởi động lại bot | `.restart` |

---

## 👤 Quản lý tài khoản

| Lệnh | Mô tả | Ví dụ |
|-------|-------|-------|
| `.tokencheck [token]` | Kiểm tra thông tin token | `.tokencheck abc123` |
| `.checkpromo [link]` | Kiểm tra Nitro promo | `.checkpromo https://discord.com/billing/promotions/...` |
| `.closealldms` | Đóng tất cả DM | `.closealldms` |
| `.delfriends` | Xóa tất cả bạn bè | `.delfriends` |
| `.afk [lý_do]` | Bật chế độ AFK | `.afk Đang bận` |
| `.unafk` | Tắt chế độ AFK | `.unafk` |

---

## 🔄 Trạng thái

| Lệnh | Mô tả | Ví dụ |
|-------|-------|-------|
| `.cyclestatus` | Bật/tắt tự động chuyển status | `.cyclestatus` |
| `.setstatus [nội_dung]` | Đặt status tùy chỉnh | `.setstatus Playing vVnK` |
| `.addstatus [nội_dung]` | Thêm status vào danh sách cycle | `.addstatus Hello world` |
| `.clearstatus` | Xóa tất cả status | `.clearstatus` |

---

## 🎮 Rich Presence (RPC)

| Lệnh | Mô tả | Ví dụ |
|-------|-------|-------|
| `.rpc playing [tên]` | Hiển thị đang chơi game | `.rpc playing Minecraft` |
| `.rpc streaming [tên]` | Hiển thị đang stream | `.rpc streaming Just Chatting` |
| `.rpc listening [nội_dung]` | Hiển thị đang nghe | `.rpc listening Spotify` |
| `.rpc watching [nội_dung]` | Hiển thị đang xem | `.rpc watching YouTube` |
| `.stoprpc` | Dừng RPC | `.stoprpc` |

---

## 🎤 Voice Channel

| Lệnh | Mô tả | Ví dụ |
|-------|-------|-------|
| `.vcjoin [id] [M] [D] [C]` | Vào voice (Y/N) | `.vcjoin 123456 N N N` |
| `.vcleave` | Rời voice | `.vcleave` |
| `.xanhac [id] [file] [D] [C]` | Phát nhạc trong voice | `.xanhac 123456 song.mp3` |
| `.tokenvc [id]` | Treo voice đa token | `.tokenvc 123456` |
| `.tokenleave` | Dừng treo voice đa token | `.tokenleave` |
| `.vcspam [id]` | Spam join/leave voice | `.vcspam 123456` |
| `.stopvcspam` | Dừng spam voice | `.stopvcspam` |
| `.forcedisconnect [@user]` | Ngắt user khỏi voice | `.forcedisconnect @user` |
| `.stopforcedisconnect` | Dừng forced disconnect | `.stopforcedisconnect` |

> **Ghi chú:** M = Mute (Y/N), D = Deafen (Y/N), C = Camera (Y/N)

---

## 💬 Spam & Tin nhắn

| Lệnh | Mô tả | Ví dụ |
|-------|-------|-------|
| `.spam [delay] [nội_dung]` | Spam với độ trễ (giây) | `.spam 2 Xin chào` |
| `.stopspam` | Dừng spam | `.stopspam` |
| `.nhay [delay]` | Spam từ file nhay.txt | `.nhay 1.5` |
| `.stopnhay` | Dừng nháy | `.stopnhay` |
| `.webhook [url] [nội_dung]` | Spam qua webhook | `.webhook https://... Hello` |
| `.stopwebhook` | Dừng webhook spam | `.stopwebhook` |
| `.tokenspam [delay] [nội_dung]` | Spam đa token | `.tokenspam 2 Hello` |
| `.stoptokenspam` | Dừng token spam | `.stoptokenspam` |
| `.tokentreodu [delay] [file]` | Treo đú đa token | `.tokentreodu 1.5 messages.txt` |
| `.stoptreodu` | Dừng treo đú | `.stoptreodu` |
| `.massreact [số] [emoji]` | Reaction hàng loạt | `.massreact 10 👍` |
| `.clear [số]` | Xóa tin nhắn | `.clear 100` |
| `.hackclear` | Xóa chat bằng tin nhắn trống | `.hackclear` |
| `.setngon [file]` | Đặt file cho tokenspam | `.setngon messages.txt` |

---

## 🏰 Quản lý Server

| Lệnh | Mô tả | Ví dụ |
|-------|-------|-------|
| `.kick [@user]` | Kick thành viên | `.kick @user` |
| `.ban [@user]` | Ban thành viên | `.ban @user` |
| `.unban [id]` | Unban thành viên | `.unban 123456789` |
| `.nuke [tên] [nội_dung]` | Nuke server | `.nuke NewServer Hello` |
| `.bomb` | Xóa tất cả channel | `.bomb` |
| `.deleteallroles` | Xóa tất cả role | `.deleteallroles` |
| `.clone_channels [id_cũ] [id_mới]` | Clone channel | `.clone_channels 111 222` |
| `.clone_roles [id_cũ] [id_mới]` | Clone role | `.clone_roles 111 222` |
| `.cloneemoji [emoji]` | Clone emoji | `.cloneemoji :smile:` |
| `.autoreact [on/off]` | Bật/tắt auto react | `.autoreact on` |

---

## 🔧 Tiện ích

| Lệnh | Mô tả | Ví dụ |
|-------|-------|-------|
| `.avatar [@user]` | Xem avatar | `.avatar @user` |
| `.banner [@user]` | Xem banner | `.banner @user` |
| `.iplookup [ip]` | Tra cứu IP | `.iplookup 8.8.8.8` |
| `.insta [tên]` | Xem Instagram | `.insta username` |
| `.math [phép_tính]` | Máy tính | `.math 2+2` |

---

## 🎮 Giải trí

| Lệnh | Mô tả | Ví dụ |
|-------|-------|-------|
| `.rizz [@user]` | Tán tỉnh | `.rizz @user` |
| `.roast [@user]` | Chế giễu | `.roast @user` |
| `.cat` | Ảnh mèo ngẫu nhiên | `.cat` |
| `.rainbowrole [@role]` | Role 7 màu | `.rainbowrole @Role` |
| `.phcomment [@user] [nội_dung]` | PornHub Comment | `.phcomment @user Hello` |
| `.succac` | Lệnh giải trí | `.succac` |

---

## 🔞 NSFW

> ⚠️ Chỉ sử dụng trong kênh đã bật NSFW

| Lệnh | Mô tả |
|-------|--------|
| `.nsfw anal` | Ảnh anal |
| `.nsfw hanal` | Ảnh hanal |
| `.nsfw 4k` | Ảnh 4K |
| `.nsfw gif` | GIF NSFW |
| `.nsfw pussy` | Ảnh pussy |
| `.nsfw boobs` | Ảnh boobs |
| `.nsfw ass` | Ảnh ass |
| `.nsfw hboobs` | Ảnh hboobs |
| `.nsfw thighs` | Ảnh thighs |

---

## 📝 Ghi chú

- **Prefix:** `.` (có thể thay đổi trong config)
- **Delay:** Đơn vị là giây (ví dụ: `1.5` = 1.5 giây)
- **@user:** Tag người dùng bằng `@username`
- **ID:** Nhập ID số (xem bằng Developer Mode)

---

> Quay lại [README chính](../README.md) | Trước: [Chỉnh sửa](CUSTOMIZE.md) | Tiếp: [Điều khoản](TERMS.md)
