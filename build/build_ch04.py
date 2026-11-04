import sys
sys.path.insert(0, '.')
from common import build
import ch04a, ch04b, ch04c
S, C = {}, {}
for m in (ch04a, ch04b, ch04c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch04a.PAGES + ch04b.PAGES + ch04c.PAGES
build({'id': 'ch04', 'no': '04', 'title': 'Egypt', 'sub': 'the gift of the Nile'}, S, C, pages, '../content/ch04.json', '4')
