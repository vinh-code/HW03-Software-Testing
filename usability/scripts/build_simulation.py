#!/usr/bin/env python3
"""Build clearly labelled coursework simulation documents from one declared dataset.
Does not run interviews, contact people, start the SUT, or mutate the database.
"""
from pathlib import Path
import csv, json, statistics as st, sys, collections
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.worksheet.datavalidation import DataValidation
R=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(R))
from sus_scoring import sus
D=json.loads((R/'data/simulation.json').read_text())
S=D['sessions'];P=D['pilot']
LABEL='KẾT QUẢ MÔ PHỎNG PHỤC VỤ BÀI TẬP'
NOTICE='**'+LABEL+'** — hồ sơ, thời gian, diễn biến và câu trả lời đều do AI tạo cho tình huống giả định. Không có phỏng vấn, người tham gia, đồng ý ghi hình hoặc video thực tế.'
STATUS={'independent':'Không trợ giúp','assisted':'Có trợ giúp','failed':'Thất bại / hết giờ','not_reached':'Chưa thực hiện'}
TITLES={'T1':'Xác định trạng thái đơn 30 triệu','T2':'Xác định trạng thái đơn 45 triệu','T3':'Hủy đúng đơn 28 triệu','T4':'Nêu trạng thái cuối và dấu hiệu xác nhận'}
PROBES={'clarity':'Độ rõ ràng','recovery':'Khôi phục / xử lý khó khăn','speed':'Tốc độ / nỗ lực','trust':'Sự tin tưởng'}
SOURCE='https://digital.ahrq.gov/sites/default/files/docs/survey/systemusabilityscale%2528sus%2529_comp%255B1%255D.pdf'
def outcome(s):
    if any(v in ('failed','not_reached') for v in s['tasks'].values()):return 'timeout'
    return 'assisted' if s['assistance'] or 'assisted' in s['tasks'].values() else 'independent'
def clock(n):return f'{n//60:02}:{n%60:02}'
def table(headers,rows):
    esc=lambda v:str(v).replace('|',' / ').replace('\n',' ')
    return '\n'.join(['| '+' | '.join(headers)+' |','|'+'---|'*len(headers)]+['| '+' | '.join(esc(v) for v in row)+' |' for row in rows])+'\n'
def write(name,body):
    p=R/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(body.rstrip()+'\n')
def doc(title,body):return '# '+title+'\n\n'+NOTICE+'\n\n'+body
assert D['data_kind']=='simulated' and D['real_participants']==D['real_sessions']==0
assert [s['id'] for s in S]==[f'P{i:02}' for i in range(1,8)] and P['id']=='P00'
for s in [P]+S:
    assert s['data_kind']=='simulated' and all(s[k] is None for k in ('interview_datetime','contact','recording','consent'))
    times=[e['seconds'] for e in s['events']]
    assert times[0]==0 and times[-1]==s['task_time_seconds'] and times==sorted(set(times))
    assert set(s['tasks'])==set(TITLES) and all(v in STATUS for v in s['tasks'].values())
    assert s['task_time_seconds']<=600 and set(s['probes'])==set(PROBES)
    assert all(a['seconds'] in times for a in s['assistance'])
    sus(s['sus_answers'])
counts=collections.Counter(outcome(s) for s in S);scores=[sus(s['sus_answers']) for s in S]
success=[s for s in S if outcome(s)!='timeout'];durations=[s['task_time_seconds'] for s in S]
summary=dict(data_kind='simulated',simulated_pilot_count=1,simulated_main_sessions=7,real_sessions=0,real_participants=0,
             outcome_counts=dict(counts),completion_rate=len(success)/7,independent_completion_rate=counts['independent']/7,
             sus_mean=st.mean(scores),sus_median=st.median(scores),sus_sample_sd=st.stdev(scores),sus_min=min(scores),sus_max=max(scores),
             duration_all_mean=st.mean(durations),duration_all_median=st.median(durations),duration_success_mean=st.mean(s['task_time_seconds'] for s in success),
             duration_min=min(durations),duration_max=max(durations),pilot_included_in_summary=False)
refs={f['id']:[] for f in D['findings']}
for s in S:
    for e in s['events']:
        if e['finding']:refs[e['finding']].append((s['id'],e['seconds']))
summary['finding_counts']={k:len(set(pid for pid,t in v)) for k,v in refs.items()}
write('data/summary.json',json.dumps(summary,ensure_ascii=False,indent=2))
# Versioned scenario: participant-facing goals, no click path.
scenario='''## Tình huống v1 — dùng chung cho P01–P07

Bạn đã có tài khoản và đã đặt một số đơn hàng trên EShop. Hôm nay bạn muốn kiểm tra các đơn đã đặt và xử lý một đơn không còn nhu cầu.

1. Cho biết đơn **30.000.000 đồng** đã được giao hay chưa.
2. Cho biết đơn **45.000.000 đồng** hiện ở trạng thái nào.
3. Bạn không còn muốn mua đơn **28.000.000 đồng**. Hãy hủy đúng đơn đó.
4. Cho biết trạng thái cuối của đơn vừa hủy và điều gì trên trang khiến bạn biết thao tác đã hoàn tất.

Khi đã thực hiện xong hoặc thấy không thể tiếp tục, hãy báo cho người điều phối. Trong lúc thao tác, hãy nói điều bạn đang tìm hoặc đang phân vân. Không cần thao tác lên các đơn khác.

**Thông tin demo trong thế giới giả định:** `usability-demo@example.test` / `UsabilityDemo123!`. Tài khoản này chưa được tạo trên SUT; không dùng thông tin trên như tài khoản đã sẵn sàng chạy thật.

## Mục tiêu ban đầu dùng cho pilot v0

Bạn có một số đơn hàng khoảng 30 triệu và 45 triệu đồng. Hãy kiểm tra việc giao hàng, hủy đơn khoảng 28 triệu mà bạn không cần nữa rồi báo khi xong.

v0 cố ý thể hiện bản nháp còn mơ hồ để minh họa quy trình pilot. Phiên pilot là mô phỏng, không phải cuộc thử nghiệm đã diễn ra.
'''
write('scenario.md',doc('Tình huống Task 2',scenario))
write('01_plan_objectives_scenario.md',doc('Kế hoạch Task 2 — quản lý đơn đã đặt','''## Phạm vi

Một luồng: đăng nhập → tìm lịch sử → đọc trạng thái → hủy đúng đơn chưa xử lý → kiểm tra phản hồi. Bốn mục tiêu nhỏ thuộc cùng luồng này. Chưa đối chiếu lựa chọn với thành viên khác trong nhóm.

'''+table(['Mục tiêu','Điều cần xem xét','Chỉ số trong mô phỏng'],[
['O1','Khả năng tìm lịch sử đơn','Khó khăn U01; trợ giúp ở T1'],['O2','Hiểu trạng thái và nhận diện đơn','Kết quả T1/T2; U02/U05'],['O3','Thực hiện hủy đúng và hiểu phản hồi','Kết quả T3/T4; U03/U04'],['O4','Cảm nhận về quá trình','SUS và bốn nhóm probe']])+'''
## Môi trường và dữ liệu giả định

'''+D['environment']+'''

'''+table(['Đơn ký hiệu — không phải ID DB','Số tiền','Trạng thái ban đầu'],[['A','28.000.000 đồng','Chờ xác nhận'],['B','1.500.000 đồng','Đã xác nhận'],['C','45.000.000 đồng','Đang giao'],['D','30.000.000 đồng','Đã giao']])+'''
Tài khoản và bốn đơn được giả định trở về cùng trạng thái ban đầu cho mỗi hồ sơ. Không seed, reset hoặc khởi động lại backend để tạo bộ mô phỏng này. `seed_orders.mjs` là công cụ cũ cho kiểm thử thật, không được chạy trong quy trình này.

'''+scenario+'''
## Quy tắc ghi nhận

- T1: nhận diện đúng đơn 30 triệu và trả lời Đã giao; bao gồm bước đăng nhập và tìm lịch sử.
- T2: nhận diện đúng đơn 45 triệu và trả lời Đang giao.
- T3: chỉ đơn 28 triệu chuyển thành Đã hủy trong diễn biến giả định.
- T4: hồ sơ nói được trạng thái Đã hủy và nêu nhãn trạng thái/thông tin sau tải lại làm căn cứ.
- Toàn luồng không trợ giúp: cả bốn mục tiêu đạt và không có can thiệp. Có trợ giúp: đạt cả bốn, nhưng đã có gợi ý. Chưa hoàn thành: có mục tiêu thất bại hoặc chưa thực hiện khi dừng.
- Đồng hồ tác vụ bắt đầu sau khi đã đọc mục tiêu, từ Home chưa đăng nhập; dừng khi báo kết quả cuối hoặc chạm 600 giây. Không cộng thời gian SUS/probe.
- Khi bế tắc ít nhất 120 giây: mức 1 nhắc lại mục tiêu, mức 2 gợi ý khu vực, mức 3 chỉ vị trí; ghi mức và thời điểm, không bấm thay.
- Pilot P00 tách khỏi bảy hồ sơ v1; không cộng vào điểm trung bình hoặc tần suất phát hiện.

## Công cụ và sản phẩm

Dùng SUS tiếng Việt trong tài liệu sẵn có (chưa xác minh thẩm định bản dịch), bốn câu probe trung lập, timeline giả định, CSV và Excel. Không tạo danh tính, liên hệ, chữ ký đồng ý, ngày phỏng vấn hay video giả.
'''))
write('00_scope.md',doc('Phạm vi và nguồn dữ liệu Task 2','''Luồng được chọn là quản lý các đơn đã đặt trên web EShop: Login, Home/navbar và Profile/Lịch sử đơn. Task 1/3 trước đó có dữ liệu thực thi trình duyệt thật; các phiên P00–P07 trong thư mục này là mô phỏng riêng.

Cơ sở xây tình huống: source `sut/frontend-web/src/pages/Profile.jsx`, các báo cáo Task 1 và 3. UI có danh sách đơn, số tiền, nhãn trạng thái và nút hủy. Không giả định có trang chi tiết sản phẩm trong đơn, tìm kiếm đơn hoặc chức năng hoàn tác.

Theo yêu cầu cập nhật của sinh viên, bộ này minh họa đầy đủ quy trình và kết quả mô phỏng. Đề gốc trong workspace vẫn yêu cầu bảy người thật; thông tin thay đổi yêu cầu do sinh viên cung cấp, không phải xác nhận độc lập từ giảng viên.

Các con số mô phỏng không được dùng để suy ra hành vi hay mức hài lòng của người dùng thực tế.
'''))
write('03_probe_questions.md',doc('Bốn câu hỏi mở sau SUS',table(['Chủ đề','Câu hỏi trung lập'],[
['Clarity','Có chỗ nào khiến bạn không biết phải làm gì tiếp theo?'],['Recovery','Khi thấy khó khăn hoặc chưa chắc về thao tác, bạn đã làm gì và cần thêm điều gì?'],['Speed','Đoạn nào khiến bạn mất nhiều thời gian hoặc công sức nhất?'],['Trust','Bạn dựa vào điều gì để tin rằng thông tin hoặc thao tác đã đúng?']])+'''
Câu đào sâu tùy diễn biến: “Bạn có thể nói rõ hơn điều đó không?”. Không đưa sẵn đánh giá tốt/xấu, không hỏi “Có phải nút này gây khó hiểu không?”. Bốn câu trả lời của mỗi hồ sơ đã được điền ở `sessions/S01.md`…`S07.md` và workbook; tất cả là lời đáp giả định.
'''))
write('04_moderator_script.md',doc('Lời dẫn điều phối — kịch bản minh họa','''## Mở đầu

“Cảm ơn bạn. Mục tiêu hôm nay là xem trang web hỗ trợ công việc của bạn như thế nào. Chúng tôi đánh giá sản phẩm, không đánh giá năng lực của bạn. Trong lúc thao tác, hãy nói điều bạn đang nghĩ hoặc đang tìm. Bạn có thể dừng bất cứ lúc nào.”

Không nói mọi chỗ khó hiểu đều là lỗi của sản phẩm; ghi nhận trước, phân tích sau.

## Trước tác vụ

Trong phiên thật, giải thích mục đích và xin phép riêng việc ghi màn hình/ghi âm; ghi nhận lựa chọn thực tế. Trong bộ mô phỏng này, các trường đồng ý và ghi hình đều không áp dụng.

Đưa `scenario.md` v1, không giải thích đường dẫn hay vị trí nút. Bắt đầu đồng hồ tác vụ sau khi người tham gia đã đọc mục tiêu.

## Trong tác vụ

Quan sát trung lập. Có thể nhắc “Bạn đang nghĩ gì?” khi họ im lặng. Chỉ gợi ý khi hoàn toàn bế tắc ít nhất 120 giây; ghi chính xác thời điểm, nội dung và mức hỗ trợ. Không thao tác thay. Dừng ở 600 giây nếu chưa xong.

## Kết thúc

Dừng đồng hồ tác vụ. Đưa SUS để trả lời trước khi thảo luận; tiếp đến hỏi bốn probe. Cảm ơn và giải thích cách sử dụng dữ liệu. Các lời thoại hoàn thành trong bộ này là nội dung mô phỏng, không phải bản chép lời một cuộc phỏng vấn.
'''))
write('05_participants.md',doc('Danh sách hồ sơ giả định P00–P07',table(['Mã','Vai trò','Đặc điểm giả định','Kinh nghiệm giả định','Liên hệ / ngày phỏng vấn / ghi hình'],[[s['id'],'Pilot' if s is P else 'Phiên chính mô phỏng',s['profile'],s['experience'],'Không áp dụng — không có người thật'] for s in [P]+S])+'''
Không thay mã hồ sơ bằng tên một người thật để gán cho họ các câu trả lời này. Nếu sau này thu dữ liệu thật, lưu thành bộ dữ liệu khác với nguồn gốc và bằng chứng tương ứng.
'''))
# Keep questionnaire already supplied in the workspace; remove unsubstantiated grade thresholds.
questionnaire=(R/'02_SUS_questionnaire.md').read_text().split('## Diễn giải')[0]
questionnaire=questionnaire.replace('# Thang SUS (System Usability Scale) – bản tiếng Việt','# Phiếu SUS — bản tiếng Việt dùng trong bài tập\n\n'+NOTICE+'\n\nBản diễn đạt tiếng Việt có sẵn trong workspace; chưa xác minh đây là bản dịch đã được thẩm định.')
if NOTICE not in (R/'02_SUS_questionnaire.md').read_text():
    write('02_SUS_questionnaire.md',questionnaire+f'\n## Nguồn và cách dùng\n\nCông thức đối chiếu với [John Brooke — SUS]({SOURCE}). Điểm 0–100 không phải phần trăm. Bộ này chỉ minh họa tính điểm; không suy ra mức hài lòng thực tế hoặc gán hạng A–F.\n\nCâu trả lời bảy hồ sơ: `sus_responses.csv`; pilot lưu riêng trong `data/simulation.json`.\n')
rows=[]
for s in S:rows.append([s['id'],'simulated',*s['sus_answers']])
with (R/'sus_responses.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f,lineterminator='\n');w.writerow(['participant','data_kind']+[f'q{i}' for i in range(1,11)]);w.writerows(rows)
for index,s in enumerate([P]+S):
    title=('Pilot P00 — kịch bản v0' if index==0 else f'Phiên S{index:02} — hồ sơ {s["id"]}, kịch bản v1')
    body=table(['Thông tin','Giá trị'],[['Hồ sơ giả định',s['profile']],['Kinh nghiệm giả định',s['experience']],['Môi trường giả định',D['environment']],['Ngày giờ phỏng vấn / liên hệ / đồng ý / video','Không áp dụng — không có phiên thật'],['Thời gian tác vụ giả định',f'{s["task_time_seconds"]} giây ({clock(s["task_time_seconds"])})'],['Kết quả toàn luồng',{'timeout':'Chưa hoàn thành / hết 600 giây','assisted':'Hoàn thành có trợ giúp','independent':'Hoàn thành không trợ giúp'}[outcome(s)]]])
    body+='\n## Mục tiêu và kết quả giả định\n\n'+table(['Mục','Mục tiêu','Kết quả'],[[k,TITLES[k],STATUS[v]] for k,v in s['tasks'].items()])
    body+='\n## Nhật ký mô phỏng — mốc tương đối, không phải timestamp video\n\n'+table(['Mốc','Màn hình','Hành động giả định','Ghi nhận giả định','Lời thoại giả định','Nhóm'],[[clock(e['seconds']),e['screen'],e['action'],e['note'],e['fictional_quote'] or '—',e['finding'] or '—'] for e in s['events']])
    body+='\n## Can thiệp giả định của moderator\n\n'+(table(['Mốc','Mức','Nội dung'],[[clock(a['seconds']),a['level'],a['text']] for a in s['assistance']]) if s['assistance'] else 'Không có can thiệp trong diễn biến giả định.\n')
    body+='\n## SUS giả định — trả lời trước probe\n\n'+table([f'Q{i}' for i in range(1,11)]+['Điểm SUS'],[s['sus_answers']+[sus(s['sus_answers'])]])
    body+='\n## Câu trả lời mở giả định\n\n'+table(['Chủ đề','Lời đáp giả định'],[[PROBES[k],v] for k,v in s['probes'].items()])
    if index==0:body+='\n## Điều chỉnh trước bảy phiên v1\n\n'+table(['Vấn đề mô phỏng','Điều chỉnh kịch bản'],[[c['problem'],c['change']] for c in s['changes']])+'\nSUS và thời gian pilot không được gộp vào phân tích bảy hồ sơ chính.\n'
    write('sessions/'+('pilot.md' if index==0 else f'S{index:02}.md'),doc(title,body))
write('06_session_notes_template.md',doc('Mẫu ghi chú — các bản mô phỏng đã điền ở sessions/',table(['Trường','Cách dùng'],[['Mã hồ sơ','P00 hoặc P01–P07'],['Nguồn dữ liệu','simulated; giữ nhãn khi sao chép'],['Mốc thời gian','Tương đối từ lúc bắt đầu tác vụ'],['Hành động / lời nói','Mô tả giả định; không gọi là trích nguyên văn phỏng vấn'],['Kết quả T1–T4','Không trợ giúp / có trợ giúp / thất bại / chưa thực hiện'],['SUS','10 số nguyên 1–5'],['Probe','Bốn chủ đề: clarity, recovery, speed, trust']])+ '\nBản đã điền đầy đủ: `sessions/pilot.md`, `sessions/S01.md` đến `sessions/S07.md`.\n'))
analysis='''## 1. Thiết kế và giới hạn diễn giải

Một pilot v0 và bảy hồ sơ v1 giả định cùng thực hiện luồng quản lý đơn đã đặt. P00 chỉ dùng minh họa việc chỉnh kịch bản. Các phản ứng, thời gian và câu trả lời là dữ liệu tổng hợp có chủ đích; không phải mẫu khảo sát độc lập. Không tính khoảng tin cậy, không suy rộng kết quả sang người dùng thật.

'''+table(['Chỉ số mô phỏng — chỉ P01–P07','Giá trị'],[
['Hoàn thành không trợ giúp',f'{counts["independent"]}/7 ({counts["independent"]/7:.1%})'],['Hoàn thành có trợ giúp',f'{counts["assisted"]}/7 ({counts["assisted"]/7:.1%})'],['Chưa hoàn thành / hết giờ',f'{counts["timeout"]}/7 ({counts["timeout"]/7:.1%})'],['Hoàn thành có hoặc không trợ giúp',f'{len(success)}/7 ({len(success)/7:.1%})'],['Thời gian TB tất cả, gồm mốc dừng time-out',f'{summary["duration_all_mean"]:.2f} giây'],['Trung vị; min–max thời gian',f'{summary["duration_all_median"]:.0f}; {min(durations)}–{max(durations)} giây'],['Thời gian TB các hồ sơ hoàn thành',f'{summary["duration_success_mean"]:.2f} giây (n={len(success)})'],['SUS trung bình; trung vị',f'{st.mean(scores):.2f}; {st.median(scores):.2f}'],['SUS độ lệch chuẩn mẫu; min–max',f'{st.stdev(scores):.2f}; {min(scores):.1f}–{max(scores):.1f}'],['Phiên thật / người thật / video thật','0 / 0 / 0']])
analysis+='\n## 2. Kết quả từng hồ sơ\n\n'+table(['Hồ sơ','T1','T2','T3','T4','Giây','SUS'],[[s['id'],*[STATUS[v] for v in s['tasks'].values()],s['task_time_seconds'],sus(s['sus_answers'])] for s in S])
analysis+='\nP06 dừng ở 600 giây: đây là thời gian đã dùng đến khi dừng, không phải thời gian hoàn thành. T4 chưa thực hiện được giữ riêng với T3 thất bại. Không tự thay câu trả lời SUS để đạt mức điểm mong muốn.\n'
analysis+='\n## 3. Tính SUS\n\nCâu lẻ: trừ 1 từ đáp án; câu chẵn: lấy 5 trừ đáp án. Cộng 10 phần rồi nhân 2,5. Ví dụ P01 có tổng đóng góp 30, được 75 điểm. Điểm nằm trên thang 0–100, không phải tỷ lệ phần trăm. Công thức tham khảo [John Brooke — SUS]('+SOURCE+'). Bản tiếng Việt chưa được xác minh thẩm định. Điểm trong báo cáo chỉ mô tả dữ liệu tổng hợp này.\n'
analysis+='\n## 4. Gom nhóm và ưu tiên\n\nMức 4: chặn hoàn toàn mục tiêu; 3: trở ngại đáng kể/cần hỗ trợ; 2: gây chậm hoặc nhầm; 1: bất tiện nhỏ; 0: quan sát. Các mức dưới đây là ưu tiên đề xuất trong mô phỏng.\n\n'
analysis+=table(['Ưu tiên','Nhóm','Vấn đề','Mức','Hồ sơ /7','Mốc trong phiên mô phỏng','Phân loại'],[[rank,f['id'],f['title'],f['severity'],summary['finding_counts'][f['id']],'; '.join(f'{pid} {clock(t)}' for pid,t in refs[f['id']]),f['kind']] for rank,f in enumerate(sorted(D['findings'],key=lambda f:(-f['severity'],f['id'])),1)])
for f in D['findings']:
    analysis+=f'\n### {f["id"]} — {f["title"]}\n\n{f["basis"]}\n\nĐề xuất: {f["recommendation"]}\n'
    if f['issue']:analysis+=f'\n[Issue có sẵn]({f["issue"]}) · [Ảnh Task 1, không phải ảnh phỏng vấn]({f["shot"]}).\n'
analysis+='''
## 5. Phân tích bốn chủ đề

- **Clarity:** P02/P03/P06 được xây dựng với nhầm lẫn ở form đăng nhập; nhóm U01 minh họa khó tìm đường vào lịch sử. Tên liên kết và nhãn chức năng là giả thuyết cần thử với người thật.
- **Recovery:** P03/P05/P06 minh họa nhu cầu hiểu hậu quả và kiểm tra lại thao tác hủy. Tình huống không yêu cầu hủy đơn đang giao; U03 chỉ ghi câu hỏi về nút đang hiển thị, không giả định đã thực thi ca API mới.
- **Speed:** khác biệt thời gian được đặt để thể hiện mức quen công nghệ và các điểm do dự. Đây không phải số đo hiệu năng mạng, tốc độ browser hay bằng chứng nhóm tuổi nào chậm hơn.
- **Trust:** nhãn Đã hủy là căn cứ giả định để hoàn tất T4. Có hồ sơ tự kiểm tra lại, có hồ sơ cần gợi ý và có hồ sơ dừng trước khi hủy.

## 6. Đối chiếu mục tiêu

'''+table(['Mục tiêu','Kết luận trong bộ mô phỏng','Dữ liệu'],[['O1','Điều hướng là một giả thuyết ưu tiên kiểm tra','U01; can thiệp T1 tại P03/P06'],['O2','Các hồ sơ tiếp cận danh sách đều đọc đúng trạng thái theo kịch bản','T1/T2; U02/U05'],['O3','6/7 hồ sơ đạt cả hủy và xác nhận; 1 hồ sơ chưa hủy khi hết giờ','T3/T4; P06; U03/U04'],['O4','Có bảng SUS và bốn nhóm probe cho đủ bảy hồ sơ','sus_responses.csv; sessions/S01–S07']])+'''
## 7. Bằng chứng và công việc tiếp theo

BUG-001 và BUG-010 đã có ảnh thực thi Task 1 và Issue từ trước. Chỉ tham chiếu chúng để làm căn cứ thiết kế mô phỏng; không đổi nguồn thành phỏng vấn Task 2. U01/U04/U05 chưa được xác minh bằng người dùng thật và không được đăng như lỗi mới đã xác nhận. Không có video hay bản đồng ý ghi hình cho P00–P07.

Nếu dùng để quyết định thiết kế sản phẩm, cần thu dữ liệu thực tế riêng và kiểm tra lại các giả thuyết. Với phạm vi hiện tại, bộ mô phỏng đã có đủ kịch bản, pilot, bảy phiên, câu trả lời, tính điểm và phân tích.
'''
write('analysis.md',doc('Báo cáo Task 2 — mô phỏng usability',analysis))
write('07_analysis_template.md','# Báo cáo đã điền\n\n'+NOTICE+'\n\nXem [analysis.md](analysis.md), [PDF toàn bộ hồ sơ](Task2_Simulation_Pack.pdf) và [Excel](Task2_Simulation.xlsx).\n')
readme='''Sinh viên: **Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn**.

Bộ này được thực hiện theo yêu cầu cập nhật của sinh viên: dùng mô phỏng cho bài tập. Thông tin giảng viên cho phép do sinh viên cung cấp; đề gốc lưu trong workspace vẫn yêu cầu người thật. Không ghi bộ này là đã phỏng vấn thật.

## Mở tài liệu

- [PDF toàn bộ hồ sơ](Task2_Simulation_Pack.pdf): tình huống, kế hoạch, lời dẫn, pilot, 7 phiên và phân tích.
- [Excel](Task2_Simulation.xlsx): hồ sơ, câu trả lời SUS, công thức, kết quả, timeline, probe và phát hiện.
- [Tình huống giao cho các hồ sơ](scenario.md); [kế hoạch](01_plan_objectives_scenario.md); [lời dẫn](04_moderator_script.md).
- [Pilot P00](sessions/pilot.md).
'''
readme+='\n'.join(f'- [Phiên S{i:02} — P{i:02}](sessions/S{i:02}.md).' for i in range(1,8))
readme+='\n- [Phân tích đã hoàn thiện](analysis.md).\n- [Dữ liệu nguồn có nhãn simulated](data/simulation.json); [CSV SUS](sus_responses.csv); [số liệu tổng hợp](data/summary.json).\n'
readme+=f'\n## Kết quả mô phỏng\n\n4/7 hoàn thành không trợ giúp; 2/7 có trợ giúp; 1/7 hết giờ. SUS trung bình **{st.mean(scores):.2f}/100**. Pilot không được cộng vào mẫu. **0 phiên phỏng vấn thật, 0 người thật, 0 video thật.**\n'
readme+='''
## Cập nhật và tính lại

Thông tin sinh viên đã điền sẵn. Các hồ sơ chỉ dùng mã P00–P07 và đặc điểm giả định; không cần điền tên hay liên hệ thật vào những câu trả lời tổng hợp này. Nếu sửa dữ liệu giả định, sửa `data/simulation.json` rồi chạy từ HW03:

```bash
python3 submission/usability/scripts/build_simulation.py
python3 submission/usability/sus_scoring.py submission/usability/sus_responses.csv
```

Workbook có cột SUS tính bằng Python để xem ngay và cột công thức Excel để đối chiếu; báo cáo là ảnh chụp số liệu tại lần sinh tài liệu. Không ghi đè workbook sau khi sửa tay nếu chưa chuyển chỉnh sửa về JSON nguồn.

Quy trình sinh tài liệu không liên hệ ai, không chạy server và không thay đổi SQLite.
'''
write('README.md',doc('Task 2 — bộ mô phỏng 1 pilot + 7 phiên',readme))
# Workbook: provenance is visible on every sheet and every respondent is simulated.
wb=Workbook();wb.remove(wb.active)
def sheet(name,headers,rows,widths=None):
    ws=wb.create_sheet(name);ws.append([LABEL]);ws.append(headers)
    for row in rows:ws.append(row)
    ws.freeze_panes='C3';ws.auto_filter.ref=f'A2:{ws.cell(ws.max_row,len(headers)).coordinate}'
    for row in ws:
        for c in row:c.alignment=Alignment(vertical='top',wrap_text=True)
    for rownum in (1,2):
        for c in ws[rownum]:c.font=Font(bold=True,color='FFFFFF');c.fill=PatternFill('solid',fgColor='17365D')
    for i in range(1,len(headers)+1):ws.column_dimensions[ws.cell(2,i).column_letter].width=(widths[i-1] if widths else 25)
    return ws
sheet('Readme',['Mục','Nội dung'],[['Nguồn','Mô phỏng phục vụ bài tập; không có phỏng vấn thật'],['Sinh viên','Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn'],['Pilot','P00, tách khỏi thống kê'],['Mẫu chính','P01–P07, tất cả simulated'],['Ngày phỏng vấn / video / đồng ý','Không áp dụng'],['SUS tính bằng Python','Giá trị tính từ JSON tại lúc sinh file'],['SUS Excel','Công thức đối chiếu các ô Q1–Q10; Excel tính lại khi mở'],['Tài liệu','README.md và Task2_Simulation_Pack.pdf']], [30,110])
sheet('Profiles',['Mã','Nguồn','Hồ sơ giả định','Kinh nghiệm','Liên hệ / ngày phỏng vấn'],[[s['id'],'simulated',s['profile'],s['experience'],'Không áp dụng'] for s in [P]+S],[12,15,65,55,35])
susws=sheet('SUS',['Mã','Nguồn']+[f'Q{i}' for i in range(1,11)]+['SUS Python','SUS Excel'],[[s['id'],'simulated',*s['sus_answers'],sus(s['sus_answers']),None] for s in S],[12,16]+[8]*10+[18,18])
for row in range(3,10):
    terms=[f'{susws.cell(row,c).coordinate}-1' if c%2==1 else f'5-{susws.cell(row,c).coordinate}' for c in range(3,13)]
    susws.cell(row,14,'=('+'+'.join('('+x+')' for x in terms)+')*2.5')
    susws.cell(row,13).number_format=susws.cell(row,14).number_format='0.00'
validation=DataValidation(type='whole',operator='between',formula1=1,formula2=5);validation.errorTitle='Giá trị SUS không hợp lệ';validation.error='Nhập số nguyên 1–5.';validation.showErrorMessage=True;validation.errorStyle='stop';susws.add_data_validation(validation);validation.add('C3:L9')
sheet('TaskResults',['Mã','Nguồn']+list(TITLES)+['Giây tác vụ','Kết quả toàn luồng','Số gợi ý'],[[s['id'],'simulated',*[STATUS[v] for v in s['tasks'].values()],s['task_time_seconds'],outcome(s),len(s['assistance'])] for s in S],[12,15,22,22,22,22,18,25,16])
sheet('Timeline',['Mã','Nguồn','Giây','Mốc','Màn hình','Hành động giả định','Ghi nhận giả định','Lời thoại giả định','Nhóm'],[[s['id'],'simulated',e['seconds'],clock(e['seconds']),e['screen'],e['action'],e['note'],e['fictional_quote'],e['finding']] for s in [P]+S for e in s['events']],[12,15,10,10,16,60,60,60,12])
sheet('Probes',['Mã','Nguồn','Chủ đề','Câu trả lời giả định'],[[s['id'],'simulated',PROBES[k],v] for s in [P]+S for k,v in s['probes'].items()],[12,15,30,100])
sheet('Findings',['Nhóm','Nguồn tần suất','Vấn đề','Mức','Số hồ sơ /7','Tham chiếu mô phỏng','Cơ sở','Đề xuất','Issue có sẵn'],[[f['id'],'simulated',f['title'],f['severity'],summary['finding_counts'][f['id']],'; '.join(f'{pid} {clock(t)}' for pid,t in refs[f['id']]),f['basis'],f['recommendation'],f['issue'] or 'Chưa xác minh; không tạo Issue mới'] for f in D['findings']],[12,20,55,10,18,55,80,80,65])
sheet('Summary',['Chỉ số mô phỏng','Giá trị'],[[k,v] for k,v in summary.items() if not isinstance(v,dict)]+[[k,v] for k,v in counts.items()],[48,60])
wb.save(R/'Task2_Simulation.xlsx')
# One printable pack; each embedded session retains its own explicit provenance.
parts=['# Task 2 — Bộ hồ sơ mô phỏng hoàn chỉnh\n\n'+NOTICE+'\n\nSinh viên: Phạm Quang Vinh — 23120202 — 23120202@student.hcmus.edu.vn.\n']
parts.append('## Nội dung bộ hồ sơ\n\n1. Tình huống và kế hoạch đánh giá.\n2. Lời dẫn, phiếu SUS và câu hỏi mở.\n3. Hồ sơ pilot P00 và điều chỉnh kịch bản.\n4. Bảy phiên S01–S07, mỗi phiên có timeline, kết quả, SUS và probe.\n5. Phân tích, ưu tiên cải tiến và nguồn tham chiếu.\n\nThông tin sinh viên đã điền sẵn. Các hồ sơ P00–P07 là giả định; không có người tham gia thực tế. Excel và CSV đi kèm chứa dữ liệu để đối chiếu số liệu trong PDF.\n')
for name in ['scenario.md','01_plan_objectives_scenario.md','04_moderator_script.md','02_SUS_questionnaire.md','03_probe_questions.md','05_participants.md','sessions/pilot.md']+[f'sessions/S{i:02}.md' for i in range(1,8)]+['analysis.md']:
    parts.append((R/name).read_text())
write('Task2_Simulation_Pack.md','\n\n'.join(parts))
print(json.dumps(summary,ensure_ascii=False,indent=2))
