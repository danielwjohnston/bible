# Copyleft corpus and licensing infrastructure

## Existing commitment and intended outcome

The user is creating a genuinely copyleft Bible corpus because reusable Scripture infrastructure needs reciprocal freedoms in the text itself. The goal is an original English translation from Hebrew, Aramaic, and Greek with reusable registers, notes, alignments, and study structures. Downstream readers, translators, teachers, developers, and publishers should be able to build on covered work while preserving its applicable reciprocal terms.

At the inspected repository revision, [LICENSE](../LICENSE), [README](../README.md), and [CONTRIBUTING](../CONTRIBUTING.md) already select **CC BY-SA 4.0**. That is an existing project choice, not an undecided proposal. This documentation preserves those files' existing terms and makes no new grant for third-party material. The earlier conversation's suggestion that the content license had not been selected is superseded by the repository evidence.

## Public domain, share-alike content, and software are distinct

Public-domain source text is useful input, but it supplies no share-alike obligation. Adding a license label does not create new rights in unchanged public-domain material. Original protectable translation and editorial contributions can carry the project's reciprocal terms; identify them separately from the underlying source.

For covered material, CC BY-SA 4.0 provides sharing and adaptation permissions, attribution/change-notice conditions, and reciprocal terms when adapted material is shared. Its scope follows the rights the licensor actually controls. Exceptions, public-domain elements, collection boundaries, and compatible-license provisions mean that the README's broad “all derivative works” language must be read with the actual legal terms. Packaging unrelated material together does not automatically relicense it. These distinctions follow the [CC BY-SA 4.0 legal code](https://creativecommons.org/licenses/by-sa/4.0/legalcode.en), especially sections 1–4.

Code and content require separate analysis. Creative Commons [recommends software-specific licenses for software](https://creativecommons.org/faq/#can-i-apply-a-creative-commons-license-to-software). GPL or AGPL could be evaluated for future application code, including whether network-service source obligations are desired. Neither has been adopted here. The existing repository-wide notices remain in place until an authorized, contribution-aware decision establishes scope; do not silently relicense the builder, embedded reader scripts, or other existing work. A software license does not grant rights to an embedded Bible corpus.

## Rights layers to maintain separately

| Layer | Project treatment / outstanding work |
| --- | --- |
| Ancient text and modern source editions | Identify edition and exact digital artifact; distinguish underlying public-domain text from editorial, apparatus, transcription, and database rights. |
| Original translation and registers | Existing CC BY-SA 4.0 commitment; record authorship, sources, adaptations, reviewer status, and changes. |
| Translation methodology | Document editorial principles, terminology, register tradeoffs, uncertainty, and review procedure independently of translation output. |
| Lexical, morphology, alignment, and other datasets | Track each dataset/version and its component license; annotations do not inherit rights merely from the text they describe. |
| Study materials and documentation | Record authorship, quotation sources, interpretation status, attribution, and applicable reciprocal terms for original contributions. |
| Software and generated packages | Preserve existing notices; decide prospective software licensing explicitly. Package code, content, and assets with distinct component notices. |
| Fonts, images, audio, video, maps, and recordings | Clear rights to each component and derivative use; performer/voice and privacy rights may require separate records. |
| Personal responses and private source documents | Private by default; excluded from public corpus, template, and analytics exports unless deliberately selected for a specified audience. |

## Source inventory: declared choices are not import evidence

The existing README names these sources. The six chapter files do not by themselves establish which exact editions, revisions, or digital artifacts were used. The following is a starting inventory, **not certification of the translation's provenance**. Upstream statements were checked on 2026-11-24.

| Source named in repository | Primary evidence | Required follow-through |
| --- | --- | --- |
| Westminster Leningrad Codex / WLC | The OSHB [README](https://github.com/openscriptures/morphhb/blob/master/README.md) and [license](https://github.com/openscriptures/morphhb/blob/master/LICENSE.md) distinguish public-domain WLC text from the project's annotations. | Pin actual WLC edition/digital version, acquisition, checksum, and transformations; preserve any source notices. |
| Open Scriptures Hebrew Bible / OSHB | Those upstream files state CC BY 4.0 for lemma/morphology data, with OSHB attribution. This is permissive attribution licensing, not share-alike. | Record which data fields are used and required attribution. Do not label every OSHB component public domain or original to this project. |
| SBL Greek New Testament / SBLGNT | The current [publisher repository README](https://github.com/Faithlife/SBLGNT/blob/master/README.md) states CC BY 4.0 and lists a 2022 license update. | Pin the exact edition/revision and corresponding terms; older downloaded releases may have different notices. Separate text, apparatus, and supplementary datasets. |
| Nestle 1904 | Named in this project's README; no exact digital artifact/version or associated rights evidence has been established in this inspection. | Select and verify the precise source rather than treating the historical edition name as proof that every modern digital derivative is unrestricted. |
| BLB and named translations in prototypes | See the private [prototype disposition](PROTOTYPES.md#rights-and-privacy-disposition). | Keep source files private and outside releases until exact component provenance and privacy review pass. |

These source descriptions do not establish that no other copyleft Bible exists. The documented fact is the user's infrastructure goal and this repository's chosen approach, not a surveyed claim about all existing translations.

## Proposed provenance record

For every imported or newly authored component, maintain: stable component ID; type and language; title/edition/version; author and rights holder; source URL and retrieval date; original artifact checksum; license identifier and terms URL; required attribution/notices; public-domain basis and relevant jurisdiction if claimed; permitted transformations and compatibility review; changes made; related source/target passage IDs; translator/editor/reviewer; review status; privacy status; approved package destinations.

For corpus releases also identify the translation revision, canon/versification profile, register, incomplete sections, and which annotations were independently reviewed. Rights records should be exportable alongside content, not only readable on a hosted website.

## Release gates

1. Inventory exact source artifacts and components before copying or adapting them. Retain upstream notices and evidence; flag unknowns explicitly.
2. Verify provenance and permission for the intended redistribution and transformation, including embedded quotations and assets. Quarantine uncertain inputs from distributable packages.
3. Establish contributor authorship/authority and preserve the existing contribution terms. Record exceptions and material that cannot be relicensed by this project.
4. Separate translation, observations, lexical data, interpretation, and application. Review claims of originality and source fidelity rather than assuming a fresh translation label proves them.
5. Generate component-level attribution and license notices for corpus, study, print, audio, and software packages. Preserve source revisions and change notices through export.
6. Review privacy separately from copyright. Removing an asset does not clear personal text; having copyright permission does not authorize exposing private responses.
7. Publish only the reviewed package and its declared coverage. Record unresolved rights questions and withhold affected components rather than representing them as cleared.

Maintainers must resolve source-specific uncertainties with appropriate rights expertise before making a release claim. This roadmap does not alter the legal terms or substitute generic assumptions for source evidence.
