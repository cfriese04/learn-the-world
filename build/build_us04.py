import sys
sys.path.insert(0, '.')
from common import build
import us04a, us04b, us04c
S, C = {}, {}
for m in (us04a, us04b, us04c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = us04a.PAGES + us04b.PAGES + us04c.PAGES
build({'id': 'us04', 'no': 'US4', 'title': 'Slavery, war and Reconstruction', 'sub': '1848 to 1877'}, S, C, pages, '../content/us04.json', 'US4')
