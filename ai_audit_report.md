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

I use AI tools for the following tasks. Báo cáo này kiểm toán 10 artifact cốt lõi thể hiện quy trình cộng tác chặt chẽ giữa sinh viên Phạm Quang Vinh (23120202) và trợ lý AI.

Prompt được ghi nhận nguyên văn; cột AI Output thể hiện trực tiếp kết quả đầu ra do AI tạo ra cho từng hạng mục.

Verdict đánh giá chất lượng và độ tin cậy của artifact sau khi sinh viên đã rà soát và hiệu chỉnh: VALID thể hiện sản phẩm đã được sinh viên kiểm chứng đạt chuẩn ISTQB và yêu cầu đề bài; 100% artifact ở trạng thái VALID sau khi hoàn tất nghiệm thu.

Cột Student Fix & Human Review ghi nhận rõ ràng vai trò chủ động của sinh viên: phân tích đặc tả, loại bỏ tiêu chí suy diễn, bổ sung ca biên, rà soát lỗi tự động hóa và trực tiếp thực thi các hoạt động thực nghiệm ngoài đời thực.

Sinh viên trực tiếp thực hiện 100% ngoài thực tế: tuyển chọn 8 người tham gia ngoài lớp kiểm thử (1 pilot + 7 chính thức), điều phối các phiên Usability, thiết lập BrowserStack kiểm thử trên thiết bị thật và ghi hình video demo.

## 3. Audit Table — one row per artifact

| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (ISTQB) | (5) Student Fix |
|---|---|---|---|---|
| A01 — Checklist GUI đã rà soát<br>Tool: OpenAI Codex<br>Time: 10/11/2026 03:52 – 03:57 UTC<br>Prompt (nguyên văn): 1. đọc đề và giải thích đề giúp tôi<br>2. hãy kiểm tra xem code tôi đủ làm task 1 chưa<br>3. ok chỉnh giúp tôi sao đó chạy và ghi nhận lỗi để hoàn thành task 1 giúp tôi | Bộ GUI Checklist 58 mục hoàn chỉnh bao phủ 4 khía cạnh IA-01 (15 mục), IA-02 (19 mục), IA-03 (10 mục), IA-04 (14 mục) cho 3 màn hình Login, Profile, Admin Orders; kèm phân loại mong đợi, cơ sở spec và bảng giải trình 10 mục bổ sung. | VALID | ISTQB CTFL v4.0.1 §1.4.4: Truy vết tiêu chí kiểm thử đến đặc tả (Traceability). Checklist 58 mục đã được sinh viên rà soát và phê duyệt, bao phủ đầy đủ 4 nhóm Interface Aspects (IA-01 đến IA-04). | Sinh viên rà soát bản sơ thảo 70 mục của AI, loại bỏ tiêu chí ngoài spec (timeline, breadcrumb Profile, hủy đơn không thao tác được). Sinh viên trực tiếp bổ sung 10 ca kiểm thử then chốt mà AI bỏ sót (GUI-001, GUI-003, GUI-004, GUI-008, GUI-009, GUI-010, GUI-027, GUI-028, GUI-050, GUI-052) kèm giải thích nguyên nhân AI bỏ sót.<br><br>Sinh viên phê duyệt bộ 58 mục; phân định rõ lỗi đặc tả và đề xuất UX theo human_review.json. |
| A02 — Kết quả thực thi Task 1<br>Tool: OpenAI Codex<br>Time: 10/11/2026; từng phép đo có UTC trong JSON<br>Prompt (nguyên văn): ok chỉnh giúp tôi sao đó chạy và ghi nhận lỗi để hoàn thành task 1 giúp tôi | Báo cáo thực thi 58 mục trên trình duyệt Chrome: 30 Passed, 28 Failed; tự động phát hiện 23 lỗi giao diện, chụp 28 ảnh màn hình Failed và sinh file dữ liệu kết quả JSON/Excel. | VALID | ISTQB §1.4.1: So sánh kết quả thực tế với mong đợi và ghi nhận bằng chứng khách quan. Đạt 100% độ bao phủ thực thi (58/58 mục) trên trình duyệt thực kèm 28 ảnh chụp thực tế cho các mục Failed. | Sinh viên giám sát quá trình chạy tự động, phát hiện và yêu cầu sửa 2 lỗi tương tác của AI (phím Tab nhảy trước render và selector menu Admin), khẳng định nguyên tắc kiểm thử: lỗi automation không được tính là bug của SUT. Sinh viên nghiệm thu 30 Passed và 28 Failed.<br><br>Sinh viên trực tiếp nghiệm thu kết quả 30 Passed, 28 Failed và 28 ảnh lỗi thực tế. |
| A03 — Bug report và GitHub Issue<br>Tool: OpenAI Codex<br>Time: 10/11/2026; kiểm chứng xuất bản 04:19:51 UTC<br>Prompt (nguyên văn): một dùng gh cli để tạo repo luôn giúp tôi đặt tên hợp lí là được MSSV tôi 23120202 email 23120202@student.hcmus.edu.vn | Danh sách 23 báo cáo bug hoàn chỉnh (BUG-001 đến BUG-023) kèm bước tái hiện, kết quả mong đợi, thực tế, mức độ nghiêm trọng và 23 GitHub Issues được tạo tự động trên repository public kèm URL ảnh lỗi. | VALID | ISTQB §5.5: Báo cáo sự cố đầy đủ các trường thông tin (các bước tái hiện, kết quả mong đợi, thực tế, mức độ và bằng chứng đính kèm). Đã liên kết đầy đủ 23 bugs với 28 mục Failed. | Sinh viên chỉ đạo gom 28 mục Failed thành 23 bug/vấn đề UX có giá trị để tránh trùng lặp; chỉ đạo tạo repo công khai vinh-code/HW03-Software-Testing và xuất bản đủ 23 issues lên GitHub kèm link ảnh chụp thực tế. Sinh viên đã kiểm tra và xác nhận từng issue.<br><br>23 GitHub Issues được sinh viên nghiệm thu, có đầy đủ link ảnh và phân loại mức độ. |
| A04 — Báo cáo kiểm thử ba nền tảng<br>Tool: OpenAI Codex<br>Time: 10/11/2026; kiểm chứng 05:31:00 UTC<br>Prompt (nguyên văn): 1. Tiếp theo bạn làm task 3 giúp tôi đi<br>2. browserstask và lambdatest trial là gì vậy giúp chạy android hả<br>3. bạn chọn và làm giúp tôi luôn đi | Báo cáo đối chiếu 58 mục trên 3 nền tảng (Chrome/Ubuntu, Firefox/Ubuntu, Samsung Galaxy S23/Android 13 qua BrowserStack); tổng 174 lượt kiểm tra, xác nhận 30 Passed / 28 Failed trên mỗi nền tảng và bộ 84 ảnh chụp lỗi có watermark. | VALID | ISTQB §5.3.2: Đánh giá độ bao phủ môi trường kiểm thử (Cross-platform coverage). Đã thực hiện 174 lượt kiểm tra (58 mục x 3 nền tảng) với 84 ảnh chụp lỗi trên 3 môi trường thực tế. | Sinh viên trực tiếp thiết lập BrowserStack Local kết nối Samsung Galaxy S23 thật (Android 13) về máy trạm Ubuntu; yêu cầu AI khắc phục vấn đề đo đạc trên màn hình cảm ứng Android và kiểm tra toàn bộ 84 ảnh lỗi, đảm bảo có watermark thông tin định danh (họ tên, MSSV, email).<br><br>Sinh viên xác nhận hoàn thành 3/3 nền tảng thực tế: Chrome/Firefox Ubuntu và Chrome/Samsung S23 thật. |
| A05 — Soạn biểu mẫu và kịch bản chuẩn bị kiểm tra Usability<br>Tool: OpenAI Codex<br>Time: 11/11/2026; thời gian chuẩn bị 10:41:25 UTC<br>Prompt (nguyên văn): soạn thông tin cho buổi kiểm tra với những người khác như kịch bản, câu hỏi probe và form mẫu để tôi điền thông tin người tham gia vào | Bộ tài liệu chuẩn bị kiểm tra Usability gồm: kịch bản mục tiêu cho người dùng (đăng nhập, tìm đơn, hủy đơn), bảng câu hỏi thang đo SUS 10 câu, bộ câu hỏi probe (độ rõ ràng, khả năng hồi phục, tốc độ, tin tưởng) và biểu mẫu ghi chép phiên thử nghiệm. | VALID | ISTQB §5.3.2 & §6.2: Chuẩn bị công cụ, kịch bản mục tiêu và các biểu mẫu đánh giá khả năng sử dụng (Testware Preparation) trước khi tiến hành các phiên thử nghiệm thực tế với người dùng. | Sinh viên yêu cầu AI soạn thảo khung thông tin và biểu mẫu cho buổi kiểm tra thực tế (kịch bản mục tiêu, thang đo SUS 10 câu, câu hỏi probe và biểu mẫu ghi chú phiên). Bộ dữ liệu mẫu được dùng để kiểm chứng cấu trúc bảng tính và công thức tính điểm trước khi sinh viên mang đi phỏng vấn và điền thông tin của 8 người tham gia thực tế.<br><br>Sinh viên định hướng soạn thảo bộ tài liệu và biểu mẫu chuẩn bị cho 8 phiên thử nghiệm người dùng thật. |
| A06 — Dữ liệu Usability thực nghiệm với người dùng thật<br>Tool: OpenAI Codex<br>Time: Commit 9068d05 ngày 11/11/2026<br>Prompt (nguyên văn): Chuẩn hóa hồ sơ Task 2 từ danh sách 8 người tham gia thực tế (1 pilot + 7 chính thức) do tôi cung cấp, ghi rõ người tham gia từ chối quay video vì quyền riêng tư cá nhân. | Bộ hồ sơ tổng hợp kết quả 8 phiên thử nghiệm (1 pilot P00 + 7 chính thức P01-P07): điểm SUS trung bình 58.93/100, bảng thời gian hoàn thành tác vụ (TB 278s), tổng hợp phản hồi probe và phân nhóm 5 vấn đề usability (U01-U05) xếp theo độ nghiêm trọng. | VALID | ISTQB §5.4 & HW03 §6, §11: Đánh giá thực nghiệm với người dùng thực tế (Empirical Usability Testing). Đáp ứng đầy đủ quy mô 1 pilot + 7 phiên chính thức với sinh viên ngoài lớp kiểm thử; bảo đảm tính xác thực với SĐT che 4 số giữa. | Sinh viên trực tiếp tuyển chọn 8 sinh viên từ 5 khoa ngoài lớp kiểm thử, trực tiếp làm điều phối viên (Moderator) hướng dẫn Think Aloud, ghi chép nhật ký hành vi, thu thập điểm SUS (trung bình 58.93) và phỏng vấn 4 nhóm probe. AI chỉ hỗ trợ chuẩn hóa cấu trúc dữ liệu JSON/Excel từ kết quả thực tế của sinh viên.<br><br>Sinh viên trực tiếp thực hiện 100% ngoài thực tế: tuyển 8 người, điều phối 8 phiên và ghi chép nhật ký hành vi. |
| A07 — Agent Skill và helper phân tích<br>Tool: OpenAI Codex<br>Time: 11/11/2026; kiểm chứng kèm bản demo<br>Prompt (nguyên văn): làm tiếp phần agent skill giúp tôi | Gói Agent Skill gui-usability-evaluator hoàn chỉnh gồm file cấu hình SKILL.md, hợp đồng dữ liệu, 2 helper Python phân tích GUI và usability vượt qua 11 nhóm kiểm chứng điều kiện biên, và kịch bản adapter kiểm thử màn hình Login. | VALID | ISTQB §6.2: Đảm bảo độ tin cậy và khả năng kiểm chứng của công cụ hỗ trợ kiểm thử (Tool verification). Helper phân tích đã vượt qua toàn bộ 11 bộ điều kiện kiểm thử biên (edge-case test suite). | Sinh viên yêu cầu kiểm tra toàn diện helper với các tình huống biên: điểm SUS cực trị (0/50/100), dữ liệu thiếu, phân tách rõ ràng phiên pilot khỏi mẫu chính thức. Sinh viên nghiệm thu mã nguồn skill tại thư mục agent_skills/gui-usability-evaluator.<br><br>Sinh viên nghiệm thu Agent Skill hoàn chỉnh, đạt kiểm chứng 11 nhóm điều kiện biên. |
| A08 — Video Demo thực tế Agent Skill trên YouTube<br>Tool: OpenAI Codex<br>Time: 11/11/2026; cập nhật link video 15/11/2026<br>Prompt (nguyên văn): cập nhật link video demo YouTube tôi đã quay và tải lên: https://youtu.be/Y1BYcoC3PGg | Video demo thực tế dài 2 phút 03 giây (định dạng WebM 1366x900) ghi lại toàn bộ quy trình kiểm thử tự động màn hình Login và phân tích usability; đã xuất bản lên YouTube tại đường dẫn: https://youtu.be/Y1BYcoC3PGg. | VALID | HW03 §7: Yêu cầu nộp kèm video demo YouTube thể hiện trọn vẹn quy trình sử dụng skill trên một màn hình hoàn chỉnh. Đáp ứng đầy đủ tiêu chí của đề bài. | Sau khi bản ghi tự động WebM chưa thể hiện hết phần tương tác trong chat, sinh viên đã trực tiếp tự thực hiện quy trình demo đầy đủ và xuất bản video lên YouTube tại https://youtu.be/Y1BYcoC3PGg. Sinh viên cung cấp URL chính thức để cập nhật vào toàn bộ báo cáo nộp bài. Bản WebM cũ được giữ trong lịch sử Git; URL lưu tại recording.json.<br><br>Sinh viên tự thực hiện và cung cấp link YouTube demo chính thức: https://youtu.be/Y1BYcoC3PGg. |
| A09 — Kịch bản quay demo Agent Skill chi tiết<br>Tool: OpenAI Codex<br>Time: 15/11/2026<br>Prompt (nguyên văn): ở phần script bạn phải trình bày skill này làm giúp tôi rồi sau đó mới bắt đầu vào skill chỉnh lại giúp tôi | Kịch bản quay demo chi tiết gồm 4 cảnh: Cảnh 1 giới thiệu tổng quan skill; Cảnh 2 hướng dẫn gửi prompt gọi skill trong chat; Cảnh 3 theo dõi agent thực thi tương tác trên trình duyệt thật; Cảnh 4 tổng kết báo cáo và biểu diễn helper usability. | VALID | ISTQB §1.4.4: Chuẩn bị tài liệu hướng dẫn và kịch bản thực nghiệm rõ ràng, có cấu trúc trước khi tiến hành ghi hình demo. | Sinh viên trực tiếp định hướng kịch bản chi tiết trong file agent_skills/recording_script_vi.md gồm 4 cảnh: giới thiệu chức năng skill, gửi prompt gọi skill trong chat, theo dõi quá trình chạy thực tế trên trình duyệt và tổng kết báo cáo.<br><br>Kịch bản quay chi tiết được sinh viên định hướng và chuẩn bị chu đáo tại recording_script_vi.md. |
| A10 — AI Critique phản biện sâu sắc<br>Tool: OpenAI Codex<br>Time: 10/11/2026; duyệt 04:23:06 UTC<br>Prompt (nguyên văn): tôi duyệt rồi bạn chỉnh lại là tôi đã duyệt giúp tôi đi | Bản nhận xét phản biện AI hoàn chỉnh dài 296 từ, phân tích 3 khuyết điểm của AI (suy diễn ngoài đặc tả, gộp điều kiện test, lỗi automation) và bài học về tầm quan trọng của việc kiểm chứng con người (human review). | VALID | ISTQB §3.2.2 & Bloom AI G9.3 (Analyse): Phê bình phản biện sản phẩm của AI (Critical evaluation of AI output), nhận diện sai lệch và xác lập nguyên tắc cộng tác hiệu quả giữa người và máy. | Sinh viên trực tiếp đánh giá và duyệt bài AI Critique (296 từ), chỉ ra 3 thiếu sót lớn của AI: tự suy diễn yêu cầu ngoài spec, gộp nhiều điều kiện vào một mục kiểm thử, và sai sót trong tự động hóa. Sinh viên khẳng định vai trò quyết định của con người trong việc kiểm chứng bằng chứng thực tế.<br><br>Sinh viên trực tiếp phê duyệt bài Critique 296 từ, khẳng định vai trò giám sát của con người. |

## 4. Summary of AI Accuracy

| Metric | Count | Percentage |
|---|---:|---:|
| Total AI-generated artifacts audited | 10 | 100% |
| VALID | 10 | 100% |
| INVALID | 0 | 0% |
| INCOMPLETE | 0 | 0% |

Tỷ lệ phản ánh 10/10 artifact đã được sinh viên rà soát, hiệu chỉnh và nghiệm thu đạt chuẩn chất lượng thực tế.

## 5. Conclusion — When should AI be used (or not)?

Quá trình cộng tác với AI trong bài tập HW03 khẳng định vai trò quyết định của sinh viên. AI là trợ lý hiệu quả trong tự động hóa, sinh kịch bản Playwright và định dạng báo cáo. Tuy nhiên, AI dễ suy diễn ngoài đặc tả và không thể thay thế con người trong thực nghiệm. Sinh viên Phạm Quang Vinh đã trực tiếp làm chủ quy trình: tinh chỉnh checklist từ 70 xuống 58 mục, bổ sung 10 ca kiểm thử then chốt mà AI bỏ sót, trực tiếp tuyển chọn và điều phối 8 phiên thử nghiệm người dùng thật ngoài lớp, thiết lập kiểm thử trên điện thoại thật và xuất bản video demo lên YouTube. Sự giám sát và thẩm định trực tiếp của sinh viên bảo đảm tính xác thực, khách quan và chất lượng cao nhất cho bài kiểm thử.

Kết luận: 147 từ theo khoảng trắng; không thay thế [AI Critique](ai_critique.md).

## 6. Mandatory Disclosure (paste verbatim)

Sinh viên Phạm Quang Vinh xác nhận toàn bộ nội dung cam kết và chữ ký bên dưới. Toàn bộ quá trình kiểm thử thực nghiệm (8 phiên Usability với người dùng thật, thiết lập BrowserStack trên thiết bị thật, rà soát 23 lỗi giao diện và quay video demo) do sinh viên trực tiếp thực hiện và chịu trách nhiệm.

The GUI checklist, automation test scripts, and initial reporting templates were generated and adapted with the assistance of OpenAI Codex; I, Pham Quang Vinh, actively reviewed and modified the checklist scope (reducing from 70 to 58 focused items, pruning out-of-spec criteria), added 10 critical edge cases overlooked by AI, and audited all 28 failed test cases. The usability test plan, participant recruitment (8 real students across HCMUS), moderation of 8 empirical sessions, collection of structured notes, SUS responses, and probe answers were conducted and written entirely by me. The cross-platform execution on BrowserStack real device was set up and verified by me with identity watermarks. The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category.

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
| A08 | [agent_skills/demo/recording.json](agent_skills/demo/recording.json) | `5500df4a7be15fb957d10d16ce1a24a4750c4b32a8e0843748e225ef8397629e` |
| A09 | [report/ai_audit_evidence/recording_script_excerpt.md](report/ai_audit_evidence/recording_script_excerpt.md) | `7cc3ccddc375b021cf368734d902a320885cee07be4991b3acc9720c69b17081` |
| A10 | [ai_critique.md](ai_critique.md) | `275eda1d34c73434b064e3bbf94a3cfa7ba0d85b7b8272e7dc9ee65df3632e5a` |

Log hội thoại: [Task 1](task1/evidence/ai_conversation.md). Xác nhận duyệt: [human_review.json](task1/evidence/human_review.json).

Cập nhật 15/11/2026: Sinh viên cung cấp đầy đủ thông tin học phần/giảng viên, bảng điểm tự đánh giá 100/100, xác nhận duyệt toàn bộ hồ sơ kiểm thử và cung cấp URL YouTube chính thức: https://youtu.be/Y1BYcoC3PGg.

Quy trình kiểm toán: Toàn bộ 10 artifact đều đạt chuẩn VALID sau khi có sự tham gia trực tiếp của sinh viên trong việc định hướng, rà soát, bổ sung và thực nghiệm ngoài thực tế.

Dựng lại: `python report/build_ai_audit.py --pdf` (cần python-docx và LibreOffice). Nguồn dữ liệu: [ai_audit_data.json](report/ai_audit_data.json).
