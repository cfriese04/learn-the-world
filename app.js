/* Learn the World: the app. See README.md. */
(() => {
'use strict';
const $ = id => document.getElementById(id);
const el = (tag, cls, html) => { const n = document.createElement(tag); if (cls) n.className = cls; if (html != null) n.innerHTML = html; return n; };
const esc = s => String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
/* Book text is escaped, then only <b> and <i> are allowed back; source links must be https. */
const rich = s => esc(s).replace(/&lt;(\/?)(b|i)&gt;/g, '<$1$2>');
const safeURL = u => /^https:\/\//i.test(String(u)) ? String(u) : '#';
const has = (o, k) => o != null && Object.prototype.hasOwnProperty.call(o, k);
const num = v => (Number.isFinite(+v) ? +v : 0);
const ANCH = a => (a === 'start' || a === 'middle' || a === 'end' ? a : null);
const NS = 'http://www.w3.org/2000/svg';
const reduce = () => matchMedia('(prefers-reduced-motion: reduce)').matches;
const narrow = () => matchMedia('(max-width: 900px)').matches;
const css = n => getComputedStyle(document.documentElement).getPropertyValue(n).trim();
let toastT; function toast(m){ const t = $('toast'); t.textContent = m; t.hidden = false; clearTimeout(toastT); toastT = setTimeout(() => t.hidden = true, 2600); }

/* ============ state ============ */
const S = { library: null, index: {}, chapters: {}, loading: {}, ch: null, page: 0, topo: null, cards: {}, read: {}, mode: 'contents', drawer: null };
/* Site settings. Set repo to the public GitHub repository's address to show the source and report-an-error links. */
const SITE = { name: 'Learn the World', repo: 'https://github.com/cfriese04/learn-the-world' };
const chapterList = () => S.library.volumes.flatMap(v => v.chapters).filter(c => c.file && S.index[c.id]);
const pageKey = (id, i) => S.index[id].n + (i ? '.' + i : '');
function nav(h){ if (location.hash.slice(1) === h) route(); else location.hash = h; }
function reportURL(where){ return SITE.repo ? SITE.repo + '/issues/new?title=' + encodeURIComponent('Error on ' + where) + '&body=' + encodeURIComponent('Page: ' + location.origin + location.pathname + location.hash + '\n\nWhat is wrong, and what does the source say? (A link to a source helps.)\n') : ''; }

/* ============ storage (owner-only db, browser fallback) ============ */
const store = {
  db: null, q: Promise.resolve(),
  async init(){
    try { if (window.claude && window.claude.use) this.db = await window.claude.use('db'); } catch (e) {}
    /* The saved database is the owner's alone; anyone the book is shared with keeps progress in their own browser. */
    if (this.db) { try { const u = await window.claude.use('user'); const own = u ? await Promise.resolve(u.isOwner()) : null; if (own === false) this.db = null; this.owner = own === true; } catch (e) {} }
  },
  local(p, b){ try { localStorage.setItem('ha2:' + p, JSON.stringify(b)); } catch (e) {} },
  async get(p){ if (this.db) { try { const s = await this.db.doc(p).get(); return s.exists ? s.data() : null; } catch (e) { return null; } } try { return JSON.parse(localStorage.getItem('ha2:' + p)); } catch (e) { return null; } },
  async list(c){ if (this.db) { try { return (await this.db.collection(c).get()).docs.map(d => [d.id, d.data()]); } catch (e) { return []; } } const o = []; try { for (let i = 0; i < localStorage.length; i++) { const k = localStorage.key(i); if (k.startsWith('ha2:' + c + '/')) o.push([k.slice(c.length + 5), JSON.parse(localStorage.getItem(k))]); } } catch (e) {} return o; },
  set(p, d){ const b = JSON.parse(JSON.stringify(d)); this.q = this.q.then(async () => { if (this.db) { try { await this.db.doc(p).set(b); } catch (e) { console.warn('save', p, e && e.code); if (e && !this.owner && (e.code === 'invalid_argument' || e.code === 'not_granted' || e.code === 'revoked')) { this.db = null; this.local(p, b); } } } else { this.local(p, b); } }); return this.q; }
};

/* ============ review schedule ============ */
/* Expanding intervals: a right answer comes back after 1 day, then 3, then about 2.5 times the last gap
   (growing a little with each success, capped at a year); a wrong answer comes back the next time you review,
   and shortens later gaps. Cards saved by older versions (with scheduled_days) carry on from their gap. */
function nextCard(prev, good, now){
  const DAY = 864e5;
  let ivl = prev ? (prev.ivl != null ? prev.ivl : (prev.scheduled_days || 0)) : 0;
  let ease = (prev && prev.ease) || 2.5, reps = (prev && prev.reps) || 0, lapses = (prev && prev.lapses) || 0;
  if (good) { ivl = ivl < 1 ? 1 : ivl < 3 ? 3 : Math.min(365, Math.round(ivl * ease)); ease = Math.min(3, ease + .05); reps++; }
  else { ivl = 0; ease = Math.max(1.3, ease - .2); lapses++; }
  const due = new Date(now.getTime() + (good ? ivl * DAY : 10 * 60e3));
  return {due: due.toISOString(), ivl, ease, reps, lapses, last_review: now.toISOString()};
}
const chN = C => (/^\d+$/.test(C.no) ? String(Number(C.no)) : C.no);
const qid = (ch, p, i) => ch + '.' + p + '.' + i;
const CARD_ID = /^(?:ch|us)\d\d\.\d{1,3}\.\d$/, READ_ID = /^(?:ch|us)\d\d\.\d{1,3}$/;
const okCard = (id, r) => CARD_ID.test(id) && has(S.index, id.split('.')[0]) && r && r.card && !isNaN(Date.parse(r.card.due));
const okLast = L => !!L && typeof L.ch === 'string' && has(S.index, L.ch) && Number.isInteger(L.page) && L.page >= 0 && L.page < S.index[L.ch].pages.length;
const cleanCard = r => ({card: {due: new Date(r.card.due).toISOString(), ivl: num(r.card.ivl != null ? r.card.ivl : r.card.scheduled_days), ease: num(r.card.ease) || 2.5, reps: num(r.card.reps), lapses: num(r.card.lapses), last_review: !isNaN(Date.parse(r.card.last_review)) ? new Date(r.card.last_review).toISOString() : null}, hist: Array.isArray(r.hist) ? r.hist.slice(-40).filter(h => Array.isArray(h) && h.length === 2).map(h => [String(h[0]).slice(0, 40), h[1] ? 1 : 0]) : []});
const cleanRead = o => { const out = {}; if (o && typeof o === 'object') Object.keys(o).forEach(k => { if (READ_ID.test(k) && has(S.index, k.split('.')[0])) out[k] = true; }); return out; };
function rate(id, good){
  const now = new Date(), r = S.cards[id];
  const c = nextCard(r && r.card, good, now);
  S.cards[id] = {card: c, hist: ((r && r.hist) || []).concat([[now.toISOString(), good ? 1 : 0]]).slice(-40)};
  store.set('cards/' + id, S.cards[id]); updateDue();
}
const dueList = () => Object.entries(S.cards).filter(([id, r]) => new Date(r.card.due) <= new Date() && findQ(id)).map(([id]) => id);
function updateDue(){ const n = dueList().length; $('dueN').textContent = n ? String(n) : ''; }
function findQ(id){ const [ch, p, i] = id.split('.'); const C = has(S.chapters, ch) ? S.chapters[ch] : null; const pg = C && C.pages[+p]; return pg && pg.practice && pg.practice[+i] ? {ch, p: +p, i: +i, q: pg.practice[+i]} : null; }

/* ============ load ============ */
async function getJSON(u){ const r = await fetch(u); if (!r.ok) throw new Error(u + ' ' + r.status); return r.json(); }
async function boot(){
  await store.init();
  try { [S.library, S.index] = await Promise.all([getJSON('content/library.json'), getJSON('content/index.json')]); } catch (e) { $('note').textContent = 'The library did not load: ' + e.message; return; }
  const [cards, prog] = await Promise.all([store.list('cards'), store.get('progress/main')]);
  cards.forEach(([id, r]) => { if (okCard(id, r)) S.cards[id] = cleanCard(r); });
  if (prog) { S.read = cleanRead(prog.read); S.last = okLast(prog.last) ? {ch: prog.last.ch, page: prog.last.page} : null; }
  /* chapters with saved questions are loaded in the background so that due reviews can be counted */
  const need = [...new Set(Object.keys(S.cards).map(id => id.split('.')[0]))].filter(id => S.index[id]);
  S.cardsReady = Promise.all(need.map(ensureChapter)).then(() => { updateDue(); if (S.mode === 'contents') renderResume(); });
  route();
}
function ensureChapter(id){
  if (S.chapters[id]) return Promise.resolve(S.chapters[id]);
  const c = S.library.volumes.flatMap(v => v.chapters).find(c => c.id === id);
  if (!c || !c.file) return Promise.resolve(null);
  if (!S.loading[id]) S.loading[id] = getJSON(c.file).then(d => (S.chapters[id] = d)).catch(() => { delete S.loading[id]; return null; });
  return S.loading[id];
}
/* TopoJSON to GeoJSON (the subset of topojson-client's feature() that the maps need) */
function topoFeature(t, o){
  const tf = t.transform;
  const arcs = t.arcs.map(a => { if (!tf) return a; let x = 0, y = 0; return a.map(p => { x += p[0]; y += p[1]; return [x * tf.scale[0] + tf.translate[0], y * tf.scale[1] + tf.translate[1]]; }); });
  const pt = p => tf ? [p[0] * tf.scale[0] + tf.translate[0], p[1] * tf.scale[1] + tf.translate[1]] : p;
  const arc = i => i < 0 ? arcs[~i].slice().reverse() : arcs[i];
  const line = ids => { const out = []; ids.forEach((i, k) => { const a = arc(i); for (let m = k ? 1 : 0; m < a.length; m++) out.push(a[m]); }); if (out.length < 2) out.push(out[0]); return out; };
  const ring = ids => { const r = line(ids); while (r.length < 4) r.push(r[0]); return r; };
  const geom = g => {
    switch (g.type) {
      case 'GeometryCollection': return {type: g.type, geometries: g.geometries.map(geom)};
      case 'Point': return {type: g.type, coordinates: pt(g.coordinates)};
      case 'MultiPoint': return {type: g.type, coordinates: g.coordinates.map(pt)};
      case 'LineString': return {type: g.type, coordinates: line(g.arcs)};
      case 'MultiLineString': return {type: g.type, coordinates: g.arcs.map(line)};
      case 'Polygon': return {type: g.type, coordinates: g.arcs.map(ring)};
      case 'MultiPolygon': return {type: g.type, coordinates: g.arcs.map(p => p.map(ring))};
      default: return null;
    }
  };
  const feat = g => ({type: 'Feature', id: g.id, properties: g.properties || {}, geometry: geom(g)});
  return o.type === 'GeometryCollection' ? {type: 'FeatureCollection', features: o.geometries.map(feat)} : feat(o);
}
function loadThumbTopo(){
  return S.thumbP || (S.thumbP = getJSON('vendor/world-110m.json').then(t => { S.thumbRivers = t.objects.rivers ? topoFeature(t, t.objects.rivers) : null; return (S.thumbLand = topoFeature(t, t.objects.land)); }).catch(() => null));
}
function loadTopo(){
  if (S.topoP) return S.topoP;
  S.topoP = getJSON('vendor/world-50m.json').then(t => {
    const f = n => t.objects[n] ? topoFeature(t, t.objects[n]) : null;
    const rv = f('rivers');
    S.geo = {land: f('land'), rivers: rv && window.d3 ? {type: 'FeatureCollection', features: rv.features.filter(x => d3.geoLength(x) > .06)} : rv, lakes: f('lakes'), coast: f('coastlines')};
    return S.geo;
  }).catch(() => null);
  return S.topoP;
}
function saveProgress(){ store.set('progress/main', {read: S.read, last: S.last}); }

/* ============ routing ============ */
function route(){
  closeModal();
  const h = location.hash.slice(1);
  const m = /^((?:ch|us)\d\d)(?:-(\d+))?$/.exec(h);
  if (m && S.index[m[1]]) openChapter(m[1], m[2] ? +m[2] : 0, true);
  else if (h === 'review') (S.cardsReady || Promise.resolve()).then(startReview);
  else if (h === 'about') showAbout();
  else { showContents(); if (h) toast('That link does not match a page in the book, so here are the contents.'); }
}
window.addEventListener('hashchange', () => { if (!S.silentHash) route(); S.silentHash = false; });
function setHash(h){ if (location.hash.slice(1) !== h) { S.silentHash = true; history.replaceState(null, '', '#' + h); S.silentHash = false; } }

/* ============ contents ============ */
function showView(v){
  S.mode = v; closeDrawer(); closePlate(); closeModal();
  $('book').hidden = v !== 'book'; $('contents').hidden = v !== 'contents'; $('about').hidden = v !== 'about';
  $('navPages').hidden = v !== 'book';
  if (v !== 'book') { $('dots').replaceChildren(); $('crumb').textContent = ''; }
}
function showContents(){
  showView('contents'); setHash('');
  document.title = SITE.name;
  const sh = $('shelves'); sh.replaceChildren();
  renderResume();
  const total = Object.values(S.index).reduce((n, c) => n + c.pages.length, 0);
  $('heroSearch').firstElementChild.textContent = 'Search ' + total + ' pages: a person, a place, a war, an idea…';
  S.library.volumes.forEach(v => {
    sh.append(el('h2', 'section', esc(v.title)));
    const shelf = el('section', 'shelf');
    v.chapters.forEach(c => {
      const X = S.index[c.id];
      const card = el(X ? 'a' : 'div', 'card');
      const pages = X ? X.pages.length : c.pages;
      card.append(el('div', 'no', '<span>No. ' + esc(c.no) + '</span><span>' + (pages ? pages + ' pages' : '') + '</span>'), el('h2', null, esc(c.title)), el('i', null, esc(c.sub)));
      if (X) {
        card.href = '#' + c.id;
        const th = el('div', 'thumb'); th.append(thumbSVG(c.id)); card.append(th);
        const sp = spanStrip(c.span); if (sp) card.append(sp);
        const n = X.pages.filter((p, i) => S.read[c.id + '.' + i]).length;
        const bar = el('div', 'bar'); bar.title = n + ' of ' + X.pages.length + ' pages read'; const s = el('span'); s.style.width = Math.round(100 * n / X.pages.length) + '%'; bar.append(s); card.append(bar);
      } else { card.setAttribute('aria-disabled', 'true'); card.classList.add('off'); card.append(el('span', 'soon', 'In preparation')); }
      shelf.append(card);
    });
    sh.append(shelf);
  });
  $('note').textContent = S.library.note || '';
  $('sitefoot').innerHTML = footHTML();
}
function renderResume(){
  const res = $('resume'); res.replaceChildren();
  const first = chapterList()[0];
  if (okLast(S.last)) {
    const X = S.index[S.last.ch]; const b = el('button', 'pill', 'Continue · ' + esc(pageKey(S.last.ch, S.last.page)) + ' ' + esc(X.pages[S.last.page].t)); b.type = 'button'; b.onclick = () => nav(S.last.ch + (S.last.page ? '-' + S.last.page : '')); res.append(b);
  } else if (first) { const b = el('button', 'pill', 'Start reading · ' + esc(S.index[first.id].title)); b.type = 'button'; b.onclick = () => nav(first.id); res.append(b); }
  const due = dueList().length; if (due) { const b = el('button', 'pill', 'Review <span class="n">' + due + '</span> due'); b.type = 'button'; b.onclick = startReview; res.append(b); }
  const a = el('a', 'pill', 'About this book'); a.href = '#about'; res.append(a);
}
function footHTML(){
  return '<span>' + esc(SITE.name) + ' · by Carter Friese</span><a href="#about">About and sources</a>' + (SITE.repo ? '<a href="' + esc(SITE.repo) + '" target="_blank" rel="noopener">Source on GitHub</a><a href="' + esc(reportURL('the site')) + '" target="_blank" rel="noopener">Report an error</a>' : '') + '<span>Text CC BY 4.0 · Code MIT</span>';
}
/* Each chapter card: a small map framed on the chapter's places, and a strip showing when it happens. */
function thumbSVG(id){
  const svg = document.createElementNS(NS, 'svg'); svg.setAttribute('viewBox', '0 0 240 124'); svg.setAttribute('aria-hidden', 'true');
  const T = S.index[id] && S.index[id].thumb;
  const draw = () => {
    if (!S.thumbLand || !window.d3) return;
    const world = !T || !T.bbox;
    let pr;
    if (world) pr = d3.geoNaturalEarth1().fitExtent([[4, 4], [236, 120]], {type: 'Sphere'});
    else { const [[w, s0], [e, n]] = T.bbox; pr = d3.geoMercator().fitExtent([[4, 4], [236, 120]], {type: 'MultiPoint', coordinates: [[w, s0], [e, n], [w, n], [e, s0]]}).clipExtent([[0, 0], [240, 124]]); }
    const gp = d3.geoPath(pr), p = g => gp(g) || '';
    let h = world ? '<path d="' + p({type: 'Sphere'}) + '" fill="var(--sea)" stroke="var(--land-ink)" stroke-width=".6"/>' : '<rect width="240" height="124" fill="var(--sea)"/>';
    h += '<path d="' + p(world ? d3.geoGraticule10() : d3.geoGraticule().step([10, 10])()) + '" fill="none" stroke="var(--grat)" stroke-width=".4"/>';
    h += '<path d="' + p(S.thumbLand) + '" fill="var(--land)" stroke="var(--land-ink)" stroke-width=".45"/>';
    if (!world && S.thumbRivers) h += '<path d="' + p(S.thumbRivers) + '" fill="none" stroke="var(--river)" stroke-width=".6"/>';
    if (!world) h += '<rect width="240" height="124" fill="none" stroke="var(--land-ink)" stroke-width="1"/>';
    ((T && T.pts) || []).forEach(q => { const xy = pr(q); if (xy && xy[0] >= 0 && xy[0] <= 240 && xy[1] >= 0 && xy[1] <= 124) h += '<circle cx="' + xy[0].toFixed(1) + '" cy="' + xy[1].toFixed(1) + '" r="2.4" fill="var(--accent)" stroke="var(--leaf)" stroke-width=".8"/>'; });
    svg.innerHTML = h;
  };
  if (S.thumbLand) draw(); else loadThumbTopo().then(draw);
  return svg;
}
const yearLabel = y => y <= -10000 ? fmt(Math.round((2026 - y) / 1000) * 1000) + ' years ago' : y < 0 ? fmt(-y) + ' BCE' : y >= 2026 ? 'now' : String(y);
function spanStrip(span){
  if (!Array.isArray(span) || span.length !== 2) return null;
  const pos = y => { const ya = Math.max(10, 2026 - num(y) + 10); return Math.max(0, Math.min(1, 1 - (Math.log10(ya) - 1) / (Math.log10(300010) - 1))); };
  const a = pos(span[0]), b = pos(span[1]), label = 'Covers ' + yearLabel(span[0]) + ' to ' + yearLabel(span[1]);
  const box = el('div', 'when'); box.title = label;
  box.innerHTML = '<span class="sr">' + esc(label) + '</span><div class="span" aria-hidden="true"><i style="left:' + (a * 100).toFixed(1) + '%;width:' + Math.max(1.2, (b - a) * 100).toFixed(1) + '%"></i></div><div class="span-lab" aria-hidden="true"><span>300,000 yrs ago</span><b style="left:' + (pos(1) * 100).toFixed(1) + '%">1 CE</b><span>now</span></div>';
  return box;
}

/* ============ the book ============ */
async function openChapter(id, page, fromHash){
  const C = S.chapters[id] || await ensureChapter(id);
  if (!C) { toast('That chapter did not load. Check your connection and try again.'); if (S.mode !== 'book') showContents(); return; }
  if (S.mode !== 'book') showView('book');
  S.mode = 'book'; S.ch = id; C.n = chN(C);
  $('crumb').textContent = 'No. ' + C.no + ' · ' + C.title;
  const dots = $('dots'); dots.replaceChildren();
  C.pages.forEach((p, i) => { const b = el('button'); b.type = 'button'; b.title = (i ? C.n + '.' + i + ' ' : '') + p.title; b.setAttribute('aria-label', b.title); b.onclick = () => go(i); dots.append(b); });
  layoutSpine();
  go(Math.max(0, Math.min(page || 0, C.pages.length - 1)), true);
}
function layoutSpine(){ const L = $('leftPage'); $('spine').style.left = (L.offsetWidth) + 'px'; }
addEventListener('resize', () => { if (S.mode === 'book') { layoutSpine(); if (FIG.spec) FIG.redraw(true); } });

function go(i, first){
  const C = S.chapters[S.ch]; if (i < 0 || i >= C.pages.length) return;
  const back = i < S.page && !first; S.page = i;
  closePlate(); if (S.drawer && S.drawer.mode !== 'review') closeDrawer();
  const P = C.pages[i];
  setHash(S.ch + (i ? '-' + i : ''));
  document.title = (i ? C.n + '.' + i + ' ' : '') + P.title + ' · ' + SITE.name;
  $('live').textContent = 'Page ' + (i + 1) + ' of ' + C.pages.length + ': ' + P.title;
  [...$('dots').children].forEach((b, j) => { b.setAttribute('aria-current', String(j === i)); b.classList.toggle('read', !!S.read[S.ch + '.' + j]); });
  $('folioL').textContent = C.title; $('pageNo').textContent = (i ? C.n + '.' + i : 'Ch. ' + C.n) + '  ·  ' + (i + 1) + ' / ' + C.pages.length;
  $('prev').disabled = i === 0; $('next').disabled = i === C.pages.length - 1;
  renderSheet(C, P, i, back);
  FIG.show(P.figure, C.n + (i ? '.' + i : ''));
  const n = (P.practice || []).length; $('practiceBtn').hidden = !n; $('practiceN').textContent = n ? '· ' + n : '';
  S.read[S.ch + '.' + i] = true; S.last = {ch: S.ch, page: i}; saveProgress();
  $('leftScroll').scrollTop = 0; if (narrow()) scrollTo(0, 0);
}
$('prev').onclick = () => go(S.page - 1);
$('next').onclick = () => go(S.page + 1);
$('navReview').onclick = startReview; $('navSearch').onclick = openSearch; $('heroSearch').onclick = openSearch; $('navPages').onclick = openToc;
$('share').onclick = sharePage;
async function sharePage(){
  const url = location.href.split('#')[0] + '#' + S.ch + (S.page ? '-' + S.page : ''), title = document.title;
  if (navigator.share && narrow()) { try { await navigator.share({title, url}); return; } catch (e) { if (e && e.name === 'AbortError') return; } }
  try { await navigator.clipboard.writeText(url); toast('Link to this page copied.'); } catch (e) { toast(url); }
}

const LABW = {consensus: 'consensus', approx: 'approx.', debated: 'debated', tradition: 'tradition'};
function renderSheet(C, P, i, back){
  const s = $('sheet'); s.className = 'sheet';
  const parts = [];
  parts.push('<div class="kicker">' + esc(P.kicker || (i ? C.n + '.' + i : 'Chapter ' + C.n)) + '</div>');
  parts.push('<h1>' + esc(P.title) + '</h1>');
  if (P.sub) parts.push('<p class="sub">' + esc(P.sub) + '</p>');
  if (P.lede) parts.push('<p class="lede">' + claimify(C, P.lede) + '</p>');
  (P.body || []).forEach(b => {
    if (typeof b === 'string') parts.push('<p>' + claimify(C, b) + '</p>');
    else if (b.table) parts.push(tableHTML(C, b.table));
    else if (b.compare) parts.push('<div class="compare"><div class="kicker">Compare</div><p>' + claimify(C, b.compare) + '</p></div>');
  });
  const nx = C.pages[i + 1], L = chapterList(), at = L.findIndex(c => c.id === S.ch), nc = !nx && L[at + 1];
  if (nx) parts.push('<button type="button" class="nextline" id="nextline"><span><span class="k">Next · ' + esc(C.n + '.' + (i + 1)) + '</span><br><span class="t">' + esc(nx.title) + '</span></span><span class="arr">→</span></button>');
  else if (nc) parts.push('<button type="button" class="nextline" id="nextline"><span><span class="k">End of chapter ' + esc(C.n) + ' · next chapter, No. ' + esc(nc.no) + '</span><br><span class="t">' + esc(S.index[nc.id].title) + '</span></span><span class="arr">→</span></button>');
  else parts.push('<button type="button" class="nextline" id="nextline"><span><span class="k">End of the book, for now</span><br><span class="t">Back to the contents</span></span><span class="arr">→</span></button>');
  if (SITE.repo) parts.push('<p class="report">Spotted an error on this page? <a href="' + esc(reportURL(C.n + (i ? '.' + i : '') + ' ' + P.title)) + '" target="_blank" rel="noopener">Report it on GitHub</a>.</p>');
  s.innerHTML = parts.join('');
  void s.offsetWidth; s.classList.add('in'); if (back) s.classList.add('back');
  const nl = $('nextline'); if (nl) nl.onclick = () => nx ? go(i + 1) : nc ? nav(nc.id) : nav('');
  s.querySelectorAll('.cl').forEach(b => b.onclick = () => openClaim(C, b.dataset.c, b));
}
// text may hold [[claimId]] markers placed after the sentence they support
function claimify(C, t){
  const RANK = {debated: 3, tradition: 2, approx: 1, consensus: 0};
  return rich(t).replace(/(?:\s*\[\[[a-z0-9-]+\]\])+/g, m => {
    const ids = [...m.matchAll(/\[\[([a-z0-9-]+)\]\]/g)].map(x => x[1]).filter(id => C.claims[id] && C.claims[id].show !== false);
    if (!ids.length) return '';
    const top = ids.reduce((a, id) => RANK[C.claims[id].label] > RANK[a] ? C.claims[id].label : a, 'consensus');
    return ' <button type="button" class="cl ' + top + '" data-c="' + ids.join(' ') + '" aria-haspopup="dialog" aria-expanded="false" title="How do we know?">' + LABW[top] + '</button>';
  });
}
function tableHTML(C, t){
  let h = '<div class="tablewrap" tabindex="0" role="region" aria-label="Table"><table class="data">';
  if (t.head) h += '<tr>' + t.head.map(x => '<th>' + claimify(C, x) + '</th>').join('') + '</tr>';
  t.rows.forEach(r => { h += '<tr>' + r.map(x => '<td>' + claimify(C, x) + '</td>').join('') + '</tr>'; });
  return h + '</table></div>' + (t.note ? '<p style="font:12px/1.5 var(--mono);color:var(--ink-3);margin-top:-8px">' + claimify(C, t.note) + '</p>' : '');
}

/* ---------- plates: one thing taken apart, over the left page ---------- */
function openPlate(html){
  closePlate();
  const p = el('div', 'plate'); p.id = 'plate'; p.setAttribute('role', 'dialog');
  p.innerHTML = '<button class="close" type="button">Back to the page · Esc</button>' + html;
  p.querySelector('.close').onclick = closePlate; S.plateReturn = document.activeElement;
  $('leftPage').append(p); p.querySelector('.close').focus({preventScroll: true});
}
function closePlate(){ closePop(); const p = $('plate'); if (p) { p.remove(); const r = S.plateReturn; S.plateReturn = null; if (r && r.isConnected && r.focus) r.focus({preventScroll: true}); } }
function sourcesHTML(C, ids){ return ids && ids.length ? '<div class="src">Sources<br>' + ids.map(s => { const x = C.sources[s]; return x ? '<a href="' + esc(safeURL(x.url)) + '" target="_blank" rel="noopener">' + esc(x.citation) + '</a>' : ''; }).join('<br>') + '</div>' : ''; }
const WORD = {consensus: 'Consensus', approx: 'Approximate', debated: 'Debated', tradition: 'Traditional account'};
function closePop(){ const p = $('pop'); if (!p) return false; const had = p.contains(document.activeElement); if (p._btn) { p._btn.setAttribute('aria-expanded', 'false'); if (had && p._btn.isConnected) p._btn.focus({preventScroll: true}); } p.remove(); return true; }
function openClaim(C, ids, btn){
  if (btn && $('pop') && $('pop')._btn === btn) { closePop(); return; }
  closePop();
  const list = String(ids).split(' ').map(id => C.claims[id]).filter(Boolean); if (!list.length) return;
  const p = el('div', 'pop'); p.id = 'pop'; p.setAttribute('role', 'dialog'); p.setAttribute('aria-label', 'How do we know?');
  p.innerHTML = '<button class="x" type="button" aria-label="Close">&times;</button><div class="ph">How do we know?</div>' + list.map(c =>
    '<div class="one"><div class="ph" style="margin-bottom:6px"><b class="' + (has(WORD, c.label) ? c.label : '') + '">' + esc(WORD[c.label]) + '</b></div><p class="claim">' + esc(c.text) + '</p>' + (c.note ? '<p>' + esc(c.note) + '</p>' : '')
    + (c.sources && c.sources.length ? '<div class="src">' + c.sources.map(s => { const x = C.sources[s]; return x ? '<a href="' + esc(safeURL(x.url)) + '" target="_blank" rel="noopener">' + esc(x.citation) + '</a>' : ''; }).join('<br>') + '</div>' : '') + '</div>').join('');
  document.body.append(p); p._btn = btn || null;
  p.querySelector('.x').onclick = closePop;
  if (btn) { btn.setAttribute('aria-expanded', 'true'); placePop(); }
  p.tabIndex = -1; p.focus({preventScroll: true});
}
function placePop(){
  const p = $('pop'); if (!p || !p._btn) return;
  const r = p._btn.getBoundingClientRect();
  const box = (p._btn.closest('.leftscroll, .plate') || document.body).getBoundingClientRect();
  if (!p._btn.isConnected || r.bottom < box.top || r.top > box.bottom) { closePop(); return; }
  const pw = p.offsetWidth, ph = p.offsetHeight, vw = innerWidth, vh = innerHeight;
  const x = Math.min(Math.max(12, r.left + r.width / 2 - pw / 2), vw - pw - 12);
  let y = r.bottom + 8; if (y + ph > vh - 12) y = Math.max(12, r.top - ph - 8);
  p.style.left = x + 'px'; p.style.top = y + 'px';
}
document.addEventListener('pointerdown', e => { const p = $('pop'); if (p && !p.contains(e.target) && !(p._btn && p._btn.contains(e.target))) closePop(); }, true);
addEventListener('resize', closePop);
document.addEventListener('scroll', e => { const p = $('pop'); if (p && !p.contains(e.target)) placePop(); }, true);
function openItemPlate(C, it){
  let h = '<div class="kicker">' + esc(it.kicker || 'On the plate') + '</div><h1>' + esc(it.title || it.label) + '</h1>';
  if (it.sub) h += '<p class="sub">' + esc(it.sub) + '</p>';
  if (it.text) {
    const prose = it.text.replace(/\s*\[\[[a-z0-9-]+\]\]/g, '').trim();
    if (prose) h += '<p>' + claimify(C, it.text) + '</p>';
    else [...it.text.matchAll(/\[\[([a-z0-9-]+)\]\]/g)].forEach(m => { const c = C.claims[m[1]]; if (c) h += '<p>' + esc(c.text) + claimify(C, ' [[' + m[1] + ']]') + '</p>'; });
  }
  if (it.facts) h += '<table class="data">' + it.facts.map(([k, v]) => '<tr><td>' + esc(k) + '</td><td>' + claimify(C, v) + '</td></tr>').join('') + '</table>';
  h += sourcesHTML(C, it.sources);
  $('tip').hidden = true; openPlate(h);
  $('plate').querySelectorAll('.cl').forEach(b => b.onclick = () => openClaim(C, b.dataset.c, b));
}

/* ============ the figure: an engraved plate ============ */
const FIG = {
  spec: null, view: null, anim: 0, proj: null,
  size(){ const r = $('fig').getBoundingClientRect(); return [Math.max(10, r.width), Math.max(10, r.height)]; },
  show(spec, figNo){
    this.spec = spec || {kind: 'map'}; this.figNo = figNo;
    $('figNo').textContent = 'Fig. ' + figNo;
    $('figCap').textContent = this.spec.caption || '';
    $('figHint').textContent = this.spec.hint || '';
    const lg = $('figLegend'); lg.replaceChildren();
    if (this.spec.legend) { const L = el('div', 'legend'); this.spec.legend.forEach(([sym, t]) => L.append(el('span', null, esc(t) + ' <i class="' + esc(sym) + '"></i>'))); lg.append(L); }
    if (this.spec.readout) lg.append(el('div', null, esc(this.spec.readout)));
    $('tip').hidden = true;
    if (this.spec.kind === 'map') this.toMap(); else this.toChart();
  },
  redraw(){ if (!this.spec) return; if (this.spec.kind === 'map') { if (!S.geo || !window.d3) return; this.drawBase(this.view, true); this.drawOver(false); } else this.toChart(); },
  /* ---- map ---- */
  projFor(v){
    const [w, h] = this.size();
    const pr = d3.geoNaturalEarth1().rotate([-(v.lon || 0), 0]);
    pr.fitExtent([[24, 24], [w - 24, h - 24]], {type: 'Sphere'});
    const k = v.zoom || 1, base = pr.scale();
    pr.scale(base * k);
    const c = pr([v.lon || 0, v.lat || 0]), t = pr.translate();
    pr.translate([t[0] + (w / 2 + (v.dx || 0) * w) - c[0], t[1] + (h / 2 + (v.dy || 0) * h) - c[1]]);
    // keep the edge of the world out of view when the map is taller than the plate; centre it when shorter
    const [[x0, y0], [x1, y1]] = d3.geoPath(pr).bounds({type: 'Sphere'}); const tt = pr.translate(); let sy = 0;
    if (y1 - y0 >= h) { if (y0 > 0) sy = -y0; else if (y1 < h) sy = h - y1; } else sy = (h - (y1 - y0)) / 2 - y0;
    pr.translate([tt[0], tt[1] + sy]);
    return pr;
  },
  async toMap(){
    { const old = $('hc'); if (old) old.remove(); $('book').classList.remove('hchart'); }
    const target = Object.assign({lon: 10, lat: 15, zoom: 1}, this.spec.view || {}); const mySpec = this.spec;
    if (!S.geo) { $('figload').hidden = false; $('figload').textContent = 'Engraving the plate…'; $('over').innerHTML = ''; { const cv = $('base'); cv.getContext('2d').clearRect(0, 0, cv.width, cv.height); } await loadTopo(); if (this.spec !== mySpec) return; if (!S.geo || !window.d3) { $('figload').textContent = 'The map could not load here.'; return; } }
    $('figload').hidden = true;
    const from = this.view || target; this.view = target;
    cancelAnimationFrame(this.anim);
    $('over').replaceChildren();
    const same = from.lon === target.lon && from.lat === target.lat && from.zoom === target.zoom;
    if (same || reduce()) { this.drawBase(target, true); this.drawOver(true); return; }
    const t0 = performance.now(), D = 1000, ease = d3.easeCubicInOut;
    const step = now => {
      const u = Math.min(1, (now - t0) / D), e = ease(u);
      const v = {lon: from.lon + (target.lon - from.lon) * e, lat: from.lat + (target.lat - from.lat) * e, zoom: from.zoom * Math.pow(target.zoom / from.zoom, e), dx: (from.dx || 0) + ((target.dx || 0) - (from.dx || 0)) * e, dy: (from.dy || 0) + ((target.dy || 0) - (from.dy || 0)) * e};
      this.drawBase(v, u === 1);
      if (u < 1) this.anim = requestAnimationFrame(step); else this.drawOver(true);
    };
    this.anim = requestAnimationFrame(step);
  },
  drawBase(v, fine){
    const cv = $('base'), [w, h] = this.size(), dpr = Math.min(2, devicePixelRatio || 1);
    if (cv.width !== Math.round(w * dpr) || cv.height !== Math.round(h * dpr)) { cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); }
    const ctx = cv.getContext('2d'); ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
    const pr = this.projFor(v); this.proj = pr;
    const path = d3.geoPath(pr, ctx);
    const C = {leaf: css('--leaf'), sea: css('--sea'), line: css('--sea-line'), land: css('--land'), ink: css('--land-ink'), river: css('--river'), grat: css('--grat')};
    ctx.clearRect(0, 0, w, h); ctx.fillStyle = C.leaf; ctx.fillRect(0, 0, w, h);
    ctx.save(); ctx.beginPath(); path({type: 'Sphere'}); ctx.fillStyle = C.sea; ctx.fill(); ctx.clip();
    // graticule
    ctx.beginPath(); path(d3.geoGraticule().step([15, 15])()); ctx.strokeStyle = C.grat; ctx.lineWidth = .6; ctx.stroke();
    ctx.beginPath(); path({type: 'LineString', coordinates: [[-180, 0], [-90, 0], [0, 0], [90, 0], [180, 0]]}); ctx.lineWidth = 1; ctx.stroke();
    // water-lining: concentric engraved lines following every coast
    if (fine) {
      const k = Math.max(.7, Math.min(1.6, pr.scale() / 220));
      const rings = [[16, .22], [11.5, .32], [7.5, .45], [4, .65]];
      ctx.lineJoin = 'round';
      rings.forEach(([g, a]) => {
        ctx.beginPath(); path(S.geo.land);
        ctx.globalAlpha = a; ctx.strokeStyle = C.line; ctx.lineWidth = g * 2 * k; ctx.stroke();
        ctx.globalAlpha = 1; ctx.strokeStyle = C.sea; ctx.lineWidth = g * 2 * k - 1.5; ctx.stroke();
      });
    }
    // land
    ctx.beginPath(); path(S.geo.land); ctx.fillStyle = C.land; ctx.fill();
    if (fine) { ctx.save(); ctx.clip(); ctx.fillStyle = this.stipple(C.ink); ctx.globalAlpha = .9; ctx.fillRect(0, 0, w, h); ctx.restore(); }
    if (S.geo.lakes) { ctx.beginPath(); path(S.geo.lakes); ctx.fillStyle = C.sea; ctx.fill(); }
    if (fine && S.geo.rivers) { ctx.beginPath(); path(S.geo.rivers); ctx.strokeStyle = C.river; ctx.lineWidth = .7; ctx.stroke(); }
    ctx.beginPath(); path(S.geo.land); ctx.strokeStyle = C.ink; ctx.lineWidth = .7; ctx.stroke();
    ctx.restore();
    ctx.beginPath(); path({type: 'Sphere'}); ctx.strokeStyle = C.ink; ctx.lineWidth = 1.1; ctx.stroke();
  },
  stipple(ink){
    const key = ink; if (this._pat && this._patKey === key) return this._pat;
    const c = document.createElement('canvas'); c.width = c.height = 9; const x = c.getContext('2d');
    x.fillStyle = ink; x.globalAlpha = .13; x.fillRect(1, 1, 1, 1); x.fillRect(5.5, 5.5, 1, 1);
    this._pat = $('base').getContext('2d').createPattern(c, 'repeat'); this._patKey = key; return this._pat;
  },
  drawOver(animate){
    const svg = $('over'), pr = this.proj, [w, h] = this.size(), spec = this.spec, C = S.chapters[S.ch];
    svg.setAttribute('viewBox', '0 0 ' + w + ' ' + h); svg.setAttribute('aria-label', spec.caption || 'Map');
    const defs = '<defs><pattern id="hatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="6" height="6" fill="transparent"/><line x1="0" y1="0" x2="0" y2="6" stroke="var(--zone)" stroke-width="1.1" opacity=".55"/></pattern>'
      + '<pattern id="icehatch" width="5" height="5" patternUnits="userSpaceOnUse"><rect width="5" height="5" fill="var(--leaf)" opacity=".9"/><line x1="0" y1="4.5" x2="5" y2="4.5" stroke="var(--sea-line)" stroke-width=".8"/></pattern>'
      + '<marker id="ah" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10L3 5z" class="head"/></marker>'
      + '<marker id="ahk" viewBox="0 0 10 10" refX="7" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10L3 5z" class="head ink"/></marker></defs>';
    let out = defs;
    const P = ll => pr(ll), gp = d3.geoPath(pr);
    const visible = ll => { const q = pr(ll); return q && q[0] > 20 && q[0] < w - 20 && q[1] > 20 && q[1] < h - 20; };
    const seas = spec.seas !== false ? (spec.seaLabels || DEFAULT_SEAS) : [];
    seas.forEach(s => { if (!visible(s.ll)) return; const q = P(s.ll); out += '<text class="sea-lab" x="' + q[0] + '" y="' + q[1] + '" text-anchor="middle">' + esc(s.t) + '</text>'; });
    const layers = spec.layers || [];
    let idx = 0; const hits = [];
    layers.forEach(L => {
      (L.items || []).forEach(it => {
        const n = idx++;
        if (L.type === 'zone') {
          const g = d3.geoCircle().center(it.ll).radius(it.r || 6)();
          out += '<g class="fade"><path class="zone" d="' + gp(g) + '"/></g>';
          if (it.label) { const q = P(it.lab || it.ll); out += '<text class="reg' + (it.lit ? ' lit' : '') + ' fade" x="' + q[0] + '" y="' + q[1] + '" text-anchor="middle">' + esc(it.label) + '</text>'; }
        }
        if (L.type === 'poly') {
          let ring = it.ring.slice(); if (ring[0][0] !== ring[ring.length - 1][0] || ring[0][1] !== ring[ring.length - 1][1]) ring.push(ring[0]);
          let g = {type: 'Polygon', coordinates: [ring]}; if (d3.geoArea(g) > 2 * Math.PI) g = {type: 'Polygon', coordinates: [ring.slice().reverse()]};
          out += '<g class="fade"><path class="' + esc(it.kind || 'ice') + '" d="' + gp(g) + '"/></g>';
          if (it.label) { const q = P(it.lab || d3.geoCentroid(g)); out += '<text class="reg' + (it.kind === 'bridge' ? '' : ' ice-lab') + ' fade" x="' + q[0] + '" y="' + q[1] + '" text-anchor="middle"' + (it.size ? ' style="font-size:' + num(it.size) + 'px"' : '') + '>' + esc(it.label) + '</text>'; }
        }
        if (L.type === 'region') { const q = P(it.ll); out += '<text class="reg' + (it.lit ? ' lit' : '') + '" x="' + q[0] + '" y="' + q[1] + '" text-anchor="middle"' + (it.rot ? ' transform="rotate(' + num(it.rot) + ' ' + q[0] + ' ' + q[1] + ')"' : '') + (it.size ? ' style="font-size:' + num(it.size) + 'px"' : '') + '>' + esc(it.label) + '</text>'; }
        if (L.type === 'arrow' || L.type === 'route') {
          const pts = it.path.map(P).filter(Boolean);
          const line = d3.line().curve(d3.curveCatmullRom.alpha(.5))(pts);
          const cls = L.type === 'arrow' ? 'arrow' : 'route' + (it.acc ? ' acc' : '');
          const mk = L.type === 'arrow' ? ' marker-end="url(#ah)"' : (it.head ? ' marker-end="url(#' + (it.acc ? 'ah' : 'ahk') + ')"' : '');
          out += '<path class="' + cls + (animate && L.type === 'arrow' ? ' draw' : '') + '" data-i="' + n + '" d="' + line + '"' + mk + ' style="animation-delay:' + (it.delay || 0) + 's"/>';
          if (it.label) { const q = P(it.lab || it.path[Math.floor(it.path.length / 2)]); out += '<text class="alab' + (L.type === 'route' && !it.acc ? ' ink' : '') + ' fade" x="' + (q[0] + (it.ldx || 0)) + '" y="' + (q[1] + (it.ldy || 0)) + '" text-anchor="' + (ANCH(it.anchor) || 'middle') + '">' + esc(it.label) + '</text>'; }
        }
        if (L.type === 'points') {
          const q = P(it.ll); if (!q) return;
          const r = it.big ? 5.5 : 4;
          const anchor = ANCH(it.anchor) || 'start', dx = it.dx != null ? it.dx : (anchor === 'end' ? -9 : anchor === 'middle' ? 0 : 9), dy = it.dy != null ? it.dy : (anchor === 'middle' ? -12 : 5);
          out += '<g class="pt' + (it.acc ? ' acc' : '') + '" data-i="' + n + '"><circle class="dot" cx="' + q[0] + '" cy="' + q[1] + '" r="' + r + '"/>'
            + (it.label ? '<text class="lab" x="' + (q[0] + dx) + '" y="' + (q[1] + dy) + '" text-anchor="' + anchor + '">' + esc(it.label) + '</text>' : '')
            + (it.date ? '<text class="date" x="' + (q[0] + dx) + '" y="' + (q[1] + dy + 14) + '" text-anchor="' + anchor + '">' + esc(it.date) + '</text>' : '')
            + ((it.plate || it.tip) ? '<circle class="hit" cx="' + q[0] + '" cy="' + q[1] + '" r="14"/>' : '') + '</g>';
          hits[n] = it;
        }
      });
    });
    if (spec.cartouche) { const [cw, ch] = [300, 92], x = w / 2 - cw / 2, y = h - ch - 46; out += '<g class="cart fade"><rect x="' + x + '" y="' + y + '" width="' + cw + '" height="' + ch + '" rx="2"/><rect x="' + (x + 4) + '" y="' + (y + 4) + '" width="' + (cw - 8) + '" height="' + (ch - 8) + '" rx="1" style="fill:none;stroke:var(--land-ink);stroke-width:.5"/><text x="' + w / 2 + '" y="' + (y + 40) + '" style="font-size:24px">' + esc(spec.cartouche[0]) + '</text><text x="' + w / 2 + '" y="' + (y + 66) + '" style="font-style:italic;font-size:15px;fill:var(--ink-2)">' + esc(spec.cartouche[1]) + '</text></g>'; }
    svg.innerHTML = out;
    svg.querySelectorAll('path.draw').forEach(p => { const L = p.getTotalLength(); p.style.setProperty('--len', L); p.style.strokeDasharray = L; p.style.strokeDashoffset = 0; });
    svg.querySelectorAll('.pt').forEach(g => {
      const it = hits[+g.dataset.i]; if (!it || !(it.plate || it.tip)) return;
      const hit = g.querySelector('.hit');
      hit.addEventListener('mouseenter', ev => tipShow(it.label, it.tip || (it.plate && it.plate.sub) || '', ev));
      hit.addEventListener('mousemove', ev => tipMove(ev));
      hit.addEventListener('mouseleave', () => $('tip').hidden = true);
      if (it.plate) hit.addEventListener('click', () => { $('tip').hidden = true; openItemPlate(C, Object.assign({label: it.label}, it.plate)); });
    });
  },
  /* ---- charts ---- */
  toChart(){ try { this.toChart_(); } catch (e) { $('over').innerHTML = ''; $('figload').hidden = false; $('figload').textContent = 'The chart could not load here.'; } },
  toChart_(){
    cancelAnimationFrame(this.anim); $('figload').hidden = true;
    const old = $('hc'); if (old) old.remove();
    const useHTML = narrow() && HCH[this.spec.chart];
    $('book').classList.toggle('hchart', !!useHTML);
    if (useHTML) {
      $('over').innerHTML = ''; const cv0 = $('base'); cv0.width = cv0.height = 0; this.view = null;
      const box = el('div', 'hc'); box.id = 'hc'; box.innerHTML = HCH[this.spec.chart](this.spec);
      $('fig').append(box);
      const items = this.spec.rows || this.spec.eras || [];
      box.querySelectorAll('button[data-pi]').forEach(b => { const it = items[+b.dataset.pi]; if (it && it.plate) b.onclick = () => openItemPlate(S.chapters[S.ch], it.plate); });
      return;
    }
    const cv = $('base'), ctx = cv.getContext('2d'); const [w, h] = this.size(); const dpr = Math.min(2, devicePixelRatio || 1);
    cv.width = Math.round(w * dpr); cv.height = Math.round(h * dpr); ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.fillStyle = css('--leaf'); ctx.fillRect(0, 0, w, h);
    this.view = null;
    const svg = $('over'); svg.setAttribute('viewBox', '0 0 ' + w + ' ' + h); svg.setAttribute('aria-label', this.spec.caption || 'Chart');
    svg.innerHTML = (CHARTS[this.spec.chart] || (() => ''))(this.spec, w, h);
    svg.querySelectorAll('[data-tip]').forEach(n => { n.addEventListener('mouseenter', ev => tipShow(n.dataset.tipT || '', n.dataset.tip, ev)); n.addEventListener('mousemove', tipMove); n.addEventListener('mouseleave', () => $('tip').hidden = true); });
    svg.querySelectorAll('path.draw').forEach(p => { const L = p.getTotalLength(); p.style.setProperty('--len', L); p.style.strokeDasharray = L; });
    const items = this.spec.rows || this.spec.eras || [];
    svg.querySelectorAll('[data-pi]').forEach(n => { const it = items[+n.dataset.pi]; if (it && it.plate) {
      const open = () => openItemPlate(S.chapters[S.ch], it.plate);
      n.classList.add('has-plate'); n.setAttribute('tabindex', '0'); n.setAttribute('role', 'button'); n.setAttribute('aria-label', (it.t || it.name || 'Detail') + ': open the plate');
      n.addEventListener('click', open); n.addEventListener('keydown', e => { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); } });
    } });
    svg.setAttribute('role', svg.querySelector('.has-plate') ? 'group' : 'img');
  }
};
const DEFAULT_SEAS = [{t: 'PACIFIC OCEAN', ll: [-150, 8]}, {t: 'PACIFIC OCEAN', ll: [160, 20]}, {t: 'ATLANTIC OCEAN', ll: [-38, 22]}, {t: 'INDIAN OCEAN', ll: [78, -22]}];
function tipShow(t, s, ev){ const tp = $('tip'); tp.innerHTML = '<b>' + esc(t) + '</b>' + (s ? '<span>' + esc(s) + '</span>' : ''); tp.hidden = false; tipMove(ev); }
function tipMove(ev){ const r = $('fig').getBoundingClientRect(), tp = $('tip'); let x = ev.clientX - r.left + 14, y = ev.clientY - r.top + 14; if (x + 270 > r.width) x -= 290; tp.style.left = x + 'px'; tp.style.top = y + 'px'; }

/* ---------- charts as plain HTML lists on narrow screens ---------- */
const HCH = {
  _row(i, r, inner){ const tag = r.plate ? 'button' : 'div'; return '<li><' + tag + (r.plate ? ' type="button"' : '') + ' class="hc-row' + (r.acc ? ' acc' : '') + (r.plate ? ' has-plate' : '') + '" data-pi="' + i + '">' + inner + (r.plate ? '<span class="hc-go" aria-hidden="true">›</span>' : '') + '</' + tag + '></li>'; },
  _head(spec){ return spec.title ? '<p class="hc-title">' + esc(spec.title) + '</p>' : ''; },
  _foot(spec){ return (spec.axis ? '<p class="hc-axis">' + esc(spec.axis) + '</p>' : '') + ((spec.notes || []).length && typeof spec.notes[0] === 'string' ? '<p class="hc-notes">' + spec.notes.map(esc).join(' ') + '</p>' : ''); },
  bars(spec){
    const lo = spec.min || 1, log = spec.scale === 'log';
    const pos = v => log ? Math.max(0, Math.min(1, (Math.log(Math.max(lo, v)) - Math.log(lo)) / (Math.log(spec.max) - Math.log(lo)))) : Math.max(0, Math.min(1, v / spec.max));
    return this._head(spec) + '<ol class="hc-rows">' + spec.rows.map((r, i) => this._row(i, r,
      '<span class="hc-t">' + esc(r.t) + '</span>' + (r.sub ? '<span class="hc-sub">' + esc(r.sub) + '</span>' : '')
      + '<span class="hc-bar"><i style="width:' + (100 * pos(r.v)).toFixed(1) + '%"></i><b>' + esc(r.lab || fmt(r.v)) + '</b></span>'
      + (r.tip ? '<span class="hc-tip">' + esc(r.tip) + '</span>' : ''))).join('') + '</ol>' + this._foot(spec);
  },
  ranges(spec){
    return this._head(spec) + '<ol class="hc-rows">' + spec.rows.map((r, i) => this._row(i, r,
      '<span class="hc-t">' + esc(r.t) + '</span>' + (r.sub ? '<span class="hc-sub">' + esc(r.sub) + '</span>' : '') + (r.lab ? '<span class="hc-val">' + esc(r.lab) + '</span>' : '')
      + (r.tip ? '<span class="hc-tip">' + esc(r.tip) + '</span>' : ''))).join('') + '</ol>' + this._foot(spec);
  },
  split(spec){
    return this._head(spec) + '<ol class="hc-rows">' + spec.rows.map((r, i) => { const tot = r.parts.reduce((a, p) => a + p.v, 0); return this._row(i, r,
      '<span class="hc-t">' + esc(r.t) + '</span><span class="hc-split">' + r.parts.map(p => '<i class="' + (p.acc ? 'acc' : '') + '" style="flex:' + p.v / tot + '"></i>').join('') + '</span>'
      + '<span class="hc-sub">' + r.parts.map(p => esc((p.name ? p.name + ' ' : '') + (p.lab || ''))).filter(Boolean).join(' · ') + '</span>'); }).join('') + '</ol>' + this._foot(spec);
  },
  ledger(spec){
    const col = (c, sign) => '<div class="hc-col"><p class="hc-h">' + esc(c.h) + '</p><ul>' + c.items.map(it => '<li><span class="hc-t">' + (spec.signs !== false ? sign + ' ' : '') + esc(it.t) + '</span>' + (it.s ? '<span class="hc-sub">' + esc(it.s) + '</span>' : '') + (it.tip ? '<span class="hc-tip">' + esc(it.tip) + '</span>' : '') + '</li>').join('') + '</ul></div>';
    return this._head(spec) + col(spec.left, '+') + col(spec.right, '−') + this._foot(spec);
  }
};

/* ---------- charts drawn as engraved plates ---------- */
const fmt = n => n.toLocaleString('en-US');
const CHARTS = {
  // deep time: a 300,000-year bar, then the last day of a 24-hour clock
  deeptime(spec, w, h){
    const L = 70, R = w - 70, T = Math.max(120, h * .22), span = spec.span;
    const x = ya => L + (1 - ya / span) * (R - L);
    let s = '<defs><pattern id="hatch2" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="var(--land-ink)" stroke-width=".7" opacity=".35"/></pattern></defs><g class="chart">';
    s += '<text class="t-fell-i" x="' + L + '" y="' + (T - 34) + '">' + esc(spec.title1) + '</text>';
    s += '<rect class="bar" x="' + L + '" y="' + T + '" width="' + (R - L) + '" height="26"/>';
    const wx = x(spec.writing);
    s += '<rect class="bar acc" x="' + wx + '" y="' + T + '" width="' + Math.max(2, R - wx) + '" height="26"/>';
    for (let ya = span; ya >= 0; ya -= spec.tick) { const xx = x(ya); s += '<line class="tick" x1="' + xx + '" x2="' + xx + '" y1="' + (T + 26) + '" y2="' + (T + 32) + '"/><text x="' + xx + '" y="' + (T + 46) + '" text-anchor="middle">' + (ya ? fmt(ya / 1000) + 'k' : 'now') + '</text>'; }
    s += '<text x="' + (L) + '" y="' + (T + 64) + '">years ago</text>';
    spec.marks.forEach((m, i) => { const xx = x(m.ya); const yy = T - 8 - (i % 2) * 14; s += '<line class="mk" x1="' + xx + '" x2="' + xx + '" y1="' + yy + '" y2="' + (T + 26) + '"/><text class="t-ink" x="' + (xx + (m.anchor === 'end' ? -4 : 4)) + '" y="' + (yy - 3) + '" text-anchor="' + (m.anchor || 'start') + '">' + esc(m.t) + '</text>'; });
    // the clock
    const T2 = T + Math.max(130, h * .26), cx = L + (R - L) / 2;
    s += '<text class="t-fell-i" x="' + L + '" y="' + (T2 - 18) + '">' + esc(spec.title2) + '</text>';
    const L2 = L, R2 = R, mins = spec.clockMinutes; const x2 = m => L2 + (1 - m / mins) * (R2 - L2);
    s += '<rect class="bar" x="' + L2 + '" y="' + T2 + '" width="' + (R2 - L2) + '" height="22"/>';
    for (let m = mins; m >= 0; m -= spec.clockTick) { const xx = x2(m); const hh = 24 - m / 60; const lab = m === 0 ? '24:00' : String(Math.floor(hh)).padStart(2, '0') + ':' + String(Math.round((hh % 1) * 60)).padStart(2, '0'); s += '<line class="tick" x1="' + xx + '" x2="' + xx + '" y1="' + (T2 + 22) + '" y2="' + (T2 + 28) + '"/><text x="' + xx + '" y="' + (T2 + 42) + '" text-anchor="middle">' + lab + '</text>'; }
    spec.clock.forEach((m, i) => {
      const minsBefore = m.ya / span * 1440; const xx = x2(minsBefore); const yy = T2 + 64 + (i % 3) * 30;
      const hh = 24 - minsBefore / 60; const hhI = Math.floor(hh), mmF = (hh - hhI) * 60, mmI = Math.floor(mmF), ss = Math.round((mmF - mmI) * 60);
      const clock = String(hhI).padStart(2, '0') + ':' + String(mmI).padStart(2, '0') + (minsBefore < 5 ? ':' + String(ss).padStart(2, '0') : '');
      s += '<line class="mk" x1="' + xx + '" x2="' + xx + '" y1="' + T2 + '" y2="' + (yy - 12) + '"/><circle class="mkdot" cx="' + xx + '" cy="' + (T2 + 11) + '" r="3"/>';
      s += '<text class="t-ink" x="' + (xx + (m.anchor === 'end' ? -5 : 5)) + '" y="' + yy + '" text-anchor="' + (m.anchor || 'start') + '">' + esc(m.t) + '</text><text class="t-acc" x="' + (xx + (m.anchor === 'end' ? -5 : 5)) + '" y="' + (yy + 13) + '" text-anchor="' + (m.anchor || 'start') + '">' + clock + '</text>';
    });
    return s + '</g>';
  },
  // world population, linear with an optional log toggle
  population(spec, w, h){
    const L = 74, R = w - 46, T = 92, B = h - 92;
    const pts = spec.series; const xs = pts.map(p => p[0]); const x0 = spec.x0 ?? Math.min(...xs), x1 = Math.max(...xs);
    const xsc = d3.scaleLinear().domain([x0, x1]).range([L, R]);
    const log = FIG.popLog; const ysc = (log ? d3.scaleLog().domain([1, 10000]) : d3.scaleLinear().domain([0, spec.ymax])).range([B, T]);
    let s = '<defs><pattern id="hatch2" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="var(--land-ink)" stroke-width=".7" opacity=".35"/></pattern></defs><g class="chart">';
    const yt = log ? [1, 10, 100, 1000, 10000] : d3.range(0, spec.ymax + 1, 1000);
    yt.forEach(v => { const y = ysc(v); s += '<line class="grid" x1="' + L + '" x2="' + R + '" y1="' + y + '" y2="' + y + '"/><text x="' + (L - 8) + '" y="' + (y + 4) + '" text-anchor="end">' + (v >= 1000 ? fmt(v / 1000) + ' bn' : fmt(v) + ' m') + '</text>'; });
    spec.xticks.forEach(v => { const x = xsc(v); s += '<line class="tick" x1="' + x + '" x2="' + x + '" y1="' + B + '" y2="' + (B + 6) + '"/><text x="' + x + '" y="' + (B + 20) + '" text-anchor="middle">' + (v < 0 ? fmt(-v) + ' BCE' : v === 0 ? '1 CE' : v) + '</text>'; });
    s += '<line class="ax" x1="' + L + '" x2="' + R + '" y1="' + B + '" y2="' + B + '"/><line class="ax" x1="' + L + '" x2="' + L + '" y1="' + T + '" y2="' + B + '"/>';
    const line = d3.line().x(p => xsc(p[0])).y(p => ysc(Math.max(1, p[1])));
    const area = d3.area().x(p => xsc(p[0])).y0(B).y1(p => ysc(Math.max(1, p[1])));
    const vis = pts.filter(p => p[0] >= x0);
    s += '<path class="area" d="' + area(vis) + '"/><path class="line draw" d="' + line(vis) + '"/>';
    vis.forEach(p => { s += '<circle class="hit" data-tip-t="' + (p[0] < 0 ? fmt(-p[0]) + ' BCE' : p[0] === 0 ? '1 CE' : p[0] + ' CE') + '" data-tip="' + (p[1] >= 1000 ? (p[1] / 1000).toFixed(2) + ' billion' : fmt(Math.round(p[1])) + ' million') + ' people" cx="' + xsc(p[0]) + '" cy="' + ysc(Math.max(1, p[1])) + '" r="9"/><circle class="mkdot" style="fill:var(--ink)" cx="' + xsc(p[0]) + '" cy="' + ysc(Math.max(1, p[1])) + '" r="2"/>'; });
    (spec.notes || []).forEach(n => { const x = xsc(n.x), y = ysc(Math.max(1, n.y)); s += '<line class="mk" x1="' + x + '" x2="' + (x + (n.dx || -40)) + '" y1="' + y + '" y2="' + (y + (n.dy || -30)) + '"/><text class="t-acc" x="' + (x + (n.dx || -40) + (n.dx > 0 ? 4 : -4)) + '" y="' + (y + (n.dy || -30) - 4) + '" text-anchor="' + (n.dx > 0 ? 'start' : 'end') + '">' + esc(n.t) + '</text>'; });
    s += '<text class="t-fell-i" x="' + L + '" y="' + (T - 30) + '">' + esc(spec.title) + (log ? ' (log scale)' : '') + '</text>';
    s += '<text data-toggle-log="1" class="t-acc" style="cursor:pointer;text-decoration:underline" x="' + R + '" y="' + (T - 30) + '" text-anchor="end">' + (log ? 'show linear scale' : 'show log scale') + '</text>';
    return s + '</g>';
  },
  // how far back each kind of evidence reaches (log scale of years ago)
  evidence(spec, w, h){
    const L = 210, R = w - 50, T = 110; const rowH = Math.min(84, (h - T - 130) / spec.rows.length);
    const xs = d3.scaleLog().domain([10, spec.max]).range([R, L]);
    let s = '<g class="chart"><text class="t-fell-i" x="' + 40 + '" y="' + (T - 46) + '">' + esc(spec.title) + '</text>';
    [10, 100, 1000, 10000, 100000, 1000000].filter(v => v <= spec.max).forEach(v => { const x = xs(v); s += '<line class="grid" x1="' + x + '" x2="' + x + '" y1="' + (T - 14) + '" y2="' + (T + rowH * spec.rows.length) + '"/><text x="' + x + '" y="' + (T - 20) + '" text-anchor="middle">' + fmt(v) + '</text>'; });
    s += '<text x="' + R + '" y="' + (T + rowH * spec.rows.length + 22) + '" text-anchor="end">years ago (each step ten times further)</text>';
    spec.rows.forEach((r, i) => { const y = T + i * rowH + 6; const x = xs(r.reach); s += '<text class="t-fell" x="40" y="' + (y + rowH * .42) + '">' + esc(r.t) + '</text><rect class="bar' + (r.acc ? ' acc' : '') + '" x="' + x + '" y="' + y + '" width="' + (R - x) + '" height="' + (rowH * .5) + '"/><text x="' + (x - 6) + '" y="' + (y + rowH * .36) + '" text-anchor="end">' + esc(r.lab) + '</text><rect class="hit" data-tip-t="' + esc(r.t) + '" data-tip="' + esc(r.tip) + '" x="40" y="' + y + '" width="' + (R - 40) + '" height="' + rowH * .7 + '"/>'; });
    return s + '</g>';
  },
  // the main road: eras as bands on a piecewise time axis
  // time ranges: one bar per row, from 'from' to 'to' years ago (0 = today)
  ranges(spec, w, h){
    const L = Math.min(230, w * .3), R = w - 44, T = 150, n = spec.rows.length;
    const rowH = Math.max(30, Math.min(58, (h - T - 120) / n));
    const max = spec.max, unit = spec.unit === 'ka' ? 1e3 : 1e6, uname = spec.unit || 'Ma';
    const lo = spec.min || 0;
    const x = spec.scale === 'log' ? (ya => { const sc = d3.scaleLog().domain([max, spec.min || 1000]).range([L, R]); return sc(Math.max(spec.min || 1000, ya)); }) : (ya => L + (max - Math.max(lo, Math.min(max, ya))) / (max - lo) * (R - L));
    let s = '<defs><pattern id="hatch2" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="var(--land-ink)" stroke-width=".7" opacity=".35"/></pattern></defs><g class="chart">';
    s += '<text class="t-fell-i" x="40" y="' + (T - 62) + '">' + esc(spec.title) + '</text>';
    const B = T + rowH * n;
    (spec.ticks || []).forEach((v, k) => { const xx = x(v); const tl = spec.tickLabels ? spec.tickLabels[k] : (v === 0 ? 'now' : fmt(+(v / unit).toFixed(2)) + ' ' + uname); s += '<line class="grid" x1="' + xx + '" x2="' + xx + '" y1="' + (T - 16) + '" y2="' + B + '"/><text x="' + xx + '" y="' + (T - 24) + '" text-anchor="middle">' + esc(tl) + '</text>'; });
    (spec.marks || []).forEach((m, k) => { const xx = x(m.ya); s += '<line class="vmark" x1="' + xx + '" x2="' + xx + '" y1="' + (T - 8) + '" y2="' + (B + 8 + k * 16) + '"/><text class="t-acc" x="' + (xx + (m.anchor === 'end' ? -5 : 5)) + '" y="' + (B + 22 + k * 16) + '" text-anchor="' + (m.anchor || 'start') + '">' + esc(m.t) + '</text>'; });
    spec.rows.forEach((r, i) => {
      const y = T + i * rowH, x0 = x(r.from), x1 = x(r.to || 0), bh = Math.min(16, rowH * .38);
      s += '<g data-pi="' + i + '"' + (r.tip ? ' data-tip-t="' + esc(r.t) + '" data-tip="' + esc(r.tip) + '"' : '') + '>';
      s += '<rect x="0" y="' + y + '" width="' + w + '" height="' + rowH + '" fill="transparent"/>';
      s += '<text class="t-fell" x="40" y="' + (y + rowH * .5) + '">' + esc(r.t) + '</text>';
      if (r.sub) s += '<text x="40" y="' + (y + rowH * .5 + 14) + '">' + esc(r.sub) + '</text>';
      s += '<rect class="rbar' + (r.acc ? ' acc' : '') + (r.open ? ' open' : '') + '" x="' + Math.min(x0, x1) + '" y="' + (y + rowH * .5 - bh * .75) + '" width="' + Math.max(3, Math.abs(x1 - x0)) + '" height="' + bh + '"/>';
      if (r.lab) { const right = x1 < R - 90; s += '<text x="' + (right ? x1 + 6 : x0 - 6) + '" y="' + (y + rowH * .5 + 2) + '" text-anchor="' + (right ? 'start' : 'end') + '">' + esc(r.lab) + '</text>'; }
      s += '</g>';
    });
    s += '<text x="' + R + '" y="' + (B + 30 + (spec.marks || []).length * 16) + '" text-anchor="end">' + esc(spec.axis || ('millions of years ago')) + '</text>';
    return s + '</g>';
  },
  // split: each row is one 100% bar divided into parts
  split(spec, w, h){
    const L = 60, R = w - 60, n = spec.rows.length, gap = Math.min(150, (h - 260) / n), T = Math.max(140, (h - gap * n) / 2);
    let s = '<defs><pattern id="hatch2" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="5" stroke="var(--land-ink)" stroke-width=".7" opacity=".35"/></pattern></defs><g class="chart">';
    s += '<text class="t-fell-i" x="' + L + '" y="' + (T - 70) + '">' + esc(spec.title) + '</text>';
    spec.rows.forEach((r, i) => {
      const y = T + i * gap; let x = L; const tot = r.parts.reduce((a, p) => a + p.v, 0);
      s += '<text class="t-fell" x="' + L + '" y="' + (y - 14) + '">' + esc(r.t) + '</text>';
      r.parts.forEach((p, k) => { const wd = (R - L) * p.v / tot; s += '<g' + (p.tip ? ' data-tip-t="' + esc(p.name || '') + '" data-tip="' + esc(p.tip) + '"' : '') + '><rect class="rbar' + (p.acc ? ' acc' : '') + (p.open ? ' open' : '') + '" x="' + x + '" y="' + y + '" width="' + Math.max(2, wd) + '" height="34"/></g>';
        const lw = (p.lab || '').length * 6.7, inside = wd > lw + 20, nearR = x + lw > R; s += p.lab ? '<text class="' + (p.acc ? 't-acc' : 't-ink') + '" x="' + (inside ? x + 10 : (nearR ? R : x)) + '" y="' + (inside ? y + 22 : y + 54) + '" text-anchor="' + (inside || !nearR ? 'start' : 'end') + '">' + esc(p.lab) + '</text>' : ''; x += wd; });
    });
    (spec.notes || []).forEach((t, k) => { s += '<text x="' + L + '" y="' + (T + gap * n + 10 + k * 16) + '">' + esc(t) + '</text>'; });
    return s + '</g>';
  },
  // ledger: two columns, gains and costs, like an engraved account book
  ledger(spec, w, h){
    const L = 50, R = w - 50, mid = (L + R) / 2, n = Math.max(spec.left.items.length, spec.right.items.length), rowH = Math.min(92, (h - 270) / n), T = Math.max(150, (h - rowH * n) / 2 + 10);
    let s = '<g class="chart"><text class="t-fell-i" x="' + L + '" y="' + (T - 80) + '">' + esc(spec.title) + '</text>';
    s += '<line class="ax" x1="' + mid + '" x2="' + mid + '" y1="' + (T - 40) + '" y2="' + (T + rowH * n) + '"/><line class="ax" x1="' + L + '" x2="' + R + '" y1="' + (T - 12) + '" y2="' + (T - 12) + '"/>';
    const signs = spec.signs !== false;
    [[spec.left, L + 4, false], [spec.right, mid + 20, signs]].forEach(([col, x0, acc]) => {
      s += '<text class="t-fell" style="font-size:20px' + (acc ? ';fill:var(--accent)' : '') + '" x="' + x0 + '" y="' + (T - 22) + '">' + esc(col.h) + '</text>';
      col.items.forEach((it, i) => { const y = T + i * rowH + 28;
        s += '<g' + (it.tip ? ' data-tip-t="' + esc(it.t) + '" data-tip="' + esc(it.tip) + '"' : '') + '><rect x="' + x0 + '" y="' + (y - 20) + '" width="' + (mid - L - 30) + '" height="' + (rowH - 8) + '" fill="transparent"/>';
        s += '<text class="t-fell" x="' + x0 + '" y="' + y + '">' + (signs ? (acc ? '− ' : '+ ') : '') + esc(it.t) + '</text>';
        if (it.s) s += '<text x="' + (x0 + 14) + '" y="' + (y + 18) + '">' + esc(it.s) + '</text>';
        s += '<line class="grid" x1="' + x0 + '" x2="' + (x0 + mid - L - 40) + '" y1="' + (y + rowH - 40) + '" y2="' + (y + rowH - 40) + '"/></g>'; });
    });
    const lines = []; (spec.notes || []).forEach(t => { let cur = ''; String(t).split(' ').forEach(wd => { if ((cur + ' ' + wd).trim().length > 92) { lines.push(cur); cur = wd; } else cur = (cur + ' ' + wd).trim(); }); if (cur) lines.push(cur); });
    lines.forEach((t, k) => { s += '<text x="' + L + '" y="' + (T + rowH * n + 30 + k * 16) + '">' + esc(t) + '</text>'; });
    return s + '</g>';
  },
  // bars: horizontal bars from zero, linear or log
  bars(spec, w, h){
    const L = Math.min(250, w * .32), R = w - 70, T = 150, n = spec.rows.length;
    const rowH = Math.max(26, Math.min(64, (h - T - 140) / n)), B = T + rowH * n;
    const lo = spec.min || 1, x = spec.scale === 'log' ? d3.scaleLog().domain([lo, spec.max]).range([L, R]).clamp(true) : d3.scaleLinear().domain([0, spec.max]).range([L, R]);
    let s = '<g class="chart"><text class="t-fell-i" x="40" y="' + (T - 62) + '">' + esc(spec.title) + '</text>';
    (spec.ticks || []).forEach((v, k) => { const xx = x(v); s += '<line class="grid" x1="' + xx + '" x2="' + xx + '" y1="' + (T - 14) + '" y2="' + B + '"/><text x="' + xx + '" y="' + (T - 22) + '" text-anchor="middle">' + esc(spec.tickLabels ? spec.tickLabels[k] : fmt(v)) + '</text>'; });
    spec.rows.forEach((r, i) => {
      const y = T + i * rowH, xv = x(Math.max(lo, r.v)), bh = Math.min(18, rowH * .42), base = spec.scale === 'log' ? L : x(0);
      s += '<g data-pi="' + i + '"' + (r.tip ? ' data-tip-t="' + esc(r.t) + '" data-tip="' + esc(r.tip) + '"' : '') + '><rect x="0" y="' + y + '" width="' + w + '" height="' + rowH + '" fill="transparent"/>';
      s += '<text class="t-fell" x="40" y="' + (y + rowH * .5) + '">' + esc(r.t) + '</text>';
      if (r.sub) s += '<text x="40" y="' + (y + rowH * .5 + 14) + '">' + esc(r.sub) + '</text>';
      s += '<rect class="rbar' + (r.acc ? ' acc' : '') + (r.open ? ' open' : '') + '" x="' + base + '" y="' + (y + rowH * .5 - bh * .75) + '" width="' + Math.max(2, xv - base) + '" height="' + bh + '"/>';
      const lab = r.lab || fmt(r.v), lw = lab.length * 6.7, inside = xv + 6 + lw > w - 16 && xv - base > lw + 16;
      s += '<text class="' + (r.acc ? 't-acc' : 't-ink') + '" x="' + (inside ? base + 8 : xv + 6) + '" y="' + (y + rowH * .5 + 2) + '">' + esc(lab) + '</text></g>';
    });
    if (spec.axis) s += '<text x="' + R + '" y="' + (B + 28) + '" text-anchor="end">' + esc(spec.axis) + '</text>';
    (spec.notes || []).forEach((t, k) => { s += '<text x="40" y="' + (B + 54 + k * 16) + '">' + esc(t) + '</text>'; });
    return s + '</g>';
  },
  road(spec, w, h){
    const L = 60, R = w - 60, T = 120; const segs = spec.eras; const hh = Math.max(220, Math.min(h - T - 120, 420));
    const n = segs.length, bw = (R - L) / n;
    let s = '<g class="chart"><text class="t-fell-i" x="' + L + '" y="' + (T - 50) + '">' + esc(spec.title) + '</text>';
    segs.forEach((e, i) => {
      const x = L + i * bw;
      s += '<rect class="bar' + (e.here ? ' acc' : '') + '" x="' + (x + 2) + '" y="' + T + '" width="' + (bw - 4) + '" height="' + hh + '"/>';
      s += '<text class="t-acc" transform="translate(' + (x + bw / 2 - 11) + ',' + (T + 14) + ') rotate(90)">' + esc(e.dates) + '</text>';
      s += '<text class="t-fell" transform="translate(' + (x + bw / 2 + 5) + ',' + (T + 14) + ') rotate(90)">' + esc(e.t) + '</text>';
      s += '<text x="' + (x + bw / 2) + '" y="' + (T - 10) + '" text-anchor="middle">' + esc(e.ch) + '</text>';
      s += '<rect class="hit" data-tip-t="' + esc(e.t) + '" data-tip="' + esc(e.dates + (e.tip ? ' · ' + e.tip : '')) + '" x="' + x + '" y="' + T + '" width="' + bw + '" height="' + hh + '"/>';
    });
    return s + '</g>';
  }
};
document.addEventListener('click', e => { const t = e.target.closest && e.target.closest('[data-toggle-log]'); if (t) { FIG.popLog = !FIG.popLog; FIG.toChart(); } });

/* ============ practice drawer ============ */
function openPractice(){
  const C = S.chapters[S.ch], P = C.pages[S.page]; if (!P.practice || !P.practice.length) return;
  S.drawer = {mode: 'page', list: P.practice.map((q, i) => qid(S.ch, S.page, i)), at: 0, right: 0};
  renderDrawer();
}
async function startReview(){
  const due = dueList();
  if (!due.length) { if (location.hash === '#review') setHash(''); if (S.mode !== 'book') { if (S.mode !== 'about') showContents(); toast('Nothing is due for review. Practise on any page to add questions.'); } else toast('Nothing is due for review right now.'); return; }
  const f = findQ(due[0]); if (S.mode !== 'book' || S.ch !== f.ch) await openChapter(f.ch, f.p); else if (S.page !== f.p) go(f.p);
  S.drawer = {mode: 'review', list: due, at: 0, right: 0}; renderDrawer();
}
function shuffleOrder(key, n){ let h = 2166136261; for (let k = 0; k < key.length; k++) { h ^= key.charCodeAt(k); h = Math.imul(h, 16777619); } const a = Array.from({length: n}, (_, i) => i); for (let i = n - 1; i > 0; i--) { h ^= h << 13; h ^= h >>> 17; h ^= h << 5; const j = (h >>> 0) % (i + 1); [a[i], a[j]] = [a[j], a[i]]; } return a; }
function closeDrawer(){ const d = $('drawer'); const had = d && d.contains(document.activeElement); if (d) d.remove(); S.drawer = null; if (had && S.mode === 'book' && !$('practiceBtn').hidden) $('practiceBtn').focus({preventScroll: true}); }
function renderDrawer(){
  const D = S.drawer; const old = $('drawer'); if (old) old.remove();
  const box = el('aside', 'drawer'); box.id = 'drawer'; box.setAttribute('aria-label', 'Practice');
  const id = D.list[D.at], f = findQ(id); const C = S.chapters[f.ch];
  if (D.mode === 'review' && (S.ch !== f.ch || S.page !== f.p)) { if (S.ch !== f.ch) openChapter(f.ch, f.p); else go(f.p); }
  const head = el('div', 'dhead');
  head.append(el('div', null, '<div class="kicker">' + (D.mode === 'review' ? 'Review' : 'Practice') + ' · ' + esc(chN(C) + '.' + f.p) + ' · question ' + (D.at + 1) + ' of ' + D.list.length + '</div><h3>' + esc(C.pages[f.p].title) + '</h3>'));
  const x = el('button', 'dclose', '×'); x.type = 'button'; x.setAttribute('aria-label', 'Close practice'); x.onclick = closeDrawer; head.append(x);
  const body = el('div', 'dbody'); const q = f.q;
  body.append(el('p', 'q', rich(q.q)));
  const ul = el('ul', 'choices'); let answered = false;
  const why = el('div', 'why'); why.hidden = true;
  const ord = shuffleOrder(String(id), q.choices.length);
  const btns = ord.map((i, pos) => { const c = q.choices[i]; const li = el('li'), b = el('button'); b.type = 'button'; b.dataset.i = i; b.innerHTML = '<span class="letter">' + 'ABCD'[pos] + '</span><span>' + rich(c) + '</span>'; b.onclick = () => pick(i); li.append(b); ul.append(li); return b; });
  function pick(i){
    if (answered) return; answered = true; const ok = i === q.answer; if (ok) D.right++;
    btns.forEach(b => { const j = +b.dataset.i; b.disabled = true; if (j === q.answer) b.classList.add('right'); else if (j === i) b.classList.add('wrong'); });
    why.innerHTML = '<p><b>' + (ok ? 'Correct.' : 'Not quite.') + '</b> ' + rich(q.why) + '</p>' + (!ok && q.wrong && q.wrong[i] ? '<p>' + rich(q.wrong[i]) + '</p>' : '');
    why.hidden = false; nextB.disabled = false; nextB.focus({preventScroll: true});
    rate(id, ok);
  }
  body.append(ul, why);
  const foot = el('div', 'dfoot'); foot.append(el('span', 'k', narrow() ? '' : 'Keys A–D or 1–4 · Enter for next'));
  const last = D.at === D.list.length - 1;
  const nextB = el('button', 'dbtn', last ? 'Done' : 'Next question'); nextB.type = 'button'; nextB.disabled = true;
  nextB.onclick = () => { if (last) { toast(D.right + ' of ' + D.list.length + ' right. ' + (D.mode === 'review' ? 'Reviews done.' : 'They will come back for review.')); closeDrawer(); } else { D.at++; renderDrawer(); } };
  foot.append(nextB);
  box.append(head, body, foot);
  $('rightPage').append(box);
  (btns[0] || x).focus({preventScroll: true});
  S.keys = {pick: pos => { if (pos < ord.length) pick(ord[pos]); }, next: () => { if (!nextB.disabled) nextB.click(); }};
}
$('practiceBtn').onclick = () => { if (S.drawer) closeDrawer(); else openPractice(); };

/* ============ search, pages panel ============ */
function closeModal(){ const m = $('modal'); if (!m) return false; m.remove(); if (S.modalReturn && S.modalReturn.focus) S.modalReturn.focus({preventScroll: true}); S.modalReturn = null; return true; }
function modal(label){
  closeModal(); S.modalReturn = document.activeElement;
  const sc = el('div', 'scrim'); sc.id = 'modal';
  const box = el('div', 'modal'); box.setAttribute('role', 'dialog'); box.setAttribute('aria-modal', 'true'); box.setAttribute('aria-label', label);
  sc.append(box); sc.addEventListener('mousedown', e => { if (e.target === sc) closeModal(); });
  box.addEventListener('keydown', e => { if (e.key !== 'Tab') return; const f = [...box.querySelectorAll('button:not([disabled]), input, a[href]')].filter(n => n.offsetParent !== null); if (!f.length) return; const a = f[0], z = f[f.length - 1]; if (e.shiftKey && document.activeElement === a) { e.preventDefault(); z.focus(); } else if (!e.shiftKey && document.activeElement === z) { e.preventDefault(); a.focus(); } });
  document.body.append(sc); return box;
}
const fold = t => String(t).toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
function openSearch(){
  const box = modal('Search the book');
  const head = el('div', 'mhead'); const inp = el('input'); inp.type = 'search'; inp.placeholder = 'Search: a person, a place, a war, an idea'; inp.setAttribute('aria-label', 'Search the book'); inp.autocomplete = 'off';
  const x = el('button', 'mx', 'Esc'); x.type = 'button'; x.onclick = closeModal; head.append(inp, x);
  const body = el('div', 'mbody'); body.setAttribute('role', 'listbox');
  box.append(head, body); inp.focus();
  let sel = 0, hits = [];
  const draw = () => {
    const q = fold(inp.value.trim());
    if (!S.search) { body.innerHTML = '<div class="mnote">Loading the index…</div>'; return; }
    if (q.length < 2) { body.innerHTML = '<div class="mnote">Type at least two letters. Results come from page titles and text across both volumes.</div>'; hits = []; return; }
    const ALIAS = {ww1: 'first world war', wwi: 'first world war', ww2: 'second world war', wwii: 'second world war', mlk: 'martin luther king', jfk: 'kennedy', fdr: 'roosevelt', lbj: 'johnson', genghis: 'chinggis', usa: 'united states', us: 'united states', uk: 'britain', ussr: 'soviet'};
    const terms = q.split(/\s+/).filter(Boolean).map(t => (has(ALIAS, t) ? ALIAS[t] : t)).join(' ').split(/\s+/);
    const starts = (hay, t) => { let at = hay.indexOf(t); while (at >= 0) { if (at === 0 || !/[a-z0-9]/.test(hay[at - 1])) return true; at = hay.indexOf(t, at + 1); } return false; };
    hits = [];
    for (const r of S.search) {
      if (!r.f) r.f = {t: fold(r.t), s: fold(r.s), x: fold(r.x)};
      let sc = 0, ok = true;
      for (const t of terms) {
        const inT = starts(r.f.t, t), inS = starts(r.f.s, t), inX = starts(r.f.x, t);
        if (!inT && !inS && !inX) { ok = false; break; }
        sc += (inT ? 12 : 0) + (inS ? 4 : 0) + (inX ? Math.min(6, r.f.x.split(' ' + t).length) : 0);
      }
      if (ok) hits.push([sc, r]);
    }
    hits.sort((a, b) => b[0] - a[0]); const totalHits = hits.length; hits = hits.slice(0, 40).map(h => h[1]); sel = 0;
    if (!hits.length) { body.innerHTML = '<div class="mnote">No page mentions that. Try a different spelling or a broader word.</div>'; return; }
    const re = new RegExp('(?<![A-Za-z0-9])(' + terms.map(t => t.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')).join('|') + ')', 'gi');
    const mark = t => String(t).split(re).map((part, k) => k % 2 ? '<mark>' + esc(part) + '</mark>' : esc(part)).join('');
    body.replaceChildren(...hits.map((r, k) => {
      const at = r.f.x.indexOf(terms[0]); const from = Math.max(0, at - 70);
      const snip = at < 0 ? r.x.slice(0, 150) + (r.x.length > 150 ? '…' : '') : (from ? '…' : '') + r.x.slice(from, from + 170) + (from + 170 < r.x.length ? '…' : '');
      const b = el('button', 'hit-row' + (k === 0 ? ' sel' : ''), '<span class="k">' + esc(r.k) + ' · ' + esc(S.index[r.c].title) + '</span><span class="t">' + mark(r.t) + '</span><span class="x">' + mark(snip) + '</span>');
      b.type = 'button'; b.setAttribute('role', 'option'); b.onclick = () => openHit(r); return b;
    }));
    if (totalHits > hits.length) body.append(el('div', 'mnote', 'Showing the best 40 of ' + totalHits + ' pages. Add a word to narrow the search.'));
  };
  const openHit = r => { closeModal(); nav(r.c + (r.p ? '-' + r.p : '')); };
  const move = d => { const rows = body.querySelectorAll('.hit-row'); if (!rows.length) return; rows[sel].classList.remove('sel'); sel = (sel + d + rows.length) % rows.length; rows[sel].classList.add('sel'); rows[sel].scrollIntoView({block: 'nearest'}); };
  inp.addEventListener('input', draw);
  inp.addEventListener('keydown', e => {
    if (e.key === 'ArrowDown') { e.preventDefault(); move(1); } else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
    else if (e.key === 'Enter' && hits[sel]) { e.preventDefault(); openHit(hits[sel]); }
  });
  draw();
  if (!S.search) { (S.searchP = S.searchP || getJSON('content/search.json')).then(d => { S.search = d; if ($('modal')) draw(); }).catch(() => { S.searchP = null; body.innerHTML = '<div class="mnote">The search index did not load. Check your connection and try again.</div>'; }); }
}
function openToc(){
  const X = S.index[S.ch]; if (!X) return;
  const box = modal('Pages in this chapter');
  const head = el('div', 'mhead'); head.append(el('span', 'kicker', 'Pages in this chapter')); const x = el('button', 'mx', 'Close'); x.type = 'button'; x.onclick = closeModal; x.style.marginLeft = 'auto'; head.append(x);
  const body = el('div', 'mbody');
  body.append(el('div', 'toc-ch', '<small>No. ' + esc(X.no) + ' · ' + X.pages.length + ' pages</small>' + esc(X.title)));
  X.pages.forEach((p, i) => {
    const b = el('button', 'toc-row', '<span class="k">' + esc(pageKey(S.ch, i)) + '</span><span>' + esc(p.t) + '</span>' + (S.read[S.ch + '.' + i] ? '<span class="rd">read</span>' : ''));
    b.type = 'button'; b.setAttribute('aria-current', String(i === S.page)); b.onclick = () => { closeModal(); go(i); }; body.append(b);
  });
  const L = chapterList(), at = L.findIndex(c => c.id === S.ch), foot = el('div', 'toc-nav');
  const mk = (c, lab) => { const b = el('button', null, c ? esc(lab) + '<br><span style="text-transform:none;letter-spacing:0;font:15px/1.3 var(--text)">' + esc(S.index[c.id].title) + '</span>' : ''); b.type = 'button'; b.disabled = !c; if (c) b.onclick = () => { closeModal(); nav(c.id); }; return b; };
  foot.append(mk(L[at - 1], '← Previous chapter'), mk(L[at + 1], 'Next chapter →'));
  box.append(head, body, foot);
  const cur = body.querySelector('[aria-current="true"]'); if (cur) { cur.focus({preventScroll: true}); cur.scrollIntoView({block: 'center'}); }
}

/* ============ about ============ */
function showAbout(){
  showView('about'); setHash('about'); document.title = 'About · ' + SITE.name;
  const repo = SITE.repo ? '<a href="' + esc(SITE.repo) + '" target="_blank" rel="noopener">GitHub</a>' : 'GitHub';
  $('about').innerHTML = `
<div class="kicker" style="margin-top:20px">About</div>
<h1>Learn the World</h1>
<p class="lede">A free, open history of the world and of the United States, written to be read a page a day and remembered.</p>
<p>Created and edited by <b>Carter Friese</b> · <a href="https://github.com/cfriese04" target="_blank" rel="noopener">@cfriese04 on GitHub</a> · <a href="https://x.com/carter_friese" target="_blank" rel="noopener">@carter_friese on X</a></p>
<p>Volume I, <i>The World</i>, runs in sixteen chapters from the first humans to the present. Volume II, <i>The United States</i>, runs in eight chapters from the first colonies to November 2026, with a chapter on how the Constitution works. Each page makes one argument in a few paragraphs, with a map or chart beside it and two practice questions at the end.</p>

<h2>How to use it</h2>
<dl>
<dt>Read</dt><dd>Open any chapter from the contents, or search. Turn pages with the arrows, the arrow keys, or a swipe on the map. <b>Pages</b> in the top bar lists every page in the chapter.</dd>
<dt>Check the evidence</dt><dd>The small labels after sentences say what kind of claim it is: <b>consensus</b> (historians agree), <b>approx.</b> (a number or date with real uncertainty), <b>debated</b> (scholars disagree, and both sides are named) or <b>tradition</b> (what a tradition reports, not established fact). Click one to read the claim, a note on the uncertainty, and links to the sources.</dd>
<dt>Explore the figure</dt><dd>Click a highlighted place on a map, or a highlighted bar on a chart, to open a short plate about it.</dd>
<dt>Practise and review</dt><dd>Two questions end each page. Every wrong answer is explained too. Questions you answer come back later on a spaced-repetition schedule: after a day, then three days, then at growing intervals, and sooner if you got them wrong. <b>Review</b> shows what is due.</dd>
<dt>Share</dt><dd>Every page has its own link. Use <b>Share</b> at the foot of a page to copy it.</dd>
</dl>

<h2>How it was made, and how far to trust it</h2>
<p>Carter Friese planned and edited the book and set its standards. It was researched, written and fact-checked with Claude, an AI model made by Anthropic, working from published sources under his direction. Every factual sentence is tied to a claim, and every claim names the sources it rests on, with links, so that you can check it yourself. Each chapter went through the same steps: research from sources that were opened and quoted; writing only from that research; two independent fact-checks of every page against the sources; corrections; and a second reader who checked every correction again. Quotations are given in the words of the source, and a historian's words appear in quotation marks only when they are the historian's own.</p>
<p>That process catches most errors, not all. Where historians disagree, the book says so and names both sides; it tries to describe each side in its strongest form rather than to decide between them. Legal and political statuses are dated, as of 2 November 2026; the midterm elections of 3 November 2026 are not covered.</p>
<p><b>Found a mistake?</b> ${SITE.repo ? 'Please <a href="' + esc(reportURL('the site')) + '" target="_blank" rel="noopener">open an issue on GitHub</a> (each page also has its own report link), ideally with a link to a source.' : 'Please report it on the project’s GitHub page, ideally with a link to a source.'}</p>

<h2>Your progress</h2>
<p>What you have read and your practice history are stored in this browser only. Nothing is sent anywhere. To move them to another device, or keep a copy, back them up here.</p>
<div class="btns"><button class="dbtn ghost" type="button" id="bkExport">Back up my progress</button><button class="dbtn ghost" type="button" id="bkImport">Restore from a backup</button><input type="file" id="bkFile" accept="application/json,.json" hidden><button class="dbtn ghost" type="button" id="bkClear">Clear my progress</button></div>

<h2>Open source</h2>
<p>The whole book, including every claim and its sources and the scripts that build the pages, is open on ${repo}. The text is licensed under <a href="https://creativecommons.org/licenses/by/4.0/" target="_blank" rel="noopener">Creative Commons Attribution 4.0</a>: you may copy, adapt and share it, including commercially, with credit to <i>Learn the World</i> by Carter Friese. The code is under the MIT License. Quotations from other works remain their authors' and publishers' and are not covered by these licenses.</p>

<h2>Credits and permissions</h2>
<p class="notice">Scripture quotations marked NRSVUE are taken from the New Revised Standard Version Updated Edition. Copyright © 2021 National Council of the Churches of Christ in the United States of America. Used by permission. All rights reserved worldwide.</p>
<p class="notice">Scripture quotations marked RSV are from the Revised Standard Version of the Bible, copyright © 1946, 1952, and 1971 the National Council of the Churches of Christ in the United States of America. Used by permission. All rights reserved worldwide.</p>
<p class="notice">Quotations from the Qur'an are from <i>The Qur'an</i>, translated by M. A. S. Abdel Haleem (Oxford University Press), quoted briefly with attribution. A quotation from the Hebrew Bible in Chapter 3 is from the Jewish Publication Society translation, via Sefaria.</p>
<p class="notice">Maps are drawn from Natural Earth data (public domain), prepared as TopoJSON by the sane-topojson project (MIT License), with d3 (ISC License). Fonts: Libre Caslon Display, Source Serif 4, IBM Plex Mono and IM Fell English, under the SIL Open Font License. All of these are served from this site itself; it loads nothing from other servers and collects no data about you.</p>
`;
  $('about').insertAdjacentHTML('beforeend', '<footer class="sitefoot">' + footHTML() + '</footer>');
  $('bkExport').onclick = exportProgress; $('bkImport').onclick = () => $('bkFile').click(); $('bkFile').onchange = importProgress;
  const clr = $('bkClear'); clr.onclick = () => { if (clr.dataset.sure) { clearProgress(); clr.textContent = 'Cleared'; clr.disabled = true; } else { clr.dataset.sure = '1'; clr.textContent = 'Click again to clear everything'; } };
  scrollTo(0, 0);
}
async function exportProgress(){
  const data = {app: 'learn-the-world', version: 1, saved: new Date().toISOString(), progress: {read: S.read, last: S.last}, cards: S.cards};
  const blob = new Blob([JSON.stringify(data)], {type: 'application/json'});
  const a = el('a'); a.href = URL.createObjectURL(blob); a.download = 'learn-the-world-progress-' + new Date().toISOString().slice(0, 10) + '.json'; document.body.append(a); a.click(); a.remove();
  setTimeout(() => URL.revokeObjectURL(a.href), 4000); toast('Backup saved to your downloads.');
}
async function importProgress(e){
  const f = e.target.files && e.target.files[0]; if (!f) return; if (f.size > 5e6) { toast('That file is too large to be a Learn the World backup.'); e.target.value = ''; return; }
  try {
    const d = JSON.parse(await f.text()); if (!d || d.app !== 'learn-the-world' || !d.progress) throw new Error('not a backup');
    Object.assign(S.read, cleanRead(d.progress.read)); if (okLast(d.progress.last)) S.last = {ch: d.progress.last.ch, page: d.progress.last.page}; saveProgress();
    Object.entries(d.cards && typeof d.cards === 'object' ? d.cards : {}).forEach(([id, r]) => { if (okCard(id, r)) { S.cards[id] = cleanCard(r); store.set('cards/' + id, S.cards[id]); } });
    const need = [...new Set(Object.keys(S.cards).map(id => id.split('.')[0]))].filter(id => S.index[id]);
    await Promise.all(need.map(ensureChapter)); updateDue();
    toast('Progress restored.'); const clr = $('bkClear'); if (clr) { clr.disabled = false; clr.textContent = 'Clear my progress'; delete clr.dataset.sure; }
  } catch (err) { toast('That file is not a Learn the World backup.'); }
  e.target.value = '';
}
function clearProgress(){
  S.read = {}; S.last = null; saveProgress();
  Object.keys(S.cards).forEach(id => store.set('cards/' + id, {cleared: true})); S.cards = {}; updateDue();
  toast('Progress cleared.');
}

/* ============ keyboard and swipe ============ */
document.addEventListener('keydown', e => {
  const typing = /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName || '');
  if ($('modal')) { if (e.key === 'Escape') { e.preventDefault(); closeModal(); } return; }
  if ((e.key === '/' && !typing && !e.metaKey && !e.ctrlKey && !e.altKey) || ((e.metaKey || e.ctrlKey) && (e.key === 'k' || e.key === 'K'))) { e.preventDefault(); openSearch(); return; }
  if (e.metaKey || e.ctrlKey || e.altKey || S.mode !== 'book' || typing) return;
  if (e.key === 'Escape') { if (closePop()) { return; } if ($('plate')) closePlate(); else if (S.drawer) closeDrawer(); return; }
  if (S.drawer && S.keys) {
    const k = e.key.toUpperCase(); const map = {A: 0, B: 1, C: 2, D: 3, '1': 0, '2': 1, '3': 2, '4': 3};
    if (k in map) { e.preventDefault(); S.keys.pick(map[k]); return; }
    if (e.key === 'Enter' && !(e.target.closest && e.target.closest('button, a, input, [tabindex]'))) { e.preventDefault(); S.keys.next(); return; }
    if (S.drawer.mode === 'review' && /^(Arrow|Page)/.test(e.key)) return;
  }
  if (e.key === 'ArrowRight' || e.key === 'PageDown') { e.preventDefault(); go(S.page + 1); }
  if (e.key === 'ArrowLeft' || e.key === 'PageUp') { e.preventDefault(); go(S.page - 1); }
  if ((e.key === 'p' || e.key === 'P') && !S.drawer) openPractice();
});
let tx = null, ty = null; $('rightPage').addEventListener('touchstart', e => { if (e.target.closest('#drawer, .hc')) { tx = null; return; } tx = e.touches[0].clientX; ty = e.touches[0].clientY; }, {passive: true});
$('rightPage').addEventListener('touchend', e => { if (tx == null || S.mode !== 'book' || S.drawer) { tx = null; return; } const dx = e.changedTouches[0].clientX - tx, dy = e.changedTouches[0].clientY - ty; if (Math.abs(dx) > 60 && Math.abs(dx) > 2 * Math.abs(dy)) go(S.page + (dx < 0 ? 1 : -1)); tx = null; });
matchMedia('(prefers-color-scheme: dark)').addEventListener('change', () => { FIG._pat = null; FIG.redraw(); });
new MutationObserver(() => { FIG._pat = null; FIG.redraw(); }).observe(document.documentElement, {attributes: true, attributeFilter: ['data-theme']});

boot();
})();
