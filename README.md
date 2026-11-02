# Agricultural Modes Reference Knowledge Base (AMRKB)

**Work in Progress — Academic Research Resource**
**Document version:** 0.3.2 · Local extraction awaiting review; not a research release.

Jonathan Minchin · Ecological Interaction · [ORCID 0000-0001-8152-1796](https://orcid.org/0000-0001-8152-1796).

## Purpose and scope

AMRKB is an independent research project within Ecological Information, covering agricultural history, modes, systems, methods, practices and technologies. It includes traditional, Indigenous, industrial, ecological, experimental and emerging approaches across historical periods and geographical regions. Its classifications remain provisional.

Research dimensions include historical development and diffusion; philosophies and traditions; technical methods and infrastructure; relationships with soil, water, biodiversity and ecological processes; climate, terrain and place-specific suitability; and labour, land tenure and productive organisation.

Keep modes, systems, methods, practices, technologies, ecological mechanisms and indicators distinct, and record explicit relationships between them.


## Research registers and source

- [Scientific Reference Register](AMRKB_Scientific_Reference_Register.md): definitions, eight overlapping working families, functional inventories, contexts, qualifications, themes and incomplete source candidates.
- [Machine Reference](AMRKB_Machine_Reference.json): the sole structured authority for this source extraction, with separate identities, classifications, memberships, assertions, references and line-level provenance.
- [Research Protocol](AMRKB_Research_Protocol.md): decisions, coverage crosswalk, identity/schema rules and limitations. Both the [recovered extraction edition](history/20261101_AMRKB_Chat_History_Extraction_Edition.md) and [current history](history/20261101_AMRKB_Chat_History.md) are preserved unchanged. See the [source-edition reconciliation](AMRKB_Source_Edition_Reconciliation.md).
- [Citation](CITATION.cff) and [changelog](CHANGELOG.md): attribution and actual development history, not a release or licence.

The 247-line extraction edition yields **292 documentary candidate entries**
(274 research terms, 13 named research/source candidates and 5 external
project/layer labels), not 292 verified agricultural entities.
There are 222 proposed family associations, counted separately from unique
entries; not every entry has a family. No scientific claim or named-source
identity is independently verified by this intake.

On 2 November 2026 the owner confirmed that both incomplete documentary editions
originate from the normal “AMRKB Overview” research conversation. This confirms
origin only, not authenticated message metadata, speakers, original dates or
conversation completeness. The 247-line edition supports the recorded extraction;
the 393-line edition was separately compared, not fully scientifically extracted.

Detailed family-1 and family-2 inventories are unavailable; detailed family-8
expansion is deferred/unavailable. Bibliography remains incomplete; five
methodological groups are unnamed and certification placement is unresolved.
ICARUS and ICARUS DDAL remain separate pending evidence. AgriFM and AgroGPT are
retained despite later omission. Lexical variants and mixed entity types remain
unresolved; the Precision/Computational repeat request does not establish
approval. Scientific and field-evidence verification remains outstanding.

## Working organisation

These provisional, overlapping labels come from the Machine Reference; they do
not constitute an accepted taxonomy or require every entry to have a family.

**Eight working families:** [Traditional and Indigenous](AMRKB_Scientific_Reference_Register.md#traditional-and-indigenous); [Extensive and pastoral](AMRKB_Scientific_Reference_Register.md#extensive-and-pastoral); [Intensive and industrial](AMRKB_Scientific_Reference_Register.md#intensive-and-industrial); [Ecological and organic](AMRKB_Scientific_Reference_Register.md#ecological-and-organic); [Regenerative and conservation](AMRKB_Scientific_Reference_Register.md#regenerative-and-conservation); [Agroecological and diversified](AMRKB_Scientific_Reference_Register.md#agroecological-and-diversified); [Precision and computational](AMRKB_Scientific_Reference_Register.md#precision-and-computational); [Experimental and emerging](AMRKB_Scientific_Reference_Register.md#experimental-and-emerging).

**Twelve cross-family functions:** [Soil management](AMRKB_Scientific_Reference_Register.md#soil-management); [Water management](AMRKB_Scientific_Reference_Register.md#water-management); [Nutrient management](AMRKB_Scientific_Reference_Register.md#nutrient-management-2); [Biodiversity management](AMRKB_Scientific_Reference_Register.md#biodiversity-management); [Crop organisation](AMRKB_Scientific_Reference_Register.md#crop-organisation-2); [Tree integration](AMRKB_Scientific_Reference_Register.md#tree-integration-1); [Livestock integration](AMRKB_Scientific_Reference_Register.md#livestock-integration-1); [Pest management](AMRKB_Scientific_Reference_Register.md#pest-management); [Microbiome management](AMRKB_Scientific_Reference_Register.md#microbiome-management); [Landscape management](AMRKB_Scientific_Reference_Register.md#landscape-management); [Climate adaptation](AMRKB_Scientific_Reference_Register.md#climate-adaptation); [Monitoring and automation](AMRKB_Scientific_Reference_Register.md#monitoring-and-automation).

**Five cross-cutting themes:** [Open agricultural technology](AMRKB_Scientific_Reference_Register.md#cross-cutting-research-and-application-domains); [Agricultural AI and knowledge systems](AMRKB_Scientific_Reference_Register.md#cross-cutting-research-and-application-domains); [Agricultural robotics](AMRKB_Scientific_Reference_Register.md#cross-cutting-research-and-application-domains); [Information infrastructure](AMRKB_Scientific_Reference_Register.md#cross-cutting-research-and-application-domains); [Ecologically informed agricultural design](AMRKB_Scientific_Reference_Register.md#cross-cutting-research-and-application-domains). These are research/application themes, not additional agricultural families.

## Method, federation and review boundary

Corpus, analysis and synthesis remain distinct. AMRKB owns its source research;
DRM develops shared conventions; IRKB independently authors interdisciplinary
research and synthesis. Candidate cross-project connections are not verified
record mappings or operational services. No three-dimensional federation taxonomy
is adopted. DRM-MSP 0.1.0 review revision 2 remains an unadopted methodological
candidate. DRM records the bounded Phase 4 documentary pilots as completed
and closed. This AMRKB update does not constitute scientific verification,
general MSP conformance or authorisation for Phase 5.

Run `python3 -B scripts/validate_amrkb.py`; optional installed `jsonschema`
validates the local extraction schema. The validator checks source preservation,
coverage, IDs, references, counts and exact human/structured presentation parity,
not scientific truth. `--render-scientific` explicitly regenerates the human
presentation from the structured authority; it is not a research acceptance step.

This Stage B update is documentation and metadata maintenance only. Stage C
visual review and owner acceptance remain pending. Further steps require explicit
review of identity, source-level bibliography and scientific evidence before
verification, taxonomy redesign, harmonisation or publication. No external
literature was researched. No licence, DOI, public repository URL or release
is assigned. Public access and citation do not grant reuse permission.
