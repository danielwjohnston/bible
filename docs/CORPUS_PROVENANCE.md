# Corpus Provenance & Rights Matrix

This document records the verified provenance, edition metadata, cryptographic checksums, licensing boundaries, textual/versification notes, and review status for the Open Copyleft Bible corpus. It complements [`docs/CORPUS_AND_LICENSING.md`](CORPUS_AND_LICENSING.md), [`docs/PROTOTYPES.md`](PROTOTYPES.md), and [`docs/DECISIONS.md`](DECISIONS.md).

---

## 1. Purpose & Separation of Rights Layers

Following [`docs/CORPUS_AND_LICENSING.md`](CORPUS_AND_LICENSING.md):

- **Original CC BY-SA 4.0 Layer:** Original multi-register translations authored from original-language critical texts (`ot/genesis/01.md`–`06.md` and Phase 2 chapters) carry the project's **CC BY-SA 4.0** license and include all five required sections (`Word-for-Word`, `Clear & Faithful`, `Everyday English`, `Crossings & Lexical Notes`, and `Supplemental Texts & Allusions`).
- **Provisional Public Domain Base Layer:** Phase 1 breadth-first base chapters (`## Base Text (Interim — WEB Updated, Public Domain)`) contain unmodified Public Domain text from the *World English Bible Updated* (`engwebu`). Adding a repository license file does not impose share-alike obligations on unchanged Public Domain prose; every Phase 1 chapter explicitly identifies its source, edition, Public Domain status, and unreviewed interim status so it is never conflated with original CC BY-SA 4.0 work.
- **Software Separation:** `build_reader.py` and compiled offline reader builds (`dist/open-copyleft-bible.html`) expose the distinct licensing of both layers cleanly in the reader header, per-chapter badges, and footer.

---

## 2. Phase 1 Verified Source Artifact (`engwebu_usfx.zip`)

| Field | Value |
|---|---|
| **Edition** | World English Bible Updated (`engwebu` / `WEBU`), American English (`LORD`/`GOD`), Byzantine Majority Text NT basis, 2024 completion (`eBible.org` Haiola build `2026-11-24`) |
| **Official Source URL** | `https://eBible.org/Scriptures/engwebu_usfx.zip` |
| **File Size** | `3,317,152` bytes |
| **SHA-256** | `48f861bfd09fc34b67dac2e9b29de6b18ca1a23fcbd9f111cdf10c3e241341d5` |
| **External Cache Path** | `/Users/dwjohnston/.gemini/antigravity/scratch/bible_sources_cache/engwebu_usfx.zip` (stored outside the git repository; not committed) |
| **Extracted XML Member** | `engwebu_usfx.xml` (`19,027,951` bytes uncompressed) |
| **License & Trademark Compliance** | Public Domain (`copr.htm`, `engwebumetadata.xml`). *"World English Bible"* is a trademark of `eBible.org` that requires the verse text to remain unmodified when credited by that name. Every Phase 1 chapter preserves `engwebu` verse prose verbatim without editorial alteration and labels itself as provisional/unreviewed interim Public Domain text. |

---

## 3. Quarantined / Excluded Prototype Resources (`E04`)

- **`blb-reader.html`** (`4,303,585` bytes; SHA-256 `1225436e925abcc4ef3f38818a966bb6772808424927f87a29b0522c4d71e6b4`):
  - Explicitly **NOT imported, referenced, or committed** (neither embedded `<script id="bible-data">` JSON payload, HTML/CSS/JS, fonts, nor other local prototype assets).
  - While the publisher statements at `https://berean.bible/licensing.htm` and `https://berean.bible/terms.htm` confirm that official Berean Bible and Majority Bible texts were dedicated to the Public Domain on 2023-04-30 (with a request not to use the Berean name on modified derivatives), the local draft HTML (`"Berean Literal Bible (draft)"`) lacks exact upstream edition/checksum provenance, omits the Deuterocanon/Apocrypha, and remains quarantined under [`docs/DECISIONS.md`](DECISIONS.md) (`E04`) and [`docs/PROTOTYPES.md`](PROTOTYPES.md) (`P1`).

---

## 4. Coverage & Review Status Matrix (Phase 1A / M1 State)

| Layer / Scope | Books | Chapters | Verse Slots | License | Review Status |
|---|---:|---:|---:|---|---|
| **Original Multi-Register Translation** (`ot/genesis/01.md`–`06.md`) | 1 (partial) | 6 | 160 | **CC BY-SA 4.0** | Original 5-section translation from WLC (exact WLC artifact pinning tracked under `D02`) |
| **Provisional 66-Book Base Layer** (`ot/genesis/07.md`–`50.md`, remaining 38 OT books, 27 NT books) | 66 (65 full + Gen 7–50) | 1,183 | 30,943 | **Public Domain** (`engwebu`) | Unreviewed interim starter text; queued for Phase 2 original-language translation |
| **66-Book Canonical Total (M1)** | **66** | **1,189** | **31,103** | Mixed (CC BY-SA 4.0 + PD) | `ot/genesis/01`–`06` preserved; `1,183` base chapters active |
| **Queued for M2 (Phase 1B): Deuterocanon / Apocrypha** (`apocrypha/`) | 18 entries | Queued | Queued | Public Domain (`engwebu`) | Queued immediately after M1 |

Note on `ot/psalms/` filename padding: Psalms chapters use 3-digit zero-padded filenames (`ot/psalms/001.md`–`ot/psalms/150.md`); all other 65 canonical books use 2-digit zero-padded filenames (`01.md`–`99.md`). Descriptive Psalm `<d>` superscriptions (excluding `PSA 119` Hebrew acrostic letters `ALEPH`–`TAV` and stripping inline `<f>` footnotes) appear as an italicized lead-in line before verse 1 where present in `engwebu`.

---

## 5. Textual Variants & Versification Notes (`engwebu`)

1. **Five `<f>`-Only Canonical Verses (Bracketed Source Textual Notes):**
   In `engwebu_usfx.xml`, five canonical `<v>` elements contain empty prose and hold manuscript/Textus Receptus (TR) variant readings inside `<f>` footnotes. Rather than fabricating prose or leaving silent blank verses, M1 renders the source footnote verbatim in brackets:
   - **`LUK 17:36` (`nt/luke/17.md`):** `[Textual note from source edition: Some Greek manuscripts add: “Two will be in the field: the one taken, and the other left.”]`
   - **`ACT 8:37` (`nt/acts/08.md`):** `[Textual note from source edition: TR adds Philip said, “If you believe with all your heart, you may.” He answered, “I believe that Jesus Christ is the Son of God.”]`
   - **`ACT 15:34` (`nt/acts/15.md`):** `[Textual note from source edition: Some manuscripts add: But it seemed good to Silas to stay there.]`
   - **`ACT 24:7` (`nt/acts/24.md`):** `[Textual note from source edition: TR adds “but the commanding officer, Lysias, came by and with great violence took him out of our hands,”]` *(Note: in `engwebu`, the surrounding TR expansion splits across `<f>` footnotes at the end of `ACT 24:6` and start of `ACT 24:8`, both of which also have regular verse prose.)*
   - **`ROM 16:25` (`nt/romans/16.md`):** `[Textual note from source edition: TR places Romans 14:24-26 at the end of Romans instead of at the end of chapter 14, and numbers these verses 16:25-27.]`

2. **`ROM 14:24–26` Doxology Placement & 66-Book Verse Total (`31,103`):**
   `engwebu` follows the Byzantine/Majority placement of the Romans closing doxology at `ROM 14:24–26` (`26` verses in `ROM 14`) rather than `ROM 16:25–27`, while `ROM 16` contains `25` verses (`16:24` benediction + `16:25` cross-reference `<f>` note above; `16:26–27` do not exist as `<v>` elements). Consequently, Romans contains `434` `<v>` elements (`+3` in ch. 14, `-2` in ch. 16 relative to 23/27 numbering) and the 66-book canonical total in `engwebu` is **`31,103`** verses across **`1,189`** chapters.

---

## 6. Phase 2 Critical Sources Queue (Planned M3–M5)

When Phase 2 replaces provisional chapters with original CC BY-SA 4.0 five-section translations, exact source commits/releases and SHA-256 checksums will be pinned here per [`docs/CORPUS_AND_LICENSING.md`](CORPUS_AND_LICENSING.md) (`D02`):

- **Old Testament (Hebrew & Aramaic):** Westminster Leningrad Codex / Open Scriptures Hebrew Bible (`openscriptures/morphhb`, WLC PD text + CC BY 4.0 morphology layer separated).
- **New Testament (Koine Greek):** `Faithlife/SBLGNT` (CC BY 4.0, pinning exact release/commit) and `biblicalhumanities/Nestle1904` (verified exact artifact).
- **Deuterocanon / Apocrypha:** Repaired Swete Septuagint (`nathans/lxx-swete` / `septuagint-contabulate`), Hebrew Ben Sira witnesses (`metz-theolab/bensira-xml`), and Public Domain Latin Vulgate + Bensly 1875 for 4 Ezra (`2 Esdras`).
