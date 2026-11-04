import sys
sys.path.insert(0, '.')
from common import build
import us01a, us01b, us01c
S, C = {}, {}
for m in (us01a, us01b, us01c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = us01a.PAGES + us01b.PAGES + us01c.PAGES
build({'id': 'us01', 'no': 'US1', 'title': 'Colonies to Constitution', 'sub': '1607 to 1789'}, S, C, pages, '../content/us01.json', 'US1')
