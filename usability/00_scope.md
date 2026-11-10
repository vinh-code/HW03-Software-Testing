# Phạm vi: Lịch sử & Theo dõi đơn hàng

| Mục | Nội dung |
|---|---|
| Chủ đề | Người dùng xem lại các đơn đã đặt, theo dõi trạng thái và hủy đơn |
| FR liên quan | FR-10 (State machine), FR-11 (Lịch sử đơn), FR-18 (Admin đơn hàng), FR-20 (Mobile); GUI: FR-21 đến FR-24 |
| Màn hình Task 1 | Order History (Web, trong `/profile`), Mobile Orders (Expo), Admin Orders; màn phụ trợ: Login, Global (navbar) |
| Flow Task 2 | Đăng nhập → Lịch sử đơn → Xem trạng thái (đã giao / đang giao) → Hủy đơn không còn cần → Thử hủy đơn đang giao |

## Những gì SUT có và không có (khảo sát mã nguồn, chưa chạy test)

| Chức năng | Có không? | Ghi chú |
|---|---|---|
| Lịch sử đơn hàng (web) | Có | `frontend-web` → `/profile`, khối "Lịch sử đơn hàng" cạnh form Hồ sơ; không có trang `/orders` riêng |
| Lịch sử đơn hàng (mobile) | Có | Expo app → Hồ sơ → "Lịch sử đơn hàng" |
| Trạng thái đơn | Có (dạng nhãn + màu) | Không có timeline/tiến trình |
| Hủy đơn | Có | Nút "Hủy đơn" trên web và mobile (theo FR-10) |
| Chi tiết đơn (sản phẩm trong đơn) | Không | Bảng `orders` không có dòng hàng; chỉ id, user_id, total_amount, status, shipping_address, created_at. API `GET /api/orders/:id` có nhưng không có UI |
| Lọc / tìm đơn | Không | |
| Đổi trả | Không | |
| Đổi trạng thái đơn | Có (Admin) | `frontend-admin` → "Quản lý Đơn hàng"; dùng để tạo tình huống đang giao/đã giao |

## Cách dùng trong bài
- Các mục checklist có `Spec ref = "Ngoài spec"` là thực hành UX tốt nhưng spec không yêu cầu. Khi chạy có thể đánh **N/A** hoặc **Failed**, ghi lý do vào Notes. Hãy thống nhất cách chấm với TA nếu cần.
- Nếu làm nhóm, màn hình chính và flow phải khác bạn cùng nhóm (đề §5).
