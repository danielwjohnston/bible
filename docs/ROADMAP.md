# Development roadmap

The full taxonomy is a continuing product requirement. Milestones sequence delivery; later milestones are not optional deletions from scope. Dates, staffing, and budgets are not established. Ship independently reviewable slices and preserve an offline path throughout.

## M0 — recover and reconcile the vision

**Requirements:** TAX-01, TAX-02, CMP-03. **Dependency:** supplied baseline and explicit source status.

**Documentation delivered:** all 82 categories and 4,588 category-list entries from the supplied reconstruction are preserved in human-readable and machine-readable forms. The Markdown/JSON/HTML views agree, and all 743 complete entries in the available original excerpt match exactly. The coverage register maps every category and entry by inheritance to requirements and milestones with planned implementation status. The generator, calculator, diagrams, lifecycle, objective mappings, and recommended methods are retained separately. No source categories were generated to fill gaps.

**Remaining fidelity gate:** the supplied files identify themselves as manually reconstructed, not independently verified against a direct transcript. Compare the remaining source against a direct original response if available, or record an explicit decision adopting the supplied reconstruction as the product baseline while retaining its provenance caveat. All supplied content is documented; original fidelity beyond the verified overlap remains D01. Keep the documentation PR draft pending that source decision. Later additions must be identified as extensions, with stable identifiers and no silent omissions.

## M1 — establish a trustworthy copyleft corpus foundation

**Requirements:** COR-01–COR-06, RIGHTS-01–RIGHTS-02, OPS-01. **Dependency:** maintainers' source/rights decisions; can proceed while M0 is pending.

Preserve the existing Markdown chapter contract and three registers. Inventory exact source editions and digital artifacts; create provenance and attribution records; define translation/review principles, passage identities, canon/versification profiles, and source-token alignment rules. Select a machine-readable export format through D04 without discarding authoring sources. Record actual corpus coverage and editorial review status. Resolve software/content boundaries before adding new licensed components.

**Prototype trace:** P1 establishes why a corpus adapter must be independent of the reader; P2 and P3 establish why quotations, lexical notes, and interpretations need separate provenance.

**Exit:** one reviewed corpus slice rebuilds into a human-readable and machine-readable release with stable references, rights notices, change history, register alignment limits, and explicit missing/unreviewed content. A corpus release gate fails if required source rights remain unknown.

## M2 — portable reader, schema, and method registry

**Requirements:** TAX-02, CMP-01 foundation, READ-01–READ-04, EXT-01–EXT-02 foundation, ACC-01, OPS-01. **Dependencies:** M1 identities and approved sample corpus; full TAX-01 is required before claiming baseline coverage.

Retain single-file offline reading; add reusable reference parsing, chapter navigation, scoped bounded search, deep links, copy attribution, and register comparison as rights permit. Define study/recipe and taxonomy schemas with stable IDs, migration rules, dimension tags, and readable fallbacks. Use neutral or cleared fixtures rather than importing prototype text. Validate offline behavior and complete keyboard/screen-reader tasks. Document search limits and canon assumptions.

**Prototype trace:** P1 navigation/search/hash/copy patterns, existing builder and reader, P2 labeled rendering selection.

**Exit:** a corpus revision and study recipe survive export/import with references and notices intact; a new taxonomy method can be registered without changing the corpus; reading and search work offline against the selected package.

## M3 — reusable authored studies and learner activities

**Requirements:** AUTH-01–AUTH-02, INV-01–INV-03, SUBJ-01, CMP-01–CMP-04, REP-01–REP-02 initial forms, LEARN-01–LEARN-02 initial forms, FORM-01, PRIV-01, ACC-01–ACC-02, RIGHTS-01. **Dependencies:** M1–M2, private-data policy D07, approved fixtures.

Create reusable thematic and statement-linked templates, named lens views, lexical/expository annotations, context/cautions, linked evidence, and guided/full disclosure. Add text/audio interaction where supported, progressive recall, typed recall, quiz/matching, discussion, prayer, journaling, and practice prompts. Keep responses separate from the template. Add deliberate export and erase workflows with clear storage limitations. Verify feedback and accessibility, including focus restoration and reduced motion.

**Prototype trace:** P2 multidimensional theme study and activities; P3 statement-to-evidence authoring and contextual cautions.

**Exit:** two newly authored studies use the same content schema and reusable behaviors, with a traceable corpus revision, interpretations labeled, notices included, private responses excluded from template export, and equivalent accessible paths. No personal source prototype needs to be published to meet this gate.

## M4 — deeper analysis, knowledge, and learning workflows

**Requirements:** COR-03 advanced alignment, INV-01–INV-03 expansion, SUBJ-01, MODEL-01, KNOW-01, REP-01, LEARN-01–LEARN-02 expansion, EXT-01, CMP-03. **Dependencies:** reviewed datasets and representation-specific evidence.

Expand lexical/morphological and discourse analysis, historical/cultural and reception lenses, comparison of arguments, source review, typed knowledge relationships, concept/argument maps, timelines, geography, and structured research. Add spaced review and reusable memory systems with user control. Each visualization remains connected to passages, provenance, perspective, uncertainty, and a textual equivalent. Extend the coverage register per original entry, rather than declaring a category complete after one demo.

**Prototype trace:** P2 lens/relationship structures and memory activities; P3 original-language notes, word list, and statement support.

**Exit:** evidence-linked analytical and learning workflows cover a documented increment of the reconciled taxonomy and can be independently inspected and reproduced. Unsupported dates, geography, alignments, and interpretations are explicitly marked.

## M5 — broader modalities, collaboration, and open ecosystem

**Requirements:** all remaining verified taxonomy entries; REP-02 expansion, GROUP-01, FORM-01 expansion, EXT-01–EXT-02, ACC-02, CMP-02–CMP-03. **Dependencies:** appropriate rights/privacy/security designs, extension interfaces, audience/moderation decisions.

Deliver remaining methods and meaningful combinations through portable activities and extensions: conversational/teaching practices, embodied/field activities, creative outputs, multimedia, simulation, models, and immersive representations where useful. Add optional collaboration, peer review, shared authoring, localization, and additional corpus/edition adapters. Preserve individual offline access and accessible alternatives. Publish extension contracts and contribution/review procedures. Do not require hosted accounts to access the core corpus.

**Prototype trace:** extend the prototypes' reusable structures rather than replicating their one-off documents. These broader capabilities are future vision, not capabilities established by P1–P3.

**Exit:** each newly supported entry has an inspectable activity, evidence, accessibility alternative, rights record, and validation; the complete baseline remains tracked. New categories can be added without invalidating old study packages.

## Continuous work and reporting

Translation proceeds canonically alongside platform work. Corpus expansion is not a substitute for editorial review, and reader expansion is not a substitute for corpus rights. Track translated, reviewed, aligned, and released coverage separately.

At each milestone publish: corpus revision/coverage; taxonomy baseline and denominator (currently 82 categories/4,588 category-list entries), source-fidelity status, requirements implemented and verified; prototype-derived capabilities delivered; accessibility tasks checked; rights/attribution status; privacy behavior; deferred entries and open decisions. The [coverage register](TAXONOMY_COVERAGE.md) assigns every category and entry by inheritance to milestones. Documentation coverage is complete against the supplied reconstruction; implemented and verified coverage require separate evidence. Do not label the whole taxonomy implemented from a handful of sample recipes.

Use [DECISIONS.md](DECISIONS.md) to record choices that change scope or prerequisites. Assign dates and owners only when maintainers establish them. A later minimum viable release may be narrow, but must link to the continuing complete vision and state exactly what it supports.
