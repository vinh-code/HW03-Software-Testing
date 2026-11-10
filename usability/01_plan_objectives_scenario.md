# Task 2 – Kế hoạch đánh giá Usability (Lịch sử & Theo dõi đơn hàng)

**Flow đã chọn:** Đăng nhập → Truy cập Lịch sử đơn hàng → Tìm đơn cũ → Xem & theo dõi trạng thái (Đang giao / Đã giao) → Hủy đơn mình không còn cần.

> Kịch bản chỉ dùng những gì SUT thật sự có (xem `00_scope.md`). SUT không có chi tiết đơn, lọc/tìm đơn hay đổi trả; nếu participant tự tìm các chức năng này thì đó cũng là dữ liệu usability đáng ghi nhận.
> Nếu làm nhóm, flow này không được trùng với bạn cùng nhóm (đề §5).

## 1. Mục tiêu (Objectives)

| # | Mục tiêu | Câu hỏi cần trả lời | Chỉ số đo |
|---|---|---|---|
| O1 | Phát hiện nút thắt điều hướng | Người dùng có tìm được chỗ xem lịch sử đơn hàng không (lối vào là link "Chào, <tên>")? | Tỷ lệ tìm thấy không trợ giúp; thời gian tới lúc thấy danh sách đơn; số lần bấm sai |
| O2 | Theo dõi trạng thái | Người dùng có hiểu đúng trạng thái đơn (Chờ xác nhận / Đã xác nhận / Đang giao / Đã giao / Đã hủy) và tự phân biệt được các đơn? | Số câu trả lời trạng thái đúng /2; số lần do dự |
| O3 | Khôi phục lỗi / hủy đơn | Người dùng hủy đúng đơn chưa muốn, hiểu vì sao đơn đang giao không hủy được? | Hủy đúng đơn; hủy nhầm đơn; hiểu thông báo lỗi |
| O4 | Độ tự tin & tin cậy | Người dùng có tin thông tin trạng thái đơn là đúng và đáng tin không? | SUS; câu probe về trust |
| O5 | Hiệu suất | Mất bao lâu để hoàn thành các nhiệm vụ? | Thời gian (giây) |

## 2. Người dùng mục tiêu

- Người mua sắm online phổ thông, 18-55 tuổi, từng theo dõi đơn hàng trên một sàn TMĐT.
- Ưu tiên người **không làm IT / không phải tester**.
- **Không** được là sinh viên đang học HW03.
- Cần **7 người** + **1 pilot** (pilot không tính vào 7).

## 3. Kịch bản tác vụ

Đưa cho participant (in ra hoặc đọc to). **Không** liệt kê từng bước.

> *Tuần trước bạn đã đặt vài đơn hàng trên cửa hàng online EShop. Bạn đã có tài khoản
> (email: `test@eshop.com`, mật khẩu: `Test1234!`).*
>
> *Hôm nay bạn muốn:*
> 1. *Kiểm tra đơn hàng khoảng **30 triệu đồng** của bạn đã được giao chưa.*
> 2. *Biết đơn hàng khoảng **45 triệu đồng** hiện đang ở giai đoạn nào.*
> 3. *Bạn đổi ý về đơn hàng khoảng **28 triệu đồng** và không muốn mua nữa, hãy hủy nó.*
> 4. *Bạn cũng đổi ý về đơn 45 triệu. Hãy thử hủy nó.*
>
> *Khi xong hoặc khi bạn thấy không làm tiếp được, hãy cho tôi biết.*

(Nhiệm vụ nhỏ 1-4 là các mục tiêu của cùng một kịch bản, vẫn là mục tiêu cần đạt chứ không phải hướng dẫn thao tác. Đơn được nhận diện bằng số tiền vì SUT không hiển thị danh sách sản phẩm trong đơn.)

**Ghi chú cho moderator (KHÔNG đọc cho participant):**
- Dữ liệu seed bằng `node seed_orders.mjs`: #A 28 triệu = pending, #B 1,5 triệu = confirmed, #C 45 triệu = shipping, #D 30 triệu = delivered.
- Đúng theo FR-10/FR-11: đơn 30 triệu "Đã giao"; đơn 45 triệu "Đang giao"; đơn 28 triệu hủy được; đơn 45 triệu (đang giao) **không** được hủy bởi user.
- Nhiệm vụ 4 là "bẫy kỳ vọng": xem người dùng phản ứng ra sao khi giao diện cho phép/không cho phép hành động.
- Cần reset + seed lại trước **mỗi** buổi (xem README mục Reset).

## 4. Tiêu chí thành công

| Nhiệm vụ | Thành công |
|---|---|
| T1 | Nói đúng "Đã giao" cho đơn 30 triệu, không cần gợi ý |
| T2 | Nói đúng "Đang giao" cho đơn 45 triệu |
| T3 | Hủy đúng đơn 28 triệu, thấy đơn đổi sang "Đã hủy", không hủy nhầm đơn khác |
| T4 | Ghi nhận kết quả thực tế (hủy được hay không), người dùng hiểu rõ vì sao (không bị bối rối). Đối chiếu với FR-10 |

Mức hoàn thành mỗi nhiệm vụ: *không trợ giúp / có trợ giúp / thất bại*. Time-out toàn buổi: **10 phút** (chỉnh sau pilot).

## 5. Dữ liệu thu thập mỗi buổi

1. Thời gian bắt đầu/kết thúc từng nhiệm vụ, kết quả.
2. Ghi chú quan sát có cấu trúc (`06_session_notes_template.md`).
3. Video màn hình (+ audio khi có đồng ý).
4. SUS (`02_SUS_questionnaire.md`).
5. Probe (`03_probe_questions.md`).

## 6. Quy trình

1. **Pilot** → ghi vào `sessions/pilot.md`.
2. 7 buổi: `sessions/S01.md` … `S07.md`.
3. Chấm SUS bằng `sus_scoring.py`.
4. Tổng hợp theo `07_analysis_template.md`.
5. Bug thật → `bugs/` **và** GitHub Issues kèm screenshot.

## 7. Chuẩn bị môi trường (mỗi buổi)

```bash
# 1. Dừng backend, reset DB, chạy lại, seed đơn mẫu
cd sut/backend && node database.js && node server.js &
cd submission/usability && node seed_orders.mjs
```
- Mở `http://localhost:5173` trong cửa sổ ẩn danh (chưa đăng nhập), để participant tự đăng nhập.
- Bật screen recording. Dùng một thiết bị cho cả 7 buổi (hoặc ghi rõ khi đổi).
- Nếu muốn một buổi trên mobile (Expo Go), ghi rõ trong bảng participant.
