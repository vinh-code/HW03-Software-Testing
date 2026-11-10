# Task 3 – Cross-browser / Cross-platform

Thực hiện lại **checklist Task 1** trên **>= 3 nền tảng**.

## Nền tảng đã chọn

| # | Nền tảng | Công cụ | Browser/OS/Device (ghi đúng version) | Cột trong Excel |
|---|---|---|---|---|
| 1 | Chrome (desktop) | Local hoặc BrowserStack | | Status (Chrome) |
| 2 | Firefox (desktop) | | | Status (Firefox) |
| 3 | Safari **hoặc** Android Chrome **hoặc** Expo Go (điện thoại thật) | | | Status (Platform 3) |

> Expo Go trên điện thoại thật được tính là 1 trong 3 nền tảng (đề §6 Task 3).

## Quy tắc screenshot (bắt buộc)

- Thấy rõ **tên browser / OS / thiết bị** và **URL localhost** của SUT.
- Overlay **email sinh viên** (đề §6) **và** MSSV + họ tên (đề §11) → ghi cả hai để chắc.
- Đặt tên: `<platform>_<GUI-id>.png` vd `firefox_GUI-014.png`.
- Ảnh phải do bạn tự chụp, **không** để AI sinh hoặc dựng.

## Chạy SUT local trên BrowserStack/LambdaTest

BrowserStack Local / LambdaTest Tunnel để truy cập `localhost:5173` từ cloud:

```bash
# BrowserStack
./BrowserStackLocal --key <ACCESS_KEY>
# LambdaTest
./LT --user <USER> --key <ACCESS_KEY>
```
Sau đó mở `http://localhost:5173` trong phiên cloud.

## Expo Go (mobile)

1. `cd sut/frontend-mobile && npm install && npx expo start`
2. Điện thoại và máy tính cùng Wi-Fi, quét QR bằng Expo Go.
3. Sửa địa chỉ API trong app thành IP LAN của máy nếu cần (xem `sut/frontend-mobile/App.js`).

## Khác biệt giữa các nền tảng

| GUI-id | Chrome | Firefox | Platform 3 | Khác biệt / ghi chú |
|---|---|---|---|---|
