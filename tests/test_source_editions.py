"""Edition reconciliation regressions; all corruptions use isolated temporary copies."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('amrkb_checks', ROOT / 'scripts/validate_amrkb.py')
checks = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checks)


class SourceEditionTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / 'AMRKB'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('.git', '__pycache__'))
        self.data = json.loads((self.root / 'AMRKB_Machine_Reference.json').read_text())

    def errors(self):
        return checks.check(self.data, self.root)

    def alter_json(self, name, change):
        path = self.root / name
        data = json.loads(path.read_text())
        change(data)
        path.write_text(json.dumps(data))

    def test_reconciled_baseline_and_documented_cli(self):
        self.assertEqual(self.errors(), [])
        result = subprocess.run([sys.executable, '-B', str(self.root / 'scripts/validate_amrkb.py')],
                                capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn('247-line extraction coverage, 393-line comparison coverage', result.stdout)

    def test_either_edition_tampering_is_rejected(self):
        for ident, (name, pin, count) in checks.EDITION_PINS.items():
            with self.subTest(edition=ident):
                path = self.root / name
                original = path.read_bytes()
                path.write_bytes(original + b' altered')
                self.assertTrue(any('Edition bytes/hash changed' in e for e in self.errors()))
                path.write_bytes(original)

    def test_provenance_requires_correct_edition_path_hash_and_quote(self):
        original = copy.deepcopy(self.data['provenance'][0])
        changes = [('source_edition_id', checks.CURRENT_EDITION), ('source_edition_id', None),
                   ('source_document', checks.EDITION_PINS[checks.CURRENT_EDITION][0]),
                   ('source_sha256', checks.EDITION_PINS[checks.CURRENT_EDITION][1]),
                   ('original_text', original['original_text'] + ' changed'), ('line_start', 9)]
        for key, value in changes:
            with self.subTest(field=key, value=value):
                self.data['provenance'][0] = dict(original, **{key: value})
                self.assertTrue(self.errors())
        self.data['provenance'][0] = original
        self.assertEqual(self.errors(), [])

    def test_audit_edition_and_coverage_cannot_be_relabelled(self):
        original = copy.deepcopy(self.data['source_audit'])
        self.data['source_audit'][0]['source_edition_id'] = checks.CURRENT_EDITION
        self.assertTrue(any('Wrong audit edition' in e for e in self.errors()))
        self.data['source_audit'] = copy.deepcopy(original)
        self.data['source_audit'][0]['line_end'] -= 1
        self.assertTrue(any('Audit/provenance span mismatch' in e for e in self.errors()))
        self.data['source_audit'] = copy.deepcopy(original[:-1])
        self.assertTrue(any('Incomplete final audit coverage' in e for e in self.errors()))
        self.data['source_audit'] = original
        self.data['metadata']['source_document']['edition_id'] = checks.CURRENT_EDITION
        self.assertTrue(self.errors())

    def test_manifest_repins_and_ledger_gaps_are_rejected(self):
        name = 'AMRKB_Source_Editions.json'
        path = self.root / name
        original = path.read_bytes()
        self.alter_json(name, lambda m: m['editions'][0].update(sha256='0' * 64))
        self.assertTrue(any('Edition declaration differs' in e for e in self.errors()))
        path.write_bytes(original)
        self.alter_json(name, lambda m: m['editions'].append(copy.deepcopy(m['editions'][0])))
        self.assertTrue(any('Duplicate/missing/unknown source editions' in e for e in self.errors()))
        path.write_bytes(original)
        name = 'AMRKB_Source_Edition_Comparison.json'
        path = self.root / name
        original = path.read_bytes()
        self.alter_json(name, lambda m: m['entries'][2].update(target_line_start=216))
        self.assertTrue(any('Comparison target gap/overlap' in e for e in self.errors()))
        path.write_bytes(original)
        self.alter_json(name, lambda m: m['entries'][4].update(source_text_sha256='0' * 64))
        self.assertTrue(any('Comparison correspondence/slice hash changed' in e for e in self.errors()))
        path.write_bytes(original)
        self.alter_json(name, lambda m: m.update(new_scientific_records=1))
        self.assertTrue(any('Unsupported comparison/intake claim' in e for e in self.errors()))
        path.write_bytes(original)
        self.alter_json(name, lambda m: m['entries'][0].update(supporting_extraction_references=['AMRKB-AUD-9999']))
        self.assertTrue(any('Unresolved comparison supporting reference' in e for e in self.errors()))

    def test_scientific_payloads_and_presentation_are_preserved(self):
        data = copy.deepcopy(self.data)
        payload = {k: data[k] for k in checks.COLLECTIONS}
        for entry in payload['provenance']:
            for key in ['source_document', 'source_sha256', 'source_edition_id']:
                entry.pop(key)
        for entry in payload['source_audit']:
            for key in ['source_document', 'source_sha256', 'source_edition_id']:
                entry.pop(key)
        actual = hashlib.sha256(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode()).hexdigest()
        self.assertEqual(actual, '43553c92d8c881f82da33dbf9cb1edd418d25b06478f66006dc2fa67d3157dac')
        scientific = (self.root / 'AMRKB_Scientific_Reference_Register.md').read_text()
        suffix = scientific.split('## Definitions and distinctions', 1)[1]
        self.assertEqual(hashlib.sha256(suffix.encode()).hexdigest(), '900700640bcfce2d545d616634020db2ffff2b36d40010f69c432a2db66e83ab')
        self.assertEqual(scientific, checks.render_scientific(self.data))


if __name__ == '__main__':
    unittest.main()
