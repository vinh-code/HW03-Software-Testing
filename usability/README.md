# Task 2 — bộ mô phỏng 1 pilot + 7 phiên

**KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.

Sinh viên: **Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn**.

Bộ này được thực hiện theo yêu cầu cập nhật của sinh viên: dùng mô phỏng cho bài tập. Thông tin giảng viên cho phép do sinh viên cung cấp; đề gốc lưu trong workspace vẫn yêu cầu người thật. Không ghi bộ này là đã phỏng vấn thật.

## Mở tài liệu

- [PDF toàn bộ hồ sơ](Task2_Simulation_Pack.pdf): tình huống, kế hoạch, lời dẫn, pilot, 7 phiên và phân tích.
- [Excel](Task2_Simulation.xlsx): hồ sơ, câu trả lời SUS, công thức, kết quả, timeline, probe và phát hiện.
- [Tình huống giao cho các hồ sơ](scenario.md); [kế hoạch](01_plan_objectives_scenario.md); [lời dẫn](04_moderator_script.md).
- [Pilot P00](sessions/pilot.md).
- [Phiên S01 — P01](sessions/S01.md).
- [Phiên S02 — P02](sessions/S02.md).
- [Phiên S03 — P03](sessions/S03.md).
- [Phiên S04 — P04](sessions/S04.md).
- [Phiên S05 — P05](sessions/S05.md).
- [Phiên S06 — P06](sessions/S06.md).
- [Phiên S07 — P07](sessions/S07.md).
- [Phân tích đã hoàn thiện](analysis.md).
- [Dữ liệu nguồn có nhãn simulated](data/simulation.json); [CSV SUS](sus_responses.csv); [số liệu tổng hợp](data/summary.json).

## Kết quả mô phỏng

4/7 hoàn thành không trợ giúp; 2/7 có trợ giúp; 1/7 hết giờ. SUS trung bình **58.93/100**. Pilot không được cộng vào mẫu. **0 phiên phỏng vấn thật, 0 người thật, 0 video thật.**

## Cập nhật và tính lại

Thông tin sinh viên đã điền sẵn. Các hồ sơ chỉ dùng mã P00–P07 và đặc điểm giả định; không cần điền tên hay liên hệ thật vào những câu trả lời tổng hợp này. Nếu sửa dữ liệu giả định, sửa `data/simulation.json` rồi chạy từ HW03:

```bash
python3 submission/usability/scripts/build_simulation.py
python3 submission/usability/sus_scoring.py submission/usability/sus_responses.csv
```

Workbook có cột SUS tính bằng Python để xem ngay và cột công thức Excel để đối chiếu; báo cáo là ảnh chụp số liệu tại lần sinh tài liệu. Không ghi đè workbook sau khi sửa tay nếu chưa chuyển chỉnh sửa về JSON nguồn.

Quy trình sinh tài liệu không liên hệ ai, không chạy server và không thay đổi SQLite.
