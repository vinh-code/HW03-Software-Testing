# Task 3 — Cross-browser / Cross-platform

Sinh viên: **Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn**.

**Trạng thái: 3/3 nền tảng; đã thực thi đủ ba nền tảng.**

## Môi trường và kết quả

| Trình duyệt | Máy / OS | Chạy | Passed | Failed | Bằng chứng |
|---|---|---|---|---|---|
| chrome 156.0.8078.79 | Cyborg 15 A12VF / Ubuntu 24.04.5 LTS | 58 | 30 | 28 | [JSON](evidence/chrome.json), [ảnh](screenshots/chrome/) |
| firefox 159.0 | Cyborg 15 A12VF / Ubuntu 24.04.5 LTS | 58 | 30 | 28 | [JSON](evidence/firefox.json), [ảnh](screenshots/firefox/) |
| android 149.0.0.0 | SM-S911B / Android 13.0 | 58 | 30 | 28 | [JSON](evidence/android.json), [ảnh](screenshots/android/) |

Chrome desktop dùng bản Google Chrome cài trên laptop MSI Cyborg 15 A12VF/Ubuntu. Firefox 159.0 là bản Gecko thật do Playwright tải về (build v1573), chạy có cửa sổ; không phải thay user-agent Chrome. Firefox hệ thống 156.0.1 không được dùng trong lượt tự động này.

Android chạy trên **Samsung Galaxy S23 thật (SM-S911B), Android 13.0**, được BrowserStack cấp cho tài khoản Free. [Phiên BrowserStack](https://automate.browserstack.com/builds/9c1d8829c902315882382e5d229eb28f2ea0d61e/sessions/b06eaac904738242824ca68b189c12e4aadac03d) · [Metadata phiên](evidence/android_session.json).

Trạng thái session passed trên BrowserStack chỉ xác nhận script hoàn tất; 28 mục ứng dụng Failed vẫn được ghi đầy đủ trong JSON/Excel.

BrowserStack Local kết nối thiết bị về EShop trên máy người làm bài; ảnh ghi URL localhost thật. User-agent Chrome bị rút gọn thành Android 10/K và version 149.0.0.0; OS Android 13.0 được xác nhận riêng bằng metadata phiên BrowserStack. Không dùng user-agent rút gọn để suy ra phiên bản OS.

## Quy trình và tính xác thực của ảnh

- Dùng 58 tiêu chí Task 1 đã duyệt; Login, Profile/Lịch sử đơn, Admin Orders; Home/navbar hỗ trợ thao tác.
- Mỗi lượt tạo dữ liệu task3-*; không thay bằng chứng hoặc fixture task1-* và không sửa source SUT.
- Desktop dùng viewport 1366×900; GUI-057 kiểm tra 360×800. Android giữ viewport do thiết bị cung cấp (ban đầu 360×649 CSS pixels, DPR 3), không ép thành desktop.
- Ảnh được chụp trực tiếp từ trình duyệt. Desktop chụp toàn trang với nhãn metadata ở cuối tài liệu. Android chụp vùng web trực tiếp từ Chrome, giới hạn theo visualViewport để tránh lỗi ghép ảnh khi trang tràn ngang; cuộn tới phần liên quan và đặt nhãn phía trên với khoảng đệm. Ảnh không bao gồm popup riêng của Chrome (lưu mật khẩu/thông báo khởi động). Ảnh màn hình thiết bị được dùng khi chẩn đoán, không thay thế ảnh bằng chứng cuối. Nhãn có email/MSSV/họ tên/browser/version/OS/device/URL/UTC, được thêm sau khi đo rồi gỡ ngay; không dựng lại UI hay sửa ảnh hậu kỳ.
- Form Hồ sơ fixture có Họ Tên = Phạm Quang Vinh — 23120202. Native alert được ghi text vào JSON rồi đóng; ảnh tương ứng là nền trang, không phải hộp thoại.
- GUI-036/037 dùng fault injection trì hoãn API/HTTP 500. Desktop trì hoãn 1800ms; Android giữ response đến sau khi đo/chụp để độ trễ cloud không làm mất trạng thái loading. GUI-013/016 dùng phím do automation gửi; trên Android đây là hỗ trợ bàn phím, không phải đánh giá bàn phím cảm ứng.
- Cho phép local-network-access riêng cho localhost:5173/5174 để Chrome kết nối BrowserStack Local. Android tap điều chỉnh theo visualViewport offset; GUI-057 so scrollWidth với visualViewport.width 360px vì layout viewport tự nới khi tràn ngang. Lỗi khởi tạo cloud hoặc timeout tự động hóa được sửa/tách khỏi lỗi SUT; không tính chúng thành Failed của ứng dụng.

Tổng lượt kiểm tra: **174**. Tổng ảnh Failed: **84**.

## Đối chiếu 58 mục

| ID | IA | Chrome | Firefox | Android Chrome | Bug / ảnh |
|---|---|---|---|---|---|
| GUI-001 | IA-01 | Failed | Failed | Failed | [BUG-001](https://github.com/vinh-code/HW03-Software-Testing/issues/1) / [ảnh chrome](screenshots/chrome/GUI-001.png) / [ảnh firefox](screenshots/firefox/GUI-001.png) / [ảnh android](screenshots/android/GUI-001.png) |
| GUI-002 | IA-01 | Failed | Failed | Failed | [BUG-002](https://github.com/vinh-code/HW03-Software-Testing/issues/2) / [ảnh chrome](screenshots/chrome/GUI-002.png) / [ảnh firefox](screenshots/firefox/GUI-002.png) / [ảnh android](screenshots/android/GUI-002.png) |
| GUI-003 | IA-01 | Failed | Failed | Failed | [BUG-003](https://github.com/vinh-code/HW03-Software-Testing/issues/3) / [ảnh chrome](screenshots/chrome/GUI-003.png) / [ảnh firefox](screenshots/firefox/GUI-003.png) / [ảnh android](screenshots/android/GUI-003.png) |
| GUI-004 | IA-01 | Failed | Failed | Failed | [BUG-003](https://github.com/vinh-code/HW03-Software-Testing/issues/3) / [ảnh chrome](screenshots/chrome/GUI-004.png) / [ảnh firefox](screenshots/firefox/GUI-004.png) / [ảnh android](screenshots/android/GUI-004.png) |
| GUI-005 | IA-02 | Failed | Failed | Failed | [BUG-004](https://github.com/vinh-code/HW03-Software-Testing/issues/4) / [ảnh chrome](screenshots/chrome/GUI-005.png) / [ảnh firefox](screenshots/firefox/GUI-005.png) / [ảnh android](screenshots/android/GUI-005.png) |
| GUI-006 | IA-02 | Failed | Failed | Failed | [BUG-005](https://github.com/vinh-code/HW03-Software-Testing/issues/5) / [ảnh chrome](screenshots/chrome/GUI-006.png) / [ảnh firefox](screenshots/firefox/GUI-006.png) / [ảnh android](screenshots/android/GUI-006.png) |
| GUI-007 | IA-02 | Failed | Failed | Failed | [BUG-006](https://github.com/vinh-code/HW03-Software-Testing/issues/6) / [ảnh chrome](screenshots/chrome/GUI-007.png) / [ảnh firefox](screenshots/firefox/GUI-007.png) / [ảnh android](screenshots/android/GUI-007.png) |
| GUI-008 | IA-02 | Passed | Passed | Passed |  |
| GUI-009 | IA-02 | Passed | Passed | Passed |  |
| GUI-010 | IA-02 | Failed | Failed | Failed | [BUG-004](https://github.com/vinh-code/HW03-Software-Testing/issues/4) / [ảnh chrome](screenshots/chrome/GUI-010.png) / [ảnh firefox](screenshots/firefox/GUI-010.png) / [ảnh android](screenshots/android/GUI-010.png) |
| GUI-011 | IA-02 | Failed | Failed | Failed | [BUG-007](https://github.com/vinh-code/HW03-Software-Testing/issues/7) / [ảnh chrome](screenshots/chrome/GUI-011.png) / [ảnh firefox](screenshots/firefox/GUI-011.png) / [ảnh android](screenshots/android/GUI-011.png) |
| GUI-012 | IA-04 | Passed | Passed | Passed |  |
| GUI-013 | IA-01 | Failed | Failed | Failed | [BUG-008](https://github.com/vinh-code/HW03-Software-Testing/issues/8) / [ảnh chrome](screenshots/chrome/GUI-013.png) / [ảnh firefox](screenshots/firefox/GUI-013.png) / [ảnh android](screenshots/android/GUI-013.png) |
| GUI-014 | IA-03 | Passed | Passed | Passed |  |
| GUI-015 | IA-03 | Passed | Passed | Passed |  |
| GUI-016 | IA-02 | Passed | Passed | Passed |  |
| GUI-017 | IA-01 | Passed | Passed | Passed |  |
| GUI-018 | IA-01 | Passed | Passed | Passed |  |
| GUI-019 | IA-01 | Passed | Passed | Passed |  |
| GUI-020 | IA-01 | Passed | Passed | Passed |  |
| GUI-021 | IA-01 | Passed | Passed | Passed |  |
| GUI-022 | IA-01 | Passed | Passed | Passed |  |
| GUI-023 | IA-01 | Failed | Failed | Failed | [BUG-002](https://github.com/vinh-code/HW03-Software-Testing/issues/2) / [ảnh chrome](screenshots/chrome/GUI-023.png) / [ảnh firefox](screenshots/firefox/GUI-023.png) / [ảnh android](screenshots/android/GUI-023.png) |
| GUI-024 | IA-02 | Passed | Passed | Passed |  |
| GUI-025 | IA-02 | Failed | Failed | Failed | [BUG-006](https://github.com/vinh-code/HW03-Software-Testing/issues/6) / [ảnh chrome](screenshots/chrome/GUI-025.png) / [ảnh firefox](screenshots/firefox/GUI-025.png) / [ảnh android](screenshots/android/GUI-025.png) |
| GUI-026 | IA-02 | Passed | Passed | Passed |  |
| GUI-027 | IA-02 | Failed | Failed | Failed | [BUG-009](https://github.com/vinh-code/HW03-Software-Testing/issues/9) / [ảnh chrome](screenshots/chrome/GUI-027.png) / [ảnh firefox](screenshots/firefox/GUI-027.png) / [ảnh android](screenshots/android/GUI-027.png) |
| GUI-028 | IA-02 | Failed | Failed | Failed | [BUG-009](https://github.com/vinh-code/HW03-Software-Testing/issues/9) / [ảnh chrome](screenshots/chrome/GUI-028.png) / [ảnh firefox](screenshots/firefox/GUI-028.png) / [ảnh android](screenshots/android/GUI-028.png) |
| GUI-029 | IA-04 | Passed | Passed | Passed |  |
| GUI-030 | IA-04 | Failed | Failed | Failed | [BUG-010](https://github.com/vinh-code/HW03-Software-Testing/issues/10) / [ảnh chrome](screenshots/chrome/GUI-030.png) / [ảnh firefox](screenshots/firefox/GUI-030.png) / [ảnh android](screenshots/android/GUI-030.png) |
| GUI-031 | IA-04 | Passed | Passed | Passed |  |
| GUI-032 | IA-04 | Passed | Passed | Passed |  |
| GUI-033 | IA-04 | Passed | Passed | Passed |  |
| GUI-034 | IA-03 | Passed | Passed | Passed |  |
| GUI-035 | IA-04 | Passed | Passed | Passed |  |
| GUI-036 | IA-04 | Failed | Failed | Failed | [BUG-011](https://github.com/vinh-code/HW03-Software-Testing/issues/11) / [ảnh chrome](screenshots/chrome/GUI-036.png) / [ảnh firefox](screenshots/firefox/GUI-036.png) / [ảnh android](screenshots/android/GUI-036.png) |
| GUI-037 | IA-04 | Failed | Failed | Failed | [BUG-012](https://github.com/vinh-code/HW03-Software-Testing/issues/12) / [ảnh chrome](screenshots/chrome/GUI-037.png) / [ảnh firefox](screenshots/firefox/GUI-037.png) / [ảnh android](screenshots/android/GUI-037.png) |
| GUI-038 | IA-04 | Failed | Failed | Failed | [BUG-013](https://github.com/vinh-code/HW03-Software-Testing/issues/13) / [ảnh chrome](screenshots/chrome/GUI-038.png) / [ảnh firefox](screenshots/firefox/GUI-038.png) / [ảnh android](screenshots/android/GUI-038.png) |
| GUI-039 | IA-03 | Failed | Failed | Failed | [BUG-014](https://github.com/vinh-code/HW03-Software-Testing/issues/14) / [ảnh chrome](screenshots/chrome/GUI-039.png) / [ảnh firefox](screenshots/firefox/GUI-039.png) / [ảnh android](screenshots/android/GUI-039.png) |
| GUI-040 | IA-03 | Failed | Failed | Failed | [BUG-015](https://github.com/vinh-code/HW03-Software-Testing/issues/15) / [ảnh chrome](screenshots/chrome/GUI-040.png) / [ảnh firefox](screenshots/firefox/GUI-040.png) / [ảnh android](screenshots/android/GUI-040.png) |
| GUI-041 | IA-03 | Passed | Passed | Passed |  |
| GUI-042 | IA-03 | Passed | Passed | Passed |  |
| GUI-043 | IA-03 | Failed | Failed | Failed | [BUG-016](https://github.com/vinh-code/HW03-Software-Testing/issues/16) / [ảnh chrome](screenshots/chrome/GUI-043.png) / [ảnh firefox](screenshots/firefox/GUI-043.png) / [ảnh android](screenshots/android/GUI-043.png) |
| GUI-044 | IA-03 | Passed | Passed | Passed |  |
| GUI-045 | IA-01 | Passed | Passed | Passed |  |
| GUI-046 | IA-02 | Passed | Passed | Passed |  |
| GUI-047 | IA-02 | Passed | Passed | Passed |  |
| GUI-048 | IA-02 | Passed | Passed | Passed |  |
| GUI-049 | IA-02 | Passed | Passed | Passed |  |
| GUI-050 | IA-02 | Failed | Failed | Failed | [BUG-017](https://github.com/vinh-code/HW03-Software-Testing/issues/17) / [ảnh chrome](screenshots/chrome/GUI-050.png) / [ảnh firefox](screenshots/firefox/GUI-050.png) / [ảnh android](screenshots/android/GUI-050.png) |
| GUI-051 | IA-03 | Passed | Passed | Passed |  |
| GUI-052 | IA-01 | Failed | Failed | Failed | [BUG-018](https://github.com/vinh-code/HW03-Software-Testing/issues/18) / [ảnh chrome](screenshots/chrome/GUI-052.png) / [ảnh firefox](screenshots/firefox/GUI-052.png) / [ảnh android](screenshots/android/GUI-052.png) |
| GUI-053 | IA-04 | Failed | Failed | Failed | [BUG-019](https://github.com/vinh-code/HW03-Software-Testing/issues/19) / [ảnh chrome](screenshots/chrome/GUI-053.png) / [ảnh firefox](screenshots/firefox/GUI-053.png) / [ảnh android](screenshots/android/GUI-053.png) |
| GUI-054 | IA-04 | Passed | Passed | Passed |  |
| GUI-055 | IA-04 | Failed | Failed | Failed | [BUG-020](https://github.com/vinh-code/HW03-Software-Testing/issues/20) / [ảnh chrome](screenshots/chrome/GUI-055.png) / [ảnh firefox](screenshots/firefox/GUI-055.png) / [ảnh android](screenshots/android/GUI-055.png) |
| GUI-056 | IA-02 | Failed | Failed | Failed | [BUG-021](https://github.com/vinh-code/HW03-Software-Testing/issues/21) / [ảnh chrome](screenshots/chrome/GUI-056.png) / [ảnh firefox](screenshots/firefox/GUI-056.png) / [ảnh android](screenshots/android/GUI-056.png) |
| GUI-057 | IA-01 | Failed | Failed | Failed | [BUG-022](https://github.com/vinh-code/HW03-Software-Testing/issues/22) / [ảnh chrome](screenshots/chrome/GUI-057.png) / [ảnh firefox](screenshots/firefox/GUI-057.png) / [ảnh android](screenshots/android/GUI-057.png) |
| GUI-058 | IA-04 | Failed | Failed | Failed | [BUG-023](https://github.com/vinh-code/HW03-Software-Testing/issues/23) / [ảnh chrome](screenshots/chrome/GUI-058.png) / [ảnh firefox](screenshots/firefox/GUI-058.png) / [ảnh android](screenshots/android/GUI-058.png) |

## Khác biệt quan sát được

Có **0 mục khác biệt Passed/Failed** giữa các lượt chạy. Kết quả chỉ áp dụng cho những môi trường và dữ liệu đã ghi.


| Mục | Chrome | Firefox | Android |
|---|---|---|---|
| GUI-011 | error.y=516, button.y=424 | error.y=516, button.y=424 | error.y=517, button.y=425 |
| GUI-013 | {"tag":"BUTTON","text":"Sign In","tabIndex":1} | {"tag":"BUTTON","text":"Sign In","tabIndex":1} | {"tag":"BUTTON","text":"Sign In","tabIndex":1} |
| GUI-057 | {"viewport":360,"scroll":392} | {"viewport":360,"scroll":394} | {"viewport":360,"layoutViewport":403,"scroll":403} |

Các lượt dùng ID đơn hàng tự tăng khác nhau. Số đo độ rộng là quan sát theo từng fixture, không chứng minh chênh lệch do riêng engine trình duyệt.

Các lỗi cùng nguyên nhân ánh xạ vào Issues hiện có; không tạo báo cáo trùng chỉ vì cùng lỗi xuất hiện trên trình duyệt khác.

## Chạy lại

Từ HW03 root, sau khi backup SQLite và với các server :3000, :5173, :5174 đang chạy:

```bash
python3 submission/cross_platform/scripts/run_platform.py chrome
python3 submission/cross_platform/scripts/run_platform.py firefox
node submission/cross_platform/scripts/run_browserstack_android.cjs
python3 submission/cross_platform/scripts/build_report.py
python3 submission/checklist/build_checklist.py
```

Android cần tài khoản BrowserStack có quyền Automate/Android và BrowserStack Local. Runner dùng playwright-core 1.62.0 cùng browserstack-local trong ~/.cache/hw03-browserstack/runtime/node_modules, binary BrowserStackLocal trong ~/.cache/hw03-browserstack, và credentials.json riêng có username/access_key (quyền file 600). Thông tin xác thực nằm trong private cache của người dùng, không đưa vào repository. Không chạy song song các lượt vì dùng chung DB fixture. Không khởi động lại backend trước khi backup: database.js reset dữ liệu khi import.

Tài liệu cấu hình: [BrowserStack Playwright Android](https://www.browserstack.com/docs/automate/playwright/playwright-android/nodejs), [Local Testing](https://www.browserstack.com/docs/automate/playwright/local-testing/introduction).

Xác nhận duyệt trước đó áp dụng Task 1. Task 3 là các lượt chạy mới, ghi nhận bằng chứng thực tế và không giả định đã được duyệt lại.
