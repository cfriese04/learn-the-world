import sys
sys.path.insert(0, '.')
from common import build
import us07a, us07b, us07c
S, C = {}, {}
for m in (us07a, us07b, us07c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = us07a.PAGES + us07b.PAGES + us07c.PAGES
build({'id': 'us07', 'no': 'US7', 'title': 'Superpower and civil rights', 'sub': '1945 to 1980'}, S, C, pages, '../content/us07.json', 'US7')
