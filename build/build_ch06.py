import sys
sys.path.insert(0, '.')
from common import build
import ch06a, ch06b, ch06c
S, C = {}, {}
for m in (ch06a, ch06b, ch06c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch06a.PAGES + ch06b.PAGES + ch06c.PAGES
build({'id': 'ch06', 'no': '06', 'title': 'The Bronze Age world', 'sub': 'a club of great powers, and its collapse'}, S, C, pages, '../content/ch06.json', '6')
