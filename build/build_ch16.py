import sys
sys.path.insert(0, '.')
from common import build
import ch16a, ch16b, ch16c
S, C = {}, {}
for m in (ch16a, ch16b, ch16c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch16a.PAGES + ch16b.PAGES + ch16c.PAGES
build({'id': 'ch16', 'no': '16', 'title': 'The present age', 'sub': '1991 to now'}, S, C, pages, '../content/ch16.json', '16')
