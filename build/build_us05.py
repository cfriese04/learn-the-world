import sys
sys.path.insert(0, '.')
from common import build
import us05a, us05b, us05c
S, C = {}, {}
for m in (us05a, us05b, us05c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = us05a.PAGES + us05b.PAGES + us05c.PAGES
build({'id': 'us05', 'no': 'US5', 'title': 'Industry, immigration and reform', 'sub': '1877 to 1920'}, S, C, pages, '../content/us05.json', 'US5')
