import sys
sys.path.insert(0, '.')
from common import build
import us02a, us02b, us02c
S, C = {}, {}
for m in (us02a, us02b, us02c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = us02a.PAGES + us02b.PAGES + us02c.PAGES
build({'id': 'us02', 'no': 'US2', 'title': 'How the government works', 'sub': 'the Constitution, clause by clause'}, S, C, pages, '../content/us02.json', 'US2')
