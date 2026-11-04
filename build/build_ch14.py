import sys
sys.path.insert(0, '.')
from common import build
import ch14a, ch14b, ch14c
S, C = {}, {}
for m in (ch14a, ch14b, ch14c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch14a.PAGES + ch14b.PAGES + ch14c.PAGES
build({'id': 'ch14', 'no': '14', 'title': 'Revolutions', 'sub': 'political and industrial, 1750 to 1914'}, S, C, pages, '../content/ch14.json', '14')
