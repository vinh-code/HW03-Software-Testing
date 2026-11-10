# Thang SUS (System Usability Scale) – bản tiếng Việt

Participant đánh giá mỗi câu từ **1 (Hoàn toàn không đồng ý)** đến **5 (Hoàn toàn đồng ý)**.
Hoàn thành **ngay sau** tác vụ, trước khi hỏi probe.

| # | Câu | 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|---|---|
| 1 | Tôi nghĩ tôi sẽ muốn dùng trang web này thường xuyên. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 2 | Tôi thấy trang web này phức tạp một cách không cần thiết. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 3 | Tôi thấy trang web này dễ sử dụng. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 4 | Tôi nghĩ tôi cần sự hỗ trợ của người có chuyên môn để dùng được trang web này. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 5 | Tôi thấy các chức năng trong trang web này được tích hợp tốt. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 6 | Tôi thấy trang web này có quá nhiều điểm không nhất quán. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 7 | Tôi nghĩ hầu hết mọi người sẽ học cách dùng trang web này rất nhanh. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 8 | Tôi thấy trang web này rất cồng kềnh, khó dùng. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 9 | Tôi cảm thấy rất tự tin khi dùng trang web này. | ☐ | ☐ | ☐ | ☐ | ☐ |
| 10 | Tôi cần học nhiều thứ trước khi có thể bắt đầu dùng trang web này. | ☐ | ☐ | ☐ | ☐ | ☐ |

## Cách tính điểm

- Câu **lẻ** (1,3,5,7,9): điểm đóng góp = `câu trả lời − 1`
- Câu **chẵn** (2,4,6,8,10): điểm đóng góp = `5 − câu trả lời`
- **SUS = tổng 10 đóng góp × 2.5** (thang 0-100)

## Diễn giải (tham khảo, Sauro & Lewis)

| SUS | Mức |
|---|---|
| ≥ 80.3 | A – Xuất sắc |
| 68 – 80.2 | B/C – Tốt / Trung bình (68 là trung bình ngành) |
| 51 – 67.9 | D – Dưới trung bình |
| < 51 | F – Kém |

## Nhập kết quả

Điền `sus_responses.csv` (1 dòng/participant, cột q1…q10), rồi chạy:

```bash
python3 sus_scoring.py sus_responses.csv
```
