"""Read-only AMRKB public validation and optional archival preservation checks.
No scientific, rights, acceptance or DRM conformance assurance is implied.
"""
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit
ROOT = Path(__file__).resolve().parents[1]
COLLECTIONS = ('records', 'classifications', 'memberships', 'relationships', 'references', 'provenance', 'themes', 'applications', 'decisions', 'source_audit')
EDITION_PINS = {
 'AMRKB-SRCED-0001': ('source-editions/20261101_AMRKB_Chat_History_Extraction_Edition.md', '1902b7263a0df34084b58532f01fa16cc70497d373a1332e568e171905b18faf', 247, 23385),
 'AMRKB-SRCED-0002': ('source-editions/20261101_AMRKB_Chat_History.md', '333c42970b7d4268aca8a848fef633bcf7b215a0179ec74fa8fd40b15ca98bf7', 393, 25900)
}
EXTRACTION_EDITION = 'AMRKB-SRCED-0001'
CURRENT_EDITION = 'AMRKB-SRCED-0002'
ORIGINAL_README_SHA256 = '4eb11eb8f9ead8d907007dc26d0c469d8dda78b1d250b9dab1b9205d10708ea1'
STATUS_LABELS = {'assistant_proposed_candidate': 'Source-proposed candidate', 'assistant_proposed_provisional': 'Source-proposed provisional definition', 'assistant_proposed_association': 'Source-proposed association', 'assistant_illustrative_hypothesis': 'Source-proposed illustrative hypothesis', 'family_inventory_relevant_details_unverified': 'Relevant inventory entry; details unverified', 'user_approved_inventory_scope_not_verified_identity': 'Owner-approved inventory scope; identity unverified', 'family_inventory_explored_not_individually_approved': 'Inventory explored; individual association not approved', 'candidate_not_verified': 'Candidate; unverified', 'user_relevance_and_further_exploration_confirmed': 'Relevance and further exploration confirmed', 'proposed_future_research_application': 'Proposed future research application', 'user_instruction': 'Recorded owner direction', 'user_relevance_decision': 'Recorded relevance decision', 'partially_supported_working_progression': 'Partially supported working progression', 'deferred': 'Deferred', 'unresolved': 'Unresolved', 'not_established_by_source': 'Not established by source'}

def cell(value):
    # Translate only complete semicolon-delimited status values, never research prose.
    text = '; '.join(STATUS_LABELS.get(part, part) for part in str(value).split('; '))
    return text.replace('|', '&#124;').replace('\n', '<br>')


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
**Research status:** incomplete documentary candidate catalogue; scientific review and owner acceptance remain pending.

Research by Jonathan Minchin, Ecological Interaction ([ORCID 0000-0001-8152-1796](https://orcid.org/0000-0001-8152-1796)).

## Reading key and source limits

This is the human presentation of the [authoritative Machine JSON](AMRKB_Machine_Reference.json).
The [Research Protocol](AMRKB_Research_Protocol.md) defines extraction, identity and review limits.
The [source-edition manifest](AMRKB_Source_Editions.json) identifies the preserved
247-line extraction edition and the distinct 393-line later edition. All L locators
below refer to the extraction edition. The later edition was compared separately;
comparison is not scientific extraction of every line. Exact source evidence is
held archivally; original dates, speaker assignments and source completeness remain
unverified. Public validation checks fingerprints and structure; full source
verification requires explicitly supplied archival evidence.

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
Five methodological groups remain unnamed; certification placement, ICAERUS
identity, lexical variants and mixed types remain unresolved. AgriFM/AgroGPT
are retained despite later omission. A request to repeat Precision/Computational
is not approval; missing content is not reconstructed. Recorded agreement supports
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
    text += '## Complete candidate identity index\n\nEvery documentary entry appears once in this index, including terms not assigned a family. Original terms remain preserved in the Machine Reference and archival evidence; current display spelling corrections do not merge identities. Different source spellings and possibly equivalent labels remain separate; identical case-insensitive labels retain occurrence-specific types. This does not resolve homonyms or prove unique real-world identity.\n\n'
    text += table(['Entry ID', 'Current label', 'Record kind / candidate types', 'Project status', 'Source occurrences'], [(r['id'], r['label'], r['record_type'] + '; ' + ', '.join(r['candidate_entity_types']), r['project_status'], loc(r['provenance_ids'])) for r in data['records']])
    text += '## Historical, geographical, ecological and socioeconomic context\n\nThe scope includes historical emergence, spread, combination and transformation; technology, land tenure, energy, labour and ecological transformation provide comparative context (L99–106). It is not restricted to contemporary regenerative agriculture (L201–203). No origins, dates or regional distributions for individual approaches are invented.\n\n'
    text += table(['Dimension', 'Source description', 'Status / provenance'], [(c['label'], c['description'], c['project_status'] + '; ' + loc(c['provenance_ids'])) for c in data['classifications'] if c['classification_kind'] == 'research_dimension'])
    text += '## Ecological mechanisms, indicators and proposed applications\n\nThe source proposes the chain agricultural method → ecological mechanism → measurable indicator → ecological outcome → place-specific suitability (L54). This is a research model, not an implemented recommendation service or proof of causation. Worked examples below retain their qualifications; management effects require later evidence and context.\n\n'
    text += table(['Application / claim ID', 'Context or purpose', 'Explanation and qualification', 'Status / provenance'], [(r['id'], r['label'], r['description'], r['project_status'] + '; ' + loc(r['provenance_ids'])) for r in data['applications']])
    text += '## Cross-cutting research and application domains\n\nThe five domains were proposed for further exploration, not as new agricultural families. Open design and distributed manufacturing connect tools and knowledge; AI/LLM/agent methods, knowledge graphs and field evidence remain distinct. The unspecified five methodological groups in the final line are not inferred from these domains or from four earlier AI method terms.\n\n'
    text += table(['Theme ID', 'Domain', 'Source-supported rationale', 'Status / provenance'], [(r['id'], r['label'], r['description'], r['project_status'] + '; ' + loc(r['provenance_ids'])) for r in data['themes']])
    text += '## Named references and bibliographic gaps\n\nThese are named candidate programmes/tools/sources, not completed bibliographic citations. The source supplies no authors, publication titles, dates, DOI or URLs. Both source lists are retained: AgriFM and AgroGPT are not rejected by omission; ICAERUS DDAL and ICAERUS remain distinct. The promise of later references/field-evidence criteria is not an accomplished literature review.\n\n'
    text += table(['Reference ID', 'Current name', 'Candidate entry', 'Evidence limitation', 'Provenance'], [(r['id'], r['label'], r['candidate_record_id'], r['bibliographic_status'], loc(r['provenance_ids'])) for r in data['references']])
    text += '## Candidate relationships and assertion limits\n\nThese local typed assertions identify contextual relevance only. They do not establish external record IDs, completed dataset bindings, a shared taxonomy or verified mechanism/outcome links.\n\n'
    text += table(['Assertion ID', 'Source', 'Relationship', 'Target', 'Status / provenance'], [(r['id'], byid[r['source_id']].get('label'), r['relationship_type'], byid[r['target_id']].get('label'), r['project_status'] + '; ' + loc(r['provenance_ids'])) for r in data['relationships']])
    text += '## Revisions, unresolved questions and research boundary\n\n'
    text += table(['Decision / issue ID', 'Subject', 'Disposition', 'Explanation', 'Provenance'], [(r['id'], r['label'], r['project_status'], r['description'], loc(r['provenance_ids'])) for r in data['decisions']])
    text += 'The [protocol audit crosswalk](AMRKB_Research_Protocol.md#source-to-destination-audit-crosswalk) accounts for every source span. Human-readable statuses translate original machine values without changing their meanings. No scientific verification, new literature, taxonomy redesign, cross-database harmonisation or publication follows automatically.\n'
    return text


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


PRESERVED_PAYLOAD_SHA256 = 'a4408033da4339102b856a5278cbdcc7ecfc6e17a44b13e11297df2f6617aac1'

def digest(value):
    return hashlib.sha256(value).hexdigest()


def load(path):
    def pairs(items):
        obj = {}
        for key, value in items:
            if key in obj:
                raise ValueError('Duplicate JSON key: ' + key)
            obj[key] = value
        return obj
    return json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=pairs,
                      parse_constant=lambda v: (_ for _ in ()).throw(ValueError('Invalid JSON number: ' + v)))


def preservation_projection(data):
    """Only explicitly approved provenance relocation and display edits are normalised."""
    import copy
    payload = copy.deepcopy({k: data[k] for k in COLLECTIONS})
    for row in payload['provenance']:
        if 'original_text' in row:
            row['quotation_sha256'] = digest(row.pop('original_text').encode())
        row.pop('speaker_status', None)
        row.pop('source_role_status', None)
        row['source_document'] = Path(row['source_document']).name
    for row in payload['source_audit']:
        row['source_document'] = Path(row['source_document']).name
    for name in ['records', 'references']:
        for row in payload[name]:
            if row.get('label') in ['ICARUS', 'ICARUS DDAL']:
                row['label'] = row['label'].replace('ICARUS', 'ICAERUS')
    for row in payload['decisions']:
        for key in ['label', 'description']:
            if key in row:
                row[key] = row[key].replace('ICARUS', 'ICAERUS')
    return digest(json.dumps(payload, sort_keys=True, ensure_ascii=False).encode())


def check(data, root=ROOT, evidence_root=None, development_root=None):
    errors = []
    def require(ok, message):
        if not ok:
            errors.append(message)
    require(isinstance(data, dict) and set(data) == {'$schema','metadata',*COLLECTIONS}, 'Wrong collection envelope')
    if errors: return errors
    meta = data['metadata']
    require(meta['schema_version'] == 'amrkb.source-extraction/0.3.0', 'Wrong local serialization schema')
    require(meta['status'] == 'source_extracted_candidates_pending_review', 'Candidate status changed')
    require(meta['attribution'] == {'author':'Jonathan Minchin','organisation':'Ecological Interaction','orcid':'https://orcid.org/0000-0001-8152-1796'}, 'Attribution changed')
    require(meta['title'] == 'Agricultural Modes Reference Knowledge Base (AMRKB)', 'Project name changed')
    require(meta['maintenance']['stage_c_visual_review'] == meta['maintenance']['owner_acceptance_of_stage_b'] == 'pending', 'Pending acceptance declarations changed')
    require(meta['drm']['conformance'] == 'not_claimed', 'DRM conformance changed')
    require(meta.get('presentation_status_labels') == STATUS_LABELS, 'Status display map changed without review')
    require(meta['counts'] == {k:len(data[k]) for k in COLLECTIONS}, 'Collection count mismatch')
    require(meta['record_count'] == len(data['records']), 'Record count mismatch')
    items = [row for k in COLLECTIONS for row in data[k]]
    ids = [row['id'] for row in items]
    require(len(ids) == len(set(ids)), 'Duplicate local identifiers')
    byid = {row['id']:row for row in items}
    pro = {row['id']:row for row in data['provenance']}
    rec = {row['id'] for row in data['records']}
    cls = {row['id'] for row in data['classifications']}
    for row in items:
        if 'scientific_verification' in row:
            require(row['scientific_verification'] == 'not_independently_verified', 'Scientific verification changed: '+row['id'])
        for ident in row.get('provenance_ids', []):
            require(ident in pro, 'Unresolved provenance: '+row['id'])
    for row in data['records']:
        require(bool(row['provenance_ids']), 'Missing record provenance')
        require(all(o['provenance_id'] in pro for o in row['occurrences']), 'Unknown occurrence provenance')
    for row in data['memberships']:
        require(row['record_id'] in rec and row['classification_id'] in cls, 'Unresolved membership endpoint')
    for row in data['relationships']:
        require(row['source_id'] in byid and row['target_id'] in byid, 'Unresolved relationship endpoint')
    for row in data['references']:
        require(row['candidate_record_id'] in rec, 'Unresolved reference candidate')
    manifest = load(root/'AMRKB_Source_Editions.json')
    require(manifest['extraction_edition_id']==EXTRACTION_EDITION and manifest['current_history_edition_id']==CURRENT_EDITION, 'Wrong source edition roles')
    require(len(manifest['editions'])==2 and {e['id'] for e in manifest['editions']}==set(EDITION_PINS), 'Missing/duplicate source editions')
    for edition in manifest['editions']:
        require(edition['id'] in EDITION_PINS, 'Unknown edition')
        if edition['id'] in EDITION_PINS:
            path,pin,lines,size=EDITION_PINS[edition['id']]
            require((edition['path'],edition['sha256'],edition['line_count'],edition['bytes'])==(path,pin,lines,size), 'Edition pin changed')
            require(edition['immutable'] is True and edition['terminal_newline'] is False,'Edition preservation declaration changed')
    require(meta['source_document']['sha256']==EDITION_PINS[EXTRACTION_EDITION][1] and meta['source_document']['edition_id']==EXTRACTION_EDITION, 'Wrong extraction metadata')
    for row in data['provenance']:
        require('original_text' not in row and 'speaker_status' not in row, 'Raw provenance leaked into public register')
        require(row['source_edition_id']==EXTRACTION_EDITION and row['source_document']==EDITION_PINS[EXTRACTION_EDITION][0] and row['source_sha256']==EDITION_PINS[EXTRACTION_EDITION][1], 'Provenance source mismatch')
        require(1 <= row['line_start'] <= row['line_end'] <= 247, 'Invalid quotation range')
        require(bool(re.fullmatch('[0-9a-f]{64}',row['quotation_sha256'])), 'Invalid quotation fingerprint')
    cursor=1
    for row in data['source_audit']:
        require(row['line_start']==cursor and row['line_end']>=row['line_start'], 'Extraction coverage gap/overlap')
        require(row['source_edition_id']==EXTRACTION_EDITION and row['source_sha256']==EDITION_PINS[EXTRACTION_EDITION][1] and row['source_document']==EDITION_PINS[EXTRACTION_EDITION][0], 'Audit edition mismatch')
        require(row['provenance_id'] in pro,'Unknown audit provenance')
        if row['provenance_id'] in pro:
            p=pro[row['provenance_id']]
            require((p['line_start'],p['line_end'])==(row['line_start'],row['line_end']), 'Audit/quotation span mismatch')
        cursor=row['line_end']+1
    require(cursor==248,'Incomplete 247-line coverage')
    ledger=load(root/'AMRKB_Source_Edition_Comparison.json')
    expected=[(1,206,1,206,'unchanged'),(198,205,207,214,'repeated'),(None,None,215,350,'added'),(None,None,351,352,'added'),(207,247,353,393,'moved')]
    require(ledger['source_edition_id']==EXTRACTION_EDITION and ledger['target_edition_id']==CURRENT_EDITION,'Wrong comparison editions')
    require(ledger['new_scientific_records']==0 and ledger['altered_or_deleted_earlier_passages']==0,'Comparison incorrectly declares intake or loss')
    require(len(ledger['entries'])==5,'Wrong comparison span count')
    for i,(row,expected_row) in enumerate(zip(ledger['entries'],expected)):
        require(tuple(row[k] for k in ['source_line_start','source_line_end','target_line_start','target_line_end','comparison'])==expected_row,'Comparison gap/overlap or changed range')
        require(row['id']==f'AMRKB-EDCMP-{i+1:04d}','Comparison identity changed')
        for ref in row['supporting_extraction_references']:
            match=re.fullmatch(r'(AMRKB-[A-Z]+-)([0-9]{4})(?:–([0-9]{4}))?',ref)
            require(bool(match),'Invalid comparison reference')
            if match:
                prefix,first,last=match.groups()
                require(int(first)<=int(last or first) and all(f'{prefix}{n:04d}' in byid for n in range(int(first),int(last or first)+1)), 'Unresolved comparison supporting reference')
    families={c['id'] for c in data['classifications'] if c['classification_kind']=='working_family'}
    require(len(families)==8,'Working family count changed')
    require(meta['family_association_count']==sum(m['classification_id'] in families for m in data['memberships']),'Family count mismatch')
    require(preservation_projection(data)==PRESERVED_PAYLOAD_SHA256,'Scientific payload changed outside approved editorial/provenance mapping')
    require((root/'AMRKB_Scientific_Reference_Register.md').read_text()==render_scientific(data),'Scientific presentation differs from authority')
    readme=(root/'README.md').read_text()
    headings=scientific_heading_targets(render_scientific(data))
    for kind,section in [('working_family','Working families and methodology inventories'),('cross_family_function','Cross-family functional organising strategies')]:
        rows=[c for c in data['classifications'] if c['classification_kind']==kind]
        targets=[h for h in headings if h['level']==3 and h['section']==section]
        require([x['label'] for x in targets]==[x['label'] for x in rows],'Scientific heading order changed')
        for row,target in zip(rows,targets):
            require(f"[{row['label']}](AMRKB_Scientific_Reference_Register.md#{target['anchor']})" in readme,'README intended section link mismatch')
    for path in root.glob('*.md'):
        for link in re.findall(r'\]\(([^)]+)\)',path.read_text()):
            u=urlsplit(link)
            if not u.scheme and not u.netloc:
                dest=path.parent/unquote(u.path) if u.path else path
                require(dest.is_file(),'Broken local file link: '+link)
                if dest.is_file() and u.fragment and dest.suffix=='.md':
                    require(unquote(u.fragment) in {x['anchor'] for x in scientific_heading_targets(dest.read_text())},'Broken local anchor: '+link)
    if evidence_root is not None:
        editions={}
        for ident,(path,pin,count,size) in EDITION_PINS.items():
            file=evidence_root/path
            require(not file.is_symlink(),'Evidence file is a symlink')
            raw=file.read_bytes()
            require(digest(raw)==pin and len(raw)==size and not raw.endswith(b'\n'),'Archival edition bytes/hash changed')
            lines=raw.decode('utf-8').splitlines();require(len(lines)==count,'Archival edition line count changed');editions[ident]=lines
        for row in data['provenance']:
            text='\n'.join(editions[row['source_edition_id']][row['line_start']-1:row['line_end']])
            require(digest(text.encode())==row['quotation_sha256'],'Archival quotation fingerprint mismatch')
        for row in data['records']:
            for occurrence in row['occurrences']:
                p=pro[occurrence['provenance_id']]
                text='\n'.join(editions[p['source_edition_id']][p['line_start']-1:p['line_end']])
                require(occurrence['original_term'].casefold() in text.casefold(),'Original term unsupported by archival evidence')
        for row in ledger['entries']:
            text='\n'.join(editions[CURRENT_EDITION][row['target_line_start']-1:row['target_line_end']])
            require(digest(text.encode())==row['target_text_sha256'],'Comparison archival target mismatch')
            if row['source_line_start'] is not None:
                source='\n'.join(editions[EXTRACTION_EDITION][row['source_line_start']-1:row['source_line_end']])
                require(source==text and digest(source.encode())==row['source_text_sha256'],'Comparison archival correspondence mismatch')
    if development_root is not None:
        preserved=development_root/'history/publication-preparation-2026-11-03'
        record=load(preserved/'PRESERVATION.json')
        for item in record['files']:
            path=preserved/item['path']
            require(digest(path.read_bytes())==item['sha256'],'Development preservation hash changed')
        baseline=development_root/'history/template-baseline-2026-11-01'
        for item in load(baseline/'SNAPSHOT.json')['files']:
            require(digest((baseline/item['path']).read_bytes())==item['sha256'],'Template baseline changed')
        original=(preserved/'README-original-2026-10-12.md').read_bytes()
        require(digest(original)==ORIGINAL_README_SHA256,'Historical original README changed')
        before=load(preserved/'before/AMRKB_Machine_Reference.json')
        require(preservation_projection(before)==preservation_projection(data),'Original/current collection preservation differs')
    return errors


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--evidence-root',type=Path,help='Owner-controlled Archive AMRKB root; no default private path.')
    parser.add_argument('--development-root',type=Path,help='Owner-controlled Development AMRKB root; checks preserved pre-edit evidence.')
    parser.add_argument('--render-scientific',action='store_true',help='Explicitly regenerate the human presentation, not scientific acceptance.')
    args=parser.parse_args()
    try:
        data=load(ROOT/'AMRKB_Machine_Reference.json')
        if args.render_scientific:
            (ROOT/'AMRKB_Scientific_Reference_Register.md').write_text(render_scientific(data),encoding='utf-8')
        errors=check(data,ROOT,args.evidence_root,args.development_root)
        try:
            from jsonschema import Draft202012Validator
        except ImportError:
            print('Optional JSON Schema validation unavailable: jsonschema not installed.')
        else:
            schema=load(ROOT/'AMRKB_Machine_Reference.schema.json');Draft202012Validator.check_schema(schema)
            errors.extend('JSON Schema: '+e.message for e in Draft202012Validator(schema).iter_errors(data))
            print('Draft 2020-12 schema and instance checked.')
    except (OSError,ValueError,KeyError,TypeError) as exc:
        print('Input/check failure: '+str(exc),file=sys.stderr);return 2
    if errors:
        for error in errors:print(error,file=sys.stderr)
        return 1
    print('Public structural/preservation-profile checks passed; scientific presentation and local links resolve.')
    print('Archival edition/quotation checks: '+('PASSED' if args.evidence_root else 'NOT RUN — archival evidence not supplied.'))
    print('Development baseline checks: '+('PASSED' if args.development_root else 'NOT RUN — development evidence not supplied.'))
    print('No scientific verification, rights permission, acceptance, publication or DRM conformance established.')
    return 0

if __name__=='__main__':
    sys.exit(main())
