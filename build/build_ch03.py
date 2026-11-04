import sys
sys.path.insert(0, '.')
from common import build
import ch03a, ch03b, ch03c
S, C = {}, {}
for m in (ch03a, ch03b, ch03c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch03a.PAGES + ch03b.PAGES + ch03c.PAGES
build({'id': 'ch03', 'no': '03', 'title': 'Mesopotamia', 'sub': 'the first cities, between two rivers'}, S, C, pages, '../content/ch03.json', '3')
