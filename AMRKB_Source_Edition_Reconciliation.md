# AMRKB source-edition reconciliation

**Prepared:** 1 November 2026. **Status:** Local provenance repair for owner review;
not a scientific intake, research release, MSP adoption or DRM pilot.

## Finding and exact recovery

The existing extraction cited a mutable history path with the hash/locators of
an earlier edition. Before repair, the documented validator exited 1: source
hash/line count mismatch, 26 quotation-slice mismatches and incomplete final
coverage. Optional full JSON Schema checking was unavailable (`jsonschema` not
installed); no dependencies were installed.

The complete earlier text is embedded in `AMRKB-PRO-0088.original_text`.
Recovery as UTF-8 **without adding a final newline** reproduced its existing hash
exactly. No quotations were reconstructed, reworded or moved to new line numbers.
The present history file was not overwritten.

| Edition | Preserved file | SHA-256 | Lines / bytes |
|---|---|---|---|
| AMRKB-SRCED-0001 | [Extraction edition](history/20261101_AMRKB_Chat_History_Extraction_Edition.md) | `1902b7263a0df34084b58532f01fa16cc70497d373a1332e568e171905b18faf` | 247 / 23385 |
| AMRKB-SRCED-0002 | [Current history](history/20261101_AMRKB_Chat_History.md) | `333c42970b7d4268aca8a848fef633bcf7b215a0179ec74fa8fd40b15ca98bf7` | 393 / 25900 |

These are local edition identifiers, not scientific/federation entity IDs.
Recovery date does not establish original creation date, original editing author,
message date, authentic speaker metadata, complete transcript or historical
approval. Both editions are immutable evidence; later evidence needs a new file
and edition identity rather than mutation.

The [edition manifest](AMRKB_Source_Editions.json) records origins, edition roles,
byte/hash/line/newline properties and the pre-repair branch, HEAD, configured
remote, working status and all 21 original file hashes. Those baseline hashes
identify inputs, not assertions that active repaired files still match old bytes.
The configured remote was not contacted or changed.

## Edition-comparison ledger and coverage

[AMRKB_Source_Edition_Comparison.json](AMRKB_Source_Edition_Comparison.json)
contains five stable local comparison entries, exact edition/range references,
slice fingerprints, dispositions and supporting extraction references.

| Comparison ID | Earlier lines | Current lines | Treatment |
|---|---|---|---|
| AMRKB-EDCMP-0001 | 1–206 | 1–206 | Unchanged and already represented by the original extraction. |
| AMRKB-EDCMP-0002 | 198–205 | 207–214 | Exact repeated next-step/scope passage, contextual only; no second approval. |
| AMRKB-EDCMP-0003 | — | 215–350 | Added spacing, greetings, opening dialogue and recap request; contextual, no scientific intake. |
| AMRKB-EDCMP-0004 | — | 351–352 | Added assistant-style recap. Scope/families/functions already represented; retrospective agreement assertions remain unauthenticated and do not create decisions. |
| AMRKB-EDCMP-0005 | 207–247 | 353–393 | Exact unchanged suffix moved by the 146-line insertion. Existing locators stay on the earlier edition. |

No earlier passage was altered or deleted. All 393 current lines have comparison
accounting; this is **not** scientific extraction of 393 lines. Original 23 audit
spans cover exactly the 247-line extraction edition. All 88 provenance entries
now name that edition/path/hash explicitly; their IDs, exact quotations and line
ranges remain unchanged. Secondary correspondence does not replace the edition
that originally supported extraction. No additional record, classification,
membership, relationship, application, theme, reference or decision was accepted.
The added recap's assertions about earlier agreement require owner review if
used as historical approval evidence; no new agricultural content is extracted.

## Files and version rationale

- Machine Reference: corrected source metadata and explicit edition references
  on provenance/audit spans; document 0.2.0 → 0.2.1. No scientific payload change.
- Source-edition manifest, comparison ledger, this report and exact recovered
  history file: documentary evidence only, no competing scientific catalogue.
- Validator/renderer: strict two-edition hashes, quotation/audit edition binding,
  comparison correspondence/coverage and corrected human source navigation.
- Scientific Register: only header version 0.2.1 and reading-key source links
  changed; all research text, tables and L labels below that correction unchanged.
- README 0.3.1 and Protocol 0.2.1: accurate edition-specific coverage and links.
  Preserved original README markers/content and template history remain exact.
- Schema retains `amrkb.source-extraction/0.2.0`: no collection/field structure or
  scientific semantics changed. Existing additive metadata is permitted already;
  document-version enum explicitly accepts 0.2.0/0.2.1. It does not equate schema,
  document or source-edition versions. Historical schema remains untouched.
- Changelog and focused regression tests document the actual repair and limits.

## Validation and preservation

Run from the repository root:

```sh
python3 -B scripts/validate_amrkb.py
python3 -B -m unittest discover -s tests -v
```

The first command must check both immutable editions, every exact provenance
slice, each source-audit edition/range and complete extraction coverage, ledger
correspondence/target coverage, IDs/endpoints, counts, preserved template/original
README, exact human rendering and local links. It rejects changed bytes or
repinning rather than normalising/remapping quotations to obtain a pass.
Focused tests use isolated temporary copies and exercise edition tampering,
wrong/missing edition references, altered quotations, audit/ledger gaps and
strict edition declarations. Synthetic corruptions are not source edits.

The repair preserves 292 candidate records, 66 classification definitions,
476 memberships, 46 relationships, 13 named references, 88 provenance IDs,
5 themes, 13 applications, 10 decisions and 23 source-audit IDs: 1,032 existing
local IDs. Scientific payloads, quotations, qualifications, uncertainty, source
ambiguities and statuses remain unchanged. Both source byte streams, original
README and existing template baseline remain preserved. No other repository
or Git metadata is modified.

Final checks on 1 November 2026: the documented validator exited 0 and all six
focused unittest methods passed, including deliberate negative cases and
scientific-payload/presentation preservation. All 88 quotations resolve to the
recovered edition; both source hashes, 23 audit spans and five comparison entries
pass. Optional full JSON Schema validation remains unavailable because
`jsonschema` is not installed; it is not counted as passed. No dependencies were
installed. Structural success is not scientific verification, legal permission
or genuine authority.

## Remaining gaps and review boundary

Detailed families 1/2, later family-8 expansion, source bibliography, five unnamed
methodological groups, certification placement and named-identity ambiguities
remain unresolved. The longer edition adds context, not proof those missing
research sections exist or that source claims were scientifically accepted.
Owner review may authorise later extraction or approval analysis separately.

The edition baseline is reproducible when the above checks pass, and can support
subsequent pilot **planning**. That is not scientific verification, pilot readiness
or permission to execute a pilot. The pre-Phase-4 checkpoint remains closed.
No DRM/MSP changes, external services, authoritative research intake, migrations,
staging, commits, remote changes, pushes, tags, publication or deployment.
