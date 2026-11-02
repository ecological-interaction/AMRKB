"""Check AMRKB's documentary extraction; no scientific verification or DRM adoption."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = ('records', 'classifications', 'memberships', 'relationships', 'references', 'provenance', 'themes', 'applications', 'decisions', 'source_audit')
ORIGINAL_README_SHA256 = '4eb11eb8f9ead8d907007dc26d0c469d8dda78b1d250b9dab1b9205d10708ea1'
SOURCE_SHA256 = '1902b7263a0df34084b58532f01fa16cc70497d373a1332e568e171905b18faf'


def cell(value):
    return str(value).replace('|', '&#124;').replace('\n', '<br>')


def render_scientific(data):
    """Deterministic presentation of the sole structured authority, not a second register."""
    byid = {r['id']: r for name in COLLECTIONS for r in data[name]}
    pro = {r['id']: r for r in data['provenance']}
    def loc(ids):
        return '; '.join(f"L{pro[i]['line_start']}–{pro[i]['line_end']}" for i in ids)
    def table(headers, rows):
        return '| ' + ' | '.join(headers) + ' |\n|' + '|'.join('---' for _ in headers) + '|\n' + ''.join('| ' + ' | '.join(cell(c) for c in row) + ' |\n' for row in rows) + '\n'
    text = f'''# AMRKB — Scientific Reference Register

**Document version:** {data['metadata']['document_version']} · **Work in Progress — Academic Research Resource**
**Maintenance revision:** {data['metadata']['maintenance']['revision']} · documentation only; scientific review pending.

Research by Jonathan Minchin, Ecological Interaction ([ORCID 0000-0001-8152-1796](https://orcid.org/0000-0001-8152-1796)).

## Reading key and source limits

This is the human presentation of the [authoritative Machine JSON](AMRKB_Machine_Reference.json).
The [Research Protocol](AMRKB_Research_Protocol.md) defines extraction, identity and review limits.
On {data['metadata']['source_document']['origin_confirmation']['confirmation_date']} the owner confirmed that both preserved incomplete editions originate
from the normal “{data['metadata']['source_document']['conversation_title']}” research conversation. This confirms origin, not authenticated
message metadata, speaker assignments, original dates or conversation completeness.

The [247-line extraction edition](history/20261101_AMRKB_Chat_History_Extraction_Edition.md)
is preserved unchanged; all 247 lines are accounted for and all L locators below
refer to that edition, not to authenticated message IDs. The
[current 393-line edition](history/20261101_AMRKB_Chat_History.md) was separately
compared across all 393 lines; comparison is not scientific extraction of every
line. Original conversation completeness remains unknown. See the
[source-edition reconciliation](AMRKB_Source_Edition_Reconciliation.md).

**Record status** describes the documentary entry's recorded inclusion/relevance;
a candidate is not an accepted agricultural fact. **Membership status** qualifies
a particular entry's association with a working group in its source context; it
is separate from record status and does not verify a classification. **Scientific
verification** remains `not_independently_verified`, regardless of relevance or
agreement to explore. Project decisions approve only their recorded scope.
Local IDs are documentary locators, not issued external identifiers. Repeated
family/function labels link the same entry, not newly verified entities.
No licence, release, DOI or field validation is assigned.

The source lacks authenticated per-message dates/speakers, detailed inventories
for families 1/2, detailed family-8 expansion and a completed bibliography.
Five methodological groups remain unnamed; certification placement, ICARUS
identity, lexical variants and mixed types remain unresolved. AgriFM/AgroGPT
are retained despite later omission. A request to repeat Precision/Computational
is not approval; missing content is not reconstructed. User agreement supports
exploration, not each example, membership or scientific claim. Scientific and
field-evidence review remains outstanding.

## Section navigation

[Definitions](#definitions-and-distinctions) · [Working families](#working-families-and-methodology-inventories) · [Cross-family functions](#cross-family-functional-organising-strategies) · [Candidate index](#complete-candidate-identity-index) · [Context](#historical-geographical-ecological-and-socioeconomic-context) · [Applications](#ecological-mechanisms-indicators-and-proposed-applications) · [Themes](#cross-cutting-research-and-application-domains) · [References](#named-references-and-bibliographic-gaps) · [Relationships](#candidate-relationships-and-assertion-limits) · [Open questions](#revisions-unresolved-questions-and-research-boundary).

## Definitions and distinctions

Modes, systems, methods, practices, technologies, ecological mechanisms and
indicators are distinct candidate representations. Agricultural approaches need
not occupy a unique level or family. Agroforestry is described as a land-use
system; agroecology as discipline, practices and social movement (L31).
These source-proposed distinctions are not a compulsory scientific hierarchy.

'''
    definitions = [c for c in data['classifications'] if c['classification_kind'] == 'candidate_entity_distinction']
    text += table(['Local definition ID', 'Distinction', 'Source definition', 'Status / provenance'], [(c['id'], c['label'], c['description'], c['project_status'] + '; ' + loc(c['provenance_ids'])) for c in definitions])
    text += '## Working families and methodology inventories\n\nThe eight source-labelled families overlap; no membership is required for every record. Functional subdivisions retain their source context rather than imply universal type equivalence. Methodology inventories are presented before finer technical review; the complete preferred order is not explicitly documented in the supplied file.\n\n'
    families = [c for c in data['classifications'] if c['classification_kind'] == 'working_family']
    for family in families:
        members = [m for m in data['memberships'] if m['classification_id'] == family['id']]
        unique = sorted({m['record_id'] for m in members})
        text += f"### {family['label']}\n\n{len(unique)} distinct candidate entries; {len(members)} source-qualified family associations. {family['description']}\n\n"
        if family == families[0] or family == families[1]:
            text += 'Only initial example entries are supplied. The later source refers to earlier family work, but its detailed methodology inventory is absent; no sub-methods were reconstructed.\n\n'
        elif family == families[-1]:
            text += 'Only the initial examples are supplied. Detailed expansion was deferred when cross-cutting exploration was selected.\n\n'
        group_ids = {m['classification_id'] for m in data['memberships'] if m['record_id'] in unique and byid[m['classification_id']]['classification_kind'] == 'family_functional_group'}
        # Only show functional groups whose provenance coincides with this family's later inventory.
        family_lines = {i for m in members for i in m['provenance_ids']}
        groups = [c for c in data['classifications'] if c['id'] in group_ids and set(c['provenance_ids']) & family_lines]
        for group in groups:
            text += f"#### {group['label']}\n\n{group['description']}\n\n"
            groupmembers = [m for m in data['memberships'] if m['classification_id'] == group['id']]
            text += table(['Entry ID', 'Original term', 'Type / evidence limitation', 'Source / project status'], [(byid[m['record_id']]['id'], byid[m['record_id']]['label'], 'Candidate inventory item; type unreviewed', loc(m['provenance_ids']) + '; ' + m['project_status']) for m in groupmembers])
        text += 'Initial family examples and any additional source occurrences:\n\n'
        text += table(['Entry ID', 'Term', 'Membership status', 'Provenance'], [(m['record_id'], byid[m['record_id']]['label'], m['project_status'], loc(m['provenance_ids'])) for m in members if m['project_status'] == 'assistant_proposed_association'])
    text += '## Cross-family functional organising strategies\n\nThe source proposes twelve ecological/productive functions. Their memberships are provisional and overlap family inventories.\n\n'
    for c in [c for c in data['classifications'] if c['classification_kind'] == 'cross_family_function']:
        text += f"### {c['label']}\n\n"
        text += table(['Entry ID', 'Term', 'Status', 'Provenance'], [(m['record_id'], byid[m['record_id']]['label'], m['project_status'], loc(m['provenance_ids'])) for m in data['memberships'] if m['classification_id'] == c['id']])
    text += '## Complete candidate identity index\n\nEvery documentary entry appears once in this index, including terms not assigned a family. Different source spellings and possibly equivalent labels remain separate; identical case-insensitive labels retain occurrence-specific types. This does not resolve homonyms or prove unique real-world identity.\n\n'
    text += table(['Entry ID', 'Original label', 'Record kind / candidate types', 'Project status', 'Source occurrences'], [(r['id'], r['label'], r['record_type'] + '; ' + ', '.join(r['candidate_entity_types']), r['project_status'], loc(r['provenance_ids'])) for r in data['records']])
    text += '## Historical, geographical, ecological and socioeconomic context\n\nThe scope includes historical emergence, spread, combination and transformation; technology, land tenure, energy, labour and ecological transformation provide comparative context (L99–106). It is not restricted to contemporary regenerative agriculture (L201–203). No origins, dates or regional distributions for individual approaches are invented.\n\n'
    text += table(['Dimension', 'Source description', 'Status / provenance'], [(c['label'], c['description'], c['project_status'] + '; ' + loc(c['provenance_ids'])) for c in data['classifications'] if c['classification_kind'] == 'research_dimension'])
    text += '## Ecological mechanisms, indicators and proposed applications\n\nThe source proposes the chain agricultural method → ecological mechanism → measurable indicator → ecological outcome → place-specific suitability (L54). This is a research model, not an implemented recommendation service or proof of causation. Worked examples below retain their qualifications; management effects require later evidence and context.\n\n'
    text += table(['Application / claim ID', 'Context or purpose', 'Explanation and qualification', 'Status / provenance'], [(r['id'], r['label'], r['description'], r['project_status'] + '; ' + loc(r['provenance_ids'])) for r in data['applications']])
    text += '## Cross-cutting research and application domains\n\nThe five domains were proposed for further exploration, not as new agricultural families. Open design and distributed manufacturing connect tools and knowledge; AI/LLM/agent methods, knowledge graphs and field evidence remain distinct. The unspecified five methodological groups in the final line are not inferred from these domains or from four earlier AI method terms.\n\n'
    text += table(['Theme ID', 'Domain', 'Source-supported rationale', 'Status / provenance'], [(r['id'], r['label'], r['description'], r['project_status'] + '; ' + loc(r['provenance_ids'])) for r in data['themes']])
    text += '## Named references and bibliographic gaps\n\nThese are named candidate programmes/tools/sources, not completed bibliographic citations. The source supplies no authors, publication titles, dates, DOI or URLs. Both source lists are retained: AgriFM and AgroGPT are not rejected by omission; ICARUS DDAL and ICARUS remain distinct. The promise of later references/field-evidence criteria is not an accomplished literature review.\n\n'
    text += table(['Reference ID', 'Name as supplied', 'Candidate entry', 'Evidence limitation', 'Provenance'], [(r['id'], r['label'], r['candidate_record_id'], r['bibliographic_status'], loc(r['provenance_ids'])) for r in data['references']])
    text += '## Candidate relationships and assertion limits\n\nThese local typed assertions identify contextual relevance only. They do not establish external record IDs, completed dataset bindings, a shared taxonomy or verified mechanism/outcome links.\n\n'
    text += table(['Assertion ID', 'Source', 'Relationship', 'Target', 'Status / provenance'], [(r['id'], byid[r['source_id']].get('label'), r['relationship_type'], byid[r['target_id']].get('label'), r['project_status'] + '; ' + loc(r['provenance_ids'])) for r in data['relationships']])
    text += '## Revisions, unresolved questions and research boundary\n\n'
    text += table(['Decision / issue ID', 'Subject', 'Disposition', 'Explanation', 'Provenance'], [(r['id'], r['label'], r['project_status'], r['description'], loc(r['provenance_ids'])) for r in data['decisions']])
    text += 'The [protocol audit crosswalk](AMRKB_Research_Protocol.md#source-to-destination-audit-crosswalk) accounts for every source span. No scientific verification, new literature, taxonomy redesign, cross-database harmonisation or publication follows automatically.\n'
    return text



EDITION_PINS = {
    'AMRKB-SRCED-0001': ('history/20261101_AMRKB_Chat_History_Extraction_Edition.md', SOURCE_SHA256, 247),
    'AMRKB-SRCED-0002': ('history/20261101_AMRKB_Chat_History.md', '333c42970b7d4268aca8a848fef633bcf7b215a0179ec74fa8fd40b15ca98bf7', 393),
}
EXTRACTION_EDITION = 'AMRKB-SRCED-0001'
CURRENT_EDITION = 'AMRKB-SRCED-0002'


def check_editions(root, require, known_ids):
    """Strict pinned editions plus complete comparison coverage, not new extraction."""
    manifest = json.loads((root / 'AMRKB_Source_Editions.json').read_text())
    require(manifest.get('manifest_version') == '0.1.0', 'Unsupported source-edition manifest.')
    require(manifest.get('extraction_edition_id') == EXTRACTION_EDITION and
            manifest.get('current_history_edition_id') == CURRENT_EDITION, 'Wrong edition roles.')
    declared = manifest['editions']
    require(len(declared) == 2 and {e['id'] for e in declared} == set(EDITION_PINS), 'Duplicate/missing/unknown source editions.')
    editions = {}
    for entry in declared:
        ident = entry['id']
        if ident not in EDITION_PINS:
            continue
        path, pin, count = EDITION_PINS[ident]
        require(entry['path'] == path and entry['sha256'] == pin and entry['line_count'] == count,
                f'Edition declaration differs from pinned edition: {ident}')
        # Read only the allowlisted path, never an unchecked manifest path.
        raw = (root / path).read_bytes()
        require(hashlib.sha256(raw).hexdigest() == pin, f'Edition bytes/hash changed: {ident}')
        lines = raw.decode('utf-8').splitlines()
        require(len(lines) == count == entry['line_count'], f'Edition line count changed: {ident}')
        require(len(raw) == entry['bytes'] and raw.endswith(b'\n') == entry['terminal_newline'],
                f'Edition byte/newline metadata changed: {ident}')
        require(entry.get('immutable') is True, f'Edition preservation flag missing: {ident}')
        editions[ident] = dict(entry, lines=lines)
    require(manifest.get('comparison_ledger') == 'AMRKB_Source_Edition_Comparison.json', 'Wrong comparison ledger path.')
    ledger = json.loads((root / 'AMRKB_Source_Edition_Comparison.json').read_text())
    require(ledger.get('source_edition_id') == EXTRACTION_EDITION and ledger.get('target_edition_id') == CURRENT_EDITION,
            'Wrong comparison edition references.')
    require(ledger.get('altered_or_deleted_earlier_passages') == 0 and ledger.get('new_scientific_records') == 0,
            'Unsupported comparison/intake claim.')
    expected = [(1, 206, 1, 206, 'unchanged'), (198, 205, 207, 214, 'repeated'),
                (None, None, 215, 350, 'added'), (None, None, 351, 352, 'added'),
                (207, 247, 353, 393, 'moved')]
    require(len(ledger['entries']) == len(expected), 'Comparison span count changed.')
    next_line = 1
    for index, entry in enumerate(ledger['entries']):
        require(entry.get('id') == f'AMRKB-EDCMP-{index + 1:04d}', 'Comparison identity changed.')
        require(entry.get('source_edition_id') == EXTRACTION_EDITION and entry.get('target_edition_id') == CURRENT_EDITION,
                'Wrong comparison entry edition.')
        a, b, c, d = [entry[k] for k in ('source_line_start', 'source_line_end', 'target_line_start', 'target_line_end')]
        require(index < len(expected) and (a, b, c, d, entry['comparison']) == expected[index],
                'Comparison ranges/kind differ from verified edition comparison.')
        require(c == next_line and c <= d, 'Comparison target gap/overlap.')
        next_line = d + 1
        target = '\n'.join(editions[CURRENT_EDITION]['lines'][c-1:d])
        require(hashlib.sha256(target.encode()).hexdigest() == entry['target_text_sha256'], 'Comparison target slice hash changed.')
        if a is not None:
            source = '\n'.join(editions[EXTRACTION_EDITION]['lines'][a-1:b])
            require(source == target and hashlib.sha256(source.encode()).hexdigest() == entry['source_text_sha256'],
                    'Comparison correspondence/slice hash changed.')
        else:
            require(entry.get('source_text_sha256') is None, 'Added material incorrectly attributed to earlier source.')
        require(bool(entry.get('disposition')) and bool(entry.get('note')) and bool(entry.get('supporting_extraction_references')),
                'Comparison disposition/evidence missing.')
        require(entry.get('disposition') in {'already_represented', 'repeated_contextual',
                'already_represented_with_historical_claim_unresolved'}, 'Unsupported comparison disposition.')
        for reference in entry.get('supporting_extraction_references', []):
            match = re.fullmatch(r'(AMRKB-[A-Z]+-)([0-9]{4})(?:–([0-9]{4}))?', reference)
            if not match:
                require(False, 'Invalid comparison supporting reference.')
                continue
            prefix, first, last = match.groups()
            end = int(last or first)
            require(int(first) <= end and all(f'{prefix}{i:04d}' in known_ids for i in range(int(first), end + 1)),
                    'Unresolved comparison supporting reference.')
    require(next_line == 394, 'Current-edition comparison coverage incomplete.')
    return editions


def scientific_heading_targets(text):
    """Resolve generated Markdown heading IDs in document order, as on GitHub.

    Keep the containing level-two section so a matching label elsewhere cannot
    satisfy a README link intended for a particular cross-family function.
    """
    used = set()
    section = None
    headings = []
    for match in re.finditer(r'^(#{1,6}) (.+)$', text, re.MULTILINE):
        level, label = len(match[1]), match[2]
        base = re.sub(r'[^\w -]', '', label.lower()).replace(' ', '-')
        slug, suffix = base, 0
        while slug in used:
            suffix += 1
            slug = f'{base}-{suffix}'
        used.add(slug)
        if level <= 2:
            section = label if level == 2 else None
        headings.append({'level': level, 'label': label, 'anchor': slug, 'section': section})
    return headings


def check_maintenance(data, root, require):
    """Bounded documentation/metadata consistency; not scientific acceptance."""
    meta = data['metadata']
    require(meta.get('document_version') in {'0.2.0', '0.2.1'}, 'Document version outside unchanged schema.')
    origin = meta['source_document'].get('origin_confirmation', {})
    require(meta['source_document'].get('conversation_title') == 'AMRKB Overview' and
            origin.get('authority') == 'owner' and origin.get('confirmation_date') == '2026-11-02' and
            origin.get('conversation_context') == 'normal research conversation', 'Owner-confirmed source origin missing/wrong.')
    require(all(origin.get(k) is False for k in ('authenticated_message_metadata',
            'authenticated_speaker_assignments', 'authenticated_original_dates')) and
            origin.get('conversation_completeness') == 'unknown', 'Origin confirmation must not authenticate unavailable metadata/completeness.')
    assessment = meta['source_document'].get('bounded_assessment', {})
    require(assessment.get('extraction_edition_id') == EXTRACTION_EDITION and
            assessment.get('extraction_lines_accounted') == 247 and
            assessment.get('comparison_edition_id') == CURRENT_EDITION and
            assessment.get('comparison_lines_accounted') == 393 and
            assessment.get('comparison_is_new_scientific_extraction') is False and
            assessment.get('conversation_completeness') == 'unknown', 'Extraction/comparison/completeness distinctions missing/wrong.')
    require('DRM-MSP 0.1.0 review revision 2' in meta['drm'].get('status', '') and
            'unadopted' in meta['drm'].get('status', '') and meta['drm'].get('conformance') == 'not_claimed' and
            'Phase 4 documentary pilots as completed and closed' in meta['drm'].get('phase_effect', '') and
            'authorisation for Phase 5' in meta['drm'].get('phase_effect', ''), 'DRM candidate/current phase limits missing/wrong.')
    require(meta['value_semantics'].get('empty_collections') ==
            'An empty collection means no content is recorded in that collection. It does not establish confirmed absence, scientific acceptance or that this populated register is an empty template.',
            'Empty collections must not imply confirmed absence or empty-template state.')
    maintenance = meta.get('maintenance', {})
    require(maintenance.get('revision') == '2026-11-02-stage-b' and
            maintenance.get('stage_c_visual_review') == 'pending' and
            maintenance.get('owner_acceptance_of_stage_b') == 'pending', 'Stage B maintenance/review scope missing/wrong.')
    readme = (root / 'README.md').read_text()
    groups = [('working_family', 'Eight working families', 8,
               'Working families and methodology inventories'),
              ('cross_family_function', 'Twelve cross-family functions', 12,
               'Cross-family functional organising strategies')]
    headings = scientific_heading_targets(render_scientific(data))
    for kind, heading, count, section in groups:
        entries = [c for c in data['classifications'] if c['classification_kind'] == kind]
        targets = [h for h in headings if h['level'] == 3 and h['section'] == section]
        require(len(entries) == count and f'**{heading}:**' in readme, f'README {heading} count/heading mismatch.')
        require([h['label'] for h in targets] == [c['label'] for c in entries],
                f'Scientific {heading} headings differ from intended structured section/order.')
        for entry, target in zip(entries, targets):
            expected = f"[{entry['label']}](AMRKB_Scientific_Reference_Register.md#{target['anchor']})"
            require(expected in readme, f"README summary label/link missing or wrong intended section: {entry['id']}")
    require(len(data['themes']) == 5 and '**Five cross-cutting themes:**' in readme, 'README five-theme count/heading mismatch.')
    for theme in data['themes']:
        require(f"[{theme['label']}](AMRKB_Scientific_Reference_Register.md#cross-cutting-research-and-application-domains)" in readme,
                f"README theme label/link missing: {theme['id']}")
    for name in ['README.md', 'AMRKB_Research_Protocol.md']:
        require('Stage C' in (root / name).read_text() and 'pending' in (root / name).read_text(), f'Pending visual/owner review absent: {name}')


def check(data, root=ROOT):
    errors = []
    def require(condition, message):
        if not condition:
            errors.append(message)
    if not isinstance(data, dict):
        return ['Machine JSON must be an object.']
    require(set(data) == {'$schema', 'metadata', *COLLECTIONS}, 'Unexpected collection envelope.')
    if errors:
        return errors
    meta = data['metadata']
    require(meta.get('schema_version') == 'amrkb.source-extraction/0.2.0', 'Wrong extraction schema version.')
    require(meta.get('status') == 'source_extracted_candidates_pending_review', 'Source review status changed.')
    require(meta.get('attribution') == {'author': 'Jonathan Minchin', 'organisation': 'Ecological Interaction', 'orcid': 'https://orcid.org/0000-0001-8152-1796'}, 'Attribution mismatch.')
    allitems = [r for n in COLLECTIONS for r in data[n]]
    ids = [r.get('id') for r in allitems]
    require(len(ids) == len(set(ids)), 'Duplicate documentary IDs.')
    byid = {r.get('id'): r for r in allitems}
    pro = {r['id']: r for r in data['provenance']}
    recordids = {r['id'] for r in data['records']}
    clsids = {r['id'] for r in data['classifications']}
    editions = check_editions(root, require, set(byid))
    source_meta = meta['source_document']
    require(source_meta.get('edition_id') == EXTRACTION_EDITION and
            source_meta.get('edition_manifest') == 'AMRKB_Source_Editions.json', 'Extraction edition metadata missing/wrong.')
    extraction = editions[EXTRACTION_EDITION]
    require(source_meta['path'] == extraction['path'] and source_meta['sha256'] == extraction['sha256'] and
            source_meta['line_count'] == extraction['line_count'], 'Extraction source metadata mismatch.')
    lines = extraction['lines']
    for r in allitems:
        if 'scientific_verification' in r:
            require(r['scientific_verification'] == 'not_independently_verified', f"Invented verification: {r['id']}")
        for i in r.get('provenance_ids', []):
            require(i in pro, f"Unknown provenance: {r['id']} {i}")
    for r in data['records']:
        require(bool(r.get('provenance_ids')), f"Missing provenance: {r['id']}")
        for occurrence in r['occurrences']:
            i = occurrence['provenance_id']
            require(i in pro, f'Unknown occurrence provenance: {i}')
            if i in pro:
                require(occurrence['original_term'].casefold() in pro[i]['original_text'].casefold(), f"Unsupported source term: {r['id']}")
    for r in data['provenance']:
        a, b = r['line_start'], r['line_end']
        require(1 <= a <= b <= len(lines), f"Invalid source locator: {r['id']}")
        require(r.get('source_edition_id') == EXTRACTION_EDITION, f"Wrong provenance edition: {r['id']}")
        require(r['source_document'] == extraction['path'] and r['source_sha256'] == extraction['sha256'], f"Wrong source: {r['id']}")
        require(r['original_text'] == '\n'.join(lines[a-1:b]), f"Source quotation changed: {r['id']}")
    for r in data['memberships']:
        require(r['record_id'] in recordids and r['classification_id'] in clsids, f"Membership endpoint missing: {r['id']}")
    for r in data['relationships']:
        require(r['source_id'] in byid and r['target_id'] in byid, f"Relationship endpoint missing: {r['id']}")
    for r in data['references']:
        require(r['candidate_record_id'] in recordids, f"Reference candidate missing: {r['id']}")
    expected = 1
    for r in data['source_audit']:
        require(r.get('source_edition_id') == EXTRACTION_EDITION and r.get('source_document') == extraction['path'] and
                r.get('source_sha256') == extraction['sha256'], f"Wrong audit edition: {r['id']}")
        if r['provenance_id'] in pro:
            quote = pro[r['provenance_id']]
            require(quote['line_start'] == r['line_start'] and quote['line_end'] == r['line_end'], f"Audit/provenance span mismatch: {r['id']}")
        require(r['line_start'] == expected, f"Audit gap/overlap at {r['id']}")
        require(r['provenance_id'] in pro, f"Audit provenance missing: {r['id']}")
        expected = r['line_end'] + 1
    require(expected == len(lines) + 1, 'Incomplete final audit coverage.')
    require(meta['record_count'] == len(data['records']), 'Unique-entry count mismatch.')
    require(meta['counts'] == {n: len(data[n]) for n in COLLECTIONS}, 'Collection count mismatch.')
    families = {r['id'] for r in data['classifications'] if r['classification_kind'] == 'working_family'}
    require(len(families) == 8, 'Eight source families not preserved.')
    require(meta['family_association_count'] == sum(m['classification_id'] in families for m in data['memberships']), 'Family association count mismatch.')
    for note in ['README.md', 'AMRKB_Research_Protocol.md', 'AMRKB_Scientific_Reference_Register.md']:
        require((root / note).is_file(), f'Missing current document: {note}')
    protocol = (root / 'AMRKB_Research_Protocol.md').read_text()
    original = protocol.split('<!-- BEGIN PRESERVED ORIGINAL README -->\n', 1)[1].split('<!-- END PRESERVED ORIGINAL README -->', 1)[0]
    require(hashlib.sha256(original.encode()).hexdigest() == ORIGINAL_README_SHA256, 'Original scope wording changed.')
    baseline = root / 'history/template-baseline-2026-11-01'
    for entry in json.loads((baseline / 'SNAPSHOT.json').read_text())['files']:
        require(hashlib.sha256((baseline / entry['path']).read_bytes()).hexdigest() == entry['sha256'], f"Template baseline changed: {entry['path']}")
    check_maintenance(data, root, require)
    if errors:
        return errors
    require((root / 'AMRKB_Scientific_Reference_Register.md').read_text() == render_scientific(data), 'Scientific presentation differs from structured authority; review before explicit regeneration.')
    for path in root.glob('*.md'):
        for link in re.findall(r'\]\(([^)]+)\)', path.read_text()):
            u = urlsplit(link)
            if not u.scheme and not u.netloc and u.path:
                require((path.parent / unquote(u.path)).is_file(), f'Broken local link: {path.name}: {link}')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--render-scientific', action='store_true', help='Explicitly regenerate the human presentation from Machine JSON.')
    args = parser.parse_args()
    try:
        data = json.loads((ROOT / 'AMRKB_Machine_Reference.json').read_text())
        schema = json.loads((ROOT / 'AMRKB_Machine_Reference.schema.json').read_text())
        if args.render_scientific:
            (ROOT / 'AMRKB_Scientific_Reference_Register.md').write_text(render_scientific(data), encoding='utf-8')
        errors = check(data)
        try:
            from jsonschema import Draft202012Validator
        except ImportError:
            print('Optional full JSON Schema validation not run: jsonschema is not installed.')
        else:
            Draft202012Validator.check_schema(schema)
            errors.extend(f'JSON Schema: {e.message}' for e in Draft202012Validator(schema).iter_errors(data))
            print('Draft 2020-12 schema and instance checked.')
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f'Input/check failure: {exc}', file=sys.stderr)
        return 2
    if errors:
        for e in errors:
            print(e, file=sys.stderr)
        return 1
    print('Both pinned source editions, 247-line extraction coverage, 393-line comparison coverage, quotations, IDs/endpoints, counts, human parity and local links passed.')
    print('Candidate extraction only; no scientific verification, DRM phase, MSP adoption or pilot approval.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
