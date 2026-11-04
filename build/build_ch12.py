import sys
sys.path.insert(0, '.')
from common import build
import ch12a, ch12b, ch12c
S, C = {}, {}
for m in (ch12a, ch12b, ch12c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch12a.PAGES + ch12b.PAGES + ch12c.PAGES
build({'id': 'ch12', 'no': '12', 'title': 'The Mongols and the Black Death', 'sub': 'c. 1250 to 1500'}, S, C, pages, '../content/ch12.json', '12')
