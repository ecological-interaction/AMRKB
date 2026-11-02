# AMRKB — Research Protocol

**Document version:** 0.1.0 · **Prepared:** 1 November 2026.  
**Work in Progress — Academic Research Resource.** Template preparation only;
not a database release, scientific review result or DRM conformance claim.

## Existing decisions and preserved scope

The existing repository defines agricultural history, modes, systems, methods,
practices and technologies as its remit. Its complete original README is
preserved verbatim in the historical section below. Those academic paragraphs
remain applicable. Its old no-remote sentence describes the original edition;
current Git configuration was inspected read-only and is not changed here.
No published repository address is asserted by these templates.

The original Markdown-first conceptual development, referenced inventory,
possible later SQLite store, Zotero/GIS compatibility and prospective exports
remain intentions. JSON is now the empty structured-record container; it is
not implementation of the proposed database engine or external integrations.
No existing accepted records or issued scientific/classification identifiers
were found in the current files or the single existing commit. This is a
bounded local file/history check, not an audit of unreviewed conversation sources.

## Neighbouring file-architecture assessment

Read-only local comparison on 1 November 2026:

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

## Adopted local structure and authority

This task adopts file roles and empty templates, not scientific classification
or DRM operational rules:

- README: purpose, status, navigation and research boundary.
- Scientific Reference Register: unpopulated readable register and source tables.
- Machine JSON: structured-record authority as separately accepted records are added.
- Research Protocol: scope, method, review rules, comparison and preserved context.
- CFF: academic attribution; CHANGELOG: actual development events, not releases.
- AGENTS: maintenance instructions; .gitignore: local artefacts only.
- Local schema and validator: repeatable empty-template integrity checks.

Corpus is collected material and its descriptions/provenance. Analysis examines
and organises it; synthesis develops attributed arguments and frameworks. These
are epistemic responsibilities, not a rule that every file has a single kind of
knowledge. AMRKB retains its own domain research and synthesis. IRKB independently
owns interdisciplinary research/synthesis. A future typed relationship does not
transfer research authority; participating databases retain their own records,
classifications, schemas, evidence and acceptance decisions.

## Current DRM authority and limits

Read current standalone DRM README, DEVELOPMENT_STATUS.md,
DRM_Architecture_and_Remit.md, DRM_v1_Roadmap.md,
DRM_Methodological_Architecture.md, DECISIONS.md and the MSP review candidate.
The standalone DRM repository is the current working authority; earlier umbrella
scaffolds and historical plans are not competing current specifications.
These names identify read-only review sources, not dependencies imported here.

Approved planning architecture treats DRM as methodology-first, distinguishes
A–F database design/evaluation from its eight development phases, permits domain
autonomy/overlap and direct application access, and separates methodology,
infrastructure, source science and IRKB authorship. Bounded Phase 1 evidence is
accepted. The specified Phase 2 decisions approved for Phase 3 concern
proportionate obligations, DRM-owner methodological exceptions, retained domain
science/rights authority, mapping/assertion roles, compatibility by effect and
accountable profile/boundary review. They are not blanket adoption of every
historical disposition or draft detail.

DRM-MSP 0.1.0, proposal template, synthetic fixtures and checker are prepared for
review, not adopted/released. Candidate lifecycle states, envelope fields and
relationship vocabularies are not installed here. P3-GATE-01 remains closed
before Phase 4 pending owner review of forthcoming domain analysis and explicit
pilot inputs, scope, rights, preservation, reviewers and success criteria.
This AMRKB file task supplies neither that domain analysis nor pilot inputs,
advances no DRM phase and awards no scientific or technical certification.

DRM governs developing shared conventions and interoperability; federation
infrastructure implements contracts, while source databases govern research
acceptance. Structural validation does not establish source truth, rights,
reviewer authority or equivalence of classifications.

## Stable identifiers and provisional classifications

No identifier sequence, namespace syntax, prefix or classification codes are
issued. Future intake must check existing source material for identities first,
distinguish source IDs from local IDs, document uncertain equivalence and obtain
an explicit allocation policy. Retain issued identifiers, never recycle them or
renumber on reclassification; aliases/deprecation need evidence and review.

Systems, modes, methods, practices and technologies are candidate distinctions
already named in scope. Their cardinalities, relations and appropriate entity
models require content review. No mandatory agricultural taxonomy, fixed domain
count or universal record shape is introduced. Reuse, semantic alignment and
new synthesis are separate operations; similar labels are not equivalence.

## Reference, provenance and assertion expectations

Future candidates need actual source/edition/locator, attributable extraction or
authorship, rights/limitations, uncertainty and the context for any interpretation.
A bibliography, explanatory source reference and claim-support relationship are
different objects. Do not invent references, verified status, contributors,
reviewers, acceptance events or dataset bindings. No research bibliography is
added by this task.

Represent relationships only after deciding what endpoints and meanings are
justified: retain type, author/source, evidence, scope and review state, and keep
structural mapping separate from scientific assertions and IRKB interpretation.
Unresolved external identity stays explicitly unresolved; internal references
must resolve within the declared authoritative scope. No cross-database mappings
or relationship instances are populated here. Detailed field contracts and
review vocabulary remain proposals for later domain/DRM review.

## Missingness and template schema

The Machine Reference metadata explains missing, unknown, not applicable and
confirmed absence. Omitted means unsupplied. A future reviewed field may pair
`value: null` with `value_status: unknown`, or with `not_applicable` plus rationale.
Bare null is not confirmed absence. Confirmed absence needs an explicit scoped
assertion and supporting evidence after review. These are proposed encoding
conventions, not assertions about agricultural entities or a mandatory payload
model for every object. Empty arrays mean zero accepted entries here.

The local `amrkb.empty-template/0.1.0` schema deliberately permits no populated
research collections at this stage. It validates the document envelope, required
metadata, template state and empty collections; it does not design agricultural
record schemas. Before population, separately approve intake, identity policy,
representation needs and a reviewed schema/validator revision. This staged
constraint prevents accidental ingestion without imposing a premature ontology.

## Maintenance, versions and proportional validation

README 0.2.0 replaces its initial 0.1.0 presentation, with full original text
preserved below. The scientific template, machine document, Research Protocol
and local empty-template schema start at 0.1.0 independently. No database/research
release, publication date, DOI or licence is assigned. CFF names Jonathan Minchin,
Ecological Interaction and ORCID 0000-0001-8152-1796, without an unverified remote
URL. Citation/public access do not grant reuse rights.

Run `python3 scripts/validate_amrkb.py`. With installed jsonschema it also checks
Draft 2020-12 schema validity and the instance; without it, the standard-library
checks still enforce this bounded template's required metadata, empty collections,
zero counts, local links and scientific header-only tables. Report that schema
validation was not run if the optional dependency is absent. No dependency
installation or shared runtime is required by this task.

The preserved README source SHA-256 is **4eb11eb8f9ead8d907007dc26d0c469d8dda78b1d250b9dab1b9205d10708ea1**; the validator verifies its exact
historical text. Checks are local file/structure checks only, not a scientific
review, MSP adoption, ingestion engine or evidence verification.

## Decisions pending before research intake

- Review the AMRKB Overview material only after separate explicit authorisation.
- Identify real source entities, existing IDs, rights, sensitivities, provenance
  and competency questions; do not infer them from scope headings.
- Decide identity/alias policy, reference model, candidate fields, classification
  ownership/extensions and typed relationships using actual evidence.
- Establish domain review/acceptance authority and proportionate change tracking;
  no reviewer assignment or Development Register duplication is needed now.
- Review schema and missingness choices against actual research; preserve
  conflicting claims and independent domain meanings.
- Approve any later diagram, storage engine, federation contract or publication
  separately. SQLite and external-service intentions remain unimplemented.

**Next task:** Separately authorised review of AMRKB Overview and candidate
research intake. No conversation or attachment was retrieved, audited, summarised
or ingested in preparing these files. No scientific acceptance or DRM gate has
been advanced.

## Historical README — preserved original scope and intentions

The following exact initial README is documentary context, not a claim that its
historical repository-setup statement remains current. Current file roles above
supersede only the earlier architecture/authority statements; research scope and
methodological intentions are preserved. No missing research is reconstructed.

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
