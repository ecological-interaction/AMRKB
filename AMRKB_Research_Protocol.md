# AMRKB — Research Protocol

**Document version:** 0.2.3 · Incomplete candidate catalogue pending local review.
**Work in Progress — Academic Research Resource**

## Authority, scope and archival provenance

AMRKB retains the name Agricultural Modes Reference Knowledge Base. Machine JSON
owns structured records; the Scientific Register is its generated human presentation.
Modes, systems, methods, practices, technologies, ecological mechanisms and indicators
remain distinct candidate representations, not a compulsory scientific hierarchy.
The scope covers historical, geographical, ecological and socioeconomic research.
The catalogue is incomplete and scientifically unverified; project relevance is not
scientific acceptance. Stage C visual review and owner acceptance remain pending.

The [source-edition manifest](AMRKB_Source_Editions.json) preserves edition IDs,
SHA-256 fingerprints, exact byte counts and line counts. The 247-line extraction
edition supports all 88 provenance entries and 23 extraction-audit spans. The
393-line later edition contains a 146-line insertion of repeated scope and contextual
material; it was compared, not newly scientifically extracted. The
[comparison ledger](AMRKB_Source_Edition_Comparison.json) preserves the correspondence.
Original source dates, role assignments and completeness remain unverified.

Exact editions are immutable in Archive. Raw quotations, prior metadata, historical
instructions and execution reports are preserved in Development. Public provenance
retains source-edition IDs, line ranges and quotation SHA-256 fingerprints. Moving
an evidence locator does not authorise changing an edition, source spelling or hash.
The public validator does not claim to have checked unavailable private sources.

## Source-to-destination audit crosswalk

Each span is represented in public JSON provenance by its source-edition identity,
line range and exact quotation SHA-256 fingerprint, together with an audit disposition.
All 247 extraction-edition lines are accounted for, including formatting/UI artefacts.
Exact source editions remain immutable in Archive; original quotations and prior
representations are preserved in Development. Dispositions preserve later revisions
without treating proposals as facts. The Scientific Register presents the relevant
research content and its qualifications; full source verification requires the
explicitly supplied archival evidence.

| Source lines | Substantive section | Treatment and destination |
|---|---|---|
| 1–5 | Research remit and distinctions | candidate definitions; records; protocol |
| 6–17 | Proposed entity definitions and examples | provisional definitions, not adopted taxonomy; classifications; memberships; scientific definitions |
| 18–31 | Eight overlapping families | source-proposed working families, no exclusive taxonomy; classifications; memberships |
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
| 235–240 | Cross-cutting applications and five domains | exploration approved; source-proposed domains not adopted scientific classification; themes; applications |
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
ICAERUS DDAL and ICAERUS are separate pending identity evidence.

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

The original extraction introduced Machine document 0.2.0 and local schema
`amrkb.source-extraction/0.2.0`, replacing the preceding empty-template constraints.
It retained records, classifications, relationships, references and provenance as
separate collections, and added memberships, themes, applications, decisions and
source_audit arrays to represent distinctions in the supplied source. Metadata
recorded source identity, counts and limitations. No mandatory agricultural taxonomy,
database engine, ingestion service or connector was introduced.

This paragraph describes the historical extraction format. The current local
serialization schema is `amrkb.source-extraction/0.3.0`; its incompatible public
provenance representation and independent versioning are described below under
[Validation, versioning and next decisions](#validation-versioning-and-next-decisions).

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

## Independent neighbouring authorities

EIRKB and EII retain their own structured references and scientific presentations.
GISDS retains its geographic-source catalogue; OSDS retains its observation-source
register. Their records, classifications and counts are not AMRKB requirements.
DRM develops methodology and governance; IRKB owns independent interdisciplinary
synthesis. No operational mappings, shared taxonomy or automatic ingestion is implied.

## Validation, versioning and next decisions

Public validation:

```sh
python3 -B scripts/validate_amrkb.py
python3 -B -m unittest discover -s tests -v
```

Full evidence verification uses explicitly supplied workspace roots:

```sh
python3 -B scripts/validate_amrkb.py --evidence-root <archive-root> --development-root <development-root>
```

The Archive root resolves the manifest's portable source-edition paths. The
Development root resolves preserved pre-edit evidence and the template snapshot.
The public mode checks current structure, unique IDs, endpoints, counts, quotation
fingerprint syntax, extraction/comparison accounting, the reviewed preservation
projection, human parity and local file/heading links. Full mode additionally
checks exact archived bytes, quotation slices, original terms, ledger correspondence,
historical template hashes, the original scope README and pre-edit collections.
Missing evidence is an explicit unavailable-input failure in full mode, not a pass.
Neither mode proves scientific truth, genuine authority, historical completeness,
legal permission, or DRM conformance. Optional `jsonschema` checks serialization.
`--render-scientific` deliberately regenerates presentation; it is not acceptance.

README 0.3.3, Protocol 0.2.3, Machine/Scientific 0.3.0 and serialization schema 0.3.0
are independent documentary editions, not research releases. The schema revision
is an incompatible local serialization revision: it replaces public raw quotations
with archival locators and fingerprints. Earlier documents require deliberate migration,
not automatic upgrade or validation under the new schema. This revision does not
adopt a new ontology or MSP format. Original structured project statuses retain
their values and meanings; neutral display labels are recorded in Machine metadata.

The current display spelling is ICAERUS DDAL and ICAERUS. Existing REC-0286/0287
and REF-0012/0013 remain distinct; original terms and archival editions retain their
historical spelling. This correction establishes no identity equivalence. No family,
membership, relationship, reference candidate or scientific status was added or removed.

The exact original README and complete pre-edit evidence are preserved in Development;
the source manifest records the original README fingerprint. Old Git commits remain
accessible, including their historical source content; current redistribution does
not remove material from Git history. No history rewriting is performed.

Jonathan Minchin, Ecological Interaction, ORCID 0000-0001-8152-1796 remain attributed.
No licence, DOI, release date or publication permission is assigned. Further research,
identity resolution, source-level bibliography, harmonisation, diagrams, website
integration and publication require separately scoped approval.
