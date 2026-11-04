import sys
sys.path.insert(0, '.')
from common import build
import ch11a, ch11b, ch11c
S, C = {}, {}
for m in (ch11a, ch11b, ch11c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch11a.PAGES + ch11b.PAGES + ch11c.PAGES
build({'id': 'ch11', 'no': '11', 'title': 'Regional webs', 'sub': 'c. 750 to 1250'}, S, C, pages, '../content/ch11.json', '11')
