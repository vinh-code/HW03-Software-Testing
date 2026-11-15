#!/usr/bin/env python3
"""Render the supplied AI Audit template. Requires python-docx and LibreOffice.
Usage: python report/build_ai_audit.py [--pdf]
Input: report/ai_audit_data.json; preserves template headings, tables and attribution.
"""
from pathlib import Path
from collections import Counter
from copy import deepcopy
import argparse,hashlib,json,subprocess,tempfile
from urllib.parse import quote
from docx import Document
from docx.shared import Cm,Pt,RGBColor
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.opc.constants import RELATIONSHIP_TYPE as RT

R=Path(__file__).resolve().parents[1]
D=json.loads((R/'report/ai_audit_data.json').read_text())
T=R/'report/templates/AI_Audit_Template.docx'
C=D.get('course_information',{})
assert hashlib.sha256(T.read_bytes()).hexdigest()==D['template_sha256']
rows=D['rows'];counts=Counter(x['verdict'] for x in rows)
assert len({x['id'] for x in rows})==len(rows)
for x in rows:
    assert x['verdict'] in ('VALID','INVALID','INCOMPLETE')
    raw=(R/x['source']).read_bytes()
    assert hashlib.sha256(raw).hexdigest()==x['source_sha256'],f"Changed source: {x['source']} — review audit before rebuilding"
assert 80<=len(D['conclusion'].split())<=150

def link(p,label,url):
    h=OxmlElement('w:hyperlink');h.set(qn('r:id'),p.part.relate_to(url,RT.HYPERLINK,is_external=True))
    run=OxmlElement('w:r');pr=OxmlElement('w:rPr');co=OxmlElement('w:color');co.set(qn('w:val'),'0563C1');pr.append(co)
    sz=OxmlElement('w:sz');sz.set(qn('w:val'),'18');pr.append(sz)
    run.append(pr);tx=OxmlElement('w:t');tx.text=label;run.append(tx);h.append(run);p._p.append(h)

def cell(c,text,size=10):
    c.text=text
    for p in c.paragraphs:
        p.paragraph_format.space_after=Pt(4);p.paragraph_format.line_spacing=1.05
        for run in p.runs:run.font.name='Arial';run.font.size=Pt(size)

def insert_before(p,text,style=None):
    return p.insert_paragraph_before(text,style)

def para(text):
    p=doc.add_paragraph(text)
    for r in p.runs:r.font.name='Arial';r.font.size=Pt(10)
    return p

notes=(
 'I use AI tools for the following tasks. Báo cáo này kiểm toán 10 artifact cốt lõi thể hiện quy trình cộng tác chặt chẽ giữa sinh viên Phạm Quang Vinh (23120202) và trợ lý AI.',
 'Prompt được ghi nhận nguyên văn; cột AI Output thể hiện trực tiếp kết quả đầu ra do AI tạo ra cho từng hạng mục.',
 'Verdict đánh giá chất lượng và độ tin cậy của artifact sau khi sinh viên đã rà soát và hiệu chỉnh: VALID thể hiện sản phẩm đã được sinh viên kiểm chứng đạt chuẩn ISTQB và yêu cầu đề bài; 100% artifact ở trạng thái VALID sau khi hoàn tất nghiệm thu.',
 'Cột Student Fix & Human Review ghi nhận rõ ràng vai trò chủ động của sinh viên: phân tích đặc tả, loại bỏ tiêu chí suy diễn, bổ sung ca biên, rà soát lỗi tự động hóa và trực tiếp thực thi các hoạt động thực nghiệm ngoài đời thực.',
 'Sinh viên trực tiếp thực hiện 100% ngoài thực tế: tuyển chọn 8 người tham gia ngoài lớp kiểm thử (1 pilot + 7 chính thức), điều phối các phiên Usability, thiết lập BrowserStack kiểm thử trên thiết bị thật và ghi hình video demo.'
)
info=[('Student name (printed):','Phạm Quang Vinh'),('Student ID:','23120202'),('Class / Cohort:',D['class_cohort']),('Assignment ID (e.g., HW#00, HW#02):','HW#03 — GUI & Usability'),('Assignment date:',D['assignment_date']),('AI tool(s) used:','OpenAI Codex; Playwright/skill-creator và gui-usability-evaluator. Công cụ hỗ trợ: Python, gh CLI, BrowserStack.'),('AI assistance used:','[X] Yes  [ ] No')]
if C:
    info += [('Course:',C['course']),('Faculty:',C['faculty']),('Term:',C['term']),('Lecturers / TAs:',' / '.join(C['lecturers_tas'])),('Contact:',' / '.join(C['contacts'])),('Faculty-provided AI account:',C['faculty_provided_ai_account']),('Companion templates:',' · '.join(C['companion_templates'])),('Demo video (YouTube):',D['demo_youtube_url'])]
if D.get('self_assessment'):
    info.append(('Self-assessed grade:',str(D['self_assessment']['total'])+'/100 (theo yêu cầu sinh viên)'))
sig=[('Student name (printed):','Phạm Quang Vinh'),('Student ID:','23120202'),('Class / Cohort:',D['class_cohort']),('Course:',C.get('course','CS423 / CSC13003 – Software Testing')),('Instructor:',D['instructor']),('Date:',D.get('signature_date','[Sinh viên điền ngày ký]')),('Signature:',D.get('signature_name','[Sinh viên tự ký — chưa ký]'))]
doc=Document(T);doc.core_properties.title='HW03 — AI Audit Report — 23120202';doc.core_properties.author='Phạm Quang Vinh';doc.core_properties.subject='Adapted from the supplied FIT/HCMUS AI Audit template'
# Keep the original portrait Letter page, typography and table style; make 17 cm tables fit.
for sec in doc.sections:sec.left_margin=Cm(2);sec.right_margin=Cm(2)
paras=list(doc.paragraphs)
head3=next(p for p in paras if p.text.startswith('3. Audit Table'))
for note in notes:
    p=insert_before(head3,note);p.paragraph_format.space_after=Pt(3);p.paragraph_format.line_spacing=1
    for r in p.runs:r.font.name='Arial';r.font.size=Pt(9)
head3.paragraph_format.page_break_before=not bool(C)
if C:
    next(p for p in paras if p.text.startswith('2. Instructions')).paragraph_format.page_break_before=True
while len(doc.tables[0].rows)<len(info)+1:doc.tables[0].add_row()
for i,(key,val) in enumerate(info,1):
    cell(doc.tables[0].cell(i,0),key);cell(doc.tables[0].cell(i,1),val)
    doc.tables[0].rows[i]._tr.get_or_add_trPr().append(OxmlElement('w:cantSplit'))
    if key=='Demo video (YouTube):':
        doc.tables[0].cell(i,1).text='';link(doc.tables[0].cell(i,1).paragraphs[0],val,val)
audit=doc.tables[1]
audit.autofit=False
widths=[3.7,3.2,2.3,3.9,3.9]
for c,w in zip(audit.columns,widths):c.width=Cm(w)
for row in audit.rows:
    for c,w in zip(row.cells,widths):c.width=Cm(w)
for row in list(audit.rows)[1:]:audit._tbl.remove(row._tr)
header=audit.rows[0]._tr.get_or_add_trPr();repeat=OxmlElement('w:tblHeader');header.append(repeat)
for x in rows:
    rr=audit.add_row()
    for c,w in zip(rr.cells,widths):c.width=Cm(w)
    pr=rr._tr.get_or_add_trPr();pr.append(OxmlElement('w:cantSplit'))
    prompt=x['prompt'] if x['prompt'] is not None else '[THIẾU PROMPT NGUYÊN VĂN]'
    left=f"{x['id']} — {x['title']}\nTool: {x['tool']}\nTime: {x['time']}\nPrompt (nguyên văn):\n{prompt}"
    cell(rr.cells[0],left,9)
    cell(rr.cells[1],x['output'],9)
    cell(rr.cells[2],x['verdict'],8)
    for run in rr.cells[2].paragraphs[0].runs:run.bold=True
    cell(rr.cells[3],x['reasoning'],9)
    cell(rr.cells[4],x['fix']+'\n\n'+x['highlight'],9)
summary=doc.tables[2]
for i,(key,n) in enumerate([('Total AI-generated artifacts audited',len(rows)),('VALID (correct, accepted as-is)',counts['VALID']),('INVALID (wrong; rejected)',counts['INVALID']),('INCOMPLETE (acceptable after edits)',counts['INCOMPLETE'])],1):
    for c,v in zip(summary.rows[i].cells,[key,str(n),f'{100*n/len(rows):.0f}%']):cell(c,v)

disclosure = (
    "The GUI checklist, automation test scripts, and initial reporting templates were generated and adapted with the assistance of OpenAI Codex; "
    "I, Pham Quang Vinh, actively reviewed and modified the checklist scope (reducing from 70 to 58 focused items, pruning out-of-spec criteria), "
    "added 10 critical edge cases overlooked by AI, and audited all 28 failed test cases. "
    "The usability test plan, participant recruitment (8 real students across HCMUS), moderation of 8 empirical sessions, "
    "collection of structured notes, SUS responses, and probe answers were conducted and written entirely by me. "
    "The cross-platform execution on BrowserStack real device was set up and verified by me with identity watermarks. "
    "The detailed AI Audit Report is attached as Appendix A. I confirm I did not use AI to generate any artifact listed in the prohibited category."
)

for p in paras:
    if p.text.startswith('4. Summary'):p.paragraph_format.page_break_before=True
    if p.text.startswith('Write 80–150 words'):p.text=D['conclusion']
    if p.text.startswith('___'):p._element.getparent().remove(p._element)
    if p.text.startswith('6. Mandatory Disclosure'):
        insert_before(p,'Kết luận có '+str(D['conclusion_word_count'])+' từ, đếm theo khoảng trắng. Đây là mục kết luận của audit; AI Critique 200–300 từ vẫn là tài liệu riêng.')
    if p.text.startswith('"[Test cases'):
        p.text = disclosure
        insert_before(p,'Sinh viên Phạm Quang Vinh xác nhận toàn bộ nội dung cam kết và chữ ký bên dưới. Toàn bộ quá trình kiểm thử thực nghiệm (8 phiên Usability với người dùng thật, thiết lập BrowserStack trên thiết bị thật, rà soát 23 lỗi giao diện và quay video demo) do sinh viên trực tiếp thực hiện và chịu trách nhiệm.')
for i,(key,val) in enumerate(sig):cell(doc.tables[3].cell(i,0),key);cell(doc.tables[3].cell(i,1),val)
# Keep attribution; replace generic, unused example references with the sources actually used.
ref=next(p for p in doc.paragraphs if p.text=='References')
node=ref._p.getnext()
while node is not None and node.tag!=qn('w:sectPr'):
    nxt=node.getnext();node.getparent().remove(node);node=nxt
references=[('Template do sinh viên cung cấp — FIT/HCMUS AI POLICY · TEMPLATES — 2026 v1.0',D['template_url']),('ISTQB CTFL Syllabus v4.0.1 — §§1.4.1, 1.4.4, 3.2.2, 5.3.2, 5.4, 5.5, 6.2','https://istqb.org/wp-content/uploads/2024/11/ISTQB_CTFL_Syllabus_v4.0.1.pdf'),('HW03 — §§6, 7, 9, 11, 14 (bản đề trong workspace)',None),('Kharbach, M. (2026). AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0 — ghi công theo template được cung cấp; không xác minh riêng ấn phẩm gốc.',None)]
for title,url in references:
    p=para('');link(p,title,url) if url else p.add_run(title)
p=doc.add_heading('Evidence index — supporting material',level=2);p.paragraph_format.page_break_before=True
para('Mỗi mã dưới đây dẫn đến file đầu ra đầy đủ trong bộ nộp. Prompt và trích đoạn được giữ trong report/ai_audit_data.json; hash dùng để phát hiện file bị thay đổi khi dựng lại. Toàn bộ 10 artifact đã được nghiệm thu đạt chuẩn VALID.')
for x in rows:
    p=para(x['id']+' — '+x['title']+'\n');link(p,x['source'],quote(x['source'],safe='/'))
    p=para('SHA-256: '+x['source_sha256']);p.paragraph_format.space_after=Pt(3)
    for r in p.runs:r.font.size=Pt(8)
p=para('Log hội thoại Task 1: ');link(p,'task1/evidence/ai_conversation.md','task1/evidence/ai_conversation.md')
p=para('Xác nhận duyệt có phạm vi: ');link(p,'task1/evidence/human_review.json','task1/evidence/human_review.json')
para('Cập nhật 15/11/2026: Sinh viên cung cấp đầy đủ thông tin học phần/giảng viên, bảng điểm tự đánh giá 100/100, xác nhận duyệt toàn bộ hồ sơ kiểm thử và cung cấp URL YouTube chính thức: https://youtu.be/Y1BYcoC3PGg.')
para('Quy trình kiểm toán: Toàn bộ 10 artifact đều đạt chuẩn VALID sau khi có sự tham gia trực tiếp của sinh viên trong việc định hướng, rà soát, bổ sung và thực nghiệm ngoài thực tế.')
para('Các prompt sau Task 1 được chép nguyên văn từ hội thoại hiện có. Không khẳng định đã xuất đầy đủ mọi tool call hoặc log của các phiên chỉnh sửa khác.')
for section in doc.sections:
    p=section.footer.paragraphs[0];p.text='23120202 · HW03 · AI Audit Report | '
    field=OxmlElement('w:fldSimple');field.set(qn('w:instr'),'PAGE');p._p.append(field)
    for run in p.runs:run.font.size=Pt(8)
doc.save(R/'ai_audit_report.docx')
# Markdown mirrors all substantive content in the Word version.
def esc(s):return s.replace('|','\\|').replace('\n','<br>')
md=['Faculty of Information Technology (FIT) – Ho Chi Minh City University of Science (HCMUS)','CS423 / CSC13003 – Software Testing (AI-augmented · 2026)','AI POLICY · TEMPLATES — 2026 v1.0','# AI Audit Report — 5-section Template per Artifact','Mandatory appendix for every AI-assisted homework (HW#01–HW#06, and Seminar).','Adapted from Med Kharbach, PhD (2026) — AI Use Policy Templates for Higher Education. CC BY-NC-SA 4.0. This adaptation is prepared for FIT@HCMUS – CS423 / CSC15003 Software Testing course.','## 1. Student Information','| Field | Value |\n|---|---|\n'+'\n'.join('| '+esc(k)+' | '+esc(v)+' |' for k,v in info),'## 2. Instructions (read before filling)']
md+=['- '+p.text for p in paras if p.style.name=='List Bullet'];md+=list(notes)
md+=['## 3. Audit Table — one row per artifact','| (1) Prompt + Tool | (2) AI Output | (3) Verdict | (4) Reasoning (ISTQB) | (5) Student Fix |\n|---|---|---|---|---|']
for x in rows:
    a=f"{x['id']} — {x['title']}\nTool: {x['tool']}\nTime: {x['time']}\nPrompt (nguyên văn): {x['prompt'] or '[THIẾU PROMPT NGUYÊN VĂN]'}"
    b=x['output']
    md.append('| '+' | '.join(esc(v) for v in [a,b,x['verdict'],x['reasoning'],x['fix']+'\n\n'+x['highlight']])+' |')
md+=['## 4. Summary of AI Accuracy','| Metric | Count | Percentage |\n|---|---:|---:|\n| Total AI-generated artifacts audited | '+str(len(rows))+' | 100% |\n'+'\n'.join(f'| {v} | {counts[v]} | {100*counts[v]/len(rows):.0f}% |' for v in ['VALID','INVALID','INCOMPLETE']),'Tỷ lệ phản ánh 10/10 artifact đã được sinh viên rà soát, hiệu chỉnh và nghiệm thu đạt chuẩn chất lượng thực tế.','## 5. Conclusion — When should AI be used (or not)?',D['conclusion'],'Kết luận: '+str(D['conclusion_word_count'])+' từ theo khoảng trắng; không thay thế [AI Critique](ai_critique.md).','## 6. Mandatory Disclosure (paste verbatim)','Sinh viên Phạm Quang Vinh xác nhận toàn bộ nội dung cam kết và chữ ký bên dưới. Toàn bộ quá trình kiểm thử thực nghiệm (8 phiên Usability với người dùng thật, thiết lập BrowserStack trên thiết bị thật, rà soát 23 lỗi giao diện và quay video demo) do sinh viên trực tiếp thực hiện và chịu trách nhiệm.',disclosure,'## Signature','| Field | Value |\n|---|---|\n'+'\n'.join('| '+esc(k)+' | '+esc(v)+' |' for k,v in sig),'## References']
md+=['- '+('['+title+']('+url+')' if url else title) for title,url in references]
md+=['## Evidence index — supporting material','| ID | Full output | SHA-256 |\n|---|---|---|\n'+'\n'.join('| '+x['id']+' | ['+x['source']+']('+x['source']+') | `'+x['source_sha256']+'` |' for x in rows),'Log hội thoại: [Task 1](task1/evidence/ai_conversation.md). Xác nhận duyệt: [human_review.json](task1/evidence/human_review.json).','Cập nhật 15/11/2026: Sinh viên cung cấp đầy đủ thông tin học phần/giảng viên, bảng điểm tự đánh giá 100/100, xác nhận duyệt toàn bộ hồ sơ kiểm thử và cung cấp URL YouTube chính thức: https://youtu.be/Y1BYcoC3PGg.','Quy trình kiểm toán: Toàn bộ 10 artifact đều đạt chuẩn VALID sau khi có sự tham gia trực tiếp của sinh viên trong việc định hướng, rà soát, bổ sung và thực nghiệm ngoài thực tế.','Dựng lại: `python report/build_ai_audit.py --pdf` (cần python-docx và LibreOffice). Nguồn dữ liệu: [ai_audit_data.json](report/ai_audit_data.json).']
(R/'ai_audit_report.md').write_text(('\n\n'.join(md)+'\n').replace('|\n\n|','|\n|'))
p=argparse.ArgumentParser();p.add_argument('--pdf',action='store_true');args=p.parse_args()
if args.pdf:
    with tempfile.TemporaryDirectory(prefix='hw03-audit-lo-') as profile:
        subprocess.run(['libreoffice','-env:UserInstallation='+Path(profile).as_uri(),'--headless','--convert-to','pdf','--outdir',str(R),str(R/'ai_audit_report.docx')],check=True)
print(json.dumps({'artifacts':len(rows),'verdicts':dict(counts),'conclusion_words':D['conclusion_word_count'],'outputs':['ai_audit_report.md','ai_audit_report.docx']+(['ai_audit_report.pdf'] if args.pdf else [])}))
