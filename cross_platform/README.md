# Task 3 — Cross-browser / Cross-platform

Sinh viên: **Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn**.

**Trạng thái: 2/3 nền tảng; chưa hoàn thành Task 3.** Đã thực thi toàn bộ 58 mục trên Chrome và Firefox. Chưa có Safari, Android Chrome hoặc Expo Go trên điện thoại thật.

## Môi trường và kết quả

| Trình duyệt | Máy / OS | Chạy | Passed | Failed | Bằng chứng |
|---|---|---|---|---|---|
| chrome 156.0.8078.79 | MSI Cyborg 15 A12VF / Ubuntu 24.04.5 LTS | 58 | 30 | 28 | [JSON](evidence/chrome.json), [ảnh](screenshots/chrome/) |
| firefox 159.0 | MSI Cyborg 15 A12VF / Ubuntu 24.04.5 LTS | 58 | 30 | 28 | [JSON](evidence/firefox.json), [ảnh](screenshots/firefox/) |
| Nền tảng 3 | Chưa có môi trường phù hợp | 0 | — | — | Not run |

Chrome là Google Chrome cài trên máy. Firefox 159.0 là bản Firefox do Playwright tải về (build v1573), chạy Gecko thật có cửa sổ; không phải đổi user-agent Chrome. Firefox hệ thống 156.0.1 không được dùng trong lượt tự động này. Cả hai chạy trên laptop thật, không phát hiện hypervisor (`systemd-detect-virt: none`). Không dùng BrowserStack/LambdaTest trong lượt này vì chưa được cung cấp tài khoản trial.

## Quy trình và tính xác thực của ảnh

- Dùng nguyên 58 tiêu chí Task 1 đã duyệt; 3 màn hình chính Login, Profile/Lịch sử đơn, Admin Orders, Home/navbar hỗ trợ thao tác.
- Mỗi trình duyệt có bộ fixture task3-* riêng theo lượt; không thay kết quả hay tài khoản fixture của Task 1. Các đơn gốc của người dùng được giữ lại.
- Viewport 1366×900; ca responsive 360×800 là kiểm tra bố cục desktop, không tính là thiết bị mobile. Locale en-US.
- Mỗi ảnh Failed được chụp trực tiếp bởi Playwright, kèm nhãn bằng chứng chứa email, MSSV, họ tên, browser/version, OS, model máy, URL localhost và UTC. Nhãn được thêm vào cuối tài liệu sau khi đo kết quả, rồi gỡ ngay; không vẽ lại giao diện hoặc chỉnh ảnh hậu kỳ.
- Form Hồ sơ của tài khoản thử chứa Họ Tên = Phạm Quang Vinh — 23120202. Các màn không có trường họ tên dùng nhãn bằng chứng.
- GUI-036/037 chủ động trì hoãn API/trả HTTP 500; native alert được ghi text vào JSON trước khi đóng. Ảnh alert là nền trang sau khi đóng, không phải ảnh hộp thoại.
- 56 ảnh Failed cho hai trình duyệt. Kết quả giữ nguyên 30 Passed/28 Failed mỗi trình duyệt.

## Đối chiếu 58 mục

| ID | IA | Chrome | Firefox | Nền tảng 3 | Bug / bằng chứng |
|---|---|---|---|---|---|
| GUI-001 | IA-01 | Failed | Failed | Not run | [BUG-001](https://github.com/vinh-code/HW03-Software-Testing/issues/1) / [ảnh chrome](screenshots/chrome/GUI-001.png) / [ảnh firefox](screenshots/firefox/GUI-001.png) |
| GUI-002 | IA-01 | Failed | Failed | Not run | [BUG-002](https://github.com/vinh-code/HW03-Software-Testing/issues/2) / [ảnh chrome](screenshots/chrome/GUI-002.png) / [ảnh firefox](screenshots/firefox/GUI-002.png) |
| GUI-003 | IA-01 | Failed | Failed | Not run | [BUG-003](https://github.com/vinh-code/HW03-Software-Testing/issues/3) / [ảnh chrome](screenshots/chrome/GUI-003.png) / [ảnh firefox](screenshots/firefox/GUI-003.png) |
| GUI-004 | IA-01 | Failed | Failed | Not run | [BUG-003](https://github.com/vinh-code/HW03-Software-Testing/issues/3) / [ảnh chrome](screenshots/chrome/GUI-004.png) / [ảnh firefox](screenshots/firefox/GUI-004.png) |
| GUI-005 | IA-02 | Failed | Failed | Not run | [BUG-004](https://github.com/vinh-code/HW03-Software-Testing/issues/4) / [ảnh chrome](screenshots/chrome/GUI-005.png) / [ảnh firefox](screenshots/firefox/GUI-005.png) |
| GUI-006 | IA-02 | Failed | Failed | Not run | [BUG-005](https://github.com/vinh-code/HW03-Software-Testing/issues/5) / [ảnh chrome](screenshots/chrome/GUI-006.png) / [ảnh firefox](screenshots/firefox/GUI-006.png) |
| GUI-007 | IA-02 | Failed | Failed | Not run | [BUG-006](https://github.com/vinh-code/HW03-Software-Testing/issues/6) / [ảnh chrome](screenshots/chrome/GUI-007.png) / [ảnh firefox](screenshots/firefox/GUI-007.png) |
| GUI-008 | IA-02 | Passed | Passed | Not run |  |
| GUI-009 | IA-02 | Passed | Passed | Not run |  |
| GUI-010 | IA-02 | Failed | Failed | Not run | [BUG-004](https://github.com/vinh-code/HW03-Software-Testing/issues/4) / [ảnh chrome](screenshots/chrome/GUI-010.png) / [ảnh firefox](screenshots/firefox/GUI-010.png) |
| GUI-011 | IA-02 | Failed | Failed | Not run | [BUG-007](https://github.com/vinh-code/HW03-Software-Testing/issues/7) / [ảnh chrome](screenshots/chrome/GUI-011.png) / [ảnh firefox](screenshots/firefox/GUI-011.png) |
| GUI-012 | IA-04 | Passed | Passed | Not run |  |
| GUI-013 | IA-01 | Failed | Failed | Not run | [BUG-008](https://github.com/vinh-code/HW03-Software-Testing/issues/8) / [ảnh chrome](screenshots/chrome/GUI-013.png) / [ảnh firefox](screenshots/firefox/GUI-013.png) |
| GUI-014 | IA-03 | Passed | Passed | Not run |  |
| GUI-015 | IA-03 | Passed | Passed | Not run |  |
| GUI-016 | IA-02 | Passed | Passed | Not run |  |
| GUI-017 | IA-01 | Passed | Passed | Not run |  |
| GUI-018 | IA-01 | Passed | Passed | Not run |  |
| GUI-019 | IA-01 | Passed | Passed | Not run |  |
| GUI-020 | IA-01 | Passed | Passed | Not run |  |
| GUI-021 | IA-01 | Passed | Passed | Not run |  |
| GUI-022 | IA-01 | Passed | Passed | Not run |  |
| GUI-023 | IA-01 | Failed | Failed | Not run | [BUG-002](https://github.com/vinh-code/HW03-Software-Testing/issues/2) / [ảnh chrome](screenshots/chrome/GUI-023.png) / [ảnh firefox](screenshots/firefox/GUI-023.png) |
| GUI-024 | IA-02 | Passed | Passed | Not run |  |
| GUI-025 | IA-02 | Failed | Failed | Not run | [BUG-006](https://github.com/vinh-code/HW03-Software-Testing/issues/6) / [ảnh chrome](screenshots/chrome/GUI-025.png) / [ảnh firefox](screenshots/firefox/GUI-025.png) |
| GUI-026 | IA-02 | Passed | Passed | Not run |  |
| GUI-027 | IA-02 | Failed | Failed | Not run | [BUG-009](https://github.com/vinh-code/HW03-Software-Testing/issues/9) / [ảnh chrome](screenshots/chrome/GUI-027.png) / [ảnh firefox](screenshots/firefox/GUI-027.png) |
| GUI-028 | IA-02 | Failed | Failed | Not run | [BUG-009](https://github.com/vinh-code/HW03-Software-Testing/issues/9) / [ảnh chrome](screenshots/chrome/GUI-028.png) / [ảnh firefox](screenshots/firefox/GUI-028.png) |
| GUI-029 | IA-04 | Passed | Passed | Not run |  |
| GUI-030 | IA-04 | Failed | Failed | Not run | [BUG-010](https://github.com/vinh-code/HW03-Software-Testing/issues/10) / [ảnh chrome](screenshots/chrome/GUI-030.png) / [ảnh firefox](screenshots/firefox/GUI-030.png) |
| GUI-031 | IA-04 | Passed | Passed | Not run |  |
| GUI-032 | IA-04 | Passed | Passed | Not run |  |
| GUI-033 | IA-04 | Passed | Passed | Not run |  |
| GUI-034 | IA-03 | Passed | Passed | Not run |  |
| GUI-035 | IA-04 | Passed | Passed | Not run |  |
| GUI-036 | IA-04 | Failed | Failed | Not run | [BUG-011](https://github.com/vinh-code/HW03-Software-Testing/issues/11) / [ảnh chrome](screenshots/chrome/GUI-036.png) / [ảnh firefox](screenshots/firefox/GUI-036.png) |
| GUI-037 | IA-04 | Failed | Failed | Not run | [BUG-012](https://github.com/vinh-code/HW03-Software-Testing/issues/12) / [ảnh chrome](screenshots/chrome/GUI-037.png) / [ảnh firefox](screenshots/firefox/GUI-037.png) |
| GUI-038 | IA-04 | Failed | Failed | Not run | [BUG-013](https://github.com/vinh-code/HW03-Software-Testing/issues/13) / [ảnh chrome](screenshots/chrome/GUI-038.png) / [ảnh firefox](screenshots/firefox/GUI-038.png) |
| GUI-039 | IA-03 | Failed | Failed | Not run | [BUG-014](https://github.com/vinh-code/HW03-Software-Testing/issues/14) / [ảnh chrome](screenshots/chrome/GUI-039.png) / [ảnh firefox](screenshots/firefox/GUI-039.png) |
| GUI-040 | IA-03 | Failed | Failed | Not run | [BUG-015](https://github.com/vinh-code/HW03-Software-Testing/issues/15) / [ảnh chrome](screenshots/chrome/GUI-040.png) / [ảnh firefox](screenshots/firefox/GUI-040.png) |
| GUI-041 | IA-03 | Passed | Passed | Not run |  |
| GUI-042 | IA-03 | Passed | Passed | Not run |  |
| GUI-043 | IA-03 | Failed | Failed | Not run | [BUG-016](https://github.com/vinh-code/HW03-Software-Testing/issues/16) / [ảnh chrome](screenshots/chrome/GUI-043.png) / [ảnh firefox](screenshots/firefox/GUI-043.png) |
| GUI-044 | IA-03 | Passed | Passed | Not run |  |
| GUI-045 | IA-01 | Passed | Passed | Not run |  |
| GUI-046 | IA-02 | Passed | Passed | Not run |  |
| GUI-047 | IA-02 | Passed | Passed | Not run |  |
| GUI-048 | IA-02 | Passed | Passed | Not run |  |
| GUI-049 | IA-02 | Passed | Passed | Not run |  |
| GUI-050 | IA-02 | Failed | Failed | Not run | [BUG-017](https://github.com/vinh-code/HW03-Software-Testing/issues/17) / [ảnh chrome](screenshots/chrome/GUI-050.png) / [ảnh firefox](screenshots/firefox/GUI-050.png) |
| GUI-051 | IA-03 | Passed | Passed | Not run |  |
| GUI-052 | IA-01 | Failed | Failed | Not run | [BUG-018](https://github.com/vinh-code/HW03-Software-Testing/issues/18) / [ảnh chrome](screenshots/chrome/GUI-052.png) / [ảnh firefox](screenshots/firefox/GUI-052.png) |
| GUI-053 | IA-04 | Failed | Failed | Not run | [BUG-019](https://github.com/vinh-code/HW03-Software-Testing/issues/19) / [ảnh chrome](screenshots/chrome/GUI-053.png) / [ảnh firefox](screenshots/firefox/GUI-053.png) |
| GUI-054 | IA-04 | Passed | Passed | Not run |  |
| GUI-055 | IA-04 | Failed | Failed | Not run | [BUG-020](https://github.com/vinh-code/HW03-Software-Testing/issues/20) / [ảnh chrome](screenshots/chrome/GUI-055.png) / [ảnh firefox](screenshots/firefox/GUI-055.png) |
| GUI-056 | IA-02 | Failed | Failed | Not run | [BUG-021](https://github.com/vinh-code/HW03-Software-Testing/issues/21) / [ảnh chrome](screenshots/chrome/GUI-056.png) / [ảnh firefox](screenshots/firefox/GUI-056.png) |
| GUI-057 | IA-01 | Failed | Failed | Not run | [BUG-022](https://github.com/vinh-code/HW03-Software-Testing/issues/22) / [ảnh chrome](screenshots/chrome/GUI-057.png) / [ảnh firefox](screenshots/firefox/GUI-057.png) |
| GUI-058 | IA-04 | Failed | Failed | Not run | [BUG-023](https://github.com/vinh-code/HW03-Software-Testing/issues/23) / [ảnh chrome](screenshots/chrome/GUI-058.png) / [ảnh firefox](screenshots/firefox/GUI-058.png) |

## Khác biệt quan sát được

Không có khác biệt Passed/Failed trong 58 mục giữa hai môi trường đã chạy. Điều này không chứng minh ứng dụng tương thích mọi nền tảng. Browser validation message và kích thước render có thể khác; số đo thực tế lưu trong JSON.

| Mục | Chrome | Firefox | Ý nghĩa |
|---|---|---|---|
| GUI-011 | error.y=516, button.y=424 | error.y=516, button.y=424 | Cùng kết luận Failed |
| GUI-013 | {"tag":"BUTTON","text":"Sign In","tabIndex":1} | {"tag":"BUTTON","text":"Sign In","tabIndex":1} | Cùng kết luận Failed |
| GUI-057 | {"viewport":360,"scroll":392} | {"viewport":360,"scroll":394} | Cùng kết luận Failed |

Các mục Failed tiếp tục ánh xạ vào 23 Issues hiện có; không tạo Issues trùng cho cùng lỗi.

## Phần còn thiếu

Cần chạy cùng checklist trên Safari thật (ví dụ qua BrowserStack/LambdaTest hoặc máy Mac), Chrome trên Android thật, hoặc Expo Go trên điện thoại thật. Playwright WebKit trên Linux và Chrome giả lập kích thước điện thoại không được tính thành Safari/Android. Khi có môi trường thứ ba, ghi rõ các mục tương ứng và bằng chứng thực tế trước khi cập nhật trạng thái hoàn tất.

## Chạy lại

Từ HW03 root, với các server :3000, :5173, :5174 đang chạy:

```bash
python3 submission/cross_platform/scripts/run_platform.py chrome
python3 submission/cross_platform/scripts/run_platform.py firefox
python3 submission/cross_platform/scripts/build_report.py
python3 submission/checklist/build_checklist.py
```

Script chỉ dùng task3-* fixtures; backup trước khi chạy. Không khởi động lại backend nếu chưa backup vì database.js reset dữ liệu khi import. Không chạy song song hai trình duyệt do fixture DB dùng chung.

Nguồn checklist và bằng chứng Task 1 được giữ nguyên. Xác nhận duyệt trước đó là cho Task 1; báo cáo này ghi nhận các lượt chạy Task 3 mới.
