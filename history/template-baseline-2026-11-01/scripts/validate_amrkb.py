"""Bounded checks for AMRKB's empty templates, not scientific or DRM certification."""

import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = ('records', 'classifications', 'relationships', 'references', 'provenance')
ORIGINAL_README_SHA256 = '4eb11eb8f9ead8d907007dc26d0c469d8dda78b1d250b9dab1b9205d10708ea1'


def check(data, schema, root=ROOT):
    errors = []
    if not isinstance(data, dict):
        return ['Machine reference must be an object.']
    required = {'$schema', 'metadata', *COLLECTIONS}
    if set(data) != required:
        errors.append('Machine-reference envelope differs from the empty-template schema.')
    metadata = data.get('metadata')
    if not isinstance(metadata, dict):
        return errors + ['Metadata must be an object.']
    for key, field_schema in schema['properties']['metadata']['properties'].items():
        value = metadata.get(key)
        if key not in metadata:
            errors.append(f'Missing template metadata: {key}')
        if field_schema.get('type') == 'string' and (not isinstance(value, str) or not value.strip()):
            errors.append(f'Expected nonempty metadata text: {key}')
        if field_schema.get('type') == 'object' and not isinstance(value, dict):
            errors.append(f'Expected metadata object: {key}')
        if 'const' in field_schema and (type(value) is not type(field_schema['const']) or value != field_schema['const']):
            errors.append(f'Unexpected template value: {key}')
    if data.get('$schema') != 'AMRKB_Machine_Reference.schema.json':
        errors.append('Wrong local schema reference.')
    for name in COLLECTIONS:
        if data.get(name) != []:
            errors.append(f'{name} must be an empty list before separately approved intake.')
    if metadata.get('attribution') != {
        'author': 'Jonathan Minchin', 'organisation': 'Ecological Interaction',
        'orcid': 'https://orcid.org/0000-0001-8152-1796',
    }:
        errors.append('Attribution differs from the approved template metadata.')
    protocol = (root / 'AMRKB_Research_Protocol.md').read_text(encoding='utf-8')
    start = '<!-- BEGIN PRESERVED ORIGINAL README -->\n'
    end = '<!-- END PRESERVED ORIGINAL README -->'
    if protocol.count(start) != 1 or protocol.count(end) != 1:
        errors.append('Original README preservation markers missing or duplicated.')
    else:
        original = protocol.split(start, 1)[1].split(end, 1)[0]
        if hashlib.sha256(original.encode('utf-8')).hexdigest() != ORIGINAL_README_SHA256:
            errors.append('Preserved original README has changed.')
    scientific = (root / 'AMRKB_Scientific_Reference_Register.md').read_text(encoding='utf-8')
    table_lines = [line for line in scientific.splitlines() if line.startswith('|')]
    expected = [
        '| Record ID | Name / source wording | Candidate entity distinction | Description / research scope | Context and limitations | Reference / provenance IDs | Review status |',
        '|---|---|---|---|---|---|---|',
        '| Reference / provenance ID | Original source / locator | Edition / date as documented | Supported record or assertion | Evidence and rights limitations | Review status |',
        '|---|---|---|---|---|---|',
    ]
    if table_lines != expected:
        errors.append('Scientific tables must contain only the approved headers/separators, no research rows.')
    for path in root.rglob('*.md'):
        if '.git' in path.relative_to(root).parts:
            continue
        for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
            url = urlsplit(target)
            if not url.scheme and not url.netloc and url.path:
                if not (path.parent / unquote(url.path)).is_file():
                    errors.append(f'Broken local link in {path.relative_to(root)}: {target}')
    return errors


def main():
    try:
        data = json.loads((ROOT / 'AMRKB_Machine_Reference.json').read_text(encoding='utf-8'))
        schema = json.loads((ROOT / 'AMRKB_Machine_Reference.schema.json').read_text(encoding='utf-8'))
        errors = check(data, schema)
        try:
            from jsonschema import Draft202012Validator
        except ImportError:
            print('Optional JSON Schema validation not run: jsonschema is not installed.')
        else:
            Draft202012Validator.check_schema(schema)
            errors.extend(f'JSON Schema: {e.message}' for e in Draft202012Validator(schema).iter_errors(data))
            print('Draft 2020-12 schema and instance checked.')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'Input/check failure: {exc}', file=sys.stderr)
        return 2
    if errors:
        for error in errors:
            print(error, file=sys.stderr)
        return 1
    print('Empty template, zero records, metadata, header-only tables, preserved scope and local links passed.')
    print('No scientific validity, DRM/MSP conformance, research intake or pilot approval is established.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
