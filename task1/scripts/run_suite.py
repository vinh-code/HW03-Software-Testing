#!/usr/bin/env python3
"""Replay the actual CLI checks. Requires the three SUT servers already running.
Mutates only dedicated task1-* fixtures. Take a database backup before invoking.
"""
import json,subprocess,sqlite3,shutil,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];S=ROOT/'submission/task1/scripts';OUT=ROOT/'output/playwright/task1'
os.chdir(ROOT);OUT.mkdir(parents=True,exist_ok=True)
cli=['bash',str(Path.home()/'.codex/skills/playwright/scripts/playwright_cli.sh'),'-s=hw03']
subprocess.run(['python3',str(S/'seed_fixture.py')],check=True)
f=json.loads((ROOT/'submission/task1/evidence/fixture.json').read_text())
subprocess.run(cli+['open','http://localhost:5173/login'],check=True,capture_output=True,text=True)
runs={};all_results=[]
for stage in ['login','profile','admin']:
 if stage=='admin':
  with sqlite3.connect(ROOT/'sut/backend/database.sqlite') as c:
   for state in ('pending','confirmed'):c.execute('update orders set status=? where id=?',(state,f['orders'][state]))
 code='async (page) => {\nconst fixture='+json.dumps(f)+';\n'+(S/'common.js').read_text()+(S/f'{stage}.body.js').read_text()+'\nreturn {results,dialogs,browser:page.context().browser().version(),ua:await page.evaluate(()=>navigator.userAgent)};\n}'
 p=S/f'{stage}.run.js';p.write_text(code)
 proc=subprocess.run(cli+['run-code','--filename',str(p)],capture_output=True,text=True,check=True)
 (OUT/f'{stage}.log').write_text(proc.stdout)
 if '### Result\n' not in proc.stdout:raise RuntimeError(f'{stage} did not return results: '+proc.stdout[:2000])
 d=json.loads(proc.stdout.split('### Result\n')[1].split('\n###')[0]);runs[stage]=d;all_results+=d['results']
all_results.sort(key=lambda r:r['id'])
assert len(all_results)==len({r['id'] for r in all_results})==58
(ROOT/'submission/task1/evidence/results.json').write_text(json.dumps({'runs':runs,'results':all_results},ensure_ascii=False,indent=2))
for r in all_results:
 if r['status']=='Failed':shutil.copy(OUT/f'{r["id"]}.png',ROOT/'submission/bugs/screenshots'/f'{r["id"]}.png')
print('58 checks recorded. Review results before rebuilding reports.')
