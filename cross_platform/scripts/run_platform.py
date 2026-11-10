#!/usr/bin/env python3
"""Execute the reviewed Task 1 checklist in a real headed Chrome or Firefox.
Uses separate task3-* fixtures and never overwrites Task 1 evidence.
"""
import json,subprocess,sqlite3,shutil,os,sys
from pathlib import Path
W=Path(__file__).resolve().parents[3];R=W/'submission';S=R/'cross_platform/scripts';T=R/'task1/scripts'
os.chdir(W)
platform=sys.argv[1];assert platform in ('chrome','firefox')
OUT=W/'output/playwright/task3'/platform;OUT.mkdir(parents=True,exist_ok=True)
images=R/'cross_platform/screenshots'/platform;images.mkdir(parents=True,exist_ok=True)
cli=['bash',str(Path.home()/'.codex/skills/playwright/scripts/playwright_cli.sh'),f'-s=hw03-t3-{platform}']
def command(*args):
 p=subprocess.run(cli+list(args),capture_output=True,text=True,timeout=100)
 if p.returncode:raise RuntimeError(p.stdout+p.stderr)
 return p.stdout
subprocess.run(['python3',str(S/'seed_fixture.py')],check=True,capture_output=True)
f=json.loads((R/'cross_platform/evidence/fixture.json').read_text());env=json.loads((R/'cross_platform/evidence/environment.json').read_text())
command('open','http://localhost:5173/login','--browser',platform,'--headed')
print(platform,'browser opened',flush=True)
runs={};all_results=[]
for stage in ('login','profile','admin'):
 if stage=='admin':
  with sqlite3.connect(W/'sut/backend/database.sqlite') as c:
   for state in ('pending','confirmed'):c.execute('update orders set status=? where id=?',(state,f['orders'][state]))
 body=(T/f'{stage}.body.js').read_text().replace('task1-','task3-').replace("name:'Task 1 Tester'","name:'Phạm Quang Vinh — 23120202'")
 if stage=='login':body="await page.goto(web+'/login');await page.evaluate(()=>localStorage.clear());await page.reload();\n"+body
 code='async (page) => {\nconst fixture='+json.dumps(f)+';\nconst environment='+json.dumps(env,ensure_ascii=False)+';\nconst platformKey='+json.dumps(platform)+';\n'+(S/'common.js').read_text()+body+'\nreturn {results,dialogs,browser:browserVersion,ua:await page.evaluate(()=>navigator.userAgent),locale:await page.evaluate(()=>navigator.language)};\n}'
 p=OUT/f'{stage}.run.js';p.write_text(code)
 log=command('run-code','--filename',str(p));(OUT/f'{stage}.log').write_text(log)
 if '### Result\n' not in log:raise RuntimeError(stage+': '+log[:2000])
 d=json.loads(log.split('### Result\n')[1].split('\n###')[0]);runs[stage]=d;all_results+=d['results'];print(platform,stage,len(d['results']),'checks',flush=True)
all_results.sort(key=lambda r:r['id']);assert len(all_results)==len({r['id'] for r in all_results})==58
result={'platform':platform,'headed':True,'environment':env,'fixture':f,'runs':runs,'results':all_results}
(R/f'cross_platform/evidence/{platform}.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
for row in all_results:
 if row['status']=='Failed':shutil.copy(OUT/f'{row["id"]}.png',images/f'{row["id"]}.png')
command('close')
print(platform, 'Passed',sum(r['status']=='Passed' for r in all_results),'Failed',sum(r['status']=='Failed' for r in all_results),flush=True)
