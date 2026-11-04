import sys
sys.path.insert(0, '.')
from common import build
import ch05a, ch05b, ch05c
S, C = {}, {}
for m in (ch05a, ch05b, ch05c):
    dupS = set(S) & set(m.S); dupC = set(C) & set(m.C)
    assert not dupS and not dupC, (dupS, dupC)
    S.update(m.S); C.update(m.C)
pages = ch05a.PAGES + ch05b.PAGES + ch05c.PAGES
build({'id': 'ch05', 'no': '05', 'title': 'The Indus and early China', 'sub': 'two river civilizations, one still unread'}, S, C, pages, '../content/ch05.json', '5')
