"""Checklist – Lịch sử & Theo dõi đơn hàng (FR-10, FR-11, FR-18, FR-20 đến FR-24).

(IA, Screen, Item/Expected result, Spec ref, Origin)

Screen:
  Order History (Web)  = mục "Lịch sử đơn hàng" trong /profile của frontend-web
  Mobile Orders        = màn Hồ sơ > "Lịch sử đơn hàng" trong Expo app
  Admin Orders         = "Quản lý Đơn hàng" trong frontend-admin (nơi đổi trạng thái để theo dõi)
  Login / Global       = màn phụ trợ trên đường đi tới Lịch sử đơn

Origin: AI-draft = bản nháp khởi tạo (bạn phải review), Student = bạn thêm vì AI bỏ sót.
"Ngoài spec" = thực hành tốt về UX nhưng spec không yêu cầu -> khi chạy có thể ra N/A hoặc ghi nhận kèm lý do.
"""

ITEMS = [
    # ================= IA-01 General UI standards =================
    ("IA-01", "Order History (Web)", "Cột Mã ĐH, Ngày đặt, Tổng tiền, Trạng thái, Thao tác đều có tiêu đề cột bằng tiếng Việt", "FR-11, FR-21", "AI-draft"),
    ("IA-01", "Order History (Web)", "Cả 5 trạng thái (pending, confirmed, shipping, delivered, canceled) hiển thị bằng tiếng Việt rõ ràng (Chờ xác nhận / Đã xác nhận / Đang giao / Đã giao / Đã hủy), không lộ mã tiếng Anh", "FR-11", "AI-draft"),
    ("IA-01", "Order History (Web)", "Mỗi trong 5 trạng thái có màu nhãn khác nhau, dễ phân biệt", "FR-11", "AI-draft"),
    ("IA-01", "Order History (Web)", "Tổng tiền hiển thị ký hiệu ₫ và phân cách hàng nghìn (vd 30.000.000 ₫)", "FR-11, FR-21", "AI-draft"),
    ("IA-01", "Order History (Web)", "Ngày đặt hiển thị định dạng dễ đọc, nhất quán kiểu Việt Nam (dd/MM/yyyy)", "FR-11", "AI-draft"),
    ("IA-01", "Order History (Web)", "Mã đơn hiển thị rõ ràng, nhất quán (vd #12), dùng font dễ đọc", "FR-11", "AI-draft"),
    ("IA-01", "Order History (Web)", "Danh sách đơn sắp xếp có thứ tự nhất quán (mới nhất trước)", "FR-11", "AI-draft"),
    ("IA-01", "Order History (Web)", "Nút Hủy đơn dùng màu đỏ (hành động nguy hiểm)", "FR-21", "AI-draft"),
    ("IA-01", "Order History (Web)", "Trang Hồ sơ/Lịch sử có đúng 1 thẻ <h1> mô tả nội dung trang", "FR-21", "AI-draft"),
    ("IA-01", "Order History (Web)", "Thứ tự focus bằng Tab đi từ trên xuống dưới, trái sang phải qua form hồ sơ và các nút Hủy đơn", "FR-21", "AI-draft"),
    ("IA-01", "Order History (Web)", "Ở độ rộng 360px bảng đơn hàng không tràn ngang/cắt chữ, vẫn đọc được đủ các cột", "FR-21", "AI-draft"),
    ("IA-01", "Order History (Web)", "Bố cục 2 cột (form hồ sơ + lịch sử) cân đối, khoảng cách và cỡ chữ nhất quán với các trang khác", "FR-21", "AI-draft"),
    ("IA-01", "Mobile Orders", "Thẻ đơn hàng trên mobile hiển thị đủ Mã, Ngày, Tổng tiền (₫, phân cách), Trạng thái bằng tiếng Việt", "FR-11, FR-20", "AI-draft"),
    ("IA-01", "Mobile Orders", "Trạng thái trên mobile cũng được phân biệt bằng màu (không chỉ chữ thuần)", "FR-11, FR-20", "AI-draft"),
    ("IA-01", "Admin Orders", "Nhãn trạng thái trong Admin dùng cùng từ ngữ và màu với người dùng", "FR-18, FR-21", "AI-draft"),
    ("IA-01", "Order History (Web)", "Nhãn trạng thái đủ tương phản với nền (>= 4.5:1) cho cả 5 trạng thái", "WCAG 1.4.3", "Student"),
    ("IA-01", "Order History (Web)", "Trạng thái truyền đạt bằng chữ chứ không chỉ bằng màu (người mù màu vẫn phân biệt được)", "WCAG 1.4.1", "Student"),
    ("IA-01", "Order History (Web)", "Phóng to 200% vẫn đọc và thao tác được bảng đơn hàng", "WCAG 1.4.4", "Student"),
    ("IA-01", "Order History (Web)", "Dark mode của OS/trình duyệt không làm mất chữ/nhãn trạng thái", "", "Student"),
    ("IA-01", "Order History (Web)", "Bố cục RTL (dir=rtl) không vỡ nghiêm trọng ở bảng đơn hàng", "", "Student"),
    ("IA-01", "Mobile Orders", "Nút Hủy đơn trên mobile đủ lớn để chạm (>= 44x44) và không sát nút khác", "", "Student"),
    # ================= IA-02 Forms =================
    ("IA-02", "Login", "Trường Email dùng type=\"email\" và có ký hiệu * ở nhãn bắt buộc", "FR-02, FR-22", "AI-draft"),
    ("IA-02", "Login", "Trường Mật khẩu dùng type=\"password\"", "FR-22", "AI-draft"),
    ("IA-02", "Login", "Thông báo lỗi đăng nhập nằm TRÊN nút Đăng nhập", "FR-22", "AI-draft"),
    ("IA-02", "Order History (Web)", "Form Hồ sơ: trường Email bị khóa (disabled) và có chú thích \"Không đổi\"", "FR-04", "AI-draft"),
    ("IA-02", "Order History (Web)", "Form Hồ sơ: Số điện thoại báo lỗi khi sai định dạng (phải bắt đầu bằng 0, 10-11 số)", "FR-04", "AI-draft"),
    ("IA-02", "Order History (Web)", "Form Hồ sơ: trường bắt buộc có ký hiệu *; nhãn gắn đúng với ô nhập", "FR-22", "AI-draft"),
    ("IA-02", "Order History (Web)", "Form Hồ sơ nằm cạnh lịch sử đơn nhưng không gây nhầm lẫn: nút Cập nhật rõ ràng, màu xanh dương", "FR-21", "AI-draft"),
    ("IA-02", "Order History (Web)", "Địa chỉ giao hàng hiển thị lại đúng giá trị đã lưu sau khi tải lại trang", "FR-04", "AI-draft"),
    ("IA-02", "Admin Orders", "Điều khiển đổi trạng thái chỉ cho chọn các trạng thái kế tiếp hợp lệ (theo state machine)", "FR-10, FR-18", "AI-draft"),
    ("IA-02", "Admin Orders", "Điều khiển đổi trạng thái có nhãn rõ ràng bằng tiếng Việt", "FR-18, FR-21", "AI-draft"),
    ("IA-02", "Order History (Web)", "Hành động Hủy đơn có hộp thoại xác nhận trước khi thực hiện (tương tự xóa trong giỏ)", "FR-24 (tương tự)", "AI-draft"),
    ("IA-02", "Login", "Autocomplete/trình quản lý mật khẩu hoạt động (thuộc tính autocomplete phù hợp)", "", "Student"),
    ("IA-02", "Login", "Nhấn Enter submit được form; nút bị vô hiệu khi đang gửi (chống bấm đúp)", "", "Student"),
    ("IA-02", "Order History (Web)", "Bấm nhanh hai lần vào Hủy đơn không gây hai yêu cầu/trạng thái lỗi", "", "Student"),
    # ================= IA-03 Navigation =================
    ("IA-03", "Global", "Từ thanh điều hướng người dùng tìm được lối vào Lịch sử đơn hàng (link có nhãn gợi ý \"Đơn hàng\"/\"Tài khoản\")", "FR-11", "AI-draft"),
    ("IA-03", "Global", "Navbar highlight mục của trang đang xem (khi ở /profile)", "FR-23", "AI-draft"),
    ("IA-03", "Global", "Nút đăng xuất có nhãn đúng là \"Đăng xuất\" (không phải \"Thoát\")", "FR-23", "AI-draft"),
    ("IA-03", "Global", "Link Giỏ hàng có badge số lượng sản phẩm", "FR-23", "AI-draft"),
    ("IA-03", "Order History (Web)", "Có breadcrumb/đường dẫn quay lại trang trước ở trang Hồ sơ/Lịch sử đơn", "FR-23 (mở rộng)", "AI-draft"),
    ("IA-03", "Order History (Web)", "Truy cập /profile khi chưa đăng nhập hiển thị thông báo kèm đường dẫn tới trang Đăng nhập", "FR-11", "AI-draft"),
    ("IA-03", "Global", "Sau khi đặt hàng thành công người dùng được dẫn/có link tới lịch sử đơn để theo dõi", "FR-08, FR-11", "AI-draft"),
    ("IA-03", "Order History (Web)", "Người dùng xem được địa chỉ giao hàng của từng đơn (trong dòng đơn hoặc màn chi tiết)", "Ngoài spec", "AI-draft"),
    ("IA-01", "Order History (Web)", "Các dòng đơn có viền/khoảng cách giúp phân biệt rõ từng đơn, dễ quét mắt; cột Tổng tiền thẳng hàng", "FR-21", "AI-draft"),
    ("IA-03", "Order History (Web)", "Nút Back của trình duyệt từ /profile quay về đúng trang trước, giữ nguyên đăng nhập", "", "AI-draft"),
    ("IA-03", "Order History (Web)", "Tải lại (F5) trang /profile vẫn giữ phiên đăng nhập và hiển thị lại lịch sử đơn", "", "AI-draft"),
    ("IA-03", "Mobile Orders", "Trên mobile có lối vào Lịch sử đơn hàng rõ ràng và nút quay lại màn hình trước", "FR-20", "AI-draft"),
    ("IA-03", "Admin Orders", "Menu Admin highlight mục \"Quản lý Đơn hàng\" khi đang xem", "FR-18, FR-23", "AI-draft"),
    ("IA-03", "Order History (Web)", "Danh sách nhiều đơn (>= 20) có phân trang hoặc cuộn dễ dùng, không làm trang quá dài khó thao tác", "", "Student"),
    ("IA-03", "Global", "Các link và nút trong lịch sử đơn truy cập được bằng bàn phím, có focus ring nhìn thấy", "WCAG 2.4.7", "Student"),
    ("IA-03", "Global", "URL không tồn tại (vd /orders) hiển thị trang 404 thân thiện có đường quay lại", "", "Student"),
    # ================= IA-04 Feedback / state =================
    ("IA-04", "Order History (Web)", "Có trạng thái loading trong lúc tải danh sách đơn (không hiện \"Bạn chưa có đơn hàng nào\" sai lúc đang tải)", "FR-11, FR-24", "AI-draft"),
    ("IA-04", "Order History (Web)", "Tài khoản chưa có đơn: empty state có icon/hình minh họa và lời nhắn thân thiện", "FR-24", "AI-draft"),
    ("IA-04", "Order History (Web)", "Hủy đơn thành công: có phản hồi rõ ràng và dòng đơn cập nhật sang \"Đã hủy\" ngay", "FR-10, FR-24", "AI-draft"),
    ("IA-04", "Order History (Web)", "Đơn ở trạng thái Đang giao KHÔNG hiện nút Hủy đơn (user không được tự hủy)", "FR-10", "AI-draft"),
    ("IA-04", "Order History (Web)", "Đơn Đã giao và Đã hủy không hiện nút Hủy đơn / thao tác nào gây hiểu nhầm", "FR-10", "AI-draft"),
    ("IA-04", "Order History (Web)", "Đơn Chờ xác nhận và Đã xác nhận hiện nút Hủy đơn", "FR-10", "AI-draft"),
    ("IA-04", "Order History (Web)", "Hủy đơn thất bại hiển thị thông báo lỗi tiếng Việt dễ hiểu (không lộ chuỗi tiếng Anh/kỹ thuật)", "FR-10, FR-21", "AI-draft"),
    ("IA-04", "Order History (Web)", "Sau khi admin đổi trạng thái, người dùng tải lại thấy trạng thái mới đúng", "FR-10, FR-11", "AI-draft"),
    ("IA-04", "Order History (Web)", "Người dùng theo dõi được tiến trình đơn (timeline/các bước) chứ không chỉ một nhãn trạng thái", "Ngoài spec", "AI-draft"),
    ("IA-04", "Order History (Web)", "Người dùng chỉ thấy đơn của chính mình (không lộ đơn người khác)", "FR-11", "AI-draft"),
    ("IA-04", "Mobile Orders", "Hủy đơn trên mobile: có hộp thoại/Alert phản hồi thành công hoặc lỗi bằng tiếng Việt", "FR-20, FR-24", "AI-draft"),
    ("IA-04", "Mobile Orders", "Mobile: chỉ đơn Chờ xác nhận/Đã xác nhận có nút Hủy đơn; Đang giao không có", "FR-10, FR-20", "AI-draft"),
    ("IA-04", "Admin Orders", "Đổi trạng thái không hợp lệ (vd Đã giao -> Đã xác nhận) hiển thị lỗi rõ ràng, trạng thái cũ giữ nguyên", "FR-10, FR-18", "AI-draft"),
    ("IA-04", "Admin Orders", "Địa chỉ giao hàng chứa HTML (<b>x</b>) hiển thị an toàn dạng văn bản", "FR-18, SEC-04", "AI-draft"),
    ("IA-04", "Global", "Tên người dùng chứa thẻ HTML trên header hiển thị an toàn", "SEC-04", "AI-draft"),
    ("IA-04", "Order History (Web)", "Khi API lỗi/mất mạng giao diện báo lỗi thân thiện (không hiển thị như \"chưa có đơn hàng\" gây hiểu nhầm)", "", "Student"),
    ("IA-04", "Order History (Web)", "Thông báo/kết quả Hủy đơn được trình đọc màn hình đọc được (role=alert/aria-live)", "WCAG 4.1.3", "Student"),
    ("IA-04", "Global", "Phiên hết hạn (token hết hạn) dẫn tới thông báo và đăng nhập lại thay vì lỗi im lặng", "", "Student"),
    ("IA-04", "Order History (Web)", "Trạng thái và số liệu đơn nhất quán giữa web, mobile và admin cho cùng một đơn", "FR-10, FR-11, FR-18", "Student"),
]
