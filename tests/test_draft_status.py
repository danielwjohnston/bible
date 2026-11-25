import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('reader', ROOT / 'build_reader.py')
reader = importlib.util.module_from_spec(spec)
spec.loader.exec_module(reader)

class DraftStatusTests(unittest.TestCase):
    def parse(self, header, sections):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / 'exodus' / '01.md'
            path.parent.mkdir()
            path.write_text('# Exodus 1\n\n' + header + '\n\n' + '\n\n'.join('## '+name+'\n\n'+text for name,text in sections.items()))
            return reader.parse_chapter(path, 'ot')

    def test_draft_is_not_promoted_by_complete_headings(self):
        sections = {name:'**1** A draft reading.' for name in reader.PHASE2_SECTIONS}
        sections['Reference Text (WEB Updated, Public Domain)'] = '**1** Existing reference.'
        chapter = self.parse('*Translation status: draft. Review pending.*', sections)
        self.assertEqual(chapter['status'], 'translation-draft')
        self.assertEqual(chapter['sections']['Reference Text (WEB Updated, Public Domain)'], '**1** Existing reference.')

    def test_draft_word_in_verse_does_not_change_base_status(self):
        chapter = self.parse('*Provisional Public Domain base.*', {'Base Text (Interim)':'**1** A draft of a letter.'})
        self.assertEqual(chapter['status'], 'provisional-pd')

    def test_legacy_sections_keep_their_existing_classification(self):
        chapter = self.parse('*Existing project translation.*', {name:'Some content.' for name in reader.PHASE2_SECTIONS})
        self.assertEqual(chapter['status'], 'original-cc-by-sa')

    def test_partial_draft_is_never_classified_as_a_finished_layer(self):
        chapter = self.parse('*Translation status: draft. Review pending.*', {'Clear & Faithful':'**1** A draft.'})
        self.assertEqual(chapter['status'], 'translation-draft')

if __name__ == '__main__':
    unittest.main()
