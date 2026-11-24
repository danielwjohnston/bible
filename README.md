# Open Copyleft Bible

A fresh, original-language translation of the Bible into English, released under a **copyleft** license (**CC BY-SA 4.0**) in the spirit of [opensourcebible.org](https://www.opensourcebible.org/).

## Core Design

1. **Canonical Order:** Translated sequentially from Genesis through Revelation.
2. **Self-Contained & Multi-Register:** Every passage is presented without needing external cross-references, serving every reading and study modality:
   - **Word-for-Word:** Preserves original Hebrew, Aramaic, and Greek syntax, particles, and idioms for deep lexical and grammatical study.
   - **Clear & Faithful:** Bridges word-for-word accuracy with natural contemporary English for careful reading, teaching, and memorization.
   - **Everyday English:** Natural, conversational English for accessible, devotional, and narrative-flow reading.
   - **Crossings & Lexical Notes:** Full semantic range, root meanings, wordplays, and alternative renderings for key terms.
   - **Supplemental Texts & Allusions:** Quoted or alluded-to passages ("it is written", echoes, and parallel texts) included inline.
3. **Offline-First Reader:** Compiled into a single-file, zero-dependency HTML reader (`dist/open-copyleft-bible.html`).
4. **Copyleft (CC BY-SA 4.0):** Free to read, print, quote, remix, and build upon—even commercially—provided all derivative works remain under **CC BY-SA 4.0**.

## Source Texts

- **Old Testament (Hebrew & Aramaic):** Westminster Leningrad Codex (WLC) / Open Scriptures Hebrew Bible (OSHB)
- **New Testament (Koine Greek):** SBL Greek New Testament (SBLGNT) / Nestle 1904

## Repository Structure

```text
bible/
├── LICENSE                      # CC BY-SA 4.0
├── README.md                    # Project overview
├── CONTRIBUTING.md              # Translation & formatting guidelines
├── build_reader.py              # Single-file offline HTML reader builder
├── dist/
│   └── open-copyleft-bible.html # Offline Bauhaus reader
├── ot/                          # Old Testament (Genesis–Malachi)
│   └── genesis/
│       ├── 01.md
│       ├── 02.md
│       ├── 03.md
│       └── 04.md
└── nt/                          # New Testament (Matthew–Revelation)
```
