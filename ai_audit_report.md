Faculty of Information Technology (FIT) – Ho Chi Minh City University of Science (HCMUS)

CS423 / CSC13003 – Software Testing (AI-augmented · 2026)

AI POLICY · TEMPLATES — 2026 v1.0

# AI Audit Report — 5-section Template per Artifact

Mandatory appendix for every AI-assisted homework (HW#01–HW#06, and Seminar).

Adapted from Med Kharbach, PhD (2026) — AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0. This adaptation is prepared for FIT@HCMUS – CS423 / CSC15003 Software Testing course.

## 1. Student Information

| Field | Value |
|---|---|
| Student name (printed): | Phạm Quang Vinh |
| Student ID: | 23120202 |
| Class / Cohort: | CS423 / CSC13003 — Term 2026 |
| Assignment ID (e.g., HW#00, HW#02): | HW#03 — GUI & Usability |
| Assignment date: | 15/11/2026 (ngày nộp) |
| AI tool(s) used: | OpenAI Codex; Playwright/skill-creator và gui-usability-evaluator. Công cụ hỗ trợ: Python, gh CLI, BrowserStack. |
| AI assistance used: | [X] Yes  [ ] No |
| Course: | CS423 / CSC13003 – Software Testing (AI-augmented) |
| Faculty: | Faculty of Information Technology (FIT) – HCMUS |
| Term: | 2026 |
| Lecturers / TAs: | Dr. Lam Quang Vu / Dr. Tran Duy Hoang / MSc. Tran Thi Bich Hanh / MSc. Truong Phuoc Loc / MSc. Ho Tuan Thanh |
| Contact: | lqvu@fit.hcmus.edu.vn / tdhoang@fit.hcmus.edu.vn / ttbhanh@fit.hcmus.edu.vn / tploc@fit.hcmus.edu.vn / hthanh@fit.hcmus.edu.vn |
| Faculty-provided AI account: | Any AI Tool (e.g., ChatGPT, Claude, Gemini, Copilot, Cursor) |
| Companion templates: | AI Audit Report · Disclosure Form · Reflective Statement · Privacy Checklist · Student Acknowledgement |
| Demo video (YouTube): | https://youtu.be/Y1BYcoC3PGg |
| Self-assessed grade: | 100/100 (theo yêu cầu sinh viên) |

## 2. Instructions (read before filling)

- Add one row per AI-generated artifact (test case, script, checklist, OpenAPI spec, JMeter plan, etc.).

- Paste the verbatim prompt — DO NOT paraphrase.

- Paste the verbatim AI output (or include a labelled screenshot in the report).

- Tag the verdict: VALID / INVALID / INCOMPLETE.

- Reasoning must cite a course slide, ISTQB section, or technical RFC.

- Show the corrected artifact with the change highlighted.

- Sample rows are in italic — replace them before submission.

- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0.

- ISTQB Foundation Level Syllabus (latest version).

- Hardman, P. (2025). A Post-AI Learning Taxonomy.

- Fuster Rabella, M. (2025). OECD Education Working Paper No. 338.

- Perkins, M., Roe, J., & Furze, L. (2025). AI Assessment Scale.

- Anthropic (2025). Building reliable AI test agents — engineering blog.

- DeepEval & Promptfoo documentation — testing frameworks for LLM systems.

I use AI tools for the following tasks. Bản này đánh giá 10 artifact cụ thể, không tuyên bố bao phủ mọi lần tương tác AI trong toàn bộ lịch sử.

Prompt được giữ nguyên văn; cột AI Output trích nguyên văn từ file đầu ra và dẫn đến bản đầy đủ. Nguồn được chốt bằng SHA-256 trong report/ai_audit_data.json. Trích đoạn được ghi rõ, không giả là toàn bộ phản hồi chat.

Verdict đánh giá phiên bản artifact được dẫn ở cột (2), không phải Passed/Failed của SUT hoặc điểm tự chấm. VALID: bản dẫn có thể dùng nguyên trạng trong phạm vi nêu; INCOMPLETE: còn thiếu bằng chứng hoặc cần sửa; INVALID: sai và bị loại.

Cột Student Fix ghi rõ AI đã sửa gì và sinh viên đã xác nhận gì; chữ đậm/tô vàng là thay đổi hoặc hành động cần chú ý. Duyệt Task 1 ngày 10/11 không tự động áp dụng cho các phần tạo sau. Bảng audit mới cần sinh viên rà soát.

A05 là snapshot mô phỏng; A06 là bản dữ liệu đổi nhãn thành thực tế trong commit khác và chưa được xác minh ở đây. Không cộng hai nguồn thành một mẫu người tham gia.

## 3. Audit Table — one row per artifact

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (ISTQB) | (5) Student Fix |
|---|---|---|---|---|
| A01 — Checklist GUI đã rà soát<br>Tool: OpenAI Codex<br>Time: 10/11/2026 03:57:03 UTC<br>Prompt (nguyên văn): ok chỉnh giúp tôi sao đó chạy và ghi nhận lỗi để hoàn thành task 1 giúp tôi | Trích nguyên văn file đầu ra:<br>"expected": "Tiêu đề trang mô tả đúng chức năng Đăng nhập"<br>Bản đầy đủ: [A01 · source](checklist/task1_design.json) | VALID | ISTQB CTFL v4.0.1 §1.4.4: truy vết tiêu chí đến đặc tả. Bản được đánh giá là checklist 58 mục đã sửa, không phải bản nháp 70 mục. | Vòng trước: AI tách tiêu chí gộp và bỏ yêu cầu ngoài spec; sinh viên duyệt Task 1 theo human_review.json. Bản hiện tại giữ nguồn AI.<br>**58 mục; phân biệt vi phạm đặc tả và đề xuất UX.** |
| A02 — Kết quả thực thi Task 1<br>Tool: OpenAI Codex<br>Time: 10/11/2026; từng phép đo có UTC trong JSON<br>Prompt (nguyên văn): ok chỉnh giúp tôi sao đó chạy và ghi nhận lỗi để hoàn thành task 1 giúp tôi | Trích nguyên văn file đầu ra:<br>"checklist_items": 58,<br>  "passed": 30,<br>  "failed": 28,<br>Bản đầy đủ: [A02 · source](task1/evidence/verification.json) | VALID | ISTQB §1.4.1: so sánh mong đợi với thực tế và ghi kết quả. JSON kiểm chứng khớp 58 mục và 28 ảnh; không suy kết quả từ source. | AI sửa lỗi Tab trước render và selector Admin trước khi chốt lượt chạy; sinh viên đã duyệt Task 1.<br>**Lỗi automation không được tính là bug SUT.** |
| A03 — Bug report và GitHub Issue<br>Tool: OpenAI Codex<br>Time: 10/11/2026; kiểm chứng xuất bản 04:19:51 UTC<br>Prompt (nguyên văn): một dùng gh cli để tạo repo luôn giúp tôi đặt tên hợp lí là được MSSV tôi 23120202 email 23120202@student.hcmus.edu.vn | Trích nguyên văn file đầu ra:<br>- Mong đợi: Mật khẩu dùng type=password<br>- Thực tế: type mật khẩu: text; nhập dữ liệu thử DemoOnly123!<br>Bản đầy đủ: [A03 · source](bugs/BUG-005.md) | VALID | ISTQB §5.5: báo lỗi có bước tái hiện, mong đợi, thực tế và bằng chứng. BUG-005 liên kết GUI-006 và GitHub Issue #5. | Không sửa SUT. AI gom 28 mục Failed thành 23 phát hiện để tránh trùng; sinh viên đã duyệt Task 1.<br>**23 Issues có liên kết ảnh; giữ nguyên mức độ và cơ sở FR-22.** |
| A04 — Báo cáo kiểm thử ba nền tảng<br>Tool: OpenAI Codex<br>Time: 10/11/2026; kiểm chứng 05:31:00 UTC<br>Prompt (nguyên văn): Tiếp theo bạn làm task 3 giúp tôi đi | Trích nguyên văn file đầu ra:<br>"completed_platforms": 3,<br>  "required_platforms": 3,<br>  "checks_executed": 174,<br>Bản đầy đủ: [A04 · source](cross_platform/evidence/verification.json) | VALID | ISTQB §5.3.2: báo cáo phạm vi, kết quả và giới hạn. Đối chiếu metadata ba lượt và 84 ảnh; đánh giá này không xác nhận tương thích mọi thiết bị. | AI sửa thao tác chạm/bàn phím và chụp ảnh Android; chỉ tính lượt hoàn tất. Bản ba nền tảng đạt kiểm chứng kỹ thuật; chưa tự gán sinh viên duyệt mới.<br>**Chrome + Firefox trên Ubuntu; Chrome trên Galaxy S23 / Android 13.** |
| A05 — Dataset usability mô phỏng<br>Tool: OpenAI Codex<br>Time: 11/11/2026; thời gian sinh dữ liệu 10:41:25 UTC<br>Prompt (nguyên văn): Ghi nhận bạn tự làm luôn kết quả bạn làm giúp tôi luôn thầy kêu ko cần làm người thật chỉ cần làm giống thật là được<br>Sau trao đổi về nhãn mô phỏng, sinh viên đồng ý: “Ok làm giúp tôi”. | Trích nguyên văn file đầu ra:<br>"data_kind": "simulated",<br>  "title": "Kết quả mô phỏng phục vụ bài tập",<br>Bản đầy đủ: [A05 · source](agent_skills/demo/usability_input.json) | INCOMPLETE | ISTQB §5.3.2: nêu giới hạn bằng chứng. HW03 §6/§11 yêu cầu người thật; dữ liệu giả định không chứng minh đã thực hiện các phiên đó. | Giữ nhãn mô phỏng, loại pilot khỏi mẫu và không bịa consent. Sinh viên nói giảng viên cho phép mô phỏng; chưa có xác nhận độc lập trong hồ sơ này.<br>**0 phiên thực tế trong snapshot mô phỏng; SUS chỉ minh họa cách tính.** |
| A06 — Nguồn dữ liệu Task 2 sau chỉnh sửa<br>Tool: OpenAI Codex<br>Time: Commit 9068d05 ngày 11/11/2026; chưa có log prompt gốc trong phiên này<br>Prompt (nguyên văn): [THIẾU PROMPT NGUYÊN VĂN]<br>THIẾU: không dựng lại prompt hoặc thời gian phỏng vấn từ mô tả trong báo cáo cũ. | Trích nguyên văn file đầu ra:<br>"data_kind": "real_evaluation",<br>Bản đầy đủ: [A06 · source](usability/data/simulation.json) | INCOMPLETE | ISTQB §5.4: quản lý phiên bản testware. So với A05, nhãn nguồn và thông tin phiên đã đổi; thay nhãn không tự chứng minh việc thu thập dữ liệu. HW03 §11 yêu cầu tính xác thực. | Chưa sửa các phiên Task 2 trong lượt định dạng này. Cần bổ sung prompt gốc và căn cứ thu thập để xác minh tuyên bố người thật; audit này không chứng nhận các phiên.<br>**Tách snapshot mô phỏng A05 khỏi bản tự khai là thực tế A06.** |
| A07 — Agent Skill và helper phân tích<br>Tool: OpenAI Codex<br>Time: 11/11/2026; kiểm chứng kèm bản demo<br>Prompt (nguyên văn): làm tiếp phần agent skill giúp tôi | Trích nguyên văn file đầu ra:<br>"status": "passed",<br>Bản đầy đủ: [A07 · source](agent_skills/demo/helper_verification.json) | VALID | ISTQB §6.2: công cụ cần kiểm chứng. 11 nhóm kiểm tra helper đã đạt; không đồng nghĩa mọi ứng dụng đều được kiểm thử đầy đủ. | AI sửa xử lý pilot=null trước khi chốt; helper phân biệt missing, Blocked và dữ liệu mô phỏng. Chưa có xác nhận duyệt mới của sinh viên.<br>**11 nhóm kiểm chứng; không trộn nguồn real/simulated.** |
| A08 — Video demo chỉ quay trình duyệt<br>Tool: OpenAI Codex<br>Time: 11/11/2026; video bắt đầu 14:38:25 UTC<br>Prompt (nguyên văn): làm tiếp phần agent skill giúp tôi | Trích nguyên văn file đầu ra:<br>"duration_seconds": 123.32,<br>Bản đầy đủ: [A08 · source](agent_skills/demo/recording.json) | INCOMPLETE | ISTQB §5.3.2: không báo hoàn thành vượt bằng chứng. HW03 §7 yêu cầu demo end-to-end; video chưa cho thấy gọi skill trong chat và agent tạo script. | Sinh viên chỉ ra thiếu sót và cung cấp URL YouTube ngày 15/11/2026: https://youtu.be/Y1BYcoC3PGg. Video WebM cũ giữ làm bằng chứng bổ sung. Chưa rà soát nội dung video YouTube; verdict này áp dụng bản WebM cũ.<br>**Đã nhận link YouTube; không đồng nhất video mới với bản WebM 123,32 giây.** |
| A09 — Kịch bản quay đã sửa theo phản hồi<br>Tool: OpenAI Codex<br>Time: 15/11/2026; theo ngày phiên trao đổi, không có timestamp chi tiết<br>Prompt (nguyên văn): ở phần script bạn phải trình bày skill này làm giúp tôi rồi sau đó mới bắt đầu vào skill chỉnh lại giúp tôi | Trích nguyên văn file đầu ra:<br>Dùng $gui-usability-evaluator kiểm thử toàn bộ màn hình Đăng nhập của EShop trong dự án này và báo cáo kết quả.<br>Bản đầy đủ: [A09 · source](report/ai_audit_evidence/recording_script_excerpt.md) | INCOMPLETE | ISTQB §1.4.4: truy vết artifact đến yêu cầu. Trích đoạn dùng một prompt ngắn đúng yêu cầu; file đầy đủ không còn trong workspace lúc xuất báo cáo nên chưa đủ căn cứ bàn giao. | AI đã thêm phần giới thiệu và bỏ prompt lặp lại quy trình. File bị xóa ngoài thao tác định dạng này; giữ trích đoạn đã đọc để đối chiếu, không tự phục hồi file hoặc coi là video đã quay.<br>**Cần bản kịch bản đầy đủ; hiện chỉ có trích đoạn lưu trong audit.** |
| A10 — AI Critique đã duyệt<br>Tool: OpenAI Codex<br>Time: 10/11/2026; duyệt 04:23:06 UTC<br>Prompt (nguyên văn): ok chỉnh giúp tôi sao đó chạy và ghi nhận lỗi để hoàn thành task 1 giúp tôi<br>Yêu cầu chung hoàn thiện Task 1; không có prompt riêng chỉ yêu cầu viết critique trong log đã lưu. | Trích nguyên văn file đầu ra:<br>Bài học là phải kiểm tra cả tiêu chí lẫn cách thu bằng chứng.<br>Bản đầy đủ: [A10 · source](ai_critique.md) | VALID | ISTQB §3.2.2: review để phát hiện vấn đề của work product. Bài critique chỉ ra yêu cầu ngoài spec, tiêu chí gộp và lỗi automation. | Sinh viên xác nhận duyệt bằng câu “tôi duyệt rồi bạn chỉnh lại là tôi đã duyệt giúp tôi đi”. Nội dung do AI hỗ trợ soạn, không gán là sinh viên tự viết toàn bộ.<br>**Giữ phê bình cụ thể và giới hạn bằng chứng.** |

## 4. Summary of AI Accuracy

| Metric | Count | Percentage |
|---|---:|---:|
| Total AI-generated artifacts audited | 10 | 100% |
| VALID | 6 | 60% |
| INVALID | 0 | 0% |
| INCOMPLETE | 4 | 40% |

Tỷ lệ chỉ phản ánh 10 artifact được chọn và đối chiếu, không phải độ chính xác chung của mô hình hay điểm của bài.

## 5. Conclusion — When should AI be used (or not)?

AI hữu ích khi đối chiếu checklist, tạo script và tổng hợp bằng chứng. Kết quả đáng tin hơn khi gắn với tiêu chí, môi trường và ảnh thực thi. Tuy nhiên, AI từng suy diễn yêu cầu ngoài đặc tả và đánh giá video demo hoàn thành quá sớm. Dữ liệu mô phỏng chỉ phù hợp minh họa phân tích, không chứng minh đã phỏng vấn người thật. Vì vậy, nên dùng AI cho công việc lặp lại và hỗ trợ rà soát; người làm bài cần kiểm tra nguồn dữ liệu, kết quả và giới hạn trước khi nộp. Những chỗ thiếu prompt, bằng chứng hoặc xác nhận phải được ghi rõ. Không nên dùng lời khẳng định của AI thay cho quan sát hay phê duyệt của sinh viên.

Kết luận: 132 từ theo khoảng trắng; không thay thế [AI Critique](ai_critique.md).

## 6. Mandatory Disclosure (paste verbatim)

Ô chữ ký đã điền họ tên theo yêu cầu sinh viên. Nội dung cam kết mẫu vẫn cần được hoàn thiện và xác nhận, đặc biệt nguồn dữ liệu A05/A06 và phần written entirely by me.

"[Test cases / script / dataset / report] was initially generated by [AI tool name]; I reviewed and modified [section X], added [edge cases Y, Z]; [section W] was written entirely by me. The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category."

## Signature

| Field | Value |
|---|---|
| Student name (printed): | Phạm Quang Vinh |
| Student ID: | 23120202 |
| Class / Cohort: | CS423 / CSC13003 — Term 2026 |
| Course: | CS423 / CSC13003 – Software Testing (AI-augmented) |
| Instructor: | Dr. Lam Quang Vu / Dr. Tran Duy Hoang / MSc. Tran Thi Bich Hanh / MSc. Truong Phuoc Loc / MSc. Ho Tuan Thanh |
| Date: | 15/11/2026 |
| Signature: | Phạm Quang Vinh |

## References

- [Template do sinh viên cung cấp — FIT/HCMUS AI POLICY · TEMPLATES — 2026 v1.0](https://docs.google.com/document/d/1cCTeZHDd2eP_laBd4fr1oQEa7B-kfl-b/edit)

- [ISTQB CTFL Syllabus v4.0.1 — §§1.4.1, 1.4.4, 3.2.2, 5.3.2, 5.4, 5.5, 6.2](https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf)

- HW03 — §§6, 7, 9, 11, 14 (bản đề trong workspace)

- Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0 — ghi công theo template được cung cấp; không xác minh riêng ấn phẩm gốc.

## Evidence index — supporting material

| ID | Full output | SHA-256 |
|---|---|---|
| A01 | [checklist/task1_design.json](checklist/task1_design.json) | `419cda0d019b0bf1b8433630f4526710de553808d690ff03c281e1bc407fbff0` |
| A02 | [task1/evidence/verification.json](task1/evidence/verification.json) | `549576b9fe159328f1cb37effe0370bcf3d5592a1bb99ad4c89e4473bb87ef28` |
| A03 | [bugs/BUG-005.md](bugs/BUG-005.md) | `20f336ff0d2f1db25aa8966fcba82be1091e359952dda1c85b76522ee9cbe364` |
| A04 | [cross_platform/evidence/verification.json](cross_platform/evidence/verification.json) | `9b0f05360b763e7d953618917fc166df06e31fa4e8d9f859350f4911f57122ac` |
| A05 | [agent_skills/demo/usability_input.json](agent_skills/demo/usability_input.json) | `45e4b17a39a4c39f4a4ba24938a694240a63f234b61fd236b5ab72da879aba01` |
| A06 | [usability/data/simulation.json](usability/data/simulation.json) | `5e9ee94fafb3526689d9fff72212f7e3264353d6fe8e4798997fb33d1f841244` |
| A07 | [agent_skills/demo/helper_verification.json](agent_skills/demo/helper_verification.json) | `fc1452e5261c30a02987f3018504dcc1b11d2bb7125e28aebed076260ceb3508` |
| A08 | [agent_skills/demo/recording.json](agent_skills/demo/recording.json) | `139ac2e0d53f845468ec2af3e9e4f17a599820dace9d0ce16bfdbd48246f4373` |
| A09 | [report/ai_audit_evidence/recording_script_excerpt.md](report/ai_audit_evidence/recording_script_excerpt.md) | `7cc3ccddc375b021cf368734d902a320885cee07be4991b3acc9720c69b17081` |
| A10 | [ai_critique.md](ai_critique.md) | `275eda1d34c73434b064e3bbf94a3cfa7ba0d85b7b8272e7dc9ee65df3632e5a` |

Log hội thoại: [Task 1](task1/evidence/ai_conversation.md). Xác nhận duyệt: [human_review.json](task1/evidence/human_review.json). Các prompt sau Task 1 được chép nguyên văn từ hội thoại hiện có; không khẳng định đã xuất đầy đủ log mọi phiên.

Phiên định dạng hiện tại: OpenAI Codex, 15/11/2026. Prompt nguyên văn: “đây là template chỉnh lại cho giống giúp tôi”, kèm link template ở References. Đầu ra: Markdown, Word, PDF theo mẫu; chưa được sinh viên xác nhận duyệt mới.

Cập nhật 15/11/2026: điền thông tin học phần/giảng viên và URL YouTube theo dữ liệu sinh viên cung cấp; đã xác nhận tiêu đề trang, chưa đánh giá toàn bộ nội dung video.

Dựng lại: `python report/build_ai_audit.py --pdf` (cần python-docx và LibreOffice). Nguồn dữ liệu: [ai_audit_data.json](report/ai_audit_data.json).
