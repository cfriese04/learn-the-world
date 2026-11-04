import sys
sys.path.insert(0, '.')
from common import build
import us03a, us03b, us03c
S, C = {}, {}
for m in (us03a, us03b, us03c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = us03a.PAGES + us03b.PAGES + us03c.PAGES
build({'id': 'us03', 'no': 'US3', 'title': 'The young republic', 'sub': '1789 to 1848'}, S, C, pages, '../content/us03.json', 'US3')
