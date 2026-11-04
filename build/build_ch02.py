import sys
sys.path.insert(0, '.')
from common import build
import ch02a, ch02b, ch02c
S, C = {}, {}
for m in (ch02a, ch02b, ch02c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch02a.PAGES + ch02b.PAGES + ch02c.PAGES
build({'id': 'ch02', 'no': '02', 'title': 'Before history', 'sub': 'foragers, and the turn to farming'}, S, C, pages, '../content/ch02.json', '2')
