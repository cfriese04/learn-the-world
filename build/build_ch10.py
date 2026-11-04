import sys
sys.path.insert(0, '.')
from common import build
import ch10a, ch10b, ch10c
S, C = {}, {}
for m in (ch10a, ch10b, ch10c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch10a.PAGES + ch10b.PAGES + ch10c.PAGES
build({'id': 'ch10', 'no': '10', 'title': 'Late antiquity and the rise of Islam', 'sub': 'c. 250 to 750'}, S, C, pages, '../content/ch10.json', '10')
