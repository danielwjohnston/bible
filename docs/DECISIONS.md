# Decisions and unresolved questions

## Established direction

| Record | Evidence and disposition |
| --- | --- |
| E01 — Comprehensive scope | The user explicitly makes the preceding 82-category taxonomy, all modalities/methods/lenses/representations/objectives, and extensible combinations the long-term vision. Initial delivery must not silently replace that vision with a small reader feature list. |
| E02 — Copyleft Bible foundation | The user is creating a copyleft corpus as reusable infrastructure. Existing repository notices select CC BY-SA 4.0. Preserve that choice; distinguish original contributions from public-domain sources and separately licensed components. |
| E03 — Preserve existing work | Keep existing translation chapters, register contract, documentation, licensing notices, builder, and generated reader. Documentation expansion is additive; the overview gains navigation and license-scope clarification. |
| E04 — Private prototype boundary | The three supplied HTML files are reference evidence for capabilities. This change does not publish their content, personal writing, embedded corpora, fonts, or scripts. Component rights and privacy review precede any future import. |
| E05 — Evidence limits | Prototype inspection is static. The original taxonomy is truncated in the available history export. Missing text, runtime behavior, interpretation accuracy, and unresolved rights must not be reported as verified. |

## Open decisions

No individual owner or deadline has been assigned. The roles below identify the decision needed, not a promise that someone has accepted it.

| ID | Decision or missing evidence | Who needs to resolve it / consequence | Next bounded action |
| --- | --- | --- | --- |
| D01 | Obtain the complete original 82-category response, including the rest of category 15 and categories 16–82. | User/source holder; blocks TAX-01 and calling this documentation complete. | Attach/export the original response; compare its category numbers and every entry to the recovered excerpt, then update the draft PR. |
| D02 | Which exact original-language editions, digital versions, apparatuses, and annotation sources produced each existing chapter? | Translation maintainers; affects provenance and distributable corpus claims. | Inventory sources for Genesis 1–6 first; record artifact checksums, versioned URLs, transformations, and review status. |
| D03 | What prospective software license and component boundaries should apply? | Rights holders/maintainers; existing CC BY-SA notices remain until an authorized decision. | Inventory builder/reader authorship and contributions; compare software-license options and document migration/consent implications. Do not relicense by implication. |
| D04 | Which corpus/interchange formats and stable-reference conventions should be adopted? | Corpus/platform maintainers; affects alignment and package compatibility. | Compare a small Genesis slice in candidate machine-readable forms, including Unicode preservation, registers, notes, versification, round-trip behavior, and notices. Retain Markdown authoring. |
| D05 | How should translation/editorial review, disagreements, and source-critical uncertainty be governed? | Translation editors and reviewers; affects trusted release status. | Define a review rubric for one passage with lexical alternatives and an allusion; record reviewer decisions without deleting alternate evidence. |
| D06 | Which canon profiles, languages, accessibility target, and early learner audiences come first? | Product maintainers with affected users; determines sequencing, not exclusion from the long-term vision. | Choose an initial profile and complete-task accessibility checks; document additional profiles and their mapping needs. Do not hardcode prototype assumptions as universal. |
| D07 | How should private learner state, backups, export/erase, shared devices, optional sync, and group audience permissions work? | Product/privacy maintainers; blocks hosted personal-data features and shared-response workflows. | Specify local-only behavior first and test export/clear boundaries with synthetic responses. Seek explicit decisions before hosted sync or public sharing. |
| D08 | Which prototype components may be reused or published, if any? | User and relevant rights holders; no import permission is inferred from authorship of the overall file. | Review P1's exact corpus edition/code, P2's quotations/literal rendering, both studies' embedded fonts, and personal text. Approve a specific sanitized artifact only if publication is desired. |
| D09 | Which methods and recipes form the first delivery slice, with what staffing and dates? | Product/project maintainers; roadmap has dependency gates rather than invented schedules. | Once D01 is resolved, select a small coverage slice using stable entry IDs and acceptance evidence while retaining the full backlog. |
| D10 | How should optional collaboration, moderation, extension permissions, and AI-assisted study be governed? | Platform/community maintainers; these are future design questions, not current commitments to particular services. | Design one bounded shared-authoring/extension use case and review its permissions, source labeling, rights, privacy, and accessible fallbacks before implementation. |

When resolving a decision, record date, decision maker, alternatives, rationale, affected requirements and taxonomy entries, migration/rights implications, and verification evidence. Do not convert a proposed implementation detail into a founder decision without recording the distinction.
