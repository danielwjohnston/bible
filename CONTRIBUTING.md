# Contributing

Original contributions are offered under **CC BY-SA 4.0** to the extent the contributor holds rights to license them. Upstream public-domain text and separately licensed source data retain their own status and attribution requirements. A license notice does not establish copyright in raw AI output. Follow the maintainer's direct-to-`main` workflow; do not create working branches or pull requests unless requested.

## Chapter Format

Each chapter file (`<testament>/<book>/<chapter>.md`, zero-padded) includes:
1. **Word-for-Word** — Preserves original word order, particles, and idioms.
2. **Clear & Faithful** — Bridges literal accuracy with natural contemporary English.
3. **Everyday English** — Natural, conversational English for accessible reading.
4. **Crossings & Lexical Notes** — Semantic range, root meanings, and alternative renderings for key terms.
5. **Supplemental Texts & Allusions** — Inline quotes/allusions when the text echoes or cites another passage.

## Draft and Review Status

New AI-assisted translations must include `Translation status: draft` in the header, identify their source basis and pinned validation references, and retain the existing public-domain comparison text until an explicit review/release decision. Record actual structural checks separately from linguistic review, scholarly-note verification, and human editorial authorship. Five section headings alone do not establish completed translation or review.

Use the [translation workflow](docs/translation/README.md) and [batch registry](docs/translation/backfill.json). Run `python3 tools/check_corpus.py`, the relevant tests, and `python3 build_reader.py` before publishing. Record unresolved edition differences rather than filling missing readings without evidence.
