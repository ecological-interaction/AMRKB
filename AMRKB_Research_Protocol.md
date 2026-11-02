# AMRKB — Research Protocol

**Document version:** 0.2.2 · Source extraction pending local review.  
**Work in Progress — Academic Research Resource**

## Stage B maintenance authority — 2 November 2026

The owner approved bounded documentation and metadata maintenance only. Machine
JSON remains the structured authority; the Scientific Register is generated from
it, and README summarises reviewed content. No collection payload, identifier,
label, status, classification, relationship, quotation or locator changes.
No new extraction, scientific verification, identity merge, acceptance event,
literature, mapping or taxonomy redesign is authorised. Stage C visual review
and owner acceptance of this maintenance remain pending; Stage D is not started.

The owner confirmed on 2 November 2026 that both preserved incomplete editions
originate from the normal “AMRKB Overview” research conversation. Owner origin
confirmation does not authenticate source-message metadata, speaker assignments,
original dates or conversation completeness. Accounting for 247 extraction lines
and comparing 393 current-edition lines are different evidence operations; the
latter does not establish scientific extraction of all 393 lines.

DRM-MSP 0.1.0 review revision 2 remains an unadopted methodological candidate.
Current DRM development status records the bounded Phase 4 documentary pilots as
completed and closed, with their scientific/rights/identity limits retained.
This maintenance update neither reruns those pilots nor establishes general MSP
conformance, scientific validity or authorisation for Phase 5. Older pre-pilot
and empty-template statements below describe their historical development stages.

## Current authority and preservation

Machine JSON is the sole structured authority for the documentary extraction;
the Scientific Register is its reproducible human presentation. Source-supported
candidate inclusion is not scientific acceptance. No existing accepted content or
issued research IDs were overwritten: the preceding templates had empty arrays
and an explicitly pending identifier convention. Their exact files, schema,
validator and documentation are retained in
[the hashed template baseline](history/template-baseline-2026-11-01/SNAPSHOT.json).
The original README remains verbatim below. Unrelated local work, original
history and all Git metadata are preserved.

## Source identification, coverage and chronology

The extraction source is [the recovered 247-line edition](history/20261101_AMRKB_Chat_History_Extraction_Edition.md),
local edition `AMRKB-SRCED-0001`, SHA-256
`1902b7263a0df34084b58532f01fa16cc70497d373a1332e568e171905b18faf`.
It was recovered exactly on 1 November 2026 from `AMRKB-PRO-0088.original_text`;
its last line has no terminating newline. All provenance and audit L locators
refer to this edition, not the longer current history.

The [current 393-line history](history/20261101_AMRKB_Chat_History.md),
`AMRKB-SRCED-0002`, remains unchanged at SHA-256
`333c42970b7d4268aca8a848fef633bcf7b215a0179ec74fa8fd40b15ca98bf7`.
It adds 146 lines of repeated scope, opening dialogue and a recap. The
[comparison ledger](AMRKB_Source_Edition_Comparison.json) accounts for every current
line without claiming those additions were scientifically extracted. See the
[edition manifest](AMRKB_Source_Editions.json) and
[reconciliation report](AMRKB_Source_Edition_Reconciliation.md).

The filename date is not a verified conversation/message or original creation
date. Heading: “Agricultural Modes and Methods”. Both editions mix structured
proposals and unlabelled dialogue; speaker assignments remain inferred. Neither
is authenticated as a complete message export. Detailed families 1/2, a full
family-8 expansion, attachments, prior sources and a finished bibliography remain
unavailable. The recap's retrospective agreement claims add no acceptance event.
No missing research was reconstructed and no literature/conversation retrieved.

## Source-to-destination audit crosswalk

Each span is represented with exact source text in JSON provenance and an audit
disposition; all 247 extraction-edition lines are accounted for, including formatting/UI
artefacts. Dispositions preserve later revisions without treating proposals as
facts. The scientific register carries the relevant explanatory content; raw
conversation wording and uncertainty remain attributable in source/provenance.

| Source lines | Substantive section | Treatment and destination |
|---|---|---|
| 1–5 | Research remit and distinctions | candidate definitions; records; protocol |
| 6–17 | Proposed entity definitions and examples | provisional definitions, not adopted taxonomy; classifications; memberships; scientific definitions |
| 18–31 | Eight overlapping families | assistant-proposed working families, no exclusive taxonomy; classifications; memberships |
| 32–50 | Twelve functional categories | cross-family functional proposal; classifications; memberships |
| 51–68 | Mechanism-indicator-outcome chain and worked examples | illustrative hypotheses, not evidenced causal claims; applications; relationships; scientific explanations |
| 69–80 | AMMI proposal and database relationships | AMMI superseded by later user AMRKB naming; scope retained; protocol; applications; source context |
| 81–106 | Four-stage investigation and historical dimension | historical proposal, later three-stage plan is not identical; protocol; decisions |
| 107–119 | Formatting whitespace | no research content; source retained unchanged |
| 120–132 | User establishes AMRKB name and autonomous parallel scope | explicit user naming/remit instruction; whitespace retained; metadata; decision |
| 133–155 | Acknowledgement, project boundaries and architecture | UI memory artefact excluded; architecture is proposal not implemented service; protocol; decisions |
| 156–171 | Six research dimensions | scope dimensions, not category membership claims; classifications; scientific context |
| 172–181 | Three-stage strategy and implementation deferral | later working plan; conceptual development before engine; protocol; decisions |
| 182–206 | Organisation diagram and full historical/geographic scope | historical organisation options; no filesystem instructions executed; protocol; decisions |
| 207–209 | Intensive/Industrial methodology inventory | approval to progress; first-two detailed inventories not supplied; records; groups; memberships |
| 210–214 | Ecological/Organic methodology inventory | family content relevant; certification placement unresolved; records; groups; memberships |
| 215–217 | Regenerative/Conservation methodology inventory | relevance not scientific verification; records; groups; memberships |
| 218–220 | Agroecological/Diversified methodology inventory | relevance not universal equivalence; records; groups; memberships |
| 221–223 | Precision/Computational methodology inventory | user requests progress; methods not products; records; groups; memberships |
| 224–226 | Request to repeat and offered branch | repeat request not answered verbatim; precision understanding not assume-confirmed; family 8 deferred; decisions; audit limitations |
| 227–234 | Open technology, AI/LLMs and reference request | explicit user relevance; no actual bibliography supplied; themes; candidate terms |
| 235–240 | Cross-cutting applications and five domains | exploration approved; assistant domains not adopted scientific classification; themes; applications |
| 241–246 | Reference-inventory scope and user agreement | candidate inventory approved for exploration; future verification promised not performed; records; incomplete references; decisions |
| 247–247 | Final narrowed list and stop before source audit | ten named terms; omissions not explicit rejection; five groups unnamed; references; unresolved decisions |

## Organising decisions and exclusions

The explicit user naming/remit instruction selects AMRKB as an autonomous
parallel project; AMMI is an earlier superseded naming proposal. Eight source
families retain their actual “and” labels and remain overlapping working groups.
Source-proposed entity distinctions, twelve cross-family functions and later
family-specific functions are separate classification objects and memberships,
not one compulsory hierarchy. No family is required for every entry.

The initial four-stage investigation and later three-stage architecture plan
are different historical proposals, retained in provenance; they are not DRM
phases. Later user exchanges support continued methodology inventories and then
cross-cutting exploration. Methodology-before-technique is a qualified working
progression here: the file lacks an explicit full-order user instruction and
the first two detailed inventories. Do not invent their sub-methods.

User agreement confirms relevance/further exploration, not each example or
membership. The repeat request for Precision/Computational was not answered
with a repetition. Family 8 detail is deferred when the user selects cross-cutting
research. Certification placement, a requested unnamed set of five methodological
groups and possible synonymous labels remain unresolved. No explicit rejection
of AgriFM or AgroGPT occurs: retain them despite omission from the final list.
ICARUS DDAL and ICARUS are separate pending identity evidence.

The five cross-cutting domains are not new agricultural families. Four AI terms
(analytical ML, LLM-based systems, knowledge graphs, agent-based tools) do not
supply the missing fifth group. Keep open technology, distributed fabrication,
AI/LLM/agent distinctions, robotics, information infrastructure and ecological
signatures/place-based application rationale source-qualified. No causal or
performance claim is independently verified.

## Identity and schema extension

The template had no issued research IDs. This task introduces **local persistent
documentary extraction locators**, not externally established agricultural or
federation identities: AMRKB-REC, CLS, MEM, REL, REF, PRO, THM, APP, DEC and AUD,
each followed by a hyphen and four-digit sequence. Preserve them on future edits;
never recycle, renumber on classification changes or infer equivalence by number.
Uncertain identity stays unresolved. Original labels and occurrence context remain.
Exact case/whitespace variants share a lexical entry; similar or differently
spelled labels are not silently merged. These are candidate lexical identities,
not proof of unique real-world entities. Type uncertainty is explicitly retained.

The original extraction introduced Machine document 0.2.0 and local schema `amrkb.source-extraction/0.2.0` replace
only the preserved empty-template constraint. Existing records, classifications,
relationships, references and provenance collections remain; separate memberships,
themes, applications, decisions and source_audit arrays are justified by the
actual source distinctions. Metadata includes source identity, counts and limits.
No mandatory agricultural taxonomy, engine, input service or connector is added.
These schema-extension statements record the earlier extraction, not a new Stage B schema change.

Classification definitions and memberships are distinct. Relationships have
local typed endpoints, project status and provenance; no external record IDs,
scientific approvals or verified bindings are invented. Reference entries are
incomplete named candidates, not manufactured author/title/date/DOI citations.
Every scientific verification field remains `not_independently_verified`.
Project decisions retain their own status. Missing, unknown, not applicable and
confirmed absence retain the preceding metadata semantics; absent source detail
is never filled or treated as confirmed absence.

## DRM and federation boundaries

DRM development status was consulted read-only for this maintenance. Its current
Phase 4 closure supersedes the earlier pre-pilot wording for present context;
DRM-MSP 0.1.0 review revision 2 remains unadopted/unreleased. No DRM file, phase,
protocol obligation or approval is changed by this AMRKB task. Documentary
preservation and structural validation remain separate from scientific review.

Source-proposed EIRKB/EII/GIS possibilities and later OSDS, GIS DS and computation
layer links remain candidate project/layer relationships, without external record
IDs or implied implementation. IRKB is not named in the supplied source; its
independent synthesis role is a DRM boundary, not an extracted mapping.
Knowledge family, functional type and epistemic orientation may be useful later
review lenses, but no three-dimensional taxonomy or memberships are adopted.
This source illustrates overlap, mixed entity granularity, contested scientific
inferences, regional/historical context and candidate evidence—not a universal
classification imposed by infrastructure.

## Neighbouring architecture comparison — preserved template-stage assessment


Historical template-stage comparison, retained from 1 November 2026; the
following empty-template assessments are superseded by the populated extraction
and current authority above, not present-state claims:

| Repository | Current authority and file arrangement | Reusable convention / boundary |
|---|---|---|
| EIRKB | Machine JSON and local serialization schema; scientific register; Research Protocol; authored A01–A03 analysis; preservation crosswalk and legacy workbooks; compatibility Master index. | Separate structured authority, authored prose, method and history. Its HA/IL/IM constructs, record counts and legacy IDs are EIRKB-specific. |
| EII | Machine JSON/schema; scientific tables and compact README; Research Protocol; preservation crosswalk; Markdown machine compatibility index; curated remote-sensing view. | Stable identity, explicit human/structured roles and lossless history. Its 15-domain taxonomy, indicators and fixed-count migration checks are not AMRKB rules. |
| GISDS | GISDS.md is a continuous seven-column 25-resource source table; compact README; RESEARCH_NOTES.md carries metadata guidance and provenance. No separate machine JSON/schema. | Keep the entry point concise and method/provenance outside dense tables. Its provider/resource/dataset distinctions and source IDs are not agricultural classifications. |
| OSDS | Scientific register plus authoritative machine JSON fences in Markdown; README and research notes; 62 candidate sources and separately qualified discovery evidence. | State container format, evidence and verification limits. Its observation categories, domain codes and source-ID convention are not copied. |

CFF 1.2.0 attribution, unreleased change histories, local links, stable filenames
and independently versioned documents/schemas recur. No single neighbour layout
is a mandatory federation template. EIRKB/EII protocols consolidate methodology;
GISDS/OSDS research notes hold usage/provenance details. AMRKB needs one protocol
now, not both overlapping notes and a protocol. The schema and validator serve
only this empty-template boundary; populated neighbours' historical preservation
crosswalks are unnecessary because AMRKB has no migrated research corpus.

Neighbour diagrams use editable Mermaid sources, generated SVG and reproducible
Python rendering, with shared palette/typography and conceptual caveats. No
diagram is created for this empty template: short file-role links communicate
the present architecture without implying a populated agricultural taxonomy or
operational federation. If later justified, adopt editable source, accessible
SVG and deterministic generation together; do not copy research categories.


## Validation, versioning and next decisions

Run `python3 -B scripts/validate_amrkb.py`; installed jsonschema adds full
Draft 2020-12 schema checking. The standard-library checks cover current envelope,
unique IDs, endpoint/reference resolution, source hashes/quotes and complete
ordered audit coverage, counts, no invented scientific verification, baseline
preservation, document links and deterministic Scientific Register parity.
`--render-scientific` explicitly regenerates the presentation, not acceptance.
No live service is contacted and the validator cannot establish scientific truth,
legal rights, genuine identity or authentic reviewer authority.

README 0.3.2 and Protocol 0.2.2 are document revisions. Machine document and
generated Scientific Register remain 0.2.1 with dated maintenance revision
`2026-11-02-stage-b`; the unchanged schema only permits document versions 0.2.0
and 0.2.1. Local schema identity remains `amrkb.source-extraction/0.2.0`. These
labels distinguish document/container maintenance from schema changes and
research releases; none is a scientific acceptance event.
Citation remains Jonathan Minchin, Ecological Interaction, the supplied ORCID;
no licence, DOI, publication or release date is assigned.

Stop after local review. Further authority is required for missing-source recovery,
source-level identity/bibliography audit, scientific verification, taxonomy redesign,
external mappings, DRM harmonisation, source ingestion services or publication.
No database acceptance/reviewer events or permission grants were fabricated.

## Historical README — preserved original scope and intentions

The following exact original README is historical evidence. Current authority
and intake rules above supersede only outdated file-role/status statements.
Academic scope, chronology and methodological intentions are preserved.

<!-- BEGIN PRESERVED ORIGINAL README -->
# Agricultural Modes Reference Knowledge Base (AMRKB)

**Status:** Stage A — scope and architecture; pre-implementation.  
**Document version:** 0.1.0  
**Created:** 2026-10-12

## Purpose and scope

AMRKB is an independent research project within Ecological Information, covering agricultural history, modes, systems, methods, practices and technologies. It includes traditional, Indigenous, industrial, ecological, experimental and emerging approaches across historical periods and geographical regions. Its classifications remain provisional.

Research dimensions include historical development and diffusion; philosophies and traditions; technical methods and infrastructure; relationships with soil, water, biodiversity and ecological processes; climate, terrain and place-specific suitability; and labour, land tenure and productive organisation.

Keep modes, systems, methods, practices, technologies, ecological mechanisms and indicators distinct, and record explicit relationships between them.

## Relationship to other projects

EIRKB provides ecological literature, concepts and theoretical research. EII inventories ecological variables and indicators. AMRKB develops agricultural knowledge independently while preparing for compatible identifiers, reference metadata, place information and cross-project relationships. Shared conventions do not require identical schemas.

## Planned architecture and development

1. Define scope, entities, classifications and relationships in Markdown.
2. Build a referenced inventory of agricultural approaches, practices and technologies.
3. Implement a SQLite database after the conceptual framework is sufficiently developed.

The intended framework includes persistent identifiers, Zotero interoperability, GIS compatibility, machine-readable exports such as CSV and JSON, and future knowledge graph compatibility. No database or validated classification is implemented yet.

## Local maintenance and provenance

Open this directory as the project workspace. Keep version notes inside documents and preserve revisions in Git. No remote repository is configured.

This initial scope summarises the “Agricultural Classification Proposal” conversation of 10 October 2026 and the repository organisation proposed in “Ecological Information Overview” on 12 October 2026.
<!-- END PRESERVED ORIGINAL README -->
