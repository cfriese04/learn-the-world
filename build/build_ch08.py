import sys
sys.path.insert(0, '.')
from common import build
import ch08a, ch08b, ch08c
S, C = {}, {}
for m in (ch08a, ch08b, ch08c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch08a.PAGES + ch08b.PAGES + ch08c.PAGES
build({'id': 'ch08', 'no': '08', 'title': 'Persia, Greece and Rome', 'sub': 'the classical Mediterranean and its neighbours'}, S, C, pages, '../content/ch08.json', '8')
