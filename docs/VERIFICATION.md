# Documentation verification and limitations

## Inspection baseline

Repository: [danielwjohnston/bible](https://github.com/danielwjohnston/bible). Baseline: [7f7e2435508969efe1653f89c09aa7e7940ad1da](https://github.com/danielwjohnston/bible/commit/7f7e2435508969efe1653f89c09aa7e7940ad1da), inspected 2026-11-24.

The root listing contained README.md, CONTRIBUTING.md, LICENSE, build_reader.py, dist/, and ot/. The inspected corpus contained Genesis 1–6, each using the five existing chapter sections. The generated reader also contained those six chapters. No New Testament directory was present in that baseline; the original README structure is an intended layout, not evidence of a completed Bible. No repository AGENTS.md or workflow configuration appeared in the inspected root listing.

The original overview, contribution guide, license, builder, six chapter files, and generated reader were read. Prototype inspection was limited to the three exact attachments identified by filename, size, and SHA-256 in [PROTOTYPES.md](PROTOTYPES.md). No broad local or cloud-storage search was needed.

## Checks for this documentation change

- Existing tracked files remain byte-for-byte unchanged except README.md, whose original bytes are preserved as an exact prefix before the appended documentation section. LICENSE and CONTRIBUTING.md are unchanged.
- New repository deliverables are Markdown documentation and one derived JSON taxonomy registry. No HTML prototypes, embedded Bible payloads, fonts, images, private responses, temporary attachment paths, or original script files are added. The supplied taxonomy HTML remains local and its JavaScript was not executed.
- Local Markdown file links and named anchors are checked, including links from the overview into the documentation set. This is a local link check, not a guarantee that external sites remain available.
- All 82 category titles and all 4,588 category-list entries agree across the supplied Markdown/JSON/HTML views. All 82 generator choices agree separately. The derived registry preserves all labels, order, category memberships, source blocks, and stable unique entry IDs, with planning coverage for every category and entry. Category 82 is a generator component with zero category-list entries, rather than an artificial 82-entry addition to the 4,588 count.
- All 743 complete bullets in the original 20,000-character conversation excerpt match the supplied reconstruction exactly and in order. This verifies the overlap, not original-transcript fidelity for the rest. The supplied files explicitly label themselves manually reconstructed and not independently verified against a direct transcript; that warning and the exact source fingerprints are retained.
- Privacy review removes one paragraph about prior personal conversation topics and generalizes its heading. Category titles/entries, method descriptions/cautions, objective mappings, recommended approaches, diagrams, lifecycle, and composition definitions remain intact. The source-specific instruction to use the local HTML edition is clarified because that artifact is not published.
- The unchanged offline builder is run against a temporary copy of the existing chapters, and its generated reader is compared byte-for-byte with the committed reader. The working corpus and generated artifact are not rewritten.
- Requirement IDs and prototype/milestone mappings receive a consistency review. Requirements are explicitly future-facing, and prototype descriptions state the limits of static inspection.

The complete supplied baseline is `supplied-reconstruction-2026-11-24-v1`. It contains 23 parts, 82 categories, 4,588 category-list entries, 82 generator options across six axes, 24 objective-to-method pairs, 10 recommended approaches, and an 11-stage learning lifecycle. Counts are artifact inventory, not evidence of product implementation or pedagogical validity. Remote PR/commit identities and file readback are reported in the delivery response, since the commit containing this page cannot contain its own hash.

## What remains unverified

This is a documentation change, not a runtime implementation or a completed rights audit. It does not establish translation fidelity, source edition provenance, originality of every contribution, theological correctness, prototype runtime behavior, accessibility conformance, offline speech availability, or rights to publish prototype content/assets. The upstream license statements cited are starting evidence; actual imported versions still need component-level review.

The missing-category gap is resolved against the complete supplied reconstruction. [D01](DECISIONS.md#open-decisions) now records the remaining fidelity question: compare a direct original transcript if available, or explicitly adopt the supplied reconstruction as the product baseline while retaining its provenance warning. The documentation PR remains draft pending that source decision; it must not claim certified verbatim fidelity beyond the 743-entry verified overlap. No new taxonomy was generated to replace the supplied material.

Other unresolved product and rights decisions are recorded with next steps in [DECISIONS.md](DECISIONS.md). Milestone exit criteria in [ROADMAP.md](ROADMAP.md) prevent incomplete documentation or prototype evidence from being mistaken for a fully delivered study platform.
