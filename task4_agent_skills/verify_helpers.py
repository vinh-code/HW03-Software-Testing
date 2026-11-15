"""Regression checks for evidence and statistical boundary cases (stdlib only)."""
import copy, importlib.util, json, tempfile
from pathlib import Path
R=Path(__file__).resolve().parent

def load(name):
    spec=importlib.util.spec_from_file_location(name,R/'gui-usability-evaluator/scripts'/f'{name}.py')
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def rejects(fn):
    try:fn()
    except ValueError:return
    raise AssertionError('Expected invalid input rejection')

g=load('summarize_gui');u=load('summarize_usability');checks=[]
for answers,expected in [([1,5]*5,0),([3]*10,50),([5,1]*5,100)]:
    assert u.score(answers)==expected
checks.append('SUS reference scores 0, 50, 100')
rejects(lambda:u.score([0]*10));rejects(lambda:u.score([True]*10));rejects(lambda:u.score([3]*9))
checks.append('SUS rejects out-of-range, boolean and short input')
d=json.loads((R/'demo/usability_input.json').read_text());_,s=u.summarize(d)
assert s['main_sessions']==7 and s['pilot_excluded'] and abs(s['sus_mean']-58.92857142857143)<1e-9
checks.append('Known seven-session sample and excluded pilot')
x=copy.deepcopy(d);x['sessions'][0]['sus_answers']=None;_,s=u.summarize(x)
assert s['sus_valid_n']==6 and s['sus_missing_n']==1
checks.append('Missing SUS excluded from score denominator')
x=copy.deepcopy(d);x['sessions'][0]['data_kind']='real';rejects(lambda:u.summarize(x));checks.append('Mixed provenance rejected')
x=copy.deepcopy(d);x['sessions'].append(x['pilot']);rejects(lambda:u.summarize(x));checks.append('Pilot contamination rejected')
x=copy.deepcopy(d);x['pilot']=None;assert not u.summarize(x)[1]['pilot_excluded'];checks.append('Optional null pilot accepted')
d,s=g.summarize(R/'demo/results.json');assert s['executed']==16 and s['counts']['Failed']==10;checks.append('Actual GUI evidence valid')
with tempfile.TemporaryDirectory() as folder:
    p=Path(folder)/'run.json';x=copy.deepcopy(d)
    for row in x['results']:row.update(status='Blocked',actual='Fixture unavailable',screenshot=None)
    p.write_text(json.dumps(x));assert g.summarize(p)[1]['coverage_state']=='incomplete';checks.append('Blocked run remains incomplete')
    x['results'].append(x['results'][0]);p.write_text(json.dumps(x));rejects(lambda:g.summarize(p));checks.append('Duplicate GUI IDs rejected')
    x=copy.deepcopy(d);p.write_text(json.dumps(x));rejects(lambda:g.summarize(p));checks.append('Missing failed screenshot rejected')
report={'status':'passed','checks':checks}
(R/'demo/helper_verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
