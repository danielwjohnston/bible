# Open Copyleft Bible

A fresh, original-language translation of the Bible into English, released under a **copyleft** license (**CC BY-SA 4.0**) in the spirit of [opensourcebible.org](https://www.opensourcebible.org/).

## Current Corpus Status

The reader contains the complete published base: **84 book entries and 1,392 content records** (1,391 chapters plus the Sirach prologue). It now distinguishes six existing multi-register chapters, **150 AI-assisted translation drafts**, and 1,236 provisional public-domain records. Draft publication is not certification of linguistic review or protectable human authorship.

The recovered drafts cover Exodus, Job, Matthew, Mark, and Luke. Their previous WEB Updated text remains available through **WEB Reference (PD)**, alongside the three draft registers. See the [translation/review workflow](docs/translation/README.md), [pinned batch registry](docs/translation/backfill.json), and [corpus provenance](docs/CORPUS_PROVENANCE.md). The full study taxonomy remains the long-term vision while original-language drafting and editorial review continue.

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

## Long-Term Scripture Study Vision

The translation and offline reader are the foundation of a comprehensive, extensible Scripture study platform. The long-term requirement includes the full preceding **82-category study taxonomy**, every listed method, and meaningful combinations of modalities, methods, frameworks, lenses, representations, objectives, participation, evaluation, and practical application.

Start with the [product documentation](docs/README.md), including the [vision](docs/VISION.md), [complete supplied taxonomy and source status](docs/STUDY_TAXONOMY.md), [coverage register](docs/TAXONOMY_COVERAGE.md), [detailed requirements](docs/REQUIREMENTS.md), [prototype capability traceability](docs/PROTOTYPES.md), and [roadmap](docs/ROADMAP.md). These describe intended capabilities; they are not claims that the complete platform is implemented. The supplied reconstruction contains all 82 categories and 4,588 category-list entries, plus composition tools and supporting material. All 743 available original-excerpt entries match; the remainder has not been independently checked against a direct original transcript.

The existing **CC BY-SA 4.0** corpus commitment remains in place. Public-domain inputs do not themselves create reciprocal obligations; the license applies to covered rights and adaptations under its actual terms. Source editions, annotations, original translation, study materials, software, and third-party assets need distinct provenance and rights records. See [corpus and licensing](docs/CORPUS_AND_LICENSING.md) and [unresolved decisions](docs/DECISIONS.md). The three personal HTML prototypes are documented by capability and have not been uploaded.
