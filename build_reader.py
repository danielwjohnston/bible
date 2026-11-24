#!/usr/bin/env python3
"""Compile Open Copyleft Bible Markdown chapters into a single-file offline HTML reader."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)

TESTAMENTS: tuple[tuple[str, str], ...] = (
    ("ot", "Old Testament"),
    ("nt", "New Testament"),
    ("apocrypha", "Deuterocanon / Apocrypha"),
)

CANON_BOOKS: dict[str, list[tuple[str, str]]] = {
    "ot": [
        ("genesis", "Genesis"),
        ("exodus", "Exodus"),
        ("leviticus", "Leviticus"),
        ("numbers", "Numbers"),
        ("deuteronomy", "Deuteronomy"),
        ("joshua", "Joshua"),
        ("judges", "Judges"),
        ("ruth", "Ruth"),
        ("1-samuel", "1 Samuel"),
        ("2-samuel", "2 Samuel"),
        ("1-kings", "1 Kings"),
        ("2-kings", "2 Kings"),
        ("1-chronicles", "1 Chronicles"),
        ("2-chronicles", "2 Chronicles"),
        ("ezra", "Ezra"),
        ("nehemiah", "Nehemiah"),
        ("esther", "Esther"),
        ("job", "Job"),
        ("psalms", "Psalms"),
        ("proverbs", "Proverbs"),
        ("ecclesiastes", "Ecclesiastes"),
        ("song-of-solomon", "Song of Solomon"),
        ("isaiah", "Isaiah"),
        ("jeremiah", "Jeremiah"),
        ("lamentations", "Lamentations"),
        ("ezekiel", "Ezekiel"),
        ("daniel", "Daniel"),
        ("hosea", "Hosea"),
        ("joel", "Joel"),
        ("amos", "Amos"),
        ("obadiah", "Obadiah"),
        ("jonah", "Jonah"),
        ("micah", "Micah"),
        ("nahum", "Nahum"),
        ("habakkuk", "Habakkuk"),
        ("zephaniah", "Zephaniah"),
        ("haggai", "Haggai"),
        ("zechariah", "Zechariah"),
        ("malachi", "Malachi"),
    ],
    "nt": [
        ("matthew", "Matthew"),
        ("mark", "Mark"),
        ("luke", "Luke"),
        ("john", "John"),
        ("acts", "Acts"),
        ("romans", "Romans"),
        ("1-corinthians", "1 Corinthians"),
        ("2-corinthians", "2 Corinthians"),
        ("galatians", "Galatians"),
        ("ephesians", "Ephesians"),
        ("philippians", "Philippians"),
        ("colossians", "Colossians"),
        ("1-thessalonians", "1 Thessalonians"),
        ("2-thessalonians", "2 Thessalonians"),
        ("1-timothy", "1 Timothy"),
        ("2-timothy", "2 Timothy"),
        ("titus", "Titus"),
        ("philemon", "Philemon"),
        ("hebrews", "Hebrews"),
        ("james", "James"),
        ("1-peter", "1 Peter"),
        ("2-peter", "2 Peter"),
        ("1-john", "1 John"),
        ("2-john", "2 John"),
        ("3-john", "3 John"),
        ("jude", "Jude"),
        ("revelation", "Revelation"),
    ],
    "apocrypha": [
        ("tobit", "Tobit"),
        ("judith", "Judith"),
        ("additions-to-esther", "Additions to Esther"),
        ("esther-greek", "Greek Esther"),
        ("wisdom-of-solomon", "Wisdom of Solomon"),
        ("sirach", "Sirach"),
        ("baruch", "Baruch"),
        ("letter-of-jeremiah", "Letter of Jeremiah"),
        ("prayer-of-azariah", "Prayer of Azariah & Song of the Three"),
        ("susanna", "Susanna"),
        ("bel-and-the-dragon", "Bel and the Dragon"),
        ("1-maccabees", "1 Maccabees"),
        ("2-maccabees", "2 Maccabees"),
        ("1-esdras", "1 Esdras"),
        ("2-esdras", "2 Esdras"),
        ("prayer-of-manasseh", "Prayer of Manasseh"),
        ("psalm-151", "Psalm 151"),
        ("3-maccabees", "3 Maccabees"),
        ("4-maccabees", "4 Maccabees"),
    ],
}

BOOK_ORDER_INDEX: dict[tuple[str, str], int] = {
    (testament, slug): idx
    for testament, books in CANON_BOOKS.items()
    for idx, (slug, _) in enumerate(books)
}

BOOK_DISPLAY_NAMES: dict[tuple[str, str], str] = {
    (testament, slug): name
    for testament, books in CANON_BOOKS.items()
    for slug, name in books
}

PHASE2_SECTIONS: tuple[str, ...] = (
    "Word-for-Word",
    "Clear & Faithful",
    "Everyday English",
    "Crossings & Lexical Notes",
    "Supplemental Texts & Allusions",
)


def chapter_sort_key(md_path: Path) -> tuple[int, int, str]:
    stem = md_path.stem
    if stem.isdigit():
        return (0, int(stem), stem)
    m = re.match(r"^(\d+)", stem)
    if m:
        return (0, int(m.group(1)), stem)
    return (1, 0, stem)


def extract_provenance(header_block: str) -> str:
    lines: list[str] = []
    for raw in header_block.splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or line == "---":
            continue
        if line.startswith("*") and line.endswith("*") and len(line) >= 2:
            line = line[1:-1].strip()
        if line:
            lines.append(line)
    return " ".join(lines)


def parse_chapter(md_path: Path, testament: str) -> dict:
    text = md_path.read_text(encoding="utf-8")
    book_slug = md_path.parent.name
    display_name = BOOK_DISPLAY_NAMES.get(
        (testament, book_slug),
        book_slug.replace("-", " ").title(),
    )

    title_m = re.match(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else f"{display_name} {md_path.stem}"

    parts = re.split(r"^##\s+(.+)$", text, flags=re.MULTILINE)
    provenance = extract_provenance(parts[0]) if parts else ""

    sections: dict[str, str] = {}
    for i in range(1, len(parts), 2):
        sec_name = parts[i].strip()
        sec_body = re.sub(r"\n+---\s*$", "", parts[i + 1].strip()).strip()
        sections[sec_name] = sec_body

    status = (
        "original-cc-by-sa"
        if all(sec in sections for sec in PHASE2_SECTIONS)
        else "provisional-pd"
    )
    chapter_label = "Prologue" if md_path.stem == "00" else (md_path.stem.lstrip("0") or "0")

    return {
        "id": f"{book_slug}-{md_path.stem}",
        "testament": testament,
        "book_slug": book_slug,
        "book": display_name,
        "chapter": chapter_label,
        "stem": md_path.stem,
        "title": title,
        "provenance": provenance,
        "status": status,
        "sections": sections,
    }


def collect_chapters() -> list[dict]:
    chapters: list[dict] = []
    for testament, _ in TESTAMENTS:
        t_dir = ROOT / testament
        if not t_dir.is_dir():
            continue
        book_dirs = sorted(
            (d for d in t_dir.iterdir() if d.is_dir()),
            key=lambda d: (
                0 if (testament, d.name) in BOOK_ORDER_INDEX else 1,
                BOOK_ORDER_INDEX.get((testament, d.name), 0),
                d.name,
            ),
        )
        for book_dir in book_dirs:
            for md_file in sorted(book_dir.glob("*.md"), key=chapter_sort_key):
                chapters.append(parse_chapter(md_file, testament))
    return chapters


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Open Copyleft Bible — Offline reader for original CC BY-SA 4.0 translations and provisional Public Domain base chapters.">
<title>Open Copyleft Bible — Offline Reader</title>
<style>
  :root {
    --bg: #000000;
    --bg-card: #0c0c0c;
    --bg-elev: #121712;
    --line: #1f3a1f;
    --ink: #00ff00;
    --ink-dim: #77cc77;
    --ink-bright: #ffffff;
    --warn: #ffd700;
    --pd: #7cc4ff;
    --display: 'Impact', 'Arial Narrow Bold', sans-serif;
    --body: system-ui, -apple-system, 'Segoe UI', Roboto, sans-serif;
    --mono: ui-monospace, 'SFMono-Regular', Menlo, monospace;
  }
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body {
    background: var(--bg);
    color: var(--ink-bright);
    font-family: var(--body);
    line-height: 1.65;
    display: grid;
    grid-template-columns: 310px 1fr;
    min-height: 100vh;
  }
  nav {
    border-right: 1px solid var(--line);
    padding: 18px;
    background: var(--bg-card);
    display: flex;
    flex-direction: column;
    gap: 14px;
    max-height: 100vh;
    position: sticky;
    top: 0;
  }
  nav h1 {
    font-family: var(--display);
    color: var(--ink);
    font-size: 1.35rem;
    letter-spacing: 0.08em;
  }
  nav .license {
    font-family: var(--mono);
    font-size: 0.72rem;
    color: var(--ink-dim);
    line-height: 1.45;
  }
  .testament-tabs {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }
  .testament-tabs button {
    flex: 1 1 auto;
    background: var(--bg);
    color: var(--ink-dim);
    border: 1px solid var(--line);
    padding: 6px 8px;
    cursor: pointer;
    font-family: var(--mono);
    font-size: 0.75rem;
    text-align: center;
  }
  .testament-tabs button.active {
    border-color: var(--ink);
    color: var(--bg);
    background: var(--ink);
    font-weight: bold;
  }
  .nav-selects {
    display: grid;
    gap: 8px;
  }
  .nav-selects label {
    display: grid;
    gap: 4px;
    font-family: var(--mono);
    font-size: 0.72rem;
    color: var(--ink-dim);
  }
  .nav-selects select {
    width: 100%;
    background: var(--bg);
    color: var(--ink-bright);
    border: 1px solid var(--line);
    padding: 6px 8px;
    font-family: var(--mono);
    font-size: 0.82rem;
  }
  .book-list {
    overflow-y: auto;
    border-top: 1px solid var(--line);
    border-bottom: 1px solid var(--line);
    padding: 8px 0;
    flex: 1 1 auto;
  }
  .book-list button {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 8px;
    width: 100%;
    text-align: left;
    background: transparent;
    color: var(--ink-dim);
    border: 1px solid transparent;
    padding: 6px 8px;
    cursor: pointer;
    font-family: var(--mono);
    font-size: 0.8rem;
  }
  .book-list button:hover, .book-list button.active {
    border-color: var(--ink);
    color: var(--ink);
    background: rgba(0, 255, 0, 0.08);
  }
  .book-meta {
    font-size: 0.68rem;
    color: var(--warn);
    white-space: nowrap;
  }
  .book-meta.cc { color: var(--ink); }
  .book-meta.pd { color: var(--pd); }
  .chapter-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(42px, 1fr));
    gap: 4px;
    max-height: 180px;
    overflow-y: auto;
    padding-right: 2px;
  }
  .chapter-grid button {
    background: var(--bg);
    color: var(--ink-dim);
    border: 1px solid var(--line);
    padding: 4px 2px;
    cursor: pointer;
    font-family: var(--mono);
    font-size: 0.75rem;
    text-align: center;
  }
  .chapter-grid button.orig {
    border-color: #2f6f2f;
  }
  .chapter-grid button:hover, .chapter-grid button.active {
    border-color: var(--ink);
    color: var(--bg);
    background: var(--ink);
    font-weight: bold;
  }
  main {
    padding: 28px 40px 48px;
    max-width: 920px;
    width: 100%;
  }
  .toolbar {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
    margin-bottom: 20px;
    padding-bottom: 14px;
    border-bottom: 1px solid var(--line);
  }
  .reg-buttons, .pager-buttons {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
  }
  .toolbar button {
    background: var(--bg-card);
    color: var(--ink-dim);
    border: 1px solid var(--line);
    padding: 6px 12px;
    cursor: pointer;
    font-family: var(--mono);
    font-size: 0.82rem;
  }
  .toolbar button.active {
    border-color: var(--ink);
    color: var(--bg);
    background: var(--ink);
    font-weight: bold;
  }
  .toolbar button:disabled {
    opacity: 0.35;
    cursor: not-allowed;
  }
  .chapter-header {
    margin-bottom: 18px;
  }
  .chapter-header h2 {
    font-family: var(--display);
    color: var(--ink);
    font-size: 2rem;
    letter-spacing: 0.04em;
    margin-bottom: 8px;
  }
  .status-badge {
    display: inline-block;
    font-family: var(--mono);
    font-size: 0.75rem;
    padding: 3px 8px;
    border: 1px solid var(--line);
    margin-bottom: 8px;
  }
  .status-badge.cc {
    color: var(--ink);
    border-color: var(--ink);
    background: rgba(0, 255, 0, 0.08);
  }
  .status-badge.pd {
    color: var(--pd);
    border-color: var(--pd);
    background: rgba(124, 196, 255, 0.08);
  }
  .provenance-line {
    font-size: 0.86rem;
    color: var(--ink-dim);
    font-style: italic;
  }
  .provisional-notice {
    margin: 14px 0 18px;
    padding: 10px 14px;
    border-left: 3px solid var(--pd);
    background: var(--bg-elev);
    color: var(--ink-dim);
    font-size: 0.88rem;
  }
  .verse-block p { margin-bottom: 10px; }
  .verse-block strong { color: var(--ink); font-family: var(--mono); }
  .verse-block em { color: var(--warn); }
  .notes {
    margin-top: 30px;
    padding-top: 18px;
    border-top: 1px solid var(--line);
  }
  .notes h3 {
    color: var(--warn);
    font-family: var(--mono);
    font-size: 1rem;
    margin: 16px 0 8px;
  }
  .notes li { margin-left: 20px; margin-bottom: 6px; color: var(--ink-dim); }
  .notes code, .verse-block code {
    font-family: var(--mono);
    color: var(--ink-bright);
    background: var(--bg-elev);
    padding: 1px 4px;
    border: 1px solid var(--line);
  }
  .bottom-pager {
    margin-top: 28px;
    padding-top: 16px;
    border-top: 1px solid var(--line);
    display: flex;
    justify-content: space-between;
    gap: 12px;
  }
  .bottom-pager button {
    background: var(--bg-card);
    color: var(--ink-dim);
    border: 1px solid var(--line);
    padding: 7px 14px;
    cursor: pointer;
    font-family: var(--mono);
    font-size: 0.82rem;
  }
  .bottom-pager button:disabled {
    opacity: 0.35;
    cursor: not-allowed;
  }
  .site-footer {
    margin-top: 28px;
    padding-top: 14px;
    border-top: 1px solid var(--line);
    font-family: var(--mono);
    font-size: 0.74rem;
    color: var(--ink-dim);
    line-height: 1.5;
  }
  @media (max-width: 860px) {
    body { grid-template-columns: 1fr; }
    nav {
      position: static;
      max-height: none;
      border-right: none;
      border-bottom: 1px solid var(--line);
    }
    main { padding: 20px; }
  }
</style>
</head>
<body>
<nav>
  <div>
    <h1>OPEN COPYLEFT BIBLE</h1>
    <div class="license" id="corpus-license"></div>
  </div>
  <div class="testament-tabs" id="testament-tabs"></div>
  <div class="nav-selects">
    <label>Book
      <select id="book-select" aria-label="Book"></select>
    </label>
    <label>Chapter
      <select id="chapter-select" aria-label="Chapter"></select>
    </label>
  </div>
  <div class="book-list" id="book-list"></div>
  <div class="chapter-grid" id="chapter-grid"></div>
</nav>
<main>
  <div class="toolbar">
    <div class="reg-buttons" id="register-bar">
      <button data-reg="Word-for-Word">Word-for-Word</button>
      <button data-reg="Clear &amp; Faithful" class="active">Clear &amp; Faithful</button>
      <button data-reg="Everyday English">Everyday English</button>
    </div>
    <div class="pager-buttons">
      <button id="prev-btn" type="button">&larr; Prev</button>
      <button id="next-btn" type="button">Next &rarr;</button>
    </div>
  </div>
  <div id="content"></div>
  <div class="bottom-pager">
    <button id="prev-btn-bottom" type="button">&larr; Prev Chapter</button>
    <button id="next-btn-bottom" type="button">Next Chapter &rarr;</button>
  </div>
  <footer class="site-footer" id="site-footer"></footer>
</main>
<script>
const CHAPTERS = __CHAPTERS_JSON__;
const TESTAMENT_NAMES = {
  ot: 'Old Testament',
  nt: 'New Testament',
  apocrypha: 'Deuterocanon / Apocrypha'
};

const BOOKS = [];
const BOOK_MAP = Object.create(null);
const HASH_MAP = Object.create(null);
let origCount = 0;
let pdCount = 0;

CHAPTERS.forEach((ch, idx) => {
  if (ch.status === 'original-cc-by-sa') origCount += 1;
  else pdCount += 1;

  const bookKey = ch.testament + ':' + ch.book_slug;
  let b = BOOK_MAP[bookKey];
  if (!b) {
    b = {
      key: bookKey,
      testament: ch.testament,
      slug: ch.book_slug,
      name: ch.book,
      chapters: [],
      origCount: 0,
      pdCount: 0
    };
    BOOK_MAP[bookKey] = b;
    BOOKS.push(b);
  }
  b.chapters.push({ idx: idx, ch: ch });
  if (ch.status === 'original-cc-by-sa') b.origCount += 1;
  else b.pdCount += 1;

  const exactHash = '#' + ch.book_slug + '-' + ch.stem;
  HASH_MAP[exactHash] = idx;
  const shortAlias = '#' + ch.book_slug + '-' + String(ch.chapter).toLowerCase();
  if (!(shortAlias in HASH_MAP)) HASH_MAP[shortAlias] = idx;
});

const ACTIVE_TESTAMENTS = ['ot', 'nt', 'apocrypha'].filter(t =>
  BOOKS.some(b => b.testament === t)
);

let currentIdx = 0;
let currentReg = 'Clear & Faithful';
let renderedTestament = null;
let renderedBookKey = null;

function escapeHtml(s) {
  return String(s)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#39;');
}

function formatInline(raw) {
  const codeTokens = [];
  let s = escapeHtml(raw).replace(/`([^`]+)`/g, (_, inner) => {
    const token = '\\u0000CODE' + codeTokens.length + '\\u0000';
    codeTokens.push('<code>' + inner + '</code>');
    return token;
  });
  s = s.replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>');
  s = s.replace(/\\*(.+?)\\*/g, '<em>$1</em>');
  return s.replace(/\\u0000CODE(\\d+)\\u0000/g, (_, idx) => codeTokens[Number(idx)]);
}

function mdToHtml(md) {
  if (!md) return '';
  const lines = String(md).split(/\\r?\\n+/);
  const out = [];
  let inList = false;

  for (const raw of lines) {
    const trimmed = raw.trim();
    if (!trimmed || trimmed === '---') {
      if (inList) {
        out.push('</ul>');
        inList = false;
      }
      continue;
    }
    if (trimmed.startsWith('- ')) {
      if (!inList) {
        out.push('<ul>');
        inList = true;
      }
      out.push('<li>' + formatInline(trimmed.slice(2)) + '</li>');
    } else {
      if (inList) {
        out.push('</ul>');
        inList = false;
      }
      out.push('<p>' + formatInline(trimmed) + '</p>');
    }
  }
  if (inList) out.push('</ul>');
  return out.join('\\n');
}

function renderCorpusNotices() {
  document.getElementById('corpus-license').textContent =
    'OFFLINE READER · ' + CHAPTERS.length + ' CHS | Original CC BY-SA 4.0: ' +
    origCount + ' · Provisional PD Base: ' + pdCount;

  document.getElementById('site-footer').textContent =
    'Mixed-License Corpus Notice: Original multi-register translations (' + origCount +
    ' chapters) are licensed under CC BY-SA 4.0. Provisional Phase 1 base-layer chapters (' +
    pdCount + ' chapters) preserve unmodified Public Domain text from the World English Bible Updated (engwebu, eBible.org) pending Phase 2 original-language translation.';
}

function renderTestamentTabs(activeTestament) {
  const container = document.getElementById('testament-tabs');
  container.innerHTML = ACTIVE_TESTAMENTS.map(t =>
    `<button type="button" data-testament="${escapeHtml(t)}" class="${t === activeTestament ? 'active' : ''}">${escapeHtml(TESTAMENT_NAMES[t] || t.toUpperCase())}</button>`
  ).join('');
  container.querySelectorAll('button').forEach(btn => {
    btn.onclick = () => {
      const firstBook = BOOKS.find(b => b.testament === btn.dataset.testament);
      if (firstBook) selectChapter(firstBook.chapters[0].idx, true);
    };
  });
}

function renderBookNav(activeBook) {
  const tBooks = BOOKS.filter(b => b.testament === activeBook.testament);
  const bookSelect = document.getElementById('book-select');
  bookSelect.innerHTML = tBooks.map(b =>
    `<option value="${escapeHtml(b.key)}">${escapeHtml(b.name)} (${b.chapters.length})</option>`
  ).join('');
  bookSelect.value = activeBook.key;
  bookSelect.onchange = () => {
    const target = BOOK_MAP[bookSelect.value];
    if (target) selectChapter(target.chapters[0].idx, true);
  };

  const bookList = document.getElementById('book-list');
  bookList.innerHTML = tBooks.map(b => {
    let badgeText = 'PD';
    let badgeClass = 'pd';
    if (b.origCount === b.chapters.length) {
      badgeText = 'CC BY-SA';
      badgeClass = 'cc';
    } else if (b.origCount > 0) {
      badgeText = b.origCount + '/' + b.chapters.length + ' CC';
      badgeClass = '';
    }
    return `<button type="button" data-book-key="${escapeHtml(b.key)}" class="${b.key === activeBook.key ? 'active' : ''}">` +
      `<span>${escapeHtml(b.name)}</span>` +
      `<span class="book-meta ${badgeClass}">${escapeHtml(badgeText)} · ${b.chapters.length}</span>` +
      `</button>`;
  }).join('');
  bookList.querySelectorAll('button').forEach(btn => {
    btn.onclick = () => {
      const target = BOOK_MAP[btn.dataset.bookKey];
      if (target) selectChapter(target.chapters[0].idx, true);
    };
  });
}

function renderChapterNav(activeBook, ch) {
  const chSelect = document.getElementById('chapter-select');
  chSelect.innerHTML = activeBook.chapters.map(entry =>
    `<option value="${entry.idx}">${escapeHtml(entry.ch.chapter)}</option>`
  ).join('');
  chSelect.value = String(currentIdx);
  chSelect.onchange = () => selectChapter(Number(chSelect.value), true);

  const grid = document.getElementById('chapter-grid');
  grid.innerHTML = activeBook.chapters.map(entry => {
    const isOrig = entry.ch.status === 'original-cc-by-sa';
    const cls = [
      isOrig ? 'orig' : '',
      entry.idx === currentIdx ? 'active' : ''
    ].filter(Boolean).join(' ');
    const label = entry.ch.chapter === 'Prologue' ? 'Pro' : entry.ch.chapter;
    return `<button type="button" data-idx="${entry.idx}" class="${cls}">${escapeHtml(label)}</button>`;
  }).join('');
  grid.querySelectorAll('button').forEach(btn => {
    btn.onclick = () => selectChapter(Number(btn.dataset.idx), true);
  });
}

function render() {
  if (!CHAPTERS.length) {
    document.getElementById('content').innerHTML = '<p>No chapters compiled.</p>';
    return;
  }

  const ch = CHAPTERS[currentIdx];
  const bookKey = ch.testament + ':' + ch.book_slug;
  const activeBook = BOOK_MAP[bookKey];

  if (renderedTestament !== ch.testament) {
    renderTestamentTabs(ch.testament);
    renderBookNav(activeBook);
    renderedTestament = ch.testament;
  } else {
    document.getElementById('book-select').value = activeBook.key;
    document.querySelectorAll('#book-list button').forEach(btn => {
      btn.classList.toggle('active', btn.dataset.bookKey === activeBook.key);
    });
  }

  if (renderedBookKey !== bookKey) {
    renderChapterNav(activeBook, ch);
    renderedBookKey = bookKey;
  } else {
    document.getElementById('chapter-select').value = String(currentIdx);
    document.querySelectorAll('#chapter-grid button').forEach(btn => {
      btn.classList.toggle('active', Number(btn.dataset.idx) === currentIdx);
    });
  }

  const isOrig = ch.status === 'original-cc-by-sa';
  document.querySelectorAll('#register-bar button').forEach(btn => {
    btn.disabled = !isOrig;
    btn.classList.toggle('active', isOrig && btn.dataset.reg === currentReg);
    btn.onclick = () => {
      if (!isOrig) return;
      currentReg = btn.dataset.reg;
      render();
    };
  });

  const atStart = currentIdx <= 0;
  const atEnd = currentIdx >= CHAPTERS.length - 1;
  ['prev-btn', 'prev-btn-bottom'].forEach(id => {
    const b = document.getElementById(id);
    b.disabled = atStart;
    b.onclick = () => { if (currentIdx > 0) selectChapter(currentIdx - 1, true); };
  });
  ['next-btn', 'next-btn-bottom'].forEach(id => {
    const b = document.getElementById(id);
    b.disabled = atEnd;
    b.onclick = () => { if (currentIdx < CHAPTERS.length - 1) selectChapter(currentIdx + 1, true); };
  });

  const badgeHtml = isOrig
    ? '<div class="status-badge cc">Original · CC BY-SA 4.0</div>'
    : '<div class="status-badge pd">Provisional Base Layer · Public Domain</div>';

  const provHtml = ch.provenance
    ? `<p class="provenance-line">${escapeHtml(ch.provenance)}</p>`
    : '';

  let headingSuffix = '';
  let body = '';
  let noticeHtml = '';
  let notesHtml = '';

  if (isOrig) {
    headingSuffix = ' — ' + currentReg;
    body = ch.sections[currentReg] || '';
    const crossings = ch.sections['Crossings & Lexical Notes'] || '';
    const supp = ch.sections['Supplemental Texts & Allusions'] || '';
    if (crossings || supp) {
      notesHtml = `<div class="notes">
        ${crossings ? `<h3>Crossings &amp; Lexical Notes</h3>${mdToHtml(crossings)}` : ''}
        ${supp ? `<h3>Supplemental Texts &amp; Allusions</h3>${mdToHtml(supp)}` : ''}
      </div>`;
    }
  } else {
    const secKeys = Object.keys(ch.sections);
    const baseKey = secKeys.find(k => k.startsWith('Base Text')) || secKeys[0] || '';
    headingSuffix = baseKey ? ' — Base Text (Provisional PD)' : '';
    body = baseKey ? ch.sections[baseKey] : '';
    noticeHtml = '<div class="provisional-notice">Phase 1 interim base layer: unmodified Public Domain text from World English Bible Updated (<code>engwebu</code>). Register views, lexical notes, and allusions will unlock as this chapter is translated from original languages in Phase 2.</div>';
  }

  document.title = ch.title + ' — Open Copyleft Bible';
  document.getElementById('content').innerHTML = `
    <div class="chapter-header">
      <h2>${escapeHtml(ch.title + headingSuffix)}</h2>
      ${badgeHtml}
      ${provHtml}
    </div>
    ${noticeHtml}
    <div class="verse-block">${mdToHtml(body)}</div>
    ${notesHtml}
  `;
}

function selectChapter(idx, updateHash) {
  if (idx < 0 || idx >= CHAPTERS.length) return;
  currentIdx = idx;
  if (updateHash) {
    const targetHash = '#' + CHAPTERS[idx].book_slug + '-' + CHAPTERS[idx].stem;
    if (window.location.hash !== targetHash) {
      window.location.hash = targetHash;
    }
  }
  render();
  window.scrollTo({ top: 0, behavior: 'auto' });
}

function syncFromHash() {
  const h = window.location.hash.toLowerCase();
  if (h && h in HASH_MAP) {
    const targetIdx = HASH_MAP[h];
    if (targetIdx !== currentIdx) {
      currentIdx = targetIdx;
      render();
      return true;
    }
  }
  return false;
}

window.addEventListener('hashchange', syncFromHash);
renderCorpusNotices();
if (window.location.hash && window.location.hash.toLowerCase() in HASH_MAP) {
  currentIdx = HASH_MAP[window.location.hash.toLowerCase()];
}
render();
</script>
</body>
</html>
"""


def main() -> None:
    chapters = collect_chapters()
    json_payload = json.dumps(chapters, ensure_ascii=False).replace("</", "<\\/")
    out = HTML_TEMPLATE.replace("__CHAPTERS_JSON__", json_payload)
    out_path = DIST / "open-copyleft-bible.html"
    out_path.write_text(out, encoding="utf-8")
    orig = sum(1 for c in chapters if c["status"] == "original-cc-by-sa")
    pd = len(chapters) - orig
    print(f"Built {out_path} ({len(chapters)} chapters: {orig} original-cc-by-sa, {pd} provisional-pd)")


if __name__ == "__main__":
    main()
