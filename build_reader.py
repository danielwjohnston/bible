#!/usr/bin/env python3
"""Compile Open Copyleft Bible Markdown chapters into a single-file offline HTML reader."""

import html
import json
import re
from pathlib import Path

ROOT = Path(__file__).parent
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)


def parse_chapter(md_path: Path) -> dict:
    text = md_path.read_text(encoding="utf-8")
    title_m = re.match(r"^#\s+(.+)$", text, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else md_path.stem

    sections = {}
    parts = re.split(r"^##\s+(.+)$", text, flags=re.MULTILINE)
    for i in range(1, len(parts), 2):
        sec_name = parts[i].strip()
        sec_body = parts[i + 1].strip()
        sections[sec_name] = sec_body

    return {
        "id": f"{md_path.parent.name}-{md_path.stem}",
        "book": md_path.parent.name.capitalize(),
        "chapter": md_path.stem.lstrip("0") or "0",
        "title": title,
        "sections": sections,
    }


def collect_chapters() -> list[dict]:
    chapters = []
    for testament in ("ot", "nt"):
        t_dir = ROOT / testament
        if not t_dir.exists():
            continue
        for book_dir in sorted(t_dir.iterdir()):
            if not book_dir.is_dir():
                continue
            for md_file in sorted(book_dir.glob("*.md")):
                chapters.append(parse_chapter(md_file))
    return chapters


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="Open Copyleft Bible — CC BY-SA 4.0 offline multi-register reader.">
<title>Open Copyleft Bible (CC BY-SA 4.0)</title>
<style>
  :root {
    --bg: #000000;
    --bg-card: #0c0c0c;
    --line: #1f3a1f;
    --ink: #00ff00;
    --ink-dim: #77cc77;
    --ink-bright: #ffffff;
    --warn: #ffd700;
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
    grid-template-columns: 260px 1fr;
    min-height: 100vh;
  }
  nav {
    border-right: 1px solid var(--line);
    padding: 20px;
    background: var(--bg-card);
  }
  nav h1 {
    font-family: var(--display);
    color: var(--ink);
    font-size: 1.4rem;
    letter-spacing: 0.08em;
    margin-bottom: 6px;
  }
  nav .license {
    font-family: var(--mono);
    font-size: 0.75rem;
    color: var(--ink-dim);
    margin-bottom: 20px;
  }
  nav button {
    display: block;
    width: 100%;
    text-align: left;
    background: transparent;
    color: var(--ink-dim);
    border: 1px solid transparent;
    padding: 8px 10px;
    cursor: pointer;
    font-family: var(--mono);
    font-size: 0.9rem;
  }
  nav button:hover, nav button.active {
    border-color: var(--ink);
    color: var(--ink);
    background: rgba(0, 255, 0, 0.08);
  }
  main {
    padding: 32px 40px;
    max-width: 900px;
  }
  .toolbar {
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    margin-bottom: 24px;
    padding-bottom: 16px;
    border-bottom: 1px solid var(--line);
  }
  .toolbar button {
    background: var(--bg-card);
    color: var(--ink-dim);
    border: 1px solid var(--line);
    padding: 6px 14px;
    cursor: pointer;
    font-family: var(--mono);
    font-size: 0.85rem;
  }
  .toolbar button.active {
    border-color: var(--ink);
    color: var(--bg);
    background: var(--ink);
    font-weight: bold;
  }
  h2 {
    font-family: var(--display);
    color: var(--ink);
    font-size: 2rem;
    letter-spacing: 0.05em;
    margin-bottom: 16px;
  }
  .verse-block p { margin-bottom: 10px; }
  .verse-block strong { color: var(--ink); font-family: var(--mono); }
  .notes {
    margin-top: 32px;
    padding-top: 20px;
    border-top: 1px solid var(--line);
  }
  .notes h3 {
    color: var(--warn);
    font-family: var(--mono);
    font-size: 1rem;
    margin: 16px 0 8px;
  }
  .notes li { margin-left: 20px; margin-bottom: 6px; color: var(--ink-dim); }
  @media (max-width: 768px) {
    body { grid-template-columns: 1fr; }
    nav { border-right: none; border-bottom: 1px solid var(--line); }
  }
</style>
</head>
<body>
<nav>
  <h1>OPEN COPYLEFT BIBLE</h1>
  <div class="license">CC BY-SA 4.0 · OFFLINE READER</div>
  <div id="chapter-list"></div>
</nav>
<main>
  <div class="toolbar" id="register-bar">
    <button data-reg="Word-for-Word">Word-for-Word</button>
    <button data-reg="Clear &amp; Faithful" class="active">Clear &amp; Faithful</button>
    <button data-reg="Everyday English">Everyday English</button>
  </div>
  <div id="content"></div>
</main>
<script>
const CHAPTERS = __CHAPTERS_JSON__;
let currentIdx = 0;
let currentReg = 'Clear & Faithful';

function mdToHtml(md) {
  return md
    .split(/\\n+/)
    .map(line => {
      line = line.replace(/\\*\\*(.+?)\\*\\*/g, '<strong>$1</strong>');
      line = line.replace(/\\*(.+?)\\*/g, '<em>$1</em>');
      if (line.startsWith('- ')) return '<li>' + line.slice(2) + '</li>';
      return '<p>' + line + '</p>';
    })
    .join('\\n');
}

function render() {
  const ch = CHAPTERS[currentIdx];
  const list = document.getElementById('chapter-list');
  list.innerHTML = CHAPTERS.map((c, i) =>
    `<button class="${i === currentIdx ? 'active' : ''}" onclick="selectChapter(${i})">${c.title}</button>`
  ).join('');

  document.querySelectorAll('#register-bar button').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.reg === currentReg);
    btn.onclick = () => { currentReg = btn.dataset.reg; render(); };
  });

  const body = ch.sections[currentReg] || '';
  const crossings = ch.sections['Crossings & Lexical Notes'] || '';
  const supp = ch.sections['Supplemental Texts & Allusions'] || '';

  document.getElementById('content').innerHTML = `
    <h2>${ch.title} — ${currentReg}</h2>
    <div class="verse-block">${mdToHtml(body)}</div>
    <div class="notes">
      ${crossings ? `<h3>Crossings &amp; Lexical Notes</h3><ul>${mdToHtml(crossings)}</ul>` : ''}
      ${supp ? `<h3>Supplemental Texts &amp; Allusions</h3><ul>${mdToHtml(supp)}</ul>` : ''}
    </div>
  `;
}

function selectChapter(i) { currentIdx = i; render(); }
render();
</script>
</body>
</html>
"""


def main():
    chapters = collect_chapters()
    out = HTML_TEMPLATE.replace("__CHAPTERS_JSON__", json.dumps(chapters, ensure_ascii=False))
    out_path = DIST / "open-copyleft-bible.html"
    out_path.write_text(out, encoding="utf-8")
    print(f"Built {out_path} ({len(chapters)} chapters)")


if __name__ == "__main__":
    main()
