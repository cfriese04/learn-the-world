"""Safety checks on the built book, run in CI on every pull request.

- Text may contain only the HTML tags <b> and <i>; anything else fails.
- Every source link must be https.
- No javascript:, data: or vbscript: URLs anywhere.

Run from the repository root:  python3 tools/check_content.py
"""
import json, glob, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TAG = re.compile(r'<\s*/?\s*([a-zA-Z][a-zA-Z0-9]*)')
BAD_URL = re.compile(r'(?i)\b(?:javascript|vbscript)\s*:|\bdata:[a-z]+/[a-z0-9.+-]+[;,]')
problems = []

def walk(o, where):
    if isinstance(o, dict):
        for k, v in o.items():
            walk(v, where + '.' + str(k))
    elif isinstance(o, list):
        for i, v in enumerate(o):
            walk(v, where + '[' + str(i) + ']')
    elif isinstance(o, str):
        for t in TAG.findall(o):
            if t.lower() not in ('b', 'i'):
                problems.append(f'{where}: tag <{t}> is not allowed')
        if BAD_URL.search(o):
            problems.append(f'{where}: script or data URL')

for f in sorted(glob.glob(os.path.join(ROOT, 'content', '*.json'))):
    name = os.path.basename(f)
    d = json.load(open(f, encoding='utf-8'))
    walk(d, name)
    if isinstance(d, dict) and isinstance(d.get('sources'), dict):
        for sid, s in d['sources'].items():
            if not str(s.get('url', '')).startswith('https://'):
                problems.append(f'{name}: source {sid} is not an https link')

for p in problems[:200]:
    print(p)
print(len(problems), 'problems')
sys.exit(1 if problems else 0)
