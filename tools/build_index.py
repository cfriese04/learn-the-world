"""Build content/index.json (chapter and page titles, for the contents and
front page) and content/search.json (plain text of every page, for search)
from the chapter files listed in content/library.json.

Run from the repository root:  python3 tools/build_index.py
"""
import json, re, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
C = lambda *p: os.path.join(ROOT, 'content', *p)
MARK = re.compile(r'\s*\[\[[a-z0-9-]+\]\]')

def plain(t):
    return re.sub(r'\s+', ' ', re.sub(r'</?(?:b|i)>', '', MARK.sub('', t or ''))).strip()

def page_text(p):
    out = [plain(p.get('lede', ''))]
    for b in p.get('body', []):
        if isinstance(b, str):
            out.append(plain(b))
        elif isinstance(b, dict) and 'table' in b:
            t = b['table']
            out.append(' '.join(' '.join(map(str, r)) for r in t.get('rows', [])))
        elif isinstance(b, dict) and 'compare' in b:
            out.append(plain(b['compare']))
    return ' '.join(x for x in out if x)

lib = json.load(open(C('library.json')))
index, search = {}, []
for v in lib['volumes']:
    for c in v['chapters']:
        if not c.get('file'):
            continue
        ch = json.load(open(os.path.join(ROOT, c['file'])))
        n = str(int(ch['no'])) if ch['no'].isdigit() else ch['no']
        index[c['id']] = {
            'no': ch['no'], 'n': n, 'title': ch['title'], 'sub': ch.get('sub', ''),
            'pages': [{'t': p['title'], 's': p.get('sub', ''), 'q': len(p.get('practice', []))} for p in ch['pages']],
        }
        for i, p in enumerate(ch['pages']):
            search.append({'c': c['id'], 'p': i, 'k': n + ('.' + str(i) if i else ''),
                           't': p['title'], 's': p.get('sub', ''), 'x': page_text(p)})

json.dump(index, open(C('index.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(search, open(C('search.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print(len(index), 'chapters,', len(search), 'pages;',
      os.path.getsize(C('index.json')) // 1024, 'KB index,', os.path.getsize(C('search.json')) // 1024, 'KB search')
