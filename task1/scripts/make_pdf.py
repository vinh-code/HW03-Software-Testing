"""Render simple submission Markdown into standalone HTML and Playwright PDF jobs."""
from pathlib import Path
import re,html,json
R=Path(__file__).resolve().parents[2];W=R.parent;OUT=W/'output/playwright/task1'
def inline(s):
 s=html.escape(s)
 s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',lambda m:'<a href="'+m[2]+'">'+m[1]+'</a>',s)
 s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
 s=re.sub(r'`([^`]+)`',r'<code>\1</code>',s)
 return s
jobs=[]
for name in ['report/main_report','ai_audit_report','ai_critique','cross_platform/README']:
 lines=(R/(name+'.md')).read_text().splitlines();parts=[];table=False
 for line in lines:
  if line.startswith('|'):
   if re.match(r'^\|[\s:|\-]+$',line):continue
   if not table:parts.append('<table>');table=True
   cells=line.strip().strip('|').split('|');parts.append('<tr>'+''.join('<td>'+inline(c.strip())+'</td>' for c in cells)+'</tr>');continue
  if table:parts.append('</table>');table=False
  if not line.strip():continue
  m=re.match(r'^(#{1,6}) (.*)',line)
  if m:parts.append(f'<h{len(m[1])}>'+inline(m[2])+f'</h{len(m[1])}>')
  else:parts.append('<p>'+inline(line)+'</p>')
 if table:parts.append('</table>')
 doc='<!doctype html><html lang="vi"><meta charset="utf-8"><style>body{font:11px Arial,sans-serif;color:#172334;line-height:1.5}h1{font-size:23px}h2{font-size:16px;border-bottom:1px solid #ddd;margin-top:22px}h3{font-size:13px}table{border-collapse:collapse;width:100%;font-size:10px}td{border:1px solid #ccc;padding:5px;vertical-align:top}tr:first-child{font-weight:bold;background:#edf2f7}tr{break-inside:avoid}p{margin:6px 0}a{color:#155a8a}code{overflow-wrap:anywhere}</style><body>'+''.join(parts)+'</body></html>'
 (OUT/(Path(name).name+'.html')).write_text(doc)
 jobs.append({'html':doc,'pdf':str(R/(name+'.pdf'))})
code='async (page) => {\nconst jobs='+json.dumps(jobs,ensure_ascii=False)+';\nfor (const job of jobs) {await page.setContent(job.html);await page.pdf({path:job.pdf,format:"A4",printBackground:true,margin:{top:"18mm",bottom:"18mm",left:"16mm",right:"16mm"}});}\nreturn jobs.map(j=>j.pdf);\n}'
(OUT/'pdf.run.js').write_text(code)
