# Private prototype capability record

## Inspection and publication boundary

Three user-supplied HTML files were inspected locally on 2026-11-24 as reference implementations. This record documents their structure and reusable capabilities. The files, their embedded Bible/quotation payloads, personal declarations, journal prompts/responses, fonts, scripts, and other assets are **not imported or licensed by this documentation**. No prototype content or assets are included in this change.

Inspection was static: HTML structure, labels, CSS asset declarations, and JavaScript behavior were read. No browser interaction, accessibility conformance test, theological validation, source-text comparison, or full rights audit was performed. A code path demonstrates an authored capability, not verified runtime behavior on every device. No network execution was needed to inspect the files.

Fingerprints identify the exact supplied versions without publishing the originals. Line numbers below are local-source evidence locators, not public links.

| ID | Supplied filename / display title | Bytes | SHA-256 |
| --- | --- | --- | --- |
| P1 | `blb-reader.html` / BLB Reader / Berean Literal Bible | 4,303,585 | `1225436e925abcc4ef3f38818a966bb6772808424927f87a29b0522c4d71e6b4` |
| P2 | `Nothing-Hidden-No-One-Alone(2).html` / Nothing Hidden, No One Alone | 455,382 | `fdbcc11b3a298cb417ee9cb3034cb1eafc60e21398b1d93a95a86221665443e9` |
| P3 | `Christ_Has_Completed_The_Work_Bauhaus(2).html` / Christ Has Completed the Work, Bauhaus Edition | 211,323 | `4d9642713920ed472a15a698ef6e2073b9812ccfb729fb9ed073f0567697ccd9` |

## P1 — portable Scripture reader

The single-file reader embeds a Bible data array and implements book/chapter navigation, previous/next chapter navigation across book boundaries, verse focus, reference parsing with abbreviations, full-text search, result highlighting, and all/OT/NT filtering. Search displays a 200-result limit rather than rendering an unlimited list. URL hashes encode book/chapter/verse state. Verse interaction copies a reference through the clipboard API with a fallback. The responsive sidebar and keyboard handlers indicate attention to mobile and keyboard use.

Evidence locators: `renderBookList`, `renderChapterGrid`, `renderReader`, `previousChapter`, `nextChapter`, `parseReference`, `runSearch`, `renderSearchResults`, `updateUrlHash`, `loadFromHash`, and `copyToClipboard`. The code's 39/27 OT/NT split and 66-book indexing are prototype assumptions; the product needs explicit canon and versification profiles.

Reusable outcome: an offline corpus-neutral reader shell. Reimplement or adapt only rights-cleared components, and replace the embedded text through a provenance-aware corpus adapter. The prototype's BLB label is not evidence that this project's original translation is complete, and a public-domain source is not itself a reciprocal corpus.

## P2 — a multidimensional thematic study

The study organizes a theme through multiple passages and conceptual threads. It explicitly offers seeing, hearing, reading/writing, and doing, and an Observe–Root–Reason–Respond sequence. Passage entries expose Words, Shape, Setting, Context, Canon, Doctrine, Christ, History, Cautions, Practice, and Discuss views. These are authored perspectives to preserve as named lenses; their conclusions are not validated by this inspection.

Translation identifiers include KJV, WEB, YLT, and an author-supplied literal rendering. Code selects among available renderings, labels them, persists selection, and supports verse copying. Listening uses browser speech synthesis with chunking and stop/state handling. Device voice availability and offline behavior have not been tested.

Memory activities include progressive word hiding/reveal and typed-recall comparison. Quizzes and matching include scoring and restart/shuffle paths. Journal text and practice/checklist state use browser-local storage, with clear operations and unavailable-storage handling. Guided/full display modes and translation choice also persist. Study drawers include keyboard handling and focus restoration. Hash navigation and scroll state connect the authored sections.

Evidence locators: `TR_LABEL`/`TR_NAME`, `setTr`, `listenText`, `speak`, `stopSpeak`, `buildMem`, `renderMem`, `checkMem`, `renderQuiz`, `renderMatch`, `sget`/`sset`/`sdel`, `setMode`, `openFromHash`, `openStudy`, and `closeStudy`. Journal-related markup begins near line 760; dialog logic is near lines 4117–4209 in this supplied version. CSS embeds two WOFF2 font payloads near the top of the file.

Reusable outcome: a study template, lens registry, translation selector, accessible detail-view pattern, activity engine, and private learner-state layer. Do not copy a person's reflections or personal responses into a shared template. Browser-local storage needs clear user expectations and export/erase semantics; it is not a durable backup service.

## P3 — statement-linked lexical and expository study

An authored declaration is paired with statement-specific Scripture study sections, original-language discussion, lexical notes, expository explanation, contextual cautions, a word list, and links among statements and their supporting study. The introductory material discusses the gap between ancient contexts and modern readers and ways notes may mislead. Selectable statement markers open detailed study drawers; the JavaScript maintains expanded state, dialog behavior, focus restoration, scroll/resize presentation, and reduced-motion-aware transitions.

Evidence locators: statement-linked `s-*` sections; lexical material near lines 491, 529, and 544; expository material near lines 627, 676, and 695; `openStudy`, `setExpanded`, `closeStudy`, and `draw`; dialog markup/logic near lines 1847–1879. CSS embeds two WOFF2 font payloads. These locators describe capabilities without reproducing the declaration or personal life context.

Reusable outcome: a statement-to-evidence model and authoring template that distinguishes the author's assertion, quoted Scripture, lexical data, interpretive reasoning, and practical response. A reader should be able to examine or challenge the support for one statement without treating the declaration itself as Scripture.

## Capability-to-requirement traceability

| Capability evidence | Source | Durable requirements | Recovered taxonomy links / vision | Delivery |
| --- | --- | --- | --- | --- |
| Single-file embedded reading and responsive navigation | P1, existing repository | READ-01, READ-03, COR-01, ACC-01 | T01, T03; offline environment | M1–M2 |
| Reference parsing, scoped search, highlighted results, hashes | P1 | READ-01, READ-02, COR-02 | T03, T08–T10 | M2 |
| Verse copy with context | P1, P2 | READ-04, RIGHTS-01 | T03–T04 | M2–M3 |
| Multiple labeled renderings | P2, existing repository | COR-03, READ-04 | T03; comparison | M1–M3 |
| Thematic passage structure and multiple lenses | P2 | INV-01, INV-02, CMP-01, AUTH-01 | T08–T13; lens axis | M3 |
| Listen/stop and mixed text/audio encounter | P2 | REP-02, ACC-02 | T02, T07 | M3 |
| Progressive recall, typed recall, quiz, matching | P2 | LEARN-01, LEARN-02 | T09, T12, T14 | M3–M4 |
| Journal, checklist, prayer/practice/discussion structure | P2 | PRIV-01, FORM-01, GROUP-01 | T04–T06; application and participation | M3–M5 |
| Guided/full display, drawers, focus restoration | P2, P3 | AUTH-02, ACC-01 | T01, T03; scaffolding | M3 |
| Statement-specific lexical and expository support | P3 | INV-01, INV-02, AUTH-01, KNOW-01 | T03–T04, T10–T13 | M3–M4 |
| Contextual cautions and limits of interpretations | P2, P3 | INV-02, LEARN-02 | T11–T12 | M3 onward |
| Inline fonts and quoted/embedded source text | P1–P3 | RIGHTS-01, COR-04, EXT-02 | Rights infrastructure, not taxonomy coverage | M1 onward |

These mappings are many-to-many. The complete supplied [taxonomy coverage register](TAXONOMY_COVERAGE.md) now provides category/entry planning links. Additional source-specific links are P1 → T25 (Scripture reading) and T77 (granularity); P2 → T26–T29 (frameworks, observation, languages, translation), T40–T42 (theological disciplines), T62–T68 (devotional/practical activities), and T81 (assessment); P3 → T28, T30–T32 (language/literary/rhetorical/argument analysis), T61 (identity/self-examination), T66 (application), and T79 (decomposition). No row claims that a prototype implements an entire category or validates every method.

The newly supplied taxonomy HTML is a separate reference artifact, not a fourth personal Scripture-study prototype. Static inspection found search/filter, expand/collapse, print/PDF, a configurable combination calculator, and compose/randomize/copy/save prompt controls. Its 4,588 category-list entries and 82 generator choices agree with the supplied JSON/Markdown. These support CMP-04, TAX-02, and portable authoring requirements; the HTML file and scripts remain local. No attached JavaScript was executed.

## Rights and privacy disposition

- P1 embeds a BLB-labeled corpus. The publisher's [licensing page](https://berean.bible/licensing.htm) states that Berean Bible texts were placed in the public domain in 2023; that does not establish the exact embedded edition's provenance or the rights to this HTML's code and other components.
- P2 embeds several named translations and an authored literal rendering. Record the exact editions, quotations, territories where relevant, authorship, and applicable terms before any content migration. A familiar translation name is not a complete rights record.
- P2 and P3 each embed two font payloads. Family/source, license, attribution, modification/embedding permissions, and any reserved font names are not established by this inspection. Do not copy them into repository or release artifacts pending component review.
- Authorship of an HTML document does not establish rights to every quotation, font, annotation, or embedded asset. Personal religious writing and potential learner responses also need a deliberate privacy review before publication.
- Initial implementation can use newly authored neutral fixtures, this project's properly reviewed corpus slices, and cleared system-font styling. Capability-level summaries can inform design while the original files remain private.
- If any prototype is later proposed for publication, inventory its components, confirm ownership/permissions, redact personal data, identify the intended audience, approve the exact sanitized artifact, and keep a public notice manifest. Current documentation is not approval of a later upload.
