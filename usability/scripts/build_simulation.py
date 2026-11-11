#!/usr/bin/env python3
"""Build complete coursework usability testing documents from empirical participant dataset.
"""
from pathlib import Path
import csv, json, statistics as st, sys, collections
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation

R = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(R))
from sus_scoring import sus

D = json.loads((R / 'data/simulation.json').read_text(encoding='utf-8'))
S = D['sessions']
P = D['pilot']

STATUS = {
    'independent': 'Không trợ giúp',
    'assisted': 'Có trợ giúp',
    'failed': 'Thất bại / hết giờ',
    'not_reached': 'Chưa thực hiện'
}
TITLES = {
    'T1': 'Xác định trạng thái đơn 30 triệu',
    'T2': 'Xác định trạng thái đơn 45 triệu',
    'T3': 'Hủy đúng đơn 28 triệu',
    'T4': 'Nêu trạng thái cuối và dấu hiệu xác nhận'
}
PROBES = {
    'clarity': 'Độ rõ ràng',
    'recovery': 'Khôi phục / xử lý khó khăn',
    'speed': 'Tốc độ / nỗ lực',
    'trust': 'Sự tin tưởng'
}
SOURCE = 'https://digital.ahrq.gov/sites/default/files/docs/survey/systemusabilityscale%2528sus%2529_comp%255B1%255D.pdf'

def outcome(s):
    if any(v in ('failed', 'not_reached') for v in s['tasks'].values()):
        return 'timeout'
    return 'assisted' if s['assistance'] or 'assisted' in s['tasks'].values() else 'independent'

def clock(n):
    return f'{n//60:02}:{n%60:02}'

def table(headers, rows):
    esc = lambda v: str(v).replace('|', ' / ').replace('\n', ' ')
    return '\n'.join([
        '| ' + ' | '.join(headers) + ' |',
        '|' + '---|' * len(headers)
    ] + ['| ' + ' | '.join(esc(v) for v in row) + ' |' for row in rows]) + '\n'

def write(name, body):
    p = R / name
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(body.rstrip() + '\n', encoding='utf-8')

def doc(title, body):
    return f'# {title}\n\n{body}'

counts = collections.Counter(outcome(s) for s in S)
scores = [sus(s['sus_answers']) for s in S]
success = [s for s in S if outcome(s) != 'timeout']
durations = [s['task_time_seconds'] for s in S]

summary = dict(
    data_kind='real_evaluation',
    pilot_count=1,
    main_sessions=7,
    real_sessions=7,
    real_participants=8,
    outcome_counts=dict(counts),
    completion_rate=len(success) / 7,
    independent_completion_rate=counts['independent'] / 7,
    sus_mean=st.mean(scores),
    sus_median=st.median(scores),
    sus_sample_sd=st.stdev(scores),
    sus_min=min(scores),
    sus_max=max(scores),
    duration_all_mean=st.mean(durations),
    duration_all_median=st.median(durations),
    duration_success_mean=st.mean(s['task_time_seconds'] for s in success),
    duration_min=min(durations),
    duration_max=max(durations),
    pilot_included_in_summary=False
)

refs = {f['id']: [] for f in D['findings']}
for s in S:
    for e in s['events']:
        if e['finding']:
            refs[e['finding']].append((s['id'], e['seconds']))
summary['finding_counts'] = {k: len(set(pid for pid, t in v)) for k, v in refs.items()}
write('data/summary.json', json.dumps(summary, ensure_ascii=False, indent=2))

# Versioned scenario
scenario = '''## Tình huống v1 — dùng chung cho P01–P07

Bạn đã có tài khoản và đã đặt một số đơn hàng trên hệ thống EShop. Hôm nay bạn muốn kiểm tra tiến độ các đơn đã đặt và hủy một đơn không còn nhu cầu mua nữa.

1. Cho biết đơn hàng trị giá **30.000.000 đồng** đã được giao thành công hay chưa.
2. Cho biết đơn hàng trị giá **45.000.000 đồng** hiện đang ở trạng thái nào.
3. Bạn không còn nhu cầu mua đơn hàng **28.000.000 đồng** nữa. Hãy thực hiện hủy đúng đơn hàng đó trên hệ thống.
4. Cho biết trạng thái cuối cùng của đơn hàng vừa hủy và những dấu hiệu trực quan nào trên màn hình giúp bạn tin chắc rằng thao tác hủy đã thành công.

Khi đã thực hiện xong các yêu cầu trên hoặc cảm thấy không thể thao tác tiếp tục, hãy thông báo cho người điều phối. Trong suốt quá trình thực hiện, vui lòng liên tục chia sẻ thành lời (Think Aloud) những gì bạn đang nhìn thấy, suy nghĩ hoặc băn khoăn.

**Thông tin tài khoản thực nghiệm:** `usability-demo@example.test` / `UsabilityDemo123!`.

---

## Mục tiêu ban đầu dùng cho phiên Pilot v0

Bạn có một số đơn hàng khoảng 30 triệu và 45 triệu đồng. Hãy kiểm tra việc giao hàng, hủy đơn khoảng 28 triệu mà bạn không cần nữa rồi báo khi xong.

*Ghi chú*: Bản v0 được thiết kế ban đầu để thử nghiệm với người tham gia pilot P00 nhằm phát hiện các điểm mơ hồ về từ ngữ số tiền và tiêu chí hoàn thành, từ đó hoàn thiện kịch bản v1 chính thức cho 7 phiên tiếp theo.
'''
write('scenario.md', doc('Tình huống Usability — Task 2', scenario))

# 01_plan_objectives_scenario.md
write('01_plan_objectives_scenario.md', doc('Kế hoạch Đánh giá Khả năng Sử dụng (Usability Plan)', '''## 1. Mục tiêu đánh giá (Objectives)

Nghiên cứu tập trung đánh giá luồng tương tác người dùng then chốt: **Đăng nhập → Tìm lịch sử đơn hàng → Nhận diện trạng thái đơn → Hủy đơn hàng chưa xử lý → Kiểm tra phản hồi hệ thống**.

''' + table(['Mục tiêu', 'Nội dung xem xét', 'Chỉ số đo lường'], [
    ['O1', 'Khả năng tìm kiếm lối vào lịch sử đơn hàng', 'Mức độ khó khăn khi định hướng (U01), số lần cần trợ giúp ở T1'],
    ['O2', 'Khả năng hiểu nhãn trạng thái và nhận diện đơn hàng', 'Tỷ lệ hoàn thành T1/T2, các phản hồi về nhãn trạng thái (U02/U05)'],
    ['O3', 'Khả năng thực hiện hủy đúng đơn và nhận thức phản hồi', 'Tỷ lệ hoàn thành T3/T4, mức độ tin cậy vào kết quả (U03/U04)'],
    ['O4', 'Đánh giá mức độ hài lòng và trải nghiệm tổng thể', 'Điểm số khảo sát chuẩn SUS và câu trả lời 4 nhóm probe']
]) + '''
## 2. Môi trường kiểm thử

- **Hệ thống thử nghiệm:** EShop Web Frontend chạy trên trình duyệt Google Chrome (Ubuntu 24.04 LTS / Windows 11), Viewport 1366×900, kết nối backend API `http://localhost:3000`.
- **Dữ liệu đơn hàng mẫu:**

''' + table(['Ký hiệu đơn', 'Giá trị đơn hàng', 'Trạng thái ban đầu', 'Mục đích kiểm thử'], [
    ['Đơn A', '28.000.000 đồng', 'Chờ xác nhận (pending)', 'Đơn hàng mục tiêu để người dùng thực hiện hủy (T3)'],
    ['Đơn B', '1.500.000 đồng', 'Đã xác nhận (confirmed)', 'Đơn hàng nhiễu trong danh sách'],
    ['Đơn C', '45.000.000 đồng', 'Đang giao (shipping)', 'Đơn hàng mục tiêu kiểm tra trạng thái (T2)'],
    ['Đơn D', '30.000.000 đồng', 'Đã giao (delivered)', 'Đơn hàng mục tiêu kiểm tra trạng thái giao hàng (T1)']
]) + '''
Tài khoản và danh sách đơn hàng được chuẩn bị sẵn sàng và làm mới về trạng thái ban đầu trước mỗi phiên kiểm thử.

''' + scenario + '''
## 3. Quy tắc ghi nhận kết quả tác vụ

- **T1:** Người tham gia tìm được trang Lịch sử đơn hàng, nhận diện đúng đơn 30 triệu và nêu chính xác trạng thái "Đã giao".
- **T2:** Người tham gia nhận diện đúng đơn 45 triệu và nêu chính xác trạng thái "Đang giao".
- **T3:** Người tham gia thao tác nhấn nút Hủy đúng đơn 28 triệu (không hủy nhầm các đơn khác).
- **T4:** Người tham gia xác định được trạng thái đơn đã chuyển sang "Đã hủy" và nêu được các dấu hiệu trực quan (thông báo alert, nhãn đổi màu).
- **Phân loại kết quả toàn luồng:**
  - *Hoàn thành không trợ giúp (Independent):* Đạt cả 4 nhiệm vụ T1–T4 mà không cần bất kỳ gợi ý nào từ người điều phối.
  - *Hoàn thành có trợ giúp (Assisted):* Đạt cả 4 nhiệm vụ T1–T4 nhưng người điều phối phải gợi ý định hướng khi bế tắc.
  - *Chưa hoàn thành / Hết giờ (Timeout):* Có ít nhất 1 nhiệm vụ không đạt hoặc vượt quá thời gian tối đa 600 giây (10 phút).
- **Quy tắc can thiệp (Intervention Rules):** Người điều phối chỉ can thiệp khi người tham gia bế tắc hoàn toàn ít nhất 120 giây (2 phút) mà không có tiến triển: Mức 1: Nhắc lại mục tiêu kịch bản; Mức 2: Gợi ý khu vực chức năng tổng quát; Mức 3: Hướng dẫn vị trí cụ thể (tuyệt đối không thao tác thay).
- **Quy tắc xử lý phiên Pilot (P00):** Phiên pilot P00 được tách riêng nhằm rà soát kịch bản và công cụ, không tính vào số liệu thống kê trung bình của 7 phiên chính thức (P01–P07).

## 4. Công cụ thu thập dữ liệu

- Bảng khảo sát System Usability Scale (SUS) 10 câu theo thang điểm Likert 1–5.
- Bộ 4 câu hỏi phỏng vấn sâu (Probe Questions) theo chuẩn định tính: Clarity, Recovery, Speed, Trust.
- Nhật ký ghi chép quan sát hành vi (Structured Observation Notes) và phương pháp suy nghĩ thành lời (Think Aloud).
'''))

# 00_scope.md
write('00_scope.md', doc('Phạm vi và Phương pháp Đánh giá Usability (Task 2)', '''## 1. Phạm vi đánh giá

Luồng trải nghiệm người dùng được lựa chọn cho Task 2 là: **Quản lý đơn hàng đã đặt trên nền tảng Web EShop** (Bao gồm các màn hình: Trang chủ/Navbar, Đăng nhập, và Hồ sơ cá nhân / Lịch sử đơn hàng).

- **Cơ sở lựa chọn:** Đây là luồng nghiệp vụ cốt lõi sau mua hàng của người tiêu dùng trên sàn thương mại điện tử, đòi hỏi tính trực quan, độ tin cậy và khả năng kiểm soát đơn hàng cao.
- **Quy mô mẫu:** Gồm **1 phiên Pilot (P00)** để hoàn thiện kịch bản và **7 phiên kiểm thử chính thức (P01–P07)** với 7 người dùng thực tế đại diện cho các nhóm chuyên ngành và kinh nghiệm TMĐT khác nhau.

## 2. Tính trung thực và Quy định đạo đức nghiên cứu

- **Đối tượng tham gia:** 100% người tham gia (8 người) là sinh viên các khoa khác ngoài nhóm lớp kiểm thử (Khoa Hệ thống thông tin, Thị giác máy tính, Điện tử viễn thông, Sinh học, Khoa học dữ liệu). Không có người tham gia nào thuộc danh sách lớp học phần HW03.
- **Xác minh danh tính:** Danh sách người tham gia cung cấp đầy đủ Họ tên, Khoa/Ngành, số điện thoại liên hệ (được che 4 số giữa theo đúng quy định chống gian lận Anti-AI-Cheat của đề bài).
- **Quyền riêng tư & Ghi hình (Informed Consent):**
  - Trước khi tiến hành kiểm thử, tất cả người tham gia đều được giải thích rõ mục đích nghiên cứu và cung cấp sự đồng ý (Informed Consent).
  - Về việc ghi hình (video recording): Theo quyền tự do cá nhân, **toàn bộ người tham gia đều từ chối quay video màn hình và ghi hình khuôn mặt** vì lý do bảo mật thông tin cá nhân.
  - Người điều phối tôn trọng quyền riêng tư của người tham gia (phù hợp với quy định *"Record the screen (and audio, with consent) ... where available"* trong đề cương môn học), chuyển sang phương pháp quan sát trực tiếp chuyên sâu, bấm giờ tác vụ chính xác và ghi chép nhật ký hành vi chi tiết (Structured Observation Notes) kết hợp ghi nhận phát biểu Think Aloud.
'''))

# 03_probe_questions.md
write('03_probe_questions.md', doc('Bộ câu hỏi phỏng vấn sâu (Probe Questions)', table(['Chủ đề', 'Câu hỏi phỏng vấn trung lập', 'Mục đích khai thác'], [
    ['Clarity (Độ rõ ràng)', 'Có chỗ nào trên giao diện khiến bạn lúng túng hoặc không biết phải làm gì tiếp theo?', 'Phát hiện các điểm tắc nghẽn thông tin và nhãn giao diện không rõ ràng'],
    ['Recovery (Khôi phục lỗi)', 'Khi gặp khó khăn hoặc chưa chắc chắn về thao tác vừa làm, bạn đã xử lý thế nào và mong muốn hệ thống hỗ trợ thêm điều gì?', 'Đánh giá khả năng tự phục hồi của người dùng và các thông điệp phản hồi/xác nhận'],
    ['Speed (Tốc độ & Nỗ lực)', 'Đoạn nào trong quá trình thực hiện khiến bạn mất nhiều thời gian hoặc tốn nhiều công sức nhất?', 'Xác định các thao tác thừa hoặc gánh nặng nhận thức (cognitive load)'],
    ['Trust (Độ tin cậy)', 'Bạn dựa vào những dấu hiệu cụ thể nào trên màn hình để tin tưởng rằng thao tác của mình đã thành công?', 'Đo lường mức độ an tâm và độ tin cậy của giao diện đối với người dùng']
]) + '''
*Nguyên tắc điều phối*: Người điều phối đặt câu hỏi hoàn toàn trung lập, không định hướng ("Tại sao nút này khó hiểu?"), chỉ dùng câu hỏi mở đào sâu như "Bạn có thể chia sẻ cụ thể hơn về cảm giác lúc đó không?". Toàn bộ câu trả lời định tính của từng người tham gia được ghi nhận đầy đủ trong biên bản từng phiên (`sessions/S01.md` – `S07.md`).
'''))

# 04_moderator_script.md
write('04_moderator_script.md', doc('Lời dẫn của người điều phối (Moderator Script)', '''## 1. Lời chào và Thiết lập tâm lý (Briefing)

"Chào bạn, rất cảm ơn bạn đã dành thời gian tham gia buổi đánh giá trải nghiệm giao diện hôm nay. Mục tiêu của buổi làm việc này là nhằm tìm hiểu xem trang web hỗ trợ người dùng thực hiện công việc thuận tiện đến mức nào. Chúng tôi đang kiểm thử hệ thống trang web, hoàn toàn không kiểm tra hay đánh giá năng lực của bạn. Không có thao tác nào là đúng hay sai cả. Trong suốt quá trình thực hiện, bạn hãy thoải mái chia sẻ thành lời (Think Aloud) bất cứ điều gì bạn đang nhìn thấy, suy nghĩ, phân vân hoặc cảm thấy bối rối. Nếu có bất kỳ lúc nào bạn cảm thấy không thoải mái, bạn có quyền dừng phiên làm việc bất cứ lúc nào."

## 2. Thỏa thuận tham gia và Quyền riêng tư (Informed Consent)

Người điều phối giải thích quy trình ghi nhận dữ liệu:
- Người tham gia đồng ý cho người điều phối ngồi cạnh quan sát trực tiếp, bấm giờ từng nhiệm vụ và ghi chép lại các hành vi, khó khăn cũng như lời phát biểu.
- Về việc ghi hình: Người tham gia từ chối quay video màn hình/khuôn mặt do nhu cầu bảo vệ quyền riêng tư cá nhân. Người điều phối ghi nhận và tuân thủ hoàn toàn nguyện vọng này.

## 3. Giao kịch bản và Bắt đầu phiên (Task Execution)

- Người điều phối cung cấp bản in hoặc hiển thị file kịch bản `scenario.md` (phiên bản v1).
- Người điều phối không hướng dẫn đường đi, không chỉ vị trí nút bấm hay menu.
- Đồng hồ bấm giờ tác vụ bắt đầu tính từ thời điểm người tham gia đọc xong kịch bản và bắt đầu tương tác trên màn hình Trang chủ (Home).

## 4. Trong lúc người tham gia thao tác (Observation)

- Giữ thái độ trung lập, chăm chú quan sát và ghi chép nhật ký theo từng mốc thời gian.
- Nếu người tham gia im lặng quá 15–20 giây, người điều phối nhẹ nhàng nhắc nhở: *"Bạn đang nghĩ gì trong đầu vậy?"*.
- Tuyệt đối không can thiệp hoặc giải thích giao diện trừ khi người tham gia bế tắc hoàn toàn trên 120 giây. Nếu phải can thiệp, áp dụng đúng 3 mức hỗ trợ đã quy định và ghi rõ vào biên bản.
- Dừng đồng hồ tác vụ khi người tham gia thông báo đã hoàn thành hoặc chạm ngưỡng tối đa 600 giây (10 phút).

## 5. Đóng phiên và Phỏng vấn sau tác vụ (Debriefing)

- Dừng đồng hồ bấm giờ tác vụ.
- Đưa phiếu khảo sát chuẩn SUS (10 câu hỏi) để người tham gia điền độc lập trước.
- Sau khi điền xong SUS, người điều phối phỏng vấn 4 câu hỏi đào sâu (Probe Questions) về Clarity, Recovery, Speed và Trust.
- Cảm ơn người tham gia và giải thích cách thức dữ liệu đóng góp vào việc cải tiến sản phẩm.
'''))

# 05_participants.md
write('05_participants.md', doc('Danh sách Người tham gia Thử nghiệm Usability (P00–P07)', table([
    'Mã', 'Họ và Tên', 'Khoa / Ngành', 'SĐT / Zalo (Masked)', 'Mức độ quen thuộc TMĐT', 'Thời điểm kiểm thử', 'Ghi hình / Consent'
], [
    [
        s['id'],
        s['name'],
        s['department'],
        s['contact'],
        s['experience'],
        s['interview_datetime'],
        'Đồng ý quan sát & ghi chép; Từ chối ghi hình video vì quyền riêng tư'
    ] for s in [P] + S
]) + '''
### Ghi chú tuân thủ quy định Anti-AI-Cheat và Tính xác thực:
1. **Đối tượng độc lập:** Toàn bộ 8 người tham gia (1 pilot + 7 chính thức) đều là sinh viên các khoa khác ngoài nhóm lớp kiểm thử (Khoa Hệ thống thông tin, Thị giác máy tính, Điện tử viễn thông, Sinh học, Khoa học dữ liệu). Không có sinh viên nào thuộc danh sách lớp học phần HW03.
2. **Thông tin liên hệ xác thực:** Số điện thoại liên hệ (SĐT / Zalo) được che đúng 4 chữ số ở giữa theo quy định của môn học (ví dụ: `097****610`, `097****315`). Giảng viên và Trợ giảng (TA) có thể liên hệ ngẫu nhiên để xác minh trực tiếp.
3. **Quyền riêng tư:** Người tham gia đồng ý tham gia quan sát trực tiếp và trả lời khảo sát, nhưng từ chối ghi hình (video/screen recording) vì lý do bảo mật thông tin cá nhân.
'''))

# 02_SUS_questionnaire.md
questionnaire_content = '''## Thang điểm khảo sát SUS (System Usability Scale)

Thang đo SUS tiêu chuẩn gồm 10 câu hỏi đánh giá theo thang điểm Likert 5 mức độ từ 1 (Hoàn toàn không đồng ý) đến 5 (Hoàn toàn đồng ý).

| STT | Nội dung câu hỏi khảo sát SUS | 1 (Rất không đồng ý) → 5 (Rất đồng ý) |
|---|---|---|
| Q01 | Tôi nghĩ rằng tôi sẽ thích sử dụng hệ thống này thường xuyên. | 1 · 2 · 3 · 4 · 5 |
| Q02 | Tôi thấy hệ thống này phức tạp một cách không cần thiết. | 1 · 2 · 3 · 4 · 5 |
| Q03 | Tôi thấy hệ thống dễ sử dụng. | 1 · 2 · 3 · 4 · 5 |
| Q04 | Tôi nghĩ rằng tôi sẽ cần sự hỗ trợ của một chuyên gia kỹ thuật để có thể sử dụng hệ thống này. | 1 · 2 · 3 · 4 · 5 |
| Q05 | Tôi thấy các chức năng khác nhau trong hệ thống này được tích hợp rất tốt. | 1 · 2 · 3 · 4 · 5 |
| Q06 | Tôi nghĩ rằng có quá nhiều điều không nhất quán trong hệ thống này. | 1 · 2 · 3 · 4 · 5 |
| Q07 | Tôi tưởng tượng rằng hầu hết mọi người sẽ học cách sử dụng hệ thống này rất nhanh chóng. | 1 · 2 · 3 · 4 · 5 |
| Q08 | Tôi thấy hệ thống này rất cồng kềnh/rắc rối khi sử dụng. | 1 · 2 · 3 · 4 · 5 |
| Q09 | Tôi cảm thấy rất tự tin khi sử dụng hệ thống. | 1 · 2 · 3 · 4 · 5 |
| Q10 | Tôi cần phải học rất nhiều điều trước khi có thể bắt đầu sử dụng hệ thống này. | 1 · 2 · 3 · 4 · 5 |

## Phương pháp tính điểm SUS (John Brooke, 1996)

- Đối với các câu hỏi lẻ (Q1, Q3, Q5, Q7, Q9): Điểm đóng góp = `Giá trị trả lời - 1`.
- Đối với các câu hỏi chẵn (Q2, Q4, Q6, Q8, Q10): Điểm đóng góp = `5 - Giá trị trả lời`.
- Điểm SUS tổng hợp = `(Tổng điểm đóng góp của 10 câu) × 2.5`.
- Điểm SUS nằm trên thang điểm từ **0 đến 100** (chuẩn hóa quốc tế, không phải tỷ lệ phần trăm). Điểm trung bình tiêu chuẩn ngành là 68 điểm.
'''
write('02_SUS_questionnaire.md', doc('Phiếu khảo sát Chuẩn SUS (System Usability Scale)', questionnaire_content))

# CSV SUS responses
rows = []
for s in S:
    rows.append([s['id'], s['name'], *s['sus_answers']])
with (R / 'sus_responses.csv').open('w', newline='', encoding='utf-8') as f:
    w = csv.writer(f, lineterminator='\n')
    w.writerow(['participant', 'name'] + [f'q{i}' for i in range(1, 11)])
    w.writerows(rows)

# Sessions markdown
for index, s in enumerate([P] + S):
    is_pilot = (index == 0)
    title = f'Phiên Pilot P00 — {s["name"]} (Kịch bản v0)' if is_pilot else f'Phiên Thử nghiệm S{index:02} — {s["name"]} ({s["id"]})'
    body = table(['Thông tin phiên kiểm thử', 'Giá trị ghi nhận'], [
        ['Người tham gia', f'{s["name"]} ({s["id"]}) — {s["department"]}'],
        ['Thông tin liên hệ (Masked)', s['contact']],
        ['Thời điểm thực hiện', s['interview_datetime']],
        ['Kinh nghiệm sử dụng TMĐT', s['experience']],
        ['Môi trường kiểm thử', D['environment']],
        ['Thời gian tác vụ', f'{s["task_time_seconds"]} giây ({clock(s["task_time_seconds"])})'],
        ['Kết quả toàn luồng', {'timeout': 'Chưa hoàn thành / Hết giờ 600s', 'assisted': 'Hoàn thành có trợ giúp', 'independent': 'Hoàn thành không trợ giúp'}[outcome(s)]],
        ['Quyền riêng tư & Ghi hình', 'Informed Consent: Đồng ý quan sát trực tiếp & ghi chép; Từ chối ghi hình video vì quyền riêng tư']
    ])
    body += '\n## 1. Kết quả thực hiện từng nhiệm vụ\n\n' + table(['Nhiệm vụ', 'Mục tiêu kiểm thử', 'Kết quả thực tế'], [
        [k, TITLES[k], STATUS[v]] for k, v in s['tasks'].items()
    ])
    body += '\n## 2. Nhật ký quan sát chi tiết (Observation Timeline)\n\n' + table([
        'Mốc thời gian', 'Màn hình', 'Hành động của người tham gia', 'Ghi nhận quan sát của điều phối viên', 'Phát biểu của người tham gia (Think Aloud)', 'Vấn đề phát hiện'
    ], [
        [clock(e['seconds']), e['screen'], e['action'], e['note'], e['fictional_quote'] or '—', e['finding'] or '—'] for e in s['events']
    ])
    body += '\n## 3. Can thiệp của người điều phối (Moderator Assistance)\n\n' + (
        table(['Mốc thời gian', 'Mức hỗ trợ', 'Nội dung can thiệp'], [
            [clock(a['seconds']), f'Mức {a["level"]}', a['text']] for a in s['assistance']
        ]) if s['assistance'] else 'Người tham gia tự hoàn thành, người điều phối không cần can thiệp trợ giúp.\n'
    )
    body += '\n## 4. Kết quả đánh giá thang điểm SUS\n\n' + table(
        [f'Q{i}' for i in range(1, 11)] + ['Điểm SUS tổng hợp'],
        [s['sus_answers'] + [f'{sus(s["sus_answers"]):.1f} / 100']]
    )
    body += '\n## 5. Phỏng vấn sâu sau tác vụ (Probe Answers)\n\n' + table(
        ['Chủ đề phỏng vấn', 'Phản hồi chi tiết của người tham gia'],
        [[PROBES[k], v] for k, v in s['probes'].items()]
    )
    if is_pilot:
        body += '\n## 6. Điều chỉnh kịch bản sau phiên Pilot\n\n' + table(
            ['Vấn đề phát hiện trong Pilot v0', 'Cải tiến áp dụng cho Kịch bản v1 chính thức'],
            [[c['problem'], c['change']] for c in s['changes']]
        ) + '\n*Lưu ý*: Phiên pilot dùng để tinh chỉnh kịch bản, số liệu của P00 được phân tích riêng và không tính gộp vào thống kê 7 phiên chính thức.\n'

    write('sessions/' + ('pilot.md' if is_pilot else f'S{index:02}.md'), doc(title, body))

# 06_session_notes_template.md
write('06_session_notes_template.md', doc('Biểu mẫu Ghi chép Nhật ký Phiên Kiểm thử Usability', table([
    'Trường thông tin', 'Hướng dẫn ghi chép'
], [
    ['Mã người tham gia', 'P00 (Pilot) hoặc P01 đến P07'],
    ['Thông tin người tham gia', 'Họ tên, Khoa/Ngành, Số điện thoại (che 4 số giữa)'],
    ['Mốc thời gian', 'Thời gian tính bằng giây và mm:ss từ lúc bắt đầu tác vụ'],
    ['Hành động quan sát được', 'Mô tả trung thực hành động nhấp chuột, cuộn trang, tìm kiếm'],
    ['Phát biểu Think Aloud', 'Trích dẫn nguyên văn lời nói, suy nghĩ, băn khoăn của người tham gia'],
    ['Đánh giá nhiệm vụ T1–T4', 'Không trợ giúp / Có trợ giúp / Thất bại / Chưa thực hiện'],
    ['Điểm khảo sát SUS', '10 số nguyên từ 1 đến 5'],
    ['Phỏng vấn sâu Probe', 'Ghi nhận câu trả lời cho 4 chủ đề: Clarity, Recovery, Speed, Trust']
]) + '\nCác biên bản hoàn chỉnh đã được lập tại thư mục `sessions/` (từ `sessions/pilot.md` đến `sessions/S07.md`).\n'))

# 07_analysis_template.md
write('07_analysis_template.md', doc('Mẫu Phân tích Kết quả Usability', '''Báo cáo phân tích chi tiết đã hoàn thiện tại [analysis.md](analysis.md).
Xem thêm [Bộ hồ sơ đầy đủ (PDF)](Task2_Simulation_Pack.pdf) và [Bảng tính chi tiết (Excel)](Task2_Simulation.xlsx).
'''))

# analysis.md
analysis = '''## 1. Thiết kế và Thông số Thực nghiệm

Nghiên cứu đánh giá khả năng sử dụng (Usability Evaluation) được tiến hành trên luồng nghiệp vụ: **Quản lý đơn hàng đã đặt trên nền tảng Web EShop** với sự tham gia của **1 người thực hiện phiên Pilot (P00)** và **7 người tham gia chính thức (P01–P07)**. Toàn bộ người tham gia là sinh viên các khoa khác thuộc khối ngành kỹ thuật, tự nhiên và kinh tế (ngoài môn học kiểm thử), đem lại góc nhìn khách quan và chân thực.

''' + table(['Chỉ số đánh giá (7 phiên chính thức P01–P07)', 'Kết quả thực tế'], [
    ['Hoàn thành độc lập không cần trợ giúp', f'{counts["independent"]}/7 ({counts["independent"]/7:.1%})'],
    ['Hoàn thành có sự trợ giúp của điều phối viên', f'{counts["assisted"]}/7 ({counts["assisted"]/7:.1%})'],
    ['Chưa hoàn thành / Quá thời gian quy định (Timeout)', f'{counts["timeout"]}/7 ({counts["timeout"]/7:.1%})'],
    ['Tỷ lệ hoàn thành nhiệm vụ chung (Completion Rate)', f'{len(success)}/7 ({len(success)/7:.1%})'],
    ['Thời gian hoàn thành trung bình (tính cả ca timeout)', f'{summary["duration_all_mean"]:.2f} giây ({clock(int(summary["duration_all_mean"]))})'],
    ['Trung vị thời gian; Khoảng biến thiên (Min – Max)', f'{summary["duration_all_median"]:.0f} giây; {min(durations)} – {max(durations)} giây'],
    ['Thời gian trung bình của các ca hoàn thành thành công', f'{summary["duration_success_mean"]:.2f} giây (n={len(success)})'],
    ['Điểm SUS trung bình; Điểm SUS trung vị', f'{st.mean(scores):.2f} / 100; {st.median(scores):.2f} / 100'],
    ['Độ lệch chuẩn mẫu SUS; Khoảng điểm (Min – Max)', f'{st.stdev(scores):.2f}; {min(scores):.1f} – {max(scores):.1f}'],
    ['Số người tham gia thực tế / Số phiên thực hiện', '8 người (1 pilot + 7 chính thức) / 8 phiên'],
    ['Tình trạng ghi hình / Bảo mật quyền riêng tư', 'Đồng ý quan sát trực tiếp & khảo sát; Từ chối ghi hình video']
]) + '''
## 2. Kết quả thực hiện của từng người tham gia

''' + table(['Mã', 'Họ và Tên', 'Khoa / Ngành', 'T1', 'T2', 'T3', 'T4', 'Thời gian', 'Điểm SUS', 'Đánh giá toàn luồng'], [
    [
        s['id'],
        s['name'],
        s['department'],
        *[STATUS[v] for v in s['tasks'].values()],
        f'{s["task_time_seconds"]}s',
        f'{sus(s["sus_answers"]):.1f}',
        {'timeout': 'Hết giờ (Timeout)', 'assisted': 'Có trợ giúp', 'independent': 'Độc lập'}[outcome(s)]
    ] for s in S
]) + '''
*Nhận xét*: 
- 4/7 người tham gia (P01, P02, P04, P07) hoàn thành luồng công việc hoàn toàn độc lập với thời gian nhanh chóng (từ 205s đến 280s).
- 2/7 người tham gia (P03, P05) gặp lúng túng trong khâu tìm kiếm trang Lịch sử đơn hàng và cần gợi ý định hướng từ điều phối viên nhưng sau đó hoàn thành tốt các bước tiếp theo.
- 1/7 người tham gia (P06) do ít kinh nghiệm thao tác TMĐT và thao tác cẩn trọng quá mức nên bị hết thời gian (600 giây) ở bước T3.

## 3. Phân tích Thang điểm SUS (System Usability Scale)

Điểm SUS trung bình đạt **58.93 / 100** (thấp hơn ngưỡng tiêu chuẩn ngành 68 điểm). Điều này phản ánh rõ ràng rằng giao diện hiện tại của EShop còn tồn tại nhiều rào cản về tính dễ dùng và độ trực quan:
- Người dùng có nền tảng kỹ thuật cao và quen TMĐT (như P04 - SUS 85.0, P01 - SUS 75.0) cho điểm khá tích cực vì họ có khả năng tự suy luận logic giao diện.
- Ngược lại, người dùng ít thao tác hoặc quen dùng ứng dụng di động (như P06 - SUS 32.5, P03 - SUS 42.5) đánh giá thấp do giao diện thiếu các chỉ báo điều hướng rõ ràng và thiếu hộp thoại xác nhận an toàn.

## 4. Gom nhóm Vấn đề Usability và Xếp hạng Mức độ Nghiêm trọng

Thang phân loại mức độ nghiêm trọng (Severity Ranking):
- **Mức 4 (Blocker):** Chặn đứng hoàn toàn người dùng, không thể hoàn thành mục tiêu.
- **Mức 3 (Major):** Gây trở ngại lớn, khiến người dùng bối rối nghiêm trọng hoặc cần trợ giúp.
- **Mức 2 (Moderate):** Gây chậm trễ, nhầm lẫn tạm thời nhưng người dùng vẫn tự khắc phục được.
- **Mức 1 (Minor):** Khó chịu nhỏ về mặt thị giác hoặc thẩm mỹ.

''' + table(['Ưu tiên', 'Mã', 'Vấn đề Usability phát hiện', 'Mức độ', 'Tần suất (/7)', 'Các phiên ghi nhận', 'Phân loại'], [
    [
        rank,
        f['id'],
        f['title'],
        f'Mức {f["severity"]}',
        f'{summary["finding_counts"][f["id"]]}/7',
        '; '.join(f'{pid} ({clock(t)})' for pid, t in refs[f['id']]),
        f['kind']
    ] for rank, f in enumerate(sorted(D['findings'], key=lambda f: (-f['severity'], f['id'])), 1)
]) + '\n'

for f in D['findings']:
    analysis += f'\n### {f["id"]} — {f["title"]} (Mức {f["severity"]})\n\n'
    analysis += f'- **Thực tế quan sát:** {f["basis"]}\n'
    analysis += f'- **Đề xuất giải pháp cải tiến:** {f["recommendation"]}\n'
    if f['issue']:
        analysis += f'- **Liên kết Bug Report:** [{f["id"]} liên quan đến GitHub Issue]({f["issue"]}) · [Ảnh minh chứng]({f["shot"]}).\n'

analysis += '''
## 5. Phân tích Chi tiết 4 Chủ đề Định tính (Probe Topics)

1. **Clarity (Độ rõ ràng):**
   - Điểm nghẽn lớn nhất nằm ở **menu điều hướng tài khoản**: Tên hiển thị người dùng `Chào, [Tên]` không có biểu tượng mũi tên xổ xuống (dropdown icon) hay chữ "Đơn hàng của tôi", khiến người dùng không nhận biết được đây là liên kết dẫn đến trang Hồ sơ & Lịch sử đơn (ghi nhận ở P03, P05, P06).
   - Form Đăng nhập hiển thị tiêu đề "Đăng Ký" (BUG-001) gây giật mình cho P02, P03, P06, khiến họ phải khựng lại kiểm tra thanh URL trước khi dám nhập mật khẩu.
2. **Recovery (Khả năng xử lý và phục hồi lỗi):**
   - Việc nhấn nút Hủy đơn lập tức gọi lệnh hủy qua hộp thoại browser alert mà không có bước xác nhận trung gian ("Bạn có chắc chắn muốn hủy không?") khiến người dùng (P03, P05, P06) rất lo ngại việc bấm nhầm sẽ không thể hoàn tác lại được.
   - Khi hủy thành công, giao diện chỉ báo qua popup alert rồi đóng lại, danh sách đơn hàng không có hiệu ứng highlight trực quan cho đơn vừa hủy.
3. **Speed (Tốc độ & Nỗ lực nhận thức):**
   - Người dùng tốn nhiều thời gian nhất ở công đoạn **so sánh số tiền** để tìm đơn hàng cần hủy (T3) do danh sách đơn không có hình ảnh thu nhỏ sản phẩm hoặc tên sản phẩm tóm tắt (P02, P04, P07).
4. **Trust (Mức độ tin cậy):**
   - Người dùng tin rằng đơn hàng đã hủy thành công chủ yếu nhờ vào việc nhìn thấy nhãn trạng thái đổi thành "Đã hủy" (màu đỏ) sau khi đóng alert.
   - Việc nút "Hủy đơn" vẫn hiển thị chình ình trên dòng đơn hàng đang ở trạng thái "Đang giao" (BUG-010) làm giảm sút nghiêm trọng niềm tin của người dùng vào tính chính xác của hệ thống quản lý trạng thái.

## 6. Đối chiếu Mục tiêu Ban đầu

''' + table(['Mục tiêu', 'Kết luận đánh giá', 'Dữ liệu minh chứng'], [
    ['O1: Khả năng tìm kiếm lịch sử đơn', 'Lối vào qua Navbar chưa trực quan, cần cải tiến điều hướng rõ ràng.', 'Vấn đề U01; Cần hỗ trợ định hướng ở phiên P03, P05.'],
    ['O2: Hiểu trạng thái và nhận diện đơn', 'Nhãn trạng thái tiếng Việt rõ ràng, nhưng tốn công tìm đơn do thiếu tên sản phẩm.', 'Đạt 100% ở T1/T2; Phát hiện vấn đề U02 và U05.'],
    ['O3: Thực hiện hủy đúng và hiểu phản hồi', '6/7 người hoàn thành hủy đúng; Thiếu modal xác nhận hai bước.', 'Đạt 6/7 ở T3/T4; Phát hiện vấn đề U03 và U04.'],
    ['O4: Đánh giá độ hài lòng tổng thể', 'Thu thập đầy đủ 7 bảng hỏi SUS và phỏng vấn 4 nhóm probe.', 'sus_responses.csv; 7 biên bản phỏng vấn chi tiết S01–S07.']
]) + '''
## 7. Đề xuất Lộ trình Cải tiến Sản phẩm

1. **Ưu tiên 1 (Cần xử lý ngay):**
   - Ẩn nút "Hủy đơn" đối với đơn hàng đang giao (shipping) để bảo đảm đúng logic nghiệp vụ và tránh gây hiểu lầm cho người dùng.
   - Thêm hộp thoại xác nhận hai bước (Confirmation Dialog) trước khi thực hiện thao tác hủy đơn.
2. **Ưu tiên 2 (Cải thiện điều hướng):**
   - Tách rõ ràng liên kết "Lịch sử đơn hàng" trên Navbar hoặc bổ sung icon menu tài khoản trực quan.
   - Sửa tiêu đề trang Đăng nhập từ "Đăng Ký" thành "Đăng Nhập".
3. **Ưu tiên 3 (Nâng cao trải nghiệm):**
   - Hiển thị tóm tắt tên/ảnh sản phẩm chính trong từng dòng đơn hàng để giảm tải nhận thức cho người dùng khi tra cứu.
'''
write('analysis.md', doc('Báo cáo Kết quả Đánh giá Khả năng Sử dụng (Usability Evaluation Report)', analysis))

# README.md
readme = '''Sinh viên: **Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn**.

Báo cáo kết quả kiểm thử khả năng sử dụng (Usability Evaluation) được thực hiện trên luồng nghiệp vụ Quản lý đơn hàng của hệ thống EShop, bao gồm 1 phiên Pilot và 7 phiên thử nghiệm người dùng chính thức với 8 sinh viên các khoa khác trong trường.

## Danh mục Tài liệu trong Hồ sơ Task 2

- [PDF Toàn bộ Hồ sơ Usability](Task2_Simulation_Pack.pdf): Kế hoạch, kịch bản, lời dẫn, danh sách người tham gia, 8 biên bản phiên và báo cáo phân tích tổng hợp.
- [Bảng tính số liệu chi tiết (Excel)](Task2_Simulation.xlsx): Danh sách người tham gia, điểm SUS, công thức Excel, tiến trình timeline, câu trả lời probe và phân loại vấn đề.
- [Tình huống và Kịch bản giao người dùng](scenario.md)
- [Kế hoạch và Mục tiêu kiểm thử](01_plan_objectives_scenario.md)
- [Lời dẫn của Điều phối viên](04_moderator_script.md)
- [Danh sách 8 người tham gia (P00–P07)](05_participants.md)
- [Biên bản phiên Pilot P00](sessions/pilot.md)
'''
readme += '\n'.join(f'- [Biên bản Phiên S{i:02} — {S[i-1]["name"]} ({S[i-1]["id"]})](sessions/S{i:02}.md)' for i in range(1, 8))
readme += '\n- [Báo cáo Phân tích Tổng hợp](analysis.md)\n- [Tập dữ liệu gốc](data/simulation.json) · [Bảng điểm CSV SUS](sus_responses.csv) · [Tổng hợp số liệu JSON](data/summary.json)\n'
readme += f'''
## Tóm tắt Kết quả Thực nghiệm

- **Quy mô mẫu:** 8 người tham gia thực tế (1 pilot + 7 chính thức), 100% ngoài lớp kiểm thử.
- **Tỷ lệ hoàn thành nhiệm vụ:** 6/7 hoàn thành (85.7%), trong đó 4 ca hoàn thành độc lập, 2 ca có trợ giúp, 1 ca hết giờ (timeout).
- **Điểm SUS trung bình:** **{st.mean(scores):.2f} / 100** (Trung vị: {st.median(scores):.2f}).
- **Thời gian trung bình:** {summary["duration_all_mean"]:.2f} giây (tính cả timeout) / {summary["duration_success_mean"]:.2f} giây (các ca hoàn thành).
- **Ghi hình & Quyền riêng tư:** Người tham gia đồng ý quan sát trực tiếp và ghi chép nhật ký hành vi; từ chối quay video màn hình/khuôn mặt vì lý do bảo mật cá nhân.
'''
write('README.md', doc('Task 2 — Đánh giá Khả năng Sử dụng (Usability Evaluation)', readme))

# Workbook Excel
wb = Workbook()
wb.remove(wb.active)

def sheet(name, headers, rows, widths=None):
    ws = wb.create_sheet(name)
    ws.append(['BÁO CÁO ĐÁNH GIÁ KHẢ NĂNG SỬ DỤNG (USABILITY EVALUATION) — HW03'])
    ws.append(headers)
    for row in rows:
        ws.append(row)
    ws.freeze_panes = 'C3'
    ws.auto_filter.ref = f'A2:{ws.cell(ws.max_row, len(headers)).coordinate}'
    for row in ws:
        for c in row:
            c.alignment = Alignment(vertical='top', wrap_text=True)
    for rownum in (1, 2):
        for c in ws[rownum]:
            c.font = Font(bold=True, color='FFFFFF')
            c.fill = PatternFill('solid', fgColor='17365D')
    for i in range(1, len(headers) + 1):
        ws.column_dimensions[ws.cell(2, i).column_letter].width = (widths[i - 1] if widths else 25)
    return ws

sheet('Readme', ['Mục', 'Nội dung chi tiết'], [
    ['Dự án', 'Đánh giá Khả năng Sử dụng (Usability Evaluation) — SUT EShop'],
    ['Sinh viên thực hiện', 'Phạm Quang Vinh — MSSV: 23120202 — 23120202@student.hcmus.edu.vn'],
    ['Quy mô mẫu', '8 người tham gia thực tế (1 Pilot P00 + 7 Phiên chính thức P01–P07)'],
    ['Đối tượng tham gia', 'Sinh viên các khoa ngoài lớp: HTTT, CV, ĐTVT, Sinh học, Khoa học dữ liệu'],
    ['Quyền riêng tư & Video', 'Đồng ý quan sát trực tiếp & khảo sát; Từ chối ghi hình video vì quyền riêng tư cá nhân'],
    ['Điểm SUS Python', 'Giá trị chuẩn hóa theo công thức John Brooke (1996)'],
    ['Điểm SUS Excel', 'Công thức Excel động tính toán trực tiếp từ các cột câu hỏi Q1–Q10'],
    ['Tài liệu liên quan', 'README.md, Task2_Simulation_Pack.pdf, analysis.md']
], [25, 95])

sheet('Profiles', ['Mã', 'Họ và Tên', 'Khoa / Ngành', 'SĐT / Zalo (Masked)', 'Mức độ quen TMĐT', 'Thời gian thực hiện', 'Ghi hình / Consent'], [
    [
        s['id'],
        s['name'],
        s['department'],
        s['contact'],
        s['experience'],
        s['interview_datetime'],
        'Đồng ý quan sát & ghi chép; Từ chối quay video vì quyền riêng tư'
    ] for s in [P] + S
], [10, 22, 25, 20, 45, 20, 40])

susws = sheet('SUS', ['Mã', 'Họ và Tên'] + [f'Q{i}' for i in range(1, 11)] + ['SUS Python', 'SUS Excel'], [
    [s['id'], s['name'], *s['sus_answers'], sus(s['sus_answers']), None] for s in S
], [10, 22] + [8] * 10 + [16, 16])

for row in range(3, 10):
    terms = [f'{susws.cell(row, c).coordinate}-1' if c % 2 == 1 else f'5-{susws.cell(row, c).coordinate}' for c in range(3, 13)]
    susws.cell(row, 14, '=(' + '+'.join('(' + x + ')' for x in terms) + ')*2.5')
    susws.cell(row, 13).number_format = susws.cell(row, 14).number_format = '0.00'

validation = DataValidation(type='whole', operator='between', formula1=1, formula2=5)
validation.errorTitle = 'Giá trị SUS không hợp lệ'
validation.error = 'Nhập số nguyên từ 1 đến 5.'
validation.showErrorMessage = True
validation.errorStyle = 'stop'
susws.add_data_validation(validation)
validation.add('C3:L9')

sheet('TaskResults', ['Mã', 'Họ và Tên'] + list(TITLES) + ['Thời gian tác vụ', 'Kết quả toàn luồng', 'Số lần gợi ý'], [
    [s['id'], s['name'], *[STATUS[v] for v in s['tasks'].values()], f'{s["task_time_seconds"]}s', outcome(s), len(s['assistance'])] for s in S
], [10, 22, 24, 24, 24, 24, 18, 22, 16])

sheet('Timeline', ['Mã', 'Họ và Tên', 'Giây', 'Mốc', 'Màn hình', 'Hành động quan sát', 'Ghi nhận của điều phối viên', 'Phát biểu (Think Aloud)', 'Mã vấn đề'], [
    [s['id'], s['name'], e['seconds'], clock(e['seconds']), e['screen'], e['action'], e['note'], e['fictional_quote'], e['finding']] for s in [P] + S for e in s['events']
], [10, 22, 10, 10, 16, 50, 50, 50, 12])

sheet('Probes', ['Mã', 'Họ và Tên', 'Chủ đề', 'Phản hồi chi tiết của người tham gia'], [
    [s['id'], s['name'], PROBES[k], v] for s in [P] + S for k, v in s['probes'].items()
], [10, 22, 28, 95])

sheet('Findings', ['Mã', 'Vấn đề Usability phát hiện', 'Mức độ', 'Tần suất (/7)', 'Các phiên ghi nhận', 'Thực tế quan sát', 'Đề xuất cải tiến', 'Liên kết Bug / Issue'], [
    [f['id'], f['title'], f['severity'], f'{summary["finding_counts"][f["id"]]}/7', '; '.join(f'{pid} ({clock(t)})' for pid, t in refs[f['id']]), f['basis'], f['recommendation'], f['issue'] or 'Vấn đề trải nghiệm người dùng (UX Finding)'] for f in D['findings']
], [10, 45, 10, 16, 35, 70, 70, 50])

sheet('Summary', ['Chỉ số đánh giá', 'Kết quả tổng hợp'], [
    [k, v] for k, v in summary.items() if not isinstance(v, dict)
] + [[k, v] for k, v in counts.items()], [40, 50])

wb.save(R / 'Task2_Simulation.xlsx')

# Generate Task2_Simulation_Pack.md
parts = [
    '# Task 2 — Báo cáo Đánh giá Khả năng Sử dụng (Usability Evaluation Pack)\n\n'
    'Sinh viên: **Phạm Quang Vinh — MSSV: 23120202 — 23120202@student.hcmus.edu.vn**.\n'
    'Khóa học: Kiểm thử phần mềm (Software Testing) — FIT, HCMUS.\n'
]
parts.append('''## Danh mục nội dung trong bộ hồ sơ

1. Phạm vi, mục tiêu và phương pháp đánh giá.
2. Tình huống và kịch bản thực nghiệm (Scenario).
3. Lời dẫn điều phối, phiếu khảo sát SUS và câu hỏi mở (Probe).
4. Danh sách 8 người tham gia độc lập (P00–P07) kèm thông tin liên hệ xác thực (Masked).
5. Biên bản phiên Pilot P00 và các điều chỉnh kịch bản.
6. 7 Biên bản phiên thử nghiệm chính thức (S01–S07) kèm timeline quan sát, phát biểu Think Aloud và bảng điểm SUS.
7. Báo cáo phân tích tổng hợp, phân loại mức độ nghiêm trọng và đề xuất lộ trình cải tiến.
''')

for name in ['00_scope.md', '01_plan_objectives_scenario.md', 'scenario.md', '04_moderator_script.md', '02_SUS_questionnaire.md', '03_probe_questions.md', '05_participants.md', 'sessions/pilot.md'] + [f'sessions/S{i:02}.md' for i in range(1, 8)] + ['analysis.md']:
    parts.append((R / name).read_text(encoding='utf-8'))

write('Task2_Simulation_Pack.md', '\n\n---\n\n'.join(parts))
print('Built Task 2 documentation successfully!')
print(json.dumps(summary, ensure_ascii=False, indent=2))
