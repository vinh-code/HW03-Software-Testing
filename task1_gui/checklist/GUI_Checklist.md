# Task 1 — GUI checklist đã thực thi

58 mục; Chrome headless 156.0.8078.79 / Linux. 30 Passed, 28 Failed. Kết quả Firefox và nền tảng 3 xem sheet Cross-platform và báo cáo Task 3.

Sinh viên 23120202 đã xác nhận duyệt Task 1. Origin AI-reviewed/AI-added vẫn ghi nguồn AI; xem task1/evidence/human_review.json.

| ID | IA | Màn hình | Mong đợi / Cơ sở | Kết quả | Thực tế | Bug / ảnh |
|---|---|---|---|---|---|---|
| GUI-001 | IA-01 | Login | Tiêu đề trang mô tả đúng chức năng Đăng nhập — FR-21 | Failed | Tiêu đề thực tế: Đăng Ký | [BUG-001](../bugs/BUG-001.md) / [ảnh](../bugs/screenshots/GUI-001.png) |
| GUI-002 | IA-01 | Login | Có đúng một h1 mô tả trang — FR-21 | Failed | Số h1: 0 | [BUG-002](../bugs/BUG-002.md) / [ảnh](../bugs/screenshots/GUI-002.png) |
| GUI-003 | IA-01 | Login | Nhãn trường email bằng tiếng Việt và đúng nội dung — FR-21 | Failed | Nhãn email: Username | [BUG-003](../bugs/BUG-003.md) / [ảnh](../bugs/screenshots/GUI-003.png) |
| GUI-004 | IA-01 | Login | Nút gửi có nhãn Đăng nhập bằng tiếng Việt — FR-21 | Failed | Nhãn nút: Sign In | [BUG-003](../bugs/BUG-003.md) / [ảnh](../bugs/screenshots/GUI-004.png) |
| GUI-005 | IA-02 | Login | Email dùng type=email — FR-02, FR-22 | Failed | type email: text | [BUG-004](../bugs/BUG-004.md) / [ảnh](../bugs/screenshots/GUI-005.png) |
| GUI-006 | IA-02 | Login | Mật khẩu dùng type=password — FR-22 | Failed | type mật khẩu: text; nhập dữ liệu thử DemoOnly123! | [BUG-005](../bugs/BUG-005.md) / [ảnh](../bugs/screenshots/GUI-006.png) |
| GUI-007 | IA-02 | Login | Hai trường bắt buộc có dấu * ở nhãn — FR-22 | Failed | Nhãn: Username / Mật khẩu | [BUG-006](../bugs/BUG-006.md) / [ảnh](../bugs/screenshots/GUI-007.png) |
| GUI-008 | IA-02 | Login | Bỏ trống email bị chặn gửi form — HTML validation / tiêu chí bổ sung | Passed | {"valid":false,"message":"Please fill out this field."} |  |
| GUI-009 | IA-02 | Login | Bỏ trống mật khẩu bị chặn gửi form — HTML validation / tiêu chí bổ sung | Passed | {"valid":false,"message":"Please fill out this field."} |  |
| GUI-010 | IA-02 | Login | Email sai định dạng bị chặn tại form — FR-02 | Failed | {"valid":true,"typeMismatch":false}; form gửi tới API và hiện lỗi đăng nhập | [BUG-004](../bugs/BUG-004.md) / [ảnh](../bugs/screenshots/GUI-010.png) |
| GUI-011 | IA-02 | Login | Lỗi đăng nhập nằm phía trên nút gửi — FR-22 | Failed | error.y=517, button.y=425 | [BUG-007](../bugs/BUG-007.md) / [ảnh](../bugs/screenshots/GUI-011.png) |
| GUI-012 | IA-04 | Login | Đăng nhập sai có thông báo lỗi tiếng Việt — FR-02, FR-21 | Passed | Đăng nhập thất bại. Vui lòng kiểm tra lại. |  |
| GUI-013 | IA-01 | Login | Tab đầu tiên đi vào phần tử tương tác trên cùng, không nhảy tới submit — FR-21 | Failed | {"tag":"BUTTON","text":"Sign In","tabIndex":1} | [BUG-008](../bugs/BUG-008.md) / [ảnh](../bugs/screenshots/GUI-013.png) |
| GUI-014 | IA-03 | Login | Liên kết Quên mật khẩu mở đúng trang — IA-03; yêu cầu điều hướng bổ sung | Passed | http://localhost:5173/forgot-password |  |
| GUI-015 | IA-03 | Login | Liên kết Đăng ký mở đúng trang — IA-03; yêu cầu điều hướng bổ sung | Passed | http://localhost:5173/register |  |
| GUI-016 | IA-02 | Login | Enter tại mật khẩu gửi form đăng nhập hợp lệ — IA-02; hỗ trợ bàn phím bổ sung | Passed | Enter đăng nhập thành công, tới http://localhost:5173/ |  |
| GUI-017 | IA-01 | Profile | Bảng có đủ tiêu đề Mã ĐH, Ngày đặt, Tổng tiền, Trạng thái, Thao tác — FR-11 | Passed | Mã ĐH  /  Ngày đặt  /  Tổng tiền  /  Trạng thái  /  Thao tác |  |
| GUI-018 | IA-01 | Profile | Cả năm trạng thái được dịch sang tiếng Việt — FR-11 | Passed | Đã hủy  /  Đã giao  /  Đang giao  /  Đã xác nhận  /  Chờ xác nhận |  |
| GUI-019 | IA-01 | Profile | Cả năm trạng thái có màu phân biệt — FR-11 | Passed | ["rgb(254, 226, 226)","rgb(220, 252, 231)","rgb(219, 234, 254)","rgb(224, 231, 255)","rgb(254, 249, 195)"] |  |
| GUI-020 | IA-01 | Profile | Tổng tiền có phân cách hàng nghìn và ký hiệu ₫ — FR-21 | Passed | 1,238,000 ₫  /  1,237,000 ₫  /  1,236,000 ₫  /  1,235,000 ₫  /  1,234,000 ₫ |  |
| GUI-021 | IA-01 | Profile | Các dòng đơn có mã và ngày đặt không rỗng — FR-11 | Passed | [["#9","11/10/2026"],["#8","11/10/2026"],["#7","11/10/2026"],["#6","11/10/2026"],["#5","11/10/2026"]] |  |
| GUI-022 | IA-01 | Profile | Nút Hủy đơn có màu đỏ — FR-21 | Passed | background: rgb(239, 68, 68) |  |
| GUI-023 | IA-01 | Profile | Có đúng một h1 mô tả trang — FR-21 | Failed | Số h1: 0 | [BUG-002](../bugs/BUG-002.md) / [ảnh](../bugs/screenshots/GUI-023.png) |
| GUI-024 | IA-02 | Profile | Email bị khóa, người dùng không sửa được — FR-04 | Passed | Email disabled=true |  |
| GUI-025 | IA-02 | Profile | Họ tên bắt buộc có dấu * ở nhãn — FR-22 | Failed | Nhãn: Họ Tên | [BUG-006](../bugs/BUG-006.md) / [ảnh](../bugs/screenshots/GUI-025.png) |
| GUI-026 | IA-02 | Profile | Nút Cập nhật có màu xanh dương — FR-21 | Passed | background: rgb(37, 99, 235) |  |
| GUI-027 | IA-02 | Profile | Số điện thoại hợp lệ 0912345678 được chấp nhận khi cập nhật — FR-04 | Failed | [{"type":"alert","message":"Số điện thoại không hợp lệ. Vui lòng nhập đúng 9-10 chữ số."}] | [BUG-009](../bugs/BUG-009.md) / [ảnh](../bugs/screenshots/GUI-027.png) |
| GUI-028 | IA-02 | Profile | Số điện thoại sai 123456789 bị từ chối — FR-04 | Failed | [{"type":"alert","message":"Cập nhật thành công!"}] | [BUG-009](../bugs/BUG-009.md) / [ảnh](../bugs/screenshots/GUI-028.png) |
| GUI-029 | IA-04 | Profile | Đơn pending và confirmed có nút Hủy đơn — FR-10 | Passed | pending và confirmed đều có nút Hủy đơn |  |
| GUI-030 | IA-04 | Profile | Đơn shipping không có nút Hủy đơn cho user — FR-10 | Failed | shipping có 1 nút Hủy đơn | [BUG-010](../bugs/BUG-010.md) / [ảnh](../bugs/screenshots/GUI-030.png) |
| GUI-031 | IA-04 | Profile | Đơn delivered và canceled không có nút Hủy đơn — FR-10 | Passed | Tổng nút ở delivered/canceled: 0 |  |
| GUI-032 | IA-04 | Profile | Hủy đơn pending có phản hồi thành công và cập nhật Đã hủy — FR-10; phản hồi bổ sung IA-04 | Passed | [{"type":"alert","message":"Hủy đơn thành công!"}]; dòng đơn hiển thị Đã hủy |  |
| GUI-033 | IA-04 | Profile | Hủy đơn confirmed có phản hồi thành công và cập nhật Đã hủy — FR-10; phản hồi bổ sung IA-04 | Passed | [{"type":"alert","message":"Hủy đơn thành công!"}]; dòng đơn hiển thị Đã hủy |  |
| GUI-034 | IA-03 | Profile | Tải lại trang vẫn giữ đăng nhập và tải lại đơn — IA-03; tính liên tục phiên bổ sung | Passed | Sau reload: 5 đơn, phiên vẫn còn |  |
| GUI-035 | IA-04 | Profile | Chỉ hiển thị đơn của người dùng hiện tại — FR-11 | Passed | Các đơn hiển thị #9, #8, #7, #6, #5; đơn khác #10 |  |
| GUI-036 | IA-04 | Profile | Đang chờ tải đơn có chỉ báo tải, không báo chưa có đơn — IA-04; tiêu chí trạng thái bổ sung | Failed | Nội dung trong lúc API trì hoãn 1800ms: Hồ sơ của bạn; Email (Không đổi); Họ Tên; Số điện thoại; Địa chỉ giao hàng; Cập nhật; Lịch sử đơn hàng; ; Bạn chưa có đơn hàng nào. | [BUG-011](../bugs/BUG-011.md) / [ảnh](../bugs/screenshots/GUI-036.png) |
| GUI-037 | IA-04 | Profile | Lỗi tải đơn có thông báo lỗi, không báo chưa có đơn — IA-04; tiêu chí phục hồi lỗi bổ sung | Failed | HTTP 500 được mô phỏng tại biên mạng; UI: Hồ sơ của bạn; Email (Không đổi); Họ Tên; Số điện thoại; Địa chỉ giao hàng; Cập nhật; Lịch sử đơn hàng; ; Bạn chưa có đơn hàng nào. | [BUG-012](../bugs/BUG-012.md) / [ảnh](../bugs/screenshots/GUI-037.png) |
| GUI-038 | IA-04 | Profile | Không có đơn: có thông điệp thân thiện và icon/hình minh họa — FR-24 | Failed | Thông điệp: Bạn chưa có đơn hàng nào.; số icon/ảnh: 0 | [BUG-013](../bugs/BUG-013.md) / [ảnh](../bugs/screenshots/GUI-038.png) |
| GUI-039 | IA-03 | Global | Nhãn nút đăng xuất là Đăng xuất — FR-23 | Failed | Nhãn: Thoát | [BUG-014](../bugs/BUG-014.md) / [ảnh](../bugs/screenshots/GUI-039.png) |
| GUI-040 | IA-03 | Global | Navbar phân biệt trang đang chọn khi chuyển Home/Profile — FR-23 | Failed | class tại Profile=hover:underline text-yellow-300; tại Home=hover:underline text-yellow-300 | [BUG-015](../bugs/BUG-015.md) / [ảnh](../bugs/screenshots/GUI-040.png) |
| GUI-041 | IA-03 | Global | Link hồ sơ mở trang có lịch sử đơn — FR-11; IA-03 | Passed | http://localhost:5173/profile |  |
| GUI-042 | IA-03 | Global | Back từ Profile trở về Home và giữ phiên — IA-03; lịch sử điều hướng bổ sung | Passed | Back -&gt; http://localhost:5173/; link hồ sơ vẫn hiện |  |
| GUI-043 | IA-03 | Global | Giỏ hàng có badge số lượng sau khi thêm một sản phẩm — FR-23 | Failed | Đã thêm 1 sản phẩm; link giỏ: Giỏ hàng | [BUG-016](../bugs/BUG-016.md) / [ảnh](../bugs/screenshots/GUI-043.png) |
| GUI-044 | IA-03 | Global | Đăng xuất làm trang Profile không còn hiển thị đơn — FR-11; IA-03 | Passed | Đăng xuất -&gt; Vui lòng đăng nhập; không hiện đơn |  |
| GUI-045 | IA-01 | Admin Orders | Trạng thái được dịch giống giao diện user — FR-11, FR-18, FR-21 | Passed | Chờ xác nhận  /  Đã xác nhận  /  Đang giao  /  Đã giao  /  Đã hủy |  |
| GUI-046 | IA-02 | Admin Orders | Đơn pending có Xác nhận và Hủy — FR-10, FR-18 | Passed | pending: Xác nhận  /  Hủy |  |
| GUI-047 | IA-02 | Admin Orders | Đơn confirmed có Giao hàng và Hủy — FR-10, FR-18 | Passed | confirmed: Giao hàng  /  Hủy |  |
| GUI-048 | IA-02 | Admin Orders | Đơn shipping có Hoàn thành — FR-10, FR-18 | Passed | shipping: Hoàn thành |  |
| GUI-049 | IA-02 | Admin Orders | Đơn delivered không có nút chuyển trạng thái — FR-10, FR-18 | Passed | delivered: [] |  |
| GUI-050 | IA-02 | Admin Orders | Đơn canceled không có nút chuyển trạng thái — FR-10, FR-18 | Failed | canceled: ["Đánh dấu Đã giao"] | [BUG-017](../bugs/BUG-017.md) / [ảnh](../bugs/screenshots/GUI-050.png) |
| GUI-051 | IA-03 | Admin Orders | Menu highlight Quản lý Đơn hàng khi chọn — FR-23 | Passed | {"class":"cursor-pointer hover:text-blue-300 text-blue-400","color":"rgb(147, 197, 253)"} |  |
| GUI-052 | IA-01 | Admin Orders | Các nút Hủy có màu đỏ — FR-21 | Failed | ["rgb(156, 163, 175)","rgb(156, 163, 175)","rgb(156, 163, 175)","rgb(156, 163, 175)","rgb(156, 163, 175)"] | [BUG-018](../bugs/BUG-018.md) / [ảnh](../bugs/screenshots/GUI-052.png) |
| GUI-053 | IA-04 | Admin Orders | Địa chỉ chứa &lt;b&gt; được hiển thị dưới dạng văn bản an toàn — FR-18, SEC-04 | Failed | Thẻ b render: 1; text: GUI_ADDRESS | [BUG-019](../bugs/BUG-019.md) / [ảnh](../bugs/screenshots/GUI-053.png) |
| GUI-054 | IA-04 | Admin Orders | Admin xác nhận pending: user tải lại thấy Đã xác nhận — FR-10, FR-11, FR-18 | Passed | Admin xác nhận #5; user tải lại thấy Đã xác nhận |  |
| GUI-055 | IA-04 | Profile | Thông báo lỗi hủy đơn từ API dùng tiếng Việt dễ hiểu — FR-21; IA-04 | Failed | [{"type":"alert","message":"Lỗi: Cannot cancel this order."}]; user đang xem trang cũ, admin đã chuyển đơn sang delivered | [BUG-020](../bugs/BUG-020.md) / [ảnh](../bugs/screenshots/GUI-055.png) |
| GUI-056 | IA-02 | Profile | Nhãn Họ tên/Điện thoại/Địa chỉ liên kết với control tương ứng — IA-02; khả năng truy cập bổ sung | Failed | [{"type":"INPUT","labels":0},{"type":"INPUT","labels":0},{"type":"TEXTAREA","labels":0}] | [BUG-021](../bugs/BUG-021.md) / [ảnh](../bugs/screenshots/GUI-056.png) |
| GUI-057 | IA-01 | Profile | Ở 360px nội dung không gây cuộn ngang toàn trang — IA-01; responsive bổ sung | Failed | {"viewport":360,"scroll":396} | [BUG-022](../bugs/BUG-022.md) / [ảnh](../bugs/screenshots/GUI-057.png) |
| GUI-058 | IA-04 | Profile | Tên người dùng chứa &lt;b&gt; hiển thị nguyên văn, không render HTML — SEC-04 | Failed | Số thẻ b được render: 1; text: Chào, GUI_NAME | [BUG-023](../bugs/BUG-023.md) / [ảnh](../bugs/screenshots/GUI-058.png) |
