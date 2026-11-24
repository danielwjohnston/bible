# Open Copyleft Bible

A fresh, original-language translation of the Bible into English, released under a **copyleft** license (**CC BY-SA 4.0**) in the spirit of [opensourcebible.org](https://www.opensourcebible.org/).

## Core Design

1. **Canonical Order:** Translated sequentially from Genesis through Revelation.
2. **Self-Contained & Multi-Register:** Every passage is presented without needing external cross-references:
   - **Ultra-Literal:** Word-for-word / formal equivalence preserving Hebrew, Aramaic, and Greek syntax and idioms.
   - **Balanced:** Clear, faithful contemporary English.
   - **Modern Informal:** Natural, everyday conversational English.
   - **Crossings & Lexical Range:** Key terms with their full semantic range, alternative renderings, and root meanings.
   - **Supplemental Texts & Allusions:** Quoted or alluded-to passages ("it is written", echoes, and parallel texts) included inline.
3. **Copyleft (CC BY-SA 4.0):** Free to read, print, quote, remix, and build upon—even commercially—provided all derivative works remain under **CC BY-SA 4.0**.

## Source Texts

- **Old Testament (Hebrew & Aramaic):** Westminster Leningrad Codex (WLC) / Open Scriptures Hebrew Bible (OSHB)
- **New Testament (Koine Greek):** SBL Greek New Testament (SBLGNT) / Nestle 1904

## Repository Structure

```text
bible/
├── LICENSE            # CC BY-SA 4.0
├── README.md          # Project overview
├── CONTRIBUTING.md    # Translation & formatting guidelines
├── ot/                # Old Testament (Genesis–Malachi)
│   └── genesis/
│       ├── 01.md
│       └── 02.md
└── nt/                # New Testament (Matthew–Revelation)
```

## Status

- [x] Repository & CC BY-SA 4.0 license initialized
- [x] [Genesis 1](ot/genesis/01.md) (Multi-register + crossings + supplemental texts)
- [x] [Genesis 2](ot/genesis/02.md) (Multi-register + crossings + supplemental texts)
- [ ] Genesis 3–50 & remaining books in canonical order
