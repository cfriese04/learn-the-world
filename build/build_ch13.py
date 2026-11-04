import sys
sys.path.insert(0, '.')
from common import build
import ch13a, ch13b, ch13c
S, C = {}, {}
for m in (ch13a, ch13b, ch13c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch13a.PAGES + ch13b.PAGES + ch13c.PAGES
build({'id': 'ch13', 'no': '13', 'title': 'The world joined', 'sub': 'c. 1450 to 1750'}, S, C, pages, '../content/ch13.json', '13')
