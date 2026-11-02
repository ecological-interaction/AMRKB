# Project instructions

Agricultural Modes Reference Knowledge Base. Read README.md. Keep classifications provisional and defer database implementation until the conceptual framework is developed.

- This directory is an independent Git repository within the ecological-information umbrella.
- Keep work within this project unless cross-project changes are explicitly requested.
- Preserve research content and provenance. Keep version information inside documents and use stable filenames.
- Prepare interoperability through explicit identifiers, references and relationships; do not merge the projects' scopes.
- Do not push to GitHub or configure a remote unless the user requests it.

## File authority and source-extraction boundary

- Read README.md, AMRKB_Research_Protocol.md and the Machine JSON before changes. Machine JSON is the structured-record authority as accepted content is added; scientific tables are the human presentation. The protocol owns methods and preserved context; README is the concise entry point.
- Preserve the original README verbatim inside the protocol's preservation markers. Do not rewrite that history or confuse historical repository-setup claims with current state.
- Local history extraction is now authorised. Preserve history bytes and the hashed template baseline; use Machine JSON as the sole authority and regenerate the Scientific Register deliberately. Extracted candidates and memberships are not independently verified science. No invented records, bibliography, external bindings or acceptance/reviewer events.
- This intake is limited to history/20261101_AMRKB_Chat_History.md. Do not retrieve other conversations, attachments or new literature. Further scientific verification, taxonomy redesign, harmonisation or publication requires separate authorisation.
- Preserve independent source/DRM/infrastructure/IRKB authority. Current DRM-MSP is a review candidate; do not advance its phase or closed pilot gate, copy neighbour taxonomies or claim conformance.
- Run python3 -B scripts/validate_amrkb.py; optional installed jsonschema checks the local extraction schema. --render-scientific explicitly regenerates the human presentation. Preserve local IDs, provenance quotes, statuses, distinctions and unresolved identity; never infer scientific validity from structural success.
- Use local links until public remote details are verified. Do not add a licence, DOI, release or website integration. Any later diagram requires editable source, accessible generated SVG and reproducible rendering; none is needed now.
