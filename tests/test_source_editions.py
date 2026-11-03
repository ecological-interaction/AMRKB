"""AMRKB public-preservation regressions; corruptions use isolated temporary copies."""
import copy
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('amrkb_checks',ROOT/'scripts/validate_amrkb.py')
checks=importlib.util.module_from_spec(spec);spec.loader.exec_module(checks)

class SourceEditionTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.root=Path(self.temp.name)/'AMRKB'
        shutil.copytree(ROOT,self.root,ignore=shutil.ignore_patterns('.git','__pycache__'))
        self.data=checks.load(self.root/'AMRKB_Machine_Reference.json')
    def errors(self):return checks.check(self.data,self.root)
    def test_public_baseline_and_cli_disclose_unchecked_evidence(self):
        self.assertEqual(self.errors(),[])
        p=subprocess.run([sys.executable,'-B',str(self.root/'scripts/validate_amrkb.py')],capture_output=True,text=True)
        self.assertEqual(p.returncode,0,p.stdout+p.stderr)
        self.assertIn('NOT RUN',p.stdout)
    def test_duplicate_ids_and_changed_scientific_fields_fail(self):
        original=copy.deepcopy(self.data)
        self.data['records'][1]['id']=self.data['records'][0]['id'];self.assertTrue(self.errors())
        self.data=copy.deepcopy(original);self.data['records'][0]['label']+=' changed';self.assertTrue(self.errors())
        self.data=copy.deepcopy(original);self.data['memberships'][0]['project_status']='accepted';self.assertTrue(self.errors())
    def test_provenance_fingerprints_and_raw_text_boundary(self):
        original=copy.deepcopy(self.data)
        for change in [{'quotation_sha256':'0'*64},{'source_edition_id':'AMRKB-SRCED-0002'},{'original_text':'raw source text'}]:
            self.data=copy.deepcopy(original);self.data['provenance'][0].update(change);self.assertTrue(self.errors())
    def test_manifest_repins_and_ledger_gaps_fail(self):
        p=self.root/'AMRKB_Source_Editions.json';old=p.read_bytes();m=json.loads(old);m['editions'][0]['sha256']='0'*64;p.write_text(json.dumps(m));self.assertTrue(self.errors());p.write_bytes(old)
        p=self.root/'AMRKB_Source_Edition_Comparison.json';m=checks.load(p);m['entries'][2]['target_line_start']=216;p.write_text(json.dumps(m));self.assertTrue(self.errors())
    def test_scientific_parity_and_duplicate_heading_targets(self):
        self.assertEqual((self.root/'AMRKB_Scientific_Reference_Register.md').read_text(),checks.render_scientific(self.data))
        p=self.root/'README.md';old=p.read_text()
        for good,bad in [('nutrient-management-2','nutrient-management'),('crop-organisation-2','crop-organisation'),('tree-integration-1','tree-integration'),('livestock-integration-1','livestock-integration')]:
            p.write_text(old.replace('#'+good+')','#'+bad+')'));self.assertTrue(any('intended section' in e for e in self.errors()))
        p.write_text(old)
    def test_missing_archival_evidence_cannot_be_reported_passed(self):
        p=subprocess.run([sys.executable,'-B',str(self.root/'scripts/validate_amrkb.py'),'--evidence-root',str(Path(self.temp.name)/'missing')],capture_output=True,text=True)
        self.assertEqual(p.returncode,2);self.assertNotIn('checks: PASSED',p.stdout)
    def test_icaerus_spelling_preserves_ids_and_source_terms(self):
        r={x['id']:x for x in self.data['records']}
        self.assertEqual(r['AMRKB-REC-0286']['label'],'ICAERUS DDAL');self.assertEqual(r['AMRKB-REC-0287']['label'],'ICAERUS')
        self.assertIn('ICARUS',r['AMRKB-REC-0287']['original_terms'])
        self.assertEqual(len(self.data['records']),292)
    def test_display_translation_does_not_rewrite_research_prose(self):
        self.assertEqual(checks.cell('an unresolved hypothesis remains deferred'), 'an unresolved hypothesis remains deferred')
        self.assertEqual(checks.cell('unresolved; L1–1'), 'Unresolved; L1–1')
    def test_pending_acceptance_and_status_display_are_guarded(self):
        self.data['metadata']['maintenance']['owner_acceptance_of_stage_b']='accepted';self.assertTrue(self.errors())

if __name__=='__main__':unittest.main()
