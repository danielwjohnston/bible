# Documentation verification and limitations

## Inspection baseline

Repository: [danielwjohnston/bible](https://github.com/danielwjohnston/bible). Baseline: [7f7e2435508969efe1653f89c09aa7e7940ad1da](https://github.com/danielwjohnston/bible/commit/7f7e2435508969efe1653f89c09aa7e7940ad1da), inspected 2026-11-24.

The root listing contained README.md, CONTRIBUTING.md, LICENSE, build_reader.py, dist/, and ot/. The inspected corpus contained Genesis 1–6, each using the five existing chapter sections. The generated reader also contained those six chapters. No New Testament directory was present in that baseline; the original README structure is an intended layout, not evidence of a completed Bible. No repository AGENTS.md or workflow configuration appeared in the inspected root listing.

The original overview, contribution guide, license, builder, six chapter files, and generated reader were read. Prototype inspection was limited to the three exact attachments identified by filename, size, and SHA-256 in [PROTOTYPES.md](PROTOTYPES.md). No broad local or cloud-storage search was needed.

## Checks for this documentation change

- Existing tracked files remain byte-for-byte unchanged except README.md, whose original bytes are preserved as an exact prefix before the appended documentation section. LICENSE and CONTRIBUTING.md are unchanged.
- New repository deliverables are Markdown documentation only. No HTML prototypes, embedded Bible payloads, fonts, images, private responses, temporary attachment paths, or original script files are added.
- Local Markdown file links and named anchors are checked, including links from the overview into the documentation set. This is a local link check, not a guarantee that external sites remain available.
- Complete recovered taxonomy bullets are compared in order against the returned source excerpt. The cut trailing bullet is omitted. Categories 1–14 appear complete in the returned excerpt; category 15 is partial. The full 82-category source is **not verified**.
- The unchanged offline builder is run against a temporary copy of the existing chapters, and its generated reader is compared byte-for-byte with the committed reader. The working corpus and generated artifact are not rewritten.
- Requirement IDs and prototype/milestone mappings receive a consistency review. Requirements are explicitly future-facing, and prototype descriptions state the limits of static inspection.

The initial link pass identified this verification page as not yet created; it was added before the final pass. Remote PR/commit identities and file readback are reported in the delivery response, since the commit containing this page cannot contain its own hash.

## What remains unverified

This is a documentation change, not a runtime implementation or a completed rights audit. It does not establish translation fidelity, source edition provenance, originality of every contribution, theological correctness, prototype runtime behavior, accessibility conformance, offline speech availability, or rights to publish prototype content/assets. The upstream license statements cited are starting evidence; actual imported versions still need component-level review.

The major completion blocker is [D01](DECISIONS.md#open-decisions): the full original taxonomy is unavailable through the bounded history export. A draft documentation PR must retain this limitation until the complete source is supplied and reconciled. New guesses or an independently written 82-category list cannot satisfy that requirement.

Other unresolved product and rights decisions are recorded with next steps in [DECISIONS.md](DECISIONS.md). Milestone exit criteria in [ROADMAP.md](ROADMAP.md) prevent incomplete documentation or prototype evidence from being mistaken for a fully delivered study platform.
