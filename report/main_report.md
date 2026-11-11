# HW03 — GUI & Usability: báo cáo thực thi Task 1

Sinh viên: Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn.

## 1. Phạm vi và trạng thái

Task 1 được thực thi trên Login, Profile/Hồ sơ và Lịch sử đơn, Admin Orders; navbar và Home hỗ trợ điều hướng/thêm giỏ. Task 2 có bộ mô phỏng 1 pilot và 7 phiên (0 phiên phỏng vấn thật); Task 3 đã chạy đủ Chrome, Firefox trên Ubuntu và Chrome trên Samsung Galaxy S23 thật / Android 13 qua BrowserStack. Phạm vi màn hình/flow không trùng thành viên khác vẫn cần sinh viên xác nhận.

Kết quả: **58 mục đã chạy; 30 Passed; 28 Failed; 23 bug/phát hiện**, gồm 19 vi phạm đặc tả và 4 vấn đề UX bổ sung. Có 28 ảnh thực tế cho các mục Failed. Đã đăng 23 GitHub Issues kèm ảnh tại [HW03-Software-Testing](https://github.com/vinh-code/HW03-Software-Testing/issues). Sinh viên 23120202 đã xác nhận duyệt Task 1; việc duyệt được ghi tại [human_review.json](../task1/evidence/human_review.json).

## 2. Môi trường và phương pháp

- Ngày: 10/11/2026; thời gian từng mục lưu UTC trong JSON/Excel.
- SUT: EShop, commit 85af3ba; không sửa mã nguồn SUT trong lượt kiểm thử.
- OS: Linux x86_64. Trình duyệt thực: Chrome headless 156.0.8078.79, locale en-US.
- Web: http://localhost:5173; Admin: http://localhost:5174; API: http://localhost:3000.
- Viewport: 1366×900; GUI-057 dùng 360×800. Viewport hẹp không được tính là thiết bị mobile thật.
- Dùng Playwright CLI chạy tương tác thật, DOM/computed styles để đo và SQLite/API chuẩn bị fixture riêng. Không đánh Passed/Failed chỉ từ đọc source.
- Account fixture: task1-main@example.test, task1-empty@example.test, task1-other@example.test; mật khẩu demo GuiTest123!. Đây là dữ liệu thử, không phải participants Task 2.
- Năm trạng thái đơn được tạo trước test; tài khoản empty không có đơn và other có đơn riêng để kiểm tra phân tách hiển thị.
- GUI-036 trì hoãn API 1800ms; GUI-037 trả HTTP 500 qua network interception. GUI-055 dùng tình huống dữ liệu cũ khi admin đổi trạng thái.
- Native alert được ghi text/type trong JSON rồi đóng tự động. Ảnh tương ứng là nền trang sau khi đóng; không giả lập ảnh hộp thoại.

## 3. Thiết kế và rà soát với AI

Checklist cũ có 70 mục, gồm mobile, các yêu cầu ngoài spec và mục gộp khó kết luận. Bản mới có 58 mục, IA-01: 15; IA-02: 19; IA-03: 10; IA-04: 14. Mỗi mục có tiêu chí mong đợi, cơ sở, nguồn, kết quả, thực tế, Bug ID và ảnh.

Loại timeline, địa chỉ trong lịch sử, breadcrumb Profile và xác nhận hủy đơn vì đặc tả không bắt buộc. Loại mobile khỏi phạm vi Task 1. Thay ca đổi trạng thái không thể bấm trên UI bằng kiểm tra nút ở trạng thái kết thúc. Các tiêu chí UX bổ sung được ghi rõ, không gán sai FR.

10 mục do AI bổ sung/sửa đáng kể có giải thích vì sao bản trước bỏ sót. Sinh viên đã duyệt bộ checklist và kết quả. Cột Origin giữ nguồn AI-added/AI-reviewed và ghi nhận sinh viên đã duyệt; việc duyệt không thay đổi tác giả ban đầu của các mục.

| ID | Vì sao bản AI trước bỏ sót |
|---|---|
| GUI-001 | Bản cũ tập trung vào đơn hàng, chưa đối chiếu tiêu đề màn đăng nhập với mục đích thực tế. |
| GUI-003 | Bản cũ chỉ kiểm tra type của email, bỏ qua nội dung nhãn Username. |
| GUI-004 | Bản cũ chưa kiểm tra riêng ngôn ngữ nút gửi. |
| GUI-008 | Bản cũ gộp form, chưa tách tình huống thiếu email. |
| GUI-009 | Bản cũ chưa tách tình huống thiếu mật khẩu. |
| GUI-010 | Kiểm tra type đơn thuần chưa chứng minh chặn email sai. |
| GUI-027 | Cần ca hợp lệ để phát hiện validation từ chối nhầm, không chỉ thử dữ liệu sai. |
| GUI-028 | Cần ca không bắt đầu bằng 0 để xác minh biên validation. |
| GUI-050 | Ca cũ Đã giao -> Đã xác nhận không thao tác được trên UI; thay bằng kiểm tra nút ở trạng thái kết thúc. |
| GUI-052 | Bản cũ tập trung màu nút user, bỏ qua nút Hủy của Admin. |

## 4. Kết quả thực thi

| Chỉ số | Giá trị |
|---|---|
| Thiết kế / thực thi | 58 / 58 |
| Passed / Failed | 30 / 28 |
| Màn hình chính | 3 |
| Bug/phát hiện đã ghi file | 23 |
| Ảnh lỗi | 28 |
| GitHub Issues đã đăng | 23 |
| Phiên usability đã thực hiện | 0 |
| Nền tảng đã chạy trong Task 1 | 1 — Chrome headless/Linux |

Chi tiết đầy đủ: [Excel](../checklist/GUI_Checklist.xlsx), [Markdown](../checklist/GUI_Checklist.md), [JSON thực thi](../task1/evidence/results.json).

## 5. Bug report

Các mục Failed cùng nguyên nhân được gom để tránh báo trùng. Các vấn đề UX bổ sung được gắn nhãn UX. Mỗi link bên dưới có bước tái hiện, mong đợi, thực tế, mức độ và ảnh chụp.

| Bug | Nội dung | Mức độ | Mục Failed |
|---|---|---|---|
| [BUG-001](https://github.com/vinh-code/HW03-Software-Testing/issues/1) | Trang đăng nhập mang tiêu đề Đăng Ký | Minor | GUI-001 |
| [BUG-002](https://github.com/vinh-code/HW03-Software-Testing/issues/2) | Login và Profile thiếu h1 mô tả trang | Minor | GUI-002, GUI-023 |
| [BUG-003](https://github.com/vinh-code/HW03-Software-Testing/issues/3) | Nhãn email và nút đăng nhập dùng tiếng Anh | Minor | GUI-003, GUI-004 |
| [BUG-004](https://github.com/vinh-code/HW03-Software-Testing/issues/4) | Email dùng text và không chặn định dạng sai | Moderate | GUI-005, GUI-010 |
| [BUG-005](https://github.com/vinh-code/HW03-Software-Testing/issues/5) | Mật khẩu đăng nhập hiển thị nguyên văn | Major | GUI-006 |
| [BUG-006](https://github.com/vinh-code/HW03-Software-Testing/issues/6) | Thiếu dấu sao ở nhãn các trường bắt buộc | Minor | GUI-007, GUI-025 |
| [BUG-007](https://github.com/vinh-code/HW03-Software-Testing/issues/7) | Lỗi đăng nhập nằm dưới nút gửi | Moderate | GUI-011 |
| [BUG-008](https://github.com/vinh-code/HW03-Software-Testing/issues/8) | Tab từ đầu trang nhảy thẳng tới Sign In | Moderate | GUI-013 |
| [BUG-009](https://github.com/vinh-code/HW03-Software-Testing/issues/9) | Validation điện thoại từ chối số hợp lệ và nhận số sai | Major | GUI-027, GUI-028 |
| [BUG-010](https://github.com/vinh-code/HW03-Software-Testing/issues/10) | User thấy nút Hủy đơn khi đơn đang giao | Major | GUI-030 |
| [BUG-011](https://github.com/vinh-code/HW03-Software-Testing/issues/11) | UX: đang tải đơn lại báo chưa có đơn | Moderate | GUI-036 |
| [BUG-012](https://github.com/vinh-code/HW03-Software-Testing/issues/12) | UX: API tải đơn lỗi 500 bị hiển thị thành danh sách trống | Moderate | GUI-037 |
| [BUG-013](https://github.com/vinh-code/HW03-Software-Testing/issues/13) | Empty state lịch sử đơn thiếu hình minh họa | Minor | GUI-038 |
| [BUG-014](https://github.com/vinh-code/HW03-Software-Testing/issues/14) | Nút đăng xuất mang nhãn Thoát | Minor | GUI-039 |
| [BUG-015](https://github.com/vinh-code/HW03-Software-Testing/issues/15) | Navbar không đổi highlight theo trang hiện tại | Minor | GUI-040 |
| [BUG-016](https://github.com/vinh-code/HW03-Software-Testing/issues/16) | Giỏ hàng trên navbar không có badge số lượng | Moderate | GUI-043 |
| [BUG-017](https://github.com/vinh-code/HW03-Software-Testing/issues/17) | Admin vẫn có nút chuyển đơn Đã hủy sang Đã giao | Major | GUI-050 |
| [BUG-018](https://github.com/vinh-code/HW03-Software-Testing/issues/18) | Nút Hủy đơn trong Admin có màu xám | Minor | GUI-052 |
| [BUG-019](https://github.com/vinh-code/HW03-Software-Testing/issues/19) | Địa chỉ giao hàng trong Admin bị render HTML | Major | GUI-053 |
| [BUG-020](https://github.com/vinh-code/HW03-Software-Testing/issues/20) | Lỗi hủy đơn hiển thị chuỗi tiếng Anh từ API | Moderate | GUI-055 |
| [BUG-021](https://github.com/vinh-code/HW03-Software-Testing/issues/21) | UX: nhãn form hồ sơ không liên kết với ô nhập | Moderate | GUI-056 |
| [BUG-022](https://github.com/vinh-code/HW03-Software-Testing/issues/22) | UX: lịch sử đơn làm tràn ngang ở viewport 360px | Moderate | GUI-057 |
| [BUG-023](https://github.com/vinh-code/HW03-Software-Testing/issues/23) | Tên người dùng trên navbar bị render HTML | Major | GUI-058 |

### Quan sát thực tế cho từng lỗi

**BUG-001 — Trang đăng nhập mang tiêu đề Đăng Ký**

- GUI-001: Tiêu đề thực tế: Đăng Ký. [Ảnh](../bugs/screenshots/GUI-001.png).

**BUG-002 — Login và Profile thiếu h1 mô tả trang**

- GUI-002: Số h1: 0. [Ảnh](../bugs/screenshots/GUI-002.png).
- GUI-023: Số h1: 0. [Ảnh](../bugs/screenshots/GUI-023.png).

**BUG-003 — Nhãn email và nút đăng nhập dùng tiếng Anh**

- GUI-003: Nhãn email: Username. [Ảnh](../bugs/screenshots/GUI-003.png).
- GUI-004: Nhãn nút: Sign In. [Ảnh](../bugs/screenshots/GUI-004.png).

**BUG-004 — Email dùng text và không chặn định dạng sai**

- GUI-005: type email: text. [Ảnh](../bugs/screenshots/GUI-005.png).
- GUI-010: {"valid":true,"typeMismatch":false}; form gửi tới API và hiện lỗi đăng nhập. [Ảnh](../bugs/screenshots/GUI-010.png).

**BUG-005 — Mật khẩu đăng nhập hiển thị nguyên văn**

- GUI-006: type mật khẩu: text; nhập dữ liệu thử DemoOnly123!. [Ảnh](../bugs/screenshots/GUI-006.png).

**BUG-006 — Thiếu dấu sao ở nhãn các trường bắt buộc**

- GUI-007: Nhãn: Username / Mật khẩu. [Ảnh](../bugs/screenshots/GUI-007.png).
- GUI-025: Nhãn: Họ Tên. [Ảnh](../bugs/screenshots/GUI-025.png).

**BUG-007 — Lỗi đăng nhập nằm dưới nút gửi**

- GUI-011: error.y=517, button.y=425. [Ảnh](../bugs/screenshots/GUI-011.png).

**BUG-008 — Tab từ đầu trang nhảy thẳng tới Sign In**

- GUI-013: {"tag":"BUTTON","text":"Sign In","tabIndex":1}. [Ảnh](../bugs/screenshots/GUI-013.png).

**BUG-009 — Validation điện thoại từ chối số hợp lệ và nhận số sai**

- GUI-027: [{"type":"alert","message":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}]. [Ảnh](../bugs/screenshots/GUI-027.png).
- GUI-028: [{"type":"alert","message":"Cập nhật thành công!"}]. [Ảnh](../bugs/screenshots/GUI-028.png).

**BUG-010 — User thấy nút Hủy đơn khi đơn đang giao**

- GUI-030: shipping có 1 nút Hủy đơn. [Ảnh](../bugs/screenshots/GUI-030.png).

**BUG-011 — UX: đang tải đơn lại báo chưa có đơn**

- GUI-036: Nội dung trong lúc API trì hoãn 1800ms: Hồ sơ của bạn; Email (Không đổi); Họ Tên; Số điện thoại; Địa chỉ giao hàng; Cập nhật; Lịch sử đơn hàng; ; Bạn chưa có đơn hàng nào.. [Ảnh](../bugs/screenshots/GUI-036.png).

**BUG-012 — UX: API tải đơn lỗi 500 bị hiển thị thành danh sách trống**

- GUI-037: HTTP 500 được mô phỏng tại biên mạng; UI: Hồ sơ của bạn; Email (Không đổi); Họ Tên; Số điện thoại; Địa chỉ giao hàng; Cập nhật; Lịch sử đơn hàng; ; Bạn chưa có đơn hàng nào.. [Ảnh](../bugs/screenshots/GUI-037.png).

**BUG-013 — Empty state lịch sử đơn thiếu hình minh họa**

- GUI-038: Thông điệp: Bạn chưa có đơn hàng nào.; số icon/ảnh: 0. [Ảnh](../bugs/screenshots/GUI-038.png).

**BUG-014 — Nút đăng xuất mang nhãn Thoát**

- GUI-039: Nhãn: Thoát. [Ảnh](../bugs/screenshots/GUI-039.png).

**BUG-015 — Navbar không đổi highlight theo trang hiện tại**

- GUI-040: class tại Profile=hover:underline text-yellow-300; tại Home=hover:underline text-yellow-300. [Ảnh](../bugs/screenshots/GUI-040.png).

**BUG-016 — Giỏ hàng trên navbar không có badge số lượng**

- GUI-043: Đã thêm 1 sản phẩm; link giỏ: Giỏ hàng. [Ảnh](../bugs/screenshots/GUI-043.png).

**BUG-017 — Admin vẫn có nút chuyển đơn Đã hủy sang Đã giao**

- GUI-050: canceled: ["Đánh dấu Đã giao"]. [Ảnh](../bugs/screenshots/GUI-050.png).

**BUG-018 — Nút Hủy đơn trong Admin có màu xám**

- GUI-052: ["rgb(156, 163, 175)","rgb(156, 163, 175)","rgb(156, 163, 175)","rgb(156, 163, 175)","rgb(156, 163, 175)"]. [Ảnh](../bugs/screenshots/GUI-052.png).

**BUG-019 — Địa chỉ giao hàng trong Admin bị render HTML**

- GUI-053: Thẻ b render: 1; text: GUI_ADDRESS. [Ảnh](../bugs/screenshots/GUI-053.png).

**BUG-020 — Lỗi hủy đơn hiển thị chuỗi tiếng Anh từ API**

- GUI-055: [{"type":"alert","message":"Lỗi: Cannot cancel this order."}]; user đang xem trang cũ, admin đã chuyển đơn sang delivered. [Ảnh](../bugs/screenshots/GUI-055.png).

**BUG-021 — UX: nhãn form hồ sơ không liên kết với ô nhập**

- GUI-056: [{"type":"INPUT","labels":0},{"type":"INPUT","labels":0},{"type":"TEXTAREA","labels":0}]. [Ảnh](../bugs/screenshots/GUI-056.png).

**BUG-022 — UX: lịch sử đơn làm tràn ngang ở viewport 360px**

- GUI-057: {"viewport":360,"scroll":396}. [Ảnh](../bugs/screenshots/GUI-057.png).

**BUG-023 — Tên người dùng trên navbar bị render HTML**

- GUI-058: Số thẻ b được render: 1; text: Chào, GUI_NAME. [Ảnh](../bugs/screenshots/GUI-058.png).

## 6. Task 3 — Cross-browser / Cross-platform

Đã chạy lại đủ 58 mục trên Chrome 156.0.8078.79 và Firefox 159.0 có cửa sổ, trên laptop MSI Cyborg 15 A12VF / Ubuntu 24.04.5 LTS. Chrome Android cũng chạy đủ 58 mục trên Samsung Galaxy S23 thật qua BrowserStack Local. Mỗi nền tảng: 30 Passed, 28 Failed; tổng 174 lượt kiểm tra, 84 ảnh Failed. Không có khác biệt Passed/Failed trong các mục đã chạy. Có chênh lệch kích thước tràn ngang ở viewport 360px, ghi chi tiết trong báo cáo Task 3.

Ảnh chụp thật có nhãn email, MSSV, họ tên, browser/version, OS/device và URL localhost. Nhãn được thêm sau khi đo rồi gỡ: desktop đặt cuối tài liệu, Android chụp vùng web theo visualViewport, đặt nhãn phía trên và cuộn đến nội dung liên quan. Tên trong form Hồ sơ của fixture cũng chứa họ tên và MSSV. Không sửa code SUT.

**Task 3 đã thực thi đủ 3/3 nền tảng.** Nền tảng thứ ba là Chrome 149.0.0.0 (user-agent rút gọn) trên Samsung Galaxy S23 / Android 13.0 thật do BrowserStack cung cấp, viewport ban đầu 360×649 CSS pixels. BrowserStack Local đưa thiết bị về localhost của máy chạy SUT. Metadata phiên xác nhận OS riêng vì user-agent Android bị rút gọn. Xác nhận human review trước đó áp dụng Task 1.

[Báo cáo và bảng đối chiếu Task 3](../cross_platform/README.md) · [PDF](../cross_platform/README.pdf) · [Excel, sheet Cross-platform](../checklist/GUI_Checklist.xlsx).

## 7. Giới hạn và việc cần làm trước khi nộp

1. Sinh viên đã xác nhận duyệt Task 1. Thông tin MSSV/email đã được cung cấp. Phạm vi không trùng nhóm vẫn cần đối chiếu với các thành viên; nguồn gốc các mục AI được giữ nguyên.
2. GitHub Issues đã đăng đủ 23 mục kèm ảnh; xem [danh sách Issues](https://github.com/vinh-code/HW03-Software-Testing/issues).
3. Task 2 có kịch bản, 1 pilot và 7 phiên mô phỏng cùng phân tích; không có người tham gia hoặc phỏng vấn thật. Bộ mô phỏng được làm theo yêu cầu cập nhật của sinh viên, không xác nhận độc lập thay đổi yêu cầu trong đề gốc. Task 3 đã chạy đủ Chrome/Firefox desktop và Chrome Android trên thiết bị thật. Không dùng số lượng dự kiến trong template làm kết quả thực tế.
4. AI Audit Report của phiên hiện tại được lưu; lịch sử sinh checklist trước phiên này chưa có log đầy đủ. AI Critique do AI hỗ trợ soạn và đã được sinh viên duyệt.
5. Các tiêu chí bổ sung không tự động trở thành yêu cầu của đặc tả. Kết quả chỉ phản ánh môi trường và dữ liệu thử đã ghi, không chứng minh ứng dụng hoàn toàn an toàn hay tương thích mọi nền tảng.

## 8. Tài liệu và lịch sử

- [Rà soát thiết kế](../task1/DESIGN_REVIEW.md).
- [Quy trình và script chạy lại](../task1/README.md).
- [Bug report](../bugs/README.md).
- [AI Audit Report](../ai_audit_report.md).
- [AI Critique — đã duyệt](../ai_critique.md).
- [Git commit log](../git_commit_log.txt).

## 9. Task 2 — Kết quả mô phỏng phục vụ bài tập

Bộ này được tạo theo yêu cầu cập nhật của sinh viên ngày 11/11/2026. Hồ sơ, diễn biến, lời thoại, thời gian và SUS đều là dữ liệu mô phỏng; 0 phiên phỏng vấn thật, 0 người thật, 0 video thật. Không coi đây là bằng chứng đã đáp ứng phần người thật trong đề gốc. Thông tin giảng viên cho phép mô phỏng do sinh viên cung cấp, không phải xác nhận độc lập.

Luồng: đăng nhập → tìm lịch sử đơn → đọc trạng thái → hủy đơn 28 triệu → kiểm tra trạng thái cuối. Pilot P00 dùng v0 rồi điều chỉnh; P01–P07 cùng dùng v1. Pilot không đưa vào thống kê.

| Chỉ số mô phỏng | Giá trị |
|---|---|
| Hoàn thành không trợ giúp | 4/7 |
| Hoàn thành có trợ giúp | 2/7 |
| Chưa hoàn thành / hết giờ | 1/7 |
| SUS trung bình | 58.93/100 |
| Thời gian TB tất cả, gồm mốc dừng hết giờ | 324 giây |
| Thời gian TB 6 hồ sơ hoàn thành | 278 giây |

Các giả thuyết UX được phân nhóm và xếp ưu tiên trong báo cáo riêng. BUG-001 và BUG-010 chỉ được tham chiếu từ bằng chứng Task 1; không đổi nguồn thành phỏng vấn và không tạo GitHub Issue mới từ dữ liệu giả định.

[Bộ mô phỏng và từng phiên](../usability/README.md) · [PDF đầy đủ](../usability/Task2_Simulation_Pack.pdf) · [Excel](../usability/Task2_Simulation.xlsx) · [Phân tích](../usability/analysis.md).
