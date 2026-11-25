#!/usr/bin/env python3
"""Check corpus coverage, draft labels, and retained reference text without network I/O."""
import hashlib
import importlib.util
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('bible_reader', ROOT / 'build_reader.py')
reader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)

def require(condition, message):
    if not condition:
        raise ValueError(message)

def main():
    registry = json.loads((ROOT / 'docs/translation/backfill.json').read_text())
    chapters = reader.collect_chapters()
    require(len(chapters) == 1392, 'Complete base coverage changed; review the declared corpus manifest.')
    require(len({c['id'] for c in chapters}) == len(chapters), 'Duplicate chapter identity.')
    require(len({(c['testament'], c['book_slug']) for c in chapters}) == 84, 'Book-entry coverage changed.')
    by_path = {f"{c['testament']}/{c['book_slug']}/{c['stem']}.md": c for c in chapters}
    seen = set()
    lines = 0
    for item in registry['chapters']:
        path = item['path']
        require(path not in seen, 'Duplicate registry path: '+path)
        seen.add(path)
        require(item['source_id'] in registry['sources'], 'Unknown source: '+path)
        chapter = by_path[path]
        require(chapter['status'] == 'translation-draft', 'Draft status missing: '+path)
        require(all(chapter['sections'].get(k, '').strip() for k in reader.PHASE2_SECTIONS), 'Required section missing: '+path)
        for register in reader.PHASE2_SECTIONS[:3]:
            labels = [int(x) for x in re.findall(r'^\*\*(\d+)\*\*', chapter['sections'][register], re.M)]
            require(labels == item['numbered_verse_labels'], 'Verse labels changed: '+path+' '+register)
        reference = chapter['sections'][item['reference_section']]
        require(hashlib.sha256(reference.encode()).hexdigest() == item['reference_body_sha256'], 'Reference text changed: '+path)
        require('Public Domain' in item['reference_section'], 'Reference rights label missing: '+path)
        require(item['checks']['independent_semantic_review'] == 'pending', 'Review-state transition requires evidence and a release check: '+path)
        lines += len(item['numbered_verse_labels'])
    require(seen == {path for path, chapter in by_path.items() if chapter['status'] == 'translation-draft'}, 'Draft registry and corpus membership differ.')
    require(all(any(body.strip() for body in c['sections'].values()) for c in chapters), 'Empty content record.')
    print(json.dumps({'content_records':len(chapters),'book_entries':84,'checked_drafts':len(seen),'draft_source_verse_lines':lines,'reference_text_integrity':'passed','semantic_review':'pending'}))

if __name__ == '__main__':
    main()
