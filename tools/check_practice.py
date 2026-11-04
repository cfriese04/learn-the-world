"""Measure answer give-aways in the practice questions.

For every question it checks whether the correct choice stands out from the
three wrong ones by length, by hedging words, by absolute words in the wrong
choices, or by sharing more words with the question. A good set gives a
test-taker who only reads those cues no better than chance (25%).

Run from the repository root:  python3 tools/check_practice.py [chapter ids...]
Exit code 1 if any chapter fails the thresholds below.
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HEDGE = re.compile(r"\b(about|roughly|some|many|most|often|largely|partly|perhaps|may|might|can|could|generally|usually|tend|tends|likely|probably|in part|at least|appear|appears|suggests?)\b", re.I)
ABSOL = re.compile(r"\b(always|never|all|none|only|every|entirely|completely|solely|no one|nothing|wholly)\b", re.I)
WORD = re.compile(r"[a-z][a-z'-]{3,}")
STOP = set('that this with from were which their there they have been into than then when what whose about over under after before between because while also more most some such these those would could should other only very much many'.split())

def words(t):
    return {w for w in WORD.findall(t.lower()) if w not in STOP}

def plain(t):
    return re.sub(r'<[^>]+>', '', t)

def analyse(ch):
    d = json.load(open(os.path.join(ROOT, 'content', ch + '.json')))
    n = longest = shortest = ratio_bad = hedge_only = absol_wrong = overlap_top = 0
    worst = []
    for pi, p in enumerate(d['pages']):
        for qi, q in enumerate(p.get('practice', [])):
            ch_ = [plain(c) for c in q['choices']]; a = q['answer']; n += 1
            L = [len(c) for c in ch_]; others = [L[i] for i in range(len(L)) if i != a]
            if L[a] == max(L) and L.count(max(L)) == 1: longest += 1
            if L[a] == min(L) and L.count(min(L)) == 1: shortest += 1
            r = L[a] / (sum(others) / len(others))
            if r > 1.3 or r < 0.7: ratio_bad += 1
            hc = [bool(HEDGE.search(c)) for c in ch_]
            if hc[a] and not any(hc[i] for i in range(len(hc)) if i != a): hedge_only += 1
            if any(ABSOL.search(ch_[i]) for i in range(len(ch_)) if i != a) and not ABSOL.search(ch_[a]): absol_wrong += 1
            qw = words(plain(q['q'])); ov = [len(qw & words(c)) for c in ch_]
            if ov[a] == max(ov) and ov.count(max(ov)) == 1 and ov[a] > 0: overlap_top += 1
            if r > 1.3: worst.append((round(r, 2), f'{pi}.{qi}'))
    pct = lambda k: round(100 * k / max(1, n))
    return {'n': n, 'longest%': pct(longest), 'shortest%': pct(shortest), 'len_off%': pct(ratio_bad),
            'hedge_only%': pct(hedge_only), 'absolute_in_wrong%': pct(absol_wrong), 'overlap_top%': pct(overlap_top),
            'worst': sorted(worst, reverse=True)[:6]}

# Thresholds: a cue that singles out the answer more often than these fails.
LIMITS = {'longest%': 35, 'shortest%': 35, 'len_off%': 25, 'hedge_only%': 15, 'absolute_in_wrong%': 20, 'overlap_top%': 40}

if __name__ == '__main__':
    lib = json.load(open(os.path.join(ROOT, 'content', 'library.json')))
    ids = sys.argv[1:] or [c['id'] for v in lib['volumes'] for c in v['chapters'] if c.get('file')]
    bad = False
    for ch in ids:
        r = analyse(ch)
        fails = [k for k, lim in LIMITS.items() if r[k] > lim]
        bad |= bool(fails)
        print(ch, {k: r[k] for k in ['n'] + list(LIMITS)}, 'FAIL ' + ','.join(fails) if fails else 'ok')
    sys.exit(1 if bad else 0)
