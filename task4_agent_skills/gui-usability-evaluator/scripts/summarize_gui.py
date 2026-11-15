#!/usr/bin/env python3
"""Validate and summarize an existing GUI run; does not execute or invent checks."""
import argparse, collections, csv, datetime, json
from pathlib import Path

def summarize(path):
    path=Path(path);d=json.loads(path.read_text());base=path.parent.resolve()
    if d.get('data_kind') not in ('real','simulated') or not d.get('screen') or not d.get('environment'):
        raise ValueError('Required: data_kind, screen and environment')
    rows=d.get('results',[])
    if not rows:raise ValueError('No checklist results')
    seen=set();aspects={'IA-01','IA-02','IA-03','IA-04'}
    for r in rows:
        for k in ('id','ia','expected','basis','origin','status','actual'):
            if not isinstance(r.get(k),str) or not r[k].strip():raise ValueError(f'Missing {k}')
        if r['id'] in seen:raise ValueError('Duplicate ID: '+r['id'])
        seen.add(r['id'])
        if r['ia'] not in aspects:raise ValueError('Invalid aspect')
        if r['status'] not in ('Passed','Failed','Blocked','Not run'):raise ValueError('Invalid status')
        if r['status'] in ('Passed','Failed'):
            if not r.get('url'):raise ValueError('Missing executed URL')
            dt=datetime.datetime.fromisoformat(r.get('time','').replace('Z','+00:00'))
            if dt.tzinfo is None:raise ValueError('Execution timestamp needs a timezone')
        if r['status']=='Failed':
            if not r.get('screenshot'):raise ValueError('Failed check requires screenshot')
            shot=(base/r['screenshot']).resolve()
            if not shot.is_relative_to(base) or not shot.is_file():raise ValueError('Screenshot missing/outside run directory')
    counts=collections.Counter(r['status'] for r in rows)
    s={'data_kind':d['data_kind'],'screen':d['screen'],'designed':len(rows),'executed':counts['Passed']+counts['Failed'],
       'counts':{k:counts[k] for k in ('Passed','Failed','Blocked','Not run')},
       'coverage_state':'complete' if counts['Blocked']+counts['Not run']==0 else 'incomplete',
       'missing_aspects':sorted(aspects-{r['ia'] for r in rows}),'environment':d['environment']}
    return d,s

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path);p.add_argument('--output',required=True,type=Path);a=p.parse_args()
    d,s=summarize(a.input);a.output.mkdir(parents=True,exist_ok=False)
    (a.output/'summary.json').write_text(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
    keys=['id','ia','expected','basis','origin','status','actual','url','time','screenshot']
    with (a.output/'results.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=keys,extrasaction='ignore',lineterminator='\n');w.writeheader();w.writerows(d['results'])
    def esc(v):return str(v).replace('|',' / ').replace('\n','; ').replace('<','&lt;').replace('>','&gt;')
    md=f'# GUI evaluation — {esc(d["screen"])}\n\nData kind: **{d["data_kind"]}**. Executed {s["executed"]}/{s["designed"]}; {s["coverage_state"]}.\n\n'
    md+=' | '.join(f'{k}: {v}' for k,v in s['counts'].items())+'\n\n| ID | Aspect | Expected / basis | Status | Actual | Evidence path relative to input |\n|---|---|---|---|---|---|\n'
    for r in d['results']:md+='| '+' | '.join(esc(v) for v in [r['id'],r['ia'],r['expected']+' / '+r['basis'],r['status'],r['actual'],r.get('screenshot','')])+' |\n'
    md+='\nValidation checks structure and local files; it does not certify observation truth or specification completeness.\n'
    (a.output/'report.md').write_text(md);print(json.dumps(s,ensure_ascii=False))
if __name__=='__main__':main()
