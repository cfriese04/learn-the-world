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


def map_points(ch):
    """Key places on all of a chapter's maps: accented points first, else all points."""
    acc, other = [], []
    for p in ch['pages']:
        f = p.get('figure') or {}
        if f.get('kind') != 'map':
            continue
        for L in f.get('layers', []):
            for it in L.get('items', L.get('points', [])) or []:
                ll = it.get('ll') if isinstance(it, dict) else None
                if not (isinstance(ll, list) and len(ll) == 2 and L.get('type', 'points') == 'points'):
                    continue
                (acc if it.get('acc') else other).append([round(ll[0], 2), round(ll[1], 2)])
    pts = acc or other
    seen, out = set(), []
    for q in pts:
        k = (round(q[0]), round(q[1]))
        if k not in seen:
            seen.add(k); out.append(q)
    return out

def frame(pts):
    """A box around the middle of the points (outliers trimmed), padded; None means the whole world."""
    if not pts:
        return None
    xs, ys = sorted(q[0] for q in pts), sorted(q[1] for q in pts)
    cut = lambda a, f: a[min(len(a) - 1, max(0, int(round(f * (len(a) - 1)))))]
    lo, hi = (0.1, 0.9) if len(pts) >= 8 else (0, 1)
    w, e, s, n = cut(xs, lo), cut(xs, hi), cut(ys, lo), cut(ys, hi)
    if e - w > 150:
        return None
    cx, cy = (w + e) / 2, (s + n) / 2
    dx, dy = max(14, (e - w) * 1.35) / 2, max(9, (n - s) * 1.35) / 2
    return [[round(cx - dx, 1), round(max(-60, cy - dy), 1)], [round(cx + dx, 1), round(min(78, cy + dy), 1)]]

US = {'bbox': [[-125, 24], [-66, 50]], 'pts': [[-77.04, 38.9]]}

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
        pts = map_points(ch)
        box = frame(pts)
        index[c['id']]['thumb'] = US if not pts else {'bbox': box, 'pts': pts[:24]}
        for i, p in enumerate(ch['pages']):
            search.append({'c': c['id'], 'p': i, 'k': n + ('.' + str(i) if i else ''),
                           't': p['title'], 's': p.get('sub', ''), 'x': page_text(p)})

json.dump(index, open(C('index.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
json.dump(search, open(C('search.json'), 'w'), ensure_ascii=False, separators=(',', ':'))
print(len(index), 'chapters,', len(search), 'pages;',
      os.path.getsize(C('index.json')) // 1024, 'KB index,', os.path.getsize(C('search.json')) // 1024, 'KB search')
