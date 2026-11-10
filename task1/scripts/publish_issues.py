#!/usr/bin/env python3
"""Publish prepared Task 1 issues using gh; reuse existing BUG IDs on rerun."""
import json,subprocess,re
from pathlib import Path
R=Path(__file__).resolve().parents[2]
repo='vinh-code/HW03-Software-Testing'
def gh(*args):return subprocess.check_output(['gh',*args],text=True,timeout=45).strip()
head=subprocess.check_output(['git','-C',str(R),'rev-parse','HEAD'],text=True).strip()
raw=f'https://raw.githubusercontent.com/{repo}/{head}'
blob=f'https://github.com/{repo}/blob/{head}'
p=R/'task1/evidence/issues.json';issues=json.loads(p.read_text())
existing=json.loads(gh('issue','list','--repo',repo,'--state','all','--limit','100','--json','title,url'))
by_id={m[1]:i['url'] for i in existing if (m:=re.match(r'\[(BUG-\d+)\]',i['title']))}
folder=R.parent/'output/playwright/task1/github';folder.mkdir(parents=True,exist_ok=True)
for i in issues:
 if i['id'] in by_id:i['url']=by_id[i['id']]
 else:
  body=(R/'bugs'/f'{i["id"]}.md').read_text()
  body='\n'.join(x for x in body.splitlines() if not x.startswith('- GitHub Issue:'))
  body=re.sub(r'\]\(screenshots/([^)]*)\)',lambda m:f']({raw}/bugs/screenshots/{m[1]})',body)
  body=body.replace('`../task1/evidence/results.json`',f'[JSON thực thi]({blob}/task1/evidence/results.json)')
  body+=f'\n\nNguồn: [báo cáo lỗi trong repository]({blob}/bugs/{i["id"]}.md). Sinh viên: 23120202.\n'
  bodyfile=folder/f'{i["id"]}.md';bodyfile.write_text(body)
  i['url']=gh('issue','create','--repo',repo,'--title',f'[{i["id"]}] {i["title"]}','--body-file',str(bodyfile),'--label','bug')
 p.write_text(json.dumps(issues,ensure_ascii=False,indent=2)+'\n')
 print(i['id'],i['url'],flush=True)
