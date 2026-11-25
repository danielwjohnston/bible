# Translation backfill and review

The complete readable base remains available while original-language drafting proceeds. The first recovered batch contains 150 AI-assisted chapter drafts: Exodus 1–40, Job 1–42, Matthew 1–28, Mark 1–16, and Luke 1–24. All five required sections are present. Each draft retains the previously published WEB Updated public-domain text in a separate **Reference Text (WEB Updated, Public Domain)** section and reader view.

These drafts are published for examination and revision. They are not certified completed translations, independently checked scholarly notes, or established human-authored copyright. Existing Genesis 1–6 remain the earlier multi-register layer; keeping them does not freeze them or certify their review history.

## What is checked

The [batch registry](backfill.json) pins the exact WLC/OSHB and SBLGNT revisions, source-file checksums, attribution, chapter membership, and verse labels used for structural validation. It distinguishes the drafts' declared source basis from the reference actually checked during takeover. The source cache's existence alone does not prove every generation-time source consultation or every linguistic claim.

All three registers in the 150 drafts contain the same 5,173 numbered source lines. Exodus and Job labels agree with WLC mapped through OSHB VerseMap.xml to English/KJV numbering. The three Gospel books agree with the selected SBLGNT verse labels. Ten numbered verses present in the WEB reference are absent from this SBLGNT base: Matthew 17:21, 18:11, 23:14; Mark 7:16, 9:44, 9:46, 11:26, 15:28; Luke 17:36, 23:17. The registry records those differences. Retaining the WEB comparison permits checking the alternative text without fabricating a reading in the chosen source.

Structural coverage does not establish semantic fidelity. A reviewer still needs to examine translation choices, idioms, grammar, register distinctions, allusions, and the evidence for specific historical/manuscript assertions. In particular, a claim about an edition or witness not included among the checked references must not be reported as independently verified.

## Review stages

1. **Draft:** preserve AI-assistance disclosure, declared source basis, pinned validation reference, and public-domain comparison text.
2. **Structural check:** verify sections, ordered verse labels, edition differences, stable chapter IDs, and unchanged comparison text.
3. **Linguistic and evidence review:** compare source meaning and interpretive claims with the actual primary texts; record corrections and unresolved alternatives.
4. **Human editorial contribution:** record substantive human translation/editing decisions, authorship, and reviewer identity/consent where appropriate. Do not infer human authorship from a submitted prompt or a model's self-description.
5. **Release decision:** record which rights can be licensed, actual review evidence, and remaining limitations before promoting draft status. Revision remains possible afterward.

The reader labels drafts explicitly and unlocks the same register controls for reading them. Choosing **WEB Reference (PD)** changes the provenance badge and hides draft notes, so commentary is not attributed to the reference edition.

## Copyleft and AI-assisted drafting

The project's existing CC BY-SA 4.0 commitment remains. That license can cover only rights a contributor actually holds. The U.S. Copyright Office's [AI copyrightability report announcement](https://copyright.gov/newsnet/2025/1060.html) distinguishes human expressive contributions from prompting alone. Human creative selection, arrangement, or modifications can be relevant, but publication of raw AI output under a license label does not itself establish protectable human authorship. This is a material limitation for the goal of a genuinely reciprocal corpus; it is not resolved by renaming a draft “original.” Applicable law and contribution-specific facts still need review.

Public-domain reference prose remains public domain. OSHB annotation data and SBLGNT attribution obligations remain separate. No new software license is selected by this batch.

Run `python3 tools/check_corpus.py` to check the published structure and comparison-text integrity. This local check does not certify translation accuracy or copyrightability. Source meaning, scholarly-note review, and human editorial review remain explicitly pending in the registry.
