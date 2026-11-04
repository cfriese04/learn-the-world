import sys
sys.path.insert(0, '.')
from common import build
import us08a, us08b, us08c
S, C = {}, {}
for m in (us08a, us08b, us08c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = us08a.PAGES + us08b.PAGES + us08c.PAGES
build({'id': 'us08', 'no': 'US8', 'title': 'The modern republic', 'sub': '1980 to now'}, S, C, pages, '../content/us08.json', 'US8')
