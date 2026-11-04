import sys
sys.path.insert(0, '.')
from common import build
import us06a, us06b, us06c
S, C = {}, {}
for m in (us06a, us06b, us06c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = us06a.PAGES + us06b.PAGES + us06c.PAGES
build({'id': 'us06', 'no': 'US6', 'title': 'Depression, New Deal and war', 'sub': '1920 to 1945'}, S, C, pages, '../content/us06.json', 'US6')
