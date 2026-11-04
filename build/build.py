import json, re, sys
sys.path.insert(0, '.')
import part1, part2
S = {**part2.S, **part1.S}; C = {**part2.C, **part1.C}
assert not set(part1.S) & set(part2.S), set(part1.S) & set(part2.S)
assert not set(part1.C) & set(part2.C), set(part1.C) & set(part2.C)
pages = part1.PAGES + part2.PAGES
errs, warns, used = [], [], set()
def text(where, t):
    if not isinstance(t, str): return
    for m in re.findall(r'\[\[([a-z0-9-]+)\]\]', t):
        used.add(m)
        if m not in C: errs.append(f'{where}: unknown claim {m}')
    if re.search(r'\b\d+\s?(BC|AD)\b', t): errs.append(f'{where}: BC/AD')
    if '!' in t: warns.append(f'{where}: exclamation')
    if re.search(r'fun fact', t, re.I): errs.append(f'{where}: fun fact')
    if '  ' in t: warns.append(f'{where}: double space')
def walk(where, o):
    if isinstance(o, str): text(where, o)
    elif isinstance(o, list): [walk(f'{where}[{i}]', x) for i, x in enumerate(o)]
    elif isinstance(o, dict):
        for k, v in o.items():
            if k == 'sources' and isinstance(v, list):
                for s in v:
                    if s not in S: errs.append(f'{where}: unknown source {s}')
            walk(f'{where}.{k}', v)
isLL = lambda v: isinstance(v, list) and len(v) == 2 and abs(v[0]) <= 180 and abs(v[1]) <= 90
for i, p in enumerate(pages):
    w = f'1.{i}'
    for k in ('title', 'sub', 'lede', 'body', 'figure'):
        if k not in p: errs.append(f'{w}: missing {k}')
    walk(w, {k: v for k, v in p.items() if k != 'practice'})
    f = p['figure']
    if f['kind'] == 'map':
        for L in f.get('layers', []):
            for it in L['items']:
                for key in ('ll', 'lab'):
                    if key in it and not isLL(it[key]): errs.append(f'{w}: bad {key} {it[key]}')
                for pt in it.get('path', []):
                    if not isLL(pt): errs.append(f'{w}: bad path point {pt}')
    pr = p.get('practice', [])
    if len(pr) != 2: warns.append(f'{w}: {len(pr)} practice questions')
    for j, qq in enumerate(pr):
        qw = f'{w} q{j}'
        if len(qq['choices']) != 4 or len(set(qq['choices'])) != 4: errs.append(f'{qw}: needs 4 distinct choices')
        if qq['answer'] not in range(4): errs.append(f'{qw}: bad answer')
        miss = {x for x in range(4) if x != qq['answer']} - set(qq['wrong'])
        if miss: errs.append(f'{qw}: wrong-answer notes missing for {miss}')
        if qq['answer'] in qq['wrong']: errs.append(f'{qw}: note on the right answer')
        if not qq['why']: errs.append(f'{qw}: no why')
        walk(qw, qq)
for k, c in C.items():
    if not c['sources']: errs.append(f'claim {k}: no sources')
    for s in c['sources']:
        if s not in S: errs.append(f'claim {k}: unknown source {s}')
    if c['label'] not in ('consensus', 'approx', 'debated', 'tradition'): errs.append(f'claim {k}: label')
    if c['show'] and c['label'] != 'consensus' and not c.get('note'): errs.append(f'claim {k}: shown non-consensus claim needs a note')
    if c['show'] and c['label'] == 'consensus': warns.append(f'claim {k}: consensus claim shown')
    if k not in used: warns.append(f'claim {k}: never used')
    text(f'claim {k}', c['text'])
for k, (cit, url) in S.items():
    if not url.startswith('https://'): errs.append(f'source {k}: not https')
usedS = set()
for c in C.values(): usedS |= set(c['sources'])
def collect(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == 'sources' and isinstance(v, list): usedS.update(v)
            else: collect(v)
    elif isinstance(o, list): [collect(x) for x in o]
collect(pages)
for k in S:
    if k not in usedS: warns.append(f'source {k}: never used')
for e in errs: print('ERROR  ', e)
for x in warns: print('warning', x)
print(len(errs), 'errors,', len(warns), 'warnings,', len(pages), 'pages,', len(C), 'claims,', len(S), 'sources')
if errs: sys.exit(1)
out = {'id': 'ch01', 'no': '01', 'title': 'The shape of human history', 'sub': 'three hundred thousand years, from far away',
       'sources': {k: {'citation': v[0], 'url': v[1]} for k, v in S.items()},
       'claims': {k: {kk: vv for kk, vv in c.items()} for k, c in C.items()},
       'pages': pages}
json.dump(out, open('../content/ch01.json', 'w'), ensure_ascii=False, indent=1)
print('wrote content/ch01.json')
