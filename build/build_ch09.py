import sys
sys.path.insert(0, '.')
from common import build
import ch09a, ch09b, ch09c
S, C = {}, {}
for m in (ch09a, ch09b, ch09c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch09a.PAGES + ch09b.PAGES + ch09c.PAGES
build({'id': 'ch09', 'no': '09', 'title': 'India and China in the classical age', 'sub': 'c. 500 BCE to 550 CE'}, S, C, pages, '../content/ch09.json', '9')
