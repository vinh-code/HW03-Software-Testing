# HW03 – GUI & Usability (HW03-AI)

Sinh viên: `<Họ tên> – <MSSV>`  ·  Chủ đề: Lịch sử & Theo dõi đơn hàng (FR-10, FR-11)  ·  File nộp: `<MSSV>_HW03_AI_GUIUsability_<NNN>.zip`

## Test summary

| Chỉ số | Giá trị |
|---|---|
| Số màn hình đã test | |
| Số flow usability | 1 |
| Số mục checklist đã thiết kế | |
| Đã thực thi | |
| Passed | |
| Failed | |
| Số bug (GitHub Issues) | |
| Số participant (không tính pilot) | 7 |
| Số nền tảng cross-platform | |
| Link video demo | |

## Self-assessment

| No. | Tiêu chí | Điểm tối đa | Tự chấm |
|---|---|---|---|
| 1 | Task 1 – GUI Checklist (thiết kế + thực thi + bug report) | 30 | |
| 2 | Task 2 – Usability Evaluation (kịch bản + 7 buổi + phân tích) | 40 | |
| 3 | Task 3 – Cross-browser/platform (>= 3 nền tảng) | 20 | |
| 4 | Agent Skills | 10 | |
| | **Tổng** | **100** | |

## Cấu trúc thư mục

```
submission/
├── README.md                      <- file này (self-assessment + test summary)
├── report/main_report.md (+ .pdf) <- báo cáo chính (checklist + usability)
├── checklist/
│   ├── GUI_Checklist.xlsx         <- checklist >40 mục + Summary
│   ├── GUI_Checklist.md
│   └── build_checklist.py
├── bugs/                          <- bug report + screenshots (+ ảnh trang GitHub Issues)
├── usability/                     <- kế hoạch, kịch bản, SUS, participants, sessions, phân tích
├── cross_platform/                <- screenshots từ >=3 nền tảng
├── evidence/                      <- video ghi màn hình các buổi usability
├── ai_audit_report.md (+ .pdf)    <- (bạn tự làm) AI Audit Report
├── ai_critique.md                 <- (bạn tự làm) 200-300 từ
├── git_commit_log.txt             <- xuất bằng make_commit_log.sh
└── make_commit_log.sh
```

## Cách dựng và chạy SUT

SUT được clone ở `../sut` (ngoài thư mục nộp bài, không nén vào zip).

```bash
cd ../sut/backend && npm install && node database.js && node server.js   # http://localhost:3000
cd ../sut/frontend-web && npm install && npm run dev                      # http://localhost:5173
cd ../sut/frontend-admin && npm install && npm run dev                    # http://localhost:5174
cd ../sut/frontend-mobile && npm install && npx expo start                # Expo Go
```

Tài khoản (theo `sut/README.md`): admin `admin@eshop.com` / `Admin123!`, user `test@eshop.com` / `Test1234!`.
> `setup_guide.md` ghi mật khẩu admin là `admin123`, mâu thuẫn với README. Thử cả hai.

### Reset dữ liệu giữa các buổi usability
```bash
pkill -f "node server.js"
cd ../sut/backend && node database.js     # DROP + tạo lại toàn bộ bảng và seed mẫu
nohup node server.js > /dev/null 2>&1 &    # khởi động lại để đọc DB mới
cd ../../submission/usability && node seed_orders.mjs   # tạo 4 đơn: pending / confirmed / shipping / delivered
```
Sau đó dùng cửa sổ ẩn danh (hoặc xóa localStorage) để participant tự đăng nhập `test@eshop.com`.

## Quy trình git (mỗi bước một commit)

1. `checklist: design` · 2. `checklist: execution` · 3. `bugs: logged` ·
4. `usability: plan + pilot` · 5-11. `usability: session S01..S07` · 12. `usability: analysis` ·
13. `cross-platform: <platform>` · 14. `report + AI audit/critique`

Cuối cùng: `./make_commit_log.sh`.

## Danh sách kiểm tra trước khi nộp (thiếu tài liệu bắt buộc = 0 điểm)

- [ ] Báo cáo chính (MD + PDF)
- [ ] Bug report + ảnh GitHub Issues
- [ ] AI Critique (200-300 từ) + AI Audit Report (MD + PDF)
- [ ] Git commit log (text)
- [ ] Excel checklist (>40 mục) + test summary
- [ ] Bằng chứng usability: kịch bản, notes, SUS, findings theo severity, video, bảng 7 participant
- [ ] Screenshot cross-platform (có email + MSSV + họ tên)
- [ ] README này đã điền
- [ ] Tên zip đúng định dạng
