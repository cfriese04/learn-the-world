import sys
sys.path.insert(0, '.')
from common import build
import ch15a, ch15b, ch15c
S, C = {}, {}
for m in (ch15a, ch15b, ch15c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch15a.PAGES + ch15b.PAGES + ch15c.PAGES
build({'id': 'ch15', 'no': '15', 'title': 'The violent century', 'sub': '1914 to 1991'}, S, C, pages, '../content/ch15.json', '15')
