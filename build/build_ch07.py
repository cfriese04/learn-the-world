import sys
sys.path.insert(0, '.')
from common import build
import ch07a, ch07b, ch07c
S, C = {}, {}
for m in (ch07a, ch07b, ch07c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch07a.PAGES + ch07b.PAGES + ch07c.PAGES
build({'id': 'ch07', 'no': '07', 'title': 'Iron, empire and the Axial Age', 'sub': 'c. 1200 to 500 BCE'}, S, C, pages, '../content/ch07.json', '7')
