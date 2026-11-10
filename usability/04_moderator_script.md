# Kịch bản điều hành buổi test (Moderator script)

Thời lượng dự kiến: 20–25 phút/buổi.

## 1. Chào và giới thiệu (2 phút)

> "Cảm ơn bạn đã tham gia. Hôm nay chúng ta đang kiểm tra **trang web**, không phải kiểm tra bạn. Bạn không thể làm sai.
> Mọi chỗ bạn thấy khó hiểu đều là lỗi của trang web, và đó chính là điều mình cần biết.
> Trong lúc làm, bạn hãy **nói to những gì bạn đang nghĩ** (think aloud): bạn đang tìm gì, vì sao bấm vào đó, điều gì làm bạn thắc mắc.
> Mình sẽ ngồi quan sát và ghi chú, mình sẽ không hướng dẫn trừ khi bạn hoàn toàn bị kẹt.
> Bạn có thể dừng bất cứ lúc nào."

## 2. Đồng ý ghi hình (1 phút)

> "Mình xin phép ghi lại màn hình (và giọng nói) chỉ để phân tích cho bài tập, không công khai và không dùng cho mục đích khác. Bạn đồng ý chứ?"

☐ Đồng ý ghi màn hình ☐ Đồng ý ghi âm ☐ Không đồng ý ghi (chỉ ghi chú tay)

## 3. Câu hỏi nền (2 phút)
- Tuổi/nghề nghiệp (không cần tên thật trong báo cáo công khai)
- Tần suất mua online; thiết bị thường dùng
- Mức quen công nghệ (1–5)

## 4. Đưa kịch bản (1 phút)
Đọc/đưa bản in kịch bản trong `01_plan_objectives_scenario.md` mục 3 (đã kèm tài khoản test). Hỏi "Bạn đã hiểu mục tiêu chưa?". Không nói tên trang hay chỗ để bấm.

## 5. Quan sát (5–10 phút)

**Nên:** im lặng, gật đầu, nhắc "bạn đang nghĩ gì?" khi họ im quá lâu.
**Không nên:**
- Nói "bấm vào đây", "nút ở bên phải", "bạn thử menu xem".
- Giải thích giao diện, biện hộ cho lỗi.
- Phản ứng biểu cảm khi họ sai.

Chỉ can thiệp khi họ **hoàn toàn kẹt** > 2 phút hoặc muốn bỏ cuộc. Ghi lại mức gợi ý (Mức 1: nhắc lại mục tiêu; Mức 2: gợi ý khu vực; Mức 3: chỉ thẳng).

## 6. Kết thúc tác vụ
Khi họ nói "xong" hoặc hết 10 phút → dừng ghi thời gian.

## 7. SUS (3 phút)
Đưa phiếu `02_SUS_questionnaire.md`. Họ tự điền, không bàn luận.

## 8. Probe (5–8 phút)
Hỏi theo `03_probe_questions.md`, tập trung vào chỗ họ gặp khó.

## 9. Cảm ơn
> "Cảm ơn bạn. Thông tin của bạn chỉ dùng cho bài tập."

## Checklist trước mỗi buổi
- [ ] Reset DB + chạy lại `node seed_orders.mjs` (4 đơn mẫu), xóa localStorage / dùng cửa sổ ẩn danh
- [ ] Backend/web đang chạy, mở trang chủ ở cửa sổ ẩn danh
- [ ] Bắt đầu ghi màn hình
- [ ] Giấy kịch bản + phiếu SUS
- [ ] Đồng hồ bấm giờ
