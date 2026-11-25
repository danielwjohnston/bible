# Corpus Provenance & Rights Matrix

This document records the verified provenance, edition metadata, cryptographic checksums, licensing boundaries, textual/versification notes, and review status for the Open Copyleft Bible corpus. It complements [`docs/CORPUS_AND_LICENSING.md`](CORPUS_AND_LICENSING.md), [`docs/PROTOTYPES.md`](PROTOTYPES.md), and [`docs/DECISIONS.md`](DECISIONS.md).

## Current Draft Backfill (2026-11-25)

The published base and its source-accounting matrix below remain the reference baseline. The current reader additionally exposes 150 AI-assisted translation drafts from Exodus, Job, Matthew, Mark, and Luke. These use 5,173 numbered lines from the selected WLC/OSHB (English-mapped) and SBLGNT references. All three draft registers have matching source verse identifiers. Ten SBLGNT omissions relative to the WEB base are recorded in the [pinned batch registry](translation/backfill.json); they are edition differences, not silently invented readings.

Current primary-view records: six existing multi-register chapters, 150 explicitly labeled translation drafts, and 1,236 provisional public-domain records, still totaling 1,392 records across 84 entries. The 150 replaced primary views retain their complete former WEB text as a separate public-domain comparison section. Comparing alternate editions does not increase the content-record denominator.

Independent linguistic review, verification of scholarly/manuscript assertions, and human editorial authorship review for these drafts remain pending. Existing project CC BY-SA terms do not establish copyright in raw AI-generated output. See [translation and review status](translation/README.md). Sections 4–7 retain the Phase 1 baseline counts and import verification history; they are not a claim that all current primary views are still public-domain-only records.

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
| **External Cache Path** | Stored outside the git repository; the machine-specific cache location is not part of the published corpus |
| **Extracted XML Member** | `engwebu_usfx.xml` (`19,027,951` bytes uncompressed) |
| **License & Trademark Compliance** | Public Domain (`copr.htm`, `engwebumetadata.xml`). *"World English Bible"* is a trademark of `eBible.org` that requires the verse text to remain unmodified when credited by that name. Every Phase 1 chapter preserves `engwebu` verse prose verbatim without editorial alteration and labels itself as provisional/unreviewed interim Public Domain text. |

---

## 3. Quarantined / Excluded Prototype Resources (`E04`)

- **`blb-reader.html`** (`4,303,585` bytes; SHA-256 `1225436e925abcc4ef3f38818a966bb6772808424927f87a29b0522c4d71e6b4`):
  - Explicitly **NOT imported, referenced, or committed** (neither embedded `<script id="bible-data">` JSON payload, HTML/CSS/JS, fonts, nor other local prototype assets).
  - While the publisher statements at `https://berean.bible/licensing.htm` and `https://berean.bible/terms.htm` confirm that official Berean Bible and Majority Bible texts were dedicated to the Public Domain on 2023-04-30 (with a request not to use the Berean name on modified derivatives), the local draft HTML (`"Berean Literal Bible (draft)"`) lacks exact upstream edition/checksum provenance, omits the Deuterocanon/Apocrypha, and remains quarantined under [`docs/DECISIONS.md`](DECISIONS.md) (`E04`) and [`docs/PROTOTYPES.md`](PROTOTYPES.md) (`P1`).

---

## 4. Coverage & Review Status Matrix (Phase 1B / M2 State)

| Layer / Scope | Books / Entries | Chapters / Files | Verse Lines (`<v>`) / Slots | License | Review Status |
|---|---:|---:|---:|---|---|
| **Original Multi-Register Translation** (`ot/genesis/01.md`–`06.md`) | 1 (partial) | 6 | 160 | **CC BY-SA 4.0** | Original 5-section translation from WLC (exact WLC artifact pinning tracked under `D02`) |
| **Provisional 66-Book Base Layer** (`ot/genesis/07.md`–`50.md`, remaining 38 OT books, 27 NT books) | 66 (65 full + Gen 7–50) | 1,183 | 30,943 | **Public Domain** (`engwebu`) | Unreviewed interim starter text; queued for Phase 2 original-language translation |
| **66-Book Canonical Subtotal (M1)** | **66** | **1,189** | **31,103** | Mixed (CC BY-SA 4.0 + PD) | `ot/genesis/01`–`06` preserved; `1,183` base chapters active |
| **Provisional Deuterocanon / Apocrypha Base Layer** (`apocrypha/`) | 18 entries | 203 (202 chs + `sirach/00.md` Prologue) | 6,598 `<v>` (6,611 verse slots) | **Public Domain** (`engwebu`) | Unreviewed interim starter text; queued for Phase 2 original-language translation |
| **Full Corpus Total (M2: OT + NT + Deuterocanon / Apocrypha)** | **84 entries (66 + 18)** | **1,392 (1,391 chs + `00.md`)** | **37,701 `<v>` (160 CC BY-SA 4.0 + 37,541 PD; 37,714 verse slots)** | **Mixed (CC BY-SA 4.0 + PD)** | `ot/genesis/01`–`06` preserved; `1,386` base files active |

### 4.1 Deuterocanon / Apocrypha Breakdown (`apocrypha/` — 18 Entries, 203 Files)

| # | `apocrypha/<slug>` | Display Name | USFX Source | Files | `<v>` Lines | Verse Slots |
|---:|---|---|---|---|---:|---:|
| 1 | `tobit` | Tobit | `TOB` chs 1–14 | 14 (`01.md`–`14.md`) | 244 | 244 |
| 2 | `judith` | Judith | `JDT` chs 1–16 | 16 (`01.md`–`16.md`) | 339 | 339 |
| 3 | `esther-greek` | Greek Esther | `ESG` chs 1–10 | 10 (`01.md`–`10.md`) | 205 | 205 |
| 4 | `wisdom-of-solomon` | Wisdom of Solomon | `WIS` chs 1–19 | 19 (`01.md`–`19.md`) | 436 | 436 |
| 5 | `sirach` | Sirach | `SIR` Prologue + chs 1–51 | 52 (`00.md` + `01.md`–`51.md`) | 1,383 | 1,395 |
| 6 | `baruch` | Baruch | `BAR` chs 1–5 | 5 (`01.md`–`05.md`) | 140 | 140 |
| 7 | `letter-of-jeremiah` | Letter of Jeremiah | `BAR` ch 6 | 1 (`01.md`) | 73 | 73 |
| 8 | `prayer-of-azariah` | Prayer of Azariah & Song of the Three | `DAG` ch 3 vv. 24–90 | 1 (`01.md`) | 67 | 67 |
| 9 | `susanna` | Susanna | `DAG` ch 13 | 1 (`01.md`) | 64 | 64 |
| 10 | `bel-and-the-dragon` | Bel and the Dragon | `DAG` ch 14 | 1 (`01.md`) | 42 | 42 |
| 11 | `1-maccabees` | 1 Maccabees | `1MA` chs 1–16 | 16 (`01.md`–`16.md`) | 924 | 924 |
| 12 | `2-maccabees` | 2 Maccabees | `2MA` chs 1–15 | 15 (`01.md`–`15.md`) | 555 | 555 |
| 13 | `1-esdras` | 1 Esdras | `1ES` chs 1–9 | 9 (`01.md`–`09.md`) | 448 | 448 |
| 14 | `2-esdras` | 2 Esdras | `2ES` chs 1–16 | 16 (`01.md`–`16.md`) | 944 | 944 |
| 15 | `prayer-of-manasseh` | Prayer of Manasseh | `MAN` ch 1 | 1 (`01.md`) | 15 | 15 |
| 16 | `psalm-151` | Psalm 151 | `PS2` ch 1 (`<cp id="151"/>`) | 1 (`01.md`) | 7 | 7 |
| 17 | `3-maccabees` | 3 Maccabees | `3MA` chs 1–7 | 7 (`01.md`–`07.md`) | 228 | 228 |
| 18 | `4-maccabees` | 4 Maccabees | `4MA` chs 1–18 | 18 (`01.md`–`18.md`) | 484 | 485 |
| | **Subtotal (`apocrypha/`)** | **18 entries** | **15 USFX books** | **203 files** | **6,598** | **6,611** |

Note on filename padding and lead-in superscriptions: `ot/psalms/` chapters use 3-digit zero-padded filenames (`ot/psalms/001.md`–`ot/psalms/150.md`); `apocrypha/sirach/00.md` holds the prose Prologue to Sirach; all other canonical and Deuterocanonical/Apocryphal chapter files use 2-digit zero-padded filenames (`01.md`–`99.md`). Descriptive `<d>` superscriptions in `ot/psalms/` (excluding `PSA 119` Hebrew acrostic letters `ALEPH`–`TAV` and stripping inline `<f>` footnotes) and `apocrypha/psalm-151/01.md` (stripping inline `<f>`), as well as the pre-verse-1 `<p style="p">` heading in `apocrypha/sirach/51.md`, appear as an italicized lead-in line before verse 1.

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

3. **Twenty-Four `<f>`-Only Verses in Sirach (`apocrypha/sirach/`, § 5.3):**
   In `engwebu_usfx.xml`, twenty-four `<v>` elements in `SIR` contain empty prose and hold manuscript/omission notes inside `<f>` footnotes. Consistent with the five canonical `<f>`-only verses above, M2 renders each source footnote verbatim in `[Textual note from source edition: ...]`:
   - `1:5`: `[Textual note from source edition: Verse 5 is omitted by the best authorities: The source of wisdom is God’s word in the highest heaven, and her ways are the eternal commandments.]`
   - `1:7`: `[Textual note from source edition: Verse 7 is omitted by the best authorities: To whom was the knowledge of wisdom manifested? Who has understood her abundant experience?]`
   - `1:21`: `[Textual note from source edition: Verse 21 is omitted by the best authorities: The fear of the Lord drives away sins. Where it resides, it will turn away all anger.]`
   - `3:19`: `[Textual note from source edition: Some manuscripts add Many are lofty and renowned, but he reveals his secrets to the humble.]`
   - `10:21`: `[Textual note from source edition: Verse 21 is omitted by the best authorities: Fear of the Lord is the beginning of acceptance, but obstinance and pride are the beginning of rejection.]`
   - `11:15-16`: `[Textual note from source edition: Verses 15 and 16 are omitted by the best authorities.]`
   - `13:14`: `[Textual note from source edition: The remainder of verse 13, and verse 14, are omitted by the best authorities.]`
   - `16:15-16`: `[Textual note from source edition: Verses 15 and 16 are omitted by the best authorities.]`
   - `17:5`: `[Textual note from source edition: Verse 5 is omitted by the best authorities.]`
   - `17:9`: `[Textual note from source edition: Verse 9 is omitted by the best authorities.]`
   - `17:16`: `[Textual note from source edition: Verses 16, 18, and 21 are omitted by the best authorities.]`
   - `17:18`: `[Textual note from source edition: Verses 16, 18, and 21 are omitted by the best authorities.]`
   - `17:21`: `[Textual note from source edition: Verses 16, 18, and 21 are omitted by the best authorities.]`
   - `18:3`: `[Textual note from source edition: The remainder of verse 2, and verse 3, are omitted by the best authorities.]`
   - `19:18-19`: `[Textual note from source edition: Verses 18 and 19 are omitted by the best authorities.]`
   - `19:21`: `[Textual note from source edition: The remainder of verse 20 and verse 21 are omitted by the best authorities.]`
   - `20:3`: `[Textual note from source edition: Verse 3 is omitted by the best authorities.]`
   - `20:32`: `[Textual note from source edition: Verse 32 is omitted by the best authorities.]`
   - `22:9-10`: `[Textual note from source edition: Verses 9 and 10 are omitted by the best authorities.]`
   - `23:28`: `[Textual note from source edition: Verse 28 is omitted by the best authorities.]`
   - `24:18`: `[Textual note from source edition: Verse 18 is omitted by the best authorities.]`
   - `24:24`: `[Textual note from source edition: Verse 24 is omitted by the best authorities.]`
   - `25:12`: `[Textual note from source edition: Verse 12 is omitted by the best authorities.]`
   - `26:19-27`: `[Textual note from source edition: Verses 19-27 are omitted by the best authorities.]`

4. **Six Hyphenated Verse Ranges (`SIR`, `4MA`, § 5.4):**
   Six `<v>` elements in `engwebu` carry hyphenated multi-verse IDs, preserved verbatim: `SIR 11:15-16` (2 slots), `SIR 16:15-16` (2 slots), `SIR 19:18-19` (2 slots), `SIR 22:9-10` (2 slots), `SIR 26:19-27` (9 slots), and `4MA 8:28-29` (2 slots; prose verse). These `6` combined `<v>` lines span `19` logical verse numbers (`+13` net slots), so `apocrypha/` contains **`6,598` `<v>` lines** representing **`6,611` logical verse slots**, and the full 84-entry corpus contains **`37,701` `<v>` lines** (`160` CC BY-SA 4.0 + `37,541` PD) representing **`37,714` logical verse slots**.

5. **Deuterocanonical Structural Mappings (`ESG`, `BAR 6`, `DAG`, `SIR 00`, `PS2`, § 5.5):**
   - **`ESG` -> `apocrypha/esther-greek/` (`01.md`–`10.md`):** `engwebu` presents Greek Esther as an integrated 10-chapter text (`205` `<v>` lines) with Additions A–F woven directly into chapters 1, 3, 4, 5, 8, and 10 (Additions A, B, C, E, F in `[square brackets]`; Addition D in unbracketed Greek court-scene prose at `5:1–3`). In `engwebu`, `ESG` omits verses `4:6`, `9:5`, and `9:30` (yielding `46` verses in ch. 4 and `30` verses in ch. 9).
   - **`BAR 6` -> `apocrypha/letter-of-jeremiah/01.md` (`73` verses):** USFX `BAR` chs 1–5 map to `apocrypha/baruch/01.md`–`05.md` (`140` verses), while `BAR` ch 6 maps to `apocrypha/letter-of-jeremiah/01.md`.
   - **`DAG` Additions -> Three Standalone Entries (`173` verses extracted; `357` canonical Daniel `<v>` excluded):** `DAG 3:24–90` (`67` verses, preserving `engwebu` verse IDs `24`–`90` with an italicized provenance note) maps to `apocrypha/prayer-of-azariah/01.md`; `DAG 13` (`64` verses) maps to `apocrypha/susanna/01.md`; `DAG 14` (`42` verses) maps to `apocrypha/bel-and-the-dragon/01.md`. Overlapping canonical Daniel chapters/verses in `DAG` (`1–2`, `3:1–23`, `3:91–97`, `4–12`, totaling `357` `<v>` elements) are excluded to avoid duplicating `ot/daniel/`.
   - **`SIR` Prologue & Ch. 51 Lead-In (`apocrypha/sirach/00.md`, `51.md`):** The `<p sfm="ip">` Prologue immediately following `<p sfm="is">The Prologue of the Wisdom of Jesus the Son of Sirach.</p>` maps to `apocrypha/sirach/00.md` (`# Sirach Prologue`, prose without numbered verses); the pre-`v1` `<p style="p">` heading in `SIR 51` (`*A Prayer of Jesus the son of Sirach.*`) renders as an italicized lead-in.
   - **`PS2` (`apocrypha/psalm-151/01.md`) & `2MA 2:18`:** `PS2` (`<cp id="151"/>`, `7` verses) emits its `<d>` superscription (stripped of inline `<f>`) as an italicized lead-in; `2MA 2:18` flushes cleanly at `<ve />` inside `<p sfm="pc">` while omitting the `———————` decorative divider.

6. **`2 Esdras 7` (`7:36–105` Bensly Fragment, § 5.6):**
   `apocrypha/2-esdras/07.md` contains all **`140` sequential verses** (`7:1`–`7:140`), inclusive of the restored Bensly section `7:36–105` (noted in `engwebu`'s `<f>` footnote at `2ES 7:35`).

---

## 6. Phase 2 Critical Sources Queue (Planned M3–M5)

When Phase 2 replaces provisional chapters with original CC BY-SA 4.0 five-section translations, exact source commits/releases and SHA-256 checksums will be pinned here per [`docs/CORPUS_AND_LICENSING.md`](CORPUS_AND_LICENSING.md) (`D02`):

- **Old Testament (Hebrew & Aramaic):** Westminster Leningrad Codex / Open Scriptures Hebrew Bible (`openscriptures/morphhb`, WLC PD text + CC BY 4.0 morphology layer separated).
- **New Testament (Koine Greek):** `Faithlife/SBLGNT` (CC BY 4.0, pinning exact release/commit) and `biblicalhumanities/Nestle1904` (verified exact artifact).
- **Deuterocanon / Apocrypha:** Repaired Swete Septuagint (`nathans/lxx-swete` / `septuagint-contabulate`), Hebrew Ben Sira witnesses (`metz-theolab/bensira-xml`), and Public Domain Latin Vulgate + Bensly 1875 for 4 Ezra (`2 Esdras`).


## 7. Phase 1B Source and Build Verification (2026-11-24)

A separate source comparison checked every one of the 203 `apocrypha/` files against the pinned official USFX artifact: all 6,598 numbered source lines, their verse IDs/ranges, all 6,611 represented verse slots, and the Sirach Prologue. Source wording and punctuation agree after normalizing whitespace introduced at XML inline boundaries and excluding the documented decorative divider at 2 Maccabees 2:18. Footnote-only readings remain explicitly marked as source textual notes. These checks establish import fidelity, not original-language translation or theological review.

An isolated rebuild reproduced the reader byte-for-byte. Its data contains 84 distinct entries and 1,392 unique content records (1,391 chapters plus the Sirach Prologue), including six original CC BY-SA records and 1,386 provisional public-domain records. Existing OT/NT files, the reader builder, original licensing/contribution guidance, and study taxonomy were unchanged from the published Phase 1A baseline. The added prose contains no active HTML elements or event-handler attributes.

The source publisher confirms the [World English Bible Updated public-domain status and naming conditions](https://ebible.org/engwebu/copyright.htm). Editorial and original-language review of this interim layer remains pending; the public-domain import is not presented as newly authored copyleft translation.
