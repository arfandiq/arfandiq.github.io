#!/usr/bin/env python3
"""Exercise folder discovery and edits in a temporary copy, never live photos."""
import json, shutil, tempfile, unittest
from pathlib import Path
from urllib.parse import unquote
import build

class PhotoWorkflowTest(unittest.TestCase):
    def setUp(self):
        self.original=build.ROOT
        self.temp=tempfile.TemporaryDirectory()
        self.root=Path(self.temp.name)
        shutil.copytree(self.original/'data',self.root/'data')
        (self.root/'assets/js').mkdir(parents=True)
        build.ROOT=self.root
    def tearDown(self):
        build.ROOT=self.original;self.temp.cleanup()
    def test_drop_sort_metadata_delete(self):
        first=build.build()
        p=first['projects'][0]
        self.assertEqual(p['photos'],[])
        folder=self.root/p['photoFolder']
        for name in ('10-result.JPG','2-build.png','00 cover.webp','notes.txt'):(folder/name).write_bytes(b'fixture')
        (folder/'metadata.json').write_text(json.dumps({'00 cover.webp':{'alt':'Original ROV photograph','caption':'Assembly'}}))
        updated=build.build()['projects'][0]['photos']
        self.assertEqual([Path(unquote(p['src'])).name for p in updated],['00 cover.webp','2-build.png','10-result.JPG'])
        self.assertIn('%20',updated[0]['src'])
        self.assertEqual(updated[0]['caption'],'Assembly')
        for name in ('10-result.JPG','2-build.png','00 cover.webp'):(folder/name).unlink()
        self.assertEqual(build.build()['projects'][0]['photos'],[])
    def test_new_project_and_photo_folder(self):
        file=self.root/'data/projects.json';data=json.loads(file.read_text())
        new=dict(data[0],id='new-research',title='New research',featured=False,photoFolder='assets/photos/projects/new-research')
        data.append(new);file.write_text(json.dumps(data))
        result=build.build()
        self.assertEqual(len(result['projects']),14)
        self.assertTrue((self.root/new['photoFolder']).is_dir())
    def test_duplicate_id_is_rejected(self):
        file=self.root/'data/projects.json';data=json.loads(file.read_text());data.append(data[0]);file.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError,'Duplicate id'):build.build()
    def test_outside_photo_folder_is_rejected(self):
        file=self.root/'data/projects.json';data=json.loads(file.read_text());data[0]['photoFolder']='assets/photos/../../outside';file.write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError,'inside assets/photos'):build.build()

if __name__=='__main__':unittest.main()
