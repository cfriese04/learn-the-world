# Learn the World

A free, open history of the world and of the United States, written to be read a page a day and remembered.

Created and edited by **Carter Friese** · GitHub [@cfriese04](https://github.com/cfriese04) · X [@carter_friese](https://x.com/carter_friese)

**Read it online:** https://cfriese04.github.io/learn-the-world/

- **Volume I, The World**: 16 chapters, from the first humans to the present.
- **Volume II, The United States**: 8 chapters, from the first colonies to November 2026, including a chapter on how the Constitution works.

Each page makes one argument in a few paragraphs, with a map or chart beside it and two practice questions at the end. Every factual sentence is tied to a claim, and every claim names its sources with links. The questions you answer come back for review on a spaced-repetition schedule: after a day, then three days, then at growing intervals.

## How to read it

- **Read**: open a chapter from the contents, or search. Turn pages with the arrows, the arrow keys, or a swipe. **Pages** in the top bar lists every page in a chapter. Press `/` to search.
- **Check the evidence**: the small labels after a sentence say what kind of claim it is. **Consensus** means historians agree. **Approx.** marks a number or date with real uncertainty. **Debated** means scholars disagree, and both sides are named. **Tradition** marks what a tradition reports rather than established fact. Click a label to see the claim, a note on its uncertainty, and links to its sources.
- **Practise and review**: answer the two questions at the end of a page. They come back later, sooner if you got them wrong.

Progress is stored in your browser only. You can back it up and restore it from the About page.

## How it was made

Carter Friese planned and edited the book and set its standards. It was researched, written and fact-checked with Claude, an AI model made by Anthropic, working from published sources under his direction. Each chapter went through these steps:

1. Research from sources that were opened and quoted.
2. Writing only from that research.
3. Two independent fact-checks of every page against the sources.
4. Corrections.
5. A second reader who checked every correction again.

That process catches most errors, not all. If you find one, please [open an issue](../../issues/new) and include a link to a source if you can.

Legal and political statuses are dated as of 2 November 2026. The midterm elections of 3 November 2026 are not covered.

## Running it locally

The site is a single `index.html` that loads its chapters from `content/`. Browsers block those loads from a `file://` page, so serve the folder:

```sh
python3 -m http.server 8000
# then open http://localhost:8000
```

Everything the page needs is in this repository: d3 (`vendor/`), the Natural Earth world map as TopoJSON (`vendor/`) and the fonts (`fonts/`). The site loads nothing from other servers, sets no cookies and collects no data.

## Layout

```
index.html            the page and its styles
app.js                the app: maps, charts, practice, review, search
vendor/               d3 7.9.0 and the Natural Earth maps (with their licenses)
fonts/                the fonts, subset to the characters the book uses (with their licenses)
content/library.json  volumes and chapters
content/chNN.json     Volume I chapters (built; do not edit by hand)
content/usNN.json     Volume II chapters (built; do not edit by hand)
content/index.json    chapter and page titles (built by tools/build_index.py)
content/search.json   plain text of every page for search (built by tools/build_index.py)
build/                the chapter sources and the scripts that build content/
tools/build_index.py  builds index.json and search.json
```

## Editing the content

Every chapter is written as Python data in `build/`. For example, `build/us05a.py`, `us05b.py` and `us05c.py` hold Chapter US5. Each file holds three things:

- `S`, the sources: `'id': ("Citation", "https://url")`.
- `C`, the claims: `'c-id': c(text, label, [source ids], note)`. The label is `consensus`, `approx`, `debated` or `tradition`. Every label except consensus needs a note that names the scholars on each side or explains the uncertainty.
- Page dictionaries with `title`, `sub`, `lede`, `body` (paragraphs and a table), `figure` (a map or chart) and `practice` (questions).

In the text, `[[c-id]]` after a sentence links it to the claim that supports it.

To rebuild after an edit:

```sh
cd build
python3 build_us05.py        # or build_chNN.py; Chapter 1 is build.py
cd ..
python3 tools/build_index.py
```

The build refuses missing claims and sources and warns about unused ones. See [CONTRIBUTING.md](CONTRIBUTING.md) for the standards a change must meet.

## Licenses

- **Text and data** (`content/`, `build/` chapter sources): [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/). You may copy, adapt and share it, including commercially, with credit to *Learn the World* by Carter Friese. See [LICENSE-CONTENT.md](LICENSE-CONTENT.md).
- **Code** (`index.html`, `app.js`, build scripts, tools): [MIT](LICENSE). Bundled third-party files in `vendor/` and `fonts/` keep their own licenses, included alongside them.
- **Quotations** from other works remain their authors' and publishers'. These licenses do not cover them.

### Credits and permissions

Scripture quotations marked NRSVUE are taken from the New Revised Standard Version Updated Edition. Copyright © 2021 National Council of the Churches of Christ in the United States of America. Used by permission. All rights reserved worldwide.

Scripture quotations marked RSV are from the Revised Standard Version of the Bible, copyright © 1946, 1952, and 1971 the National Council of the Churches of Christ in the United States of America. Used by permission. All rights reserved worldwide.

Quotations from the Qur'an are from *The Qur'an*, translated by M. A. S. Abdel Haleem (Oxford University Press). They are quoted briefly and with attribution. A quotation from the Hebrew Bible in Chapter 3 is from the Jewish Publication Society translation, via Sefaria.

The maps use Natural Earth data (public domain), prepared as TopoJSON by the sane-topojson project (MIT License), and are drawn with d3 (ISC License). The fonts are Libre Caslon Display, Source Serif 4, IBM Plex Mono and IM Fell English, all under the SIL Open Font License. Their license files are in `vendor/` and `fonts/`.
