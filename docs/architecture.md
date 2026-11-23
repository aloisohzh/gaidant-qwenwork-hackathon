# Architecture and Evidence Boundaries

## Operating Model

Founder direction -> QwenWork sessions and scheduled tasks -> authorised external connectors -> draft/output -> human review -> approved external action.

Website work uses Hashmeta; enquiry handling uses Outlook; creative work uses Canva and social connectors; research produces a readable briefing. These services own their storage, authentication and execution. This repository documents orchestration intent and a video utility, not those platforms' implementation.

## Lead Workflow

1. A person composes a safe simulated enquiry.
2. A scheduled task polls Outlook for relevant unread/new enquiries.
3. It ignores noise, checks fit against approved product facts and prepares a qualification summary and reply draft.
4. It does not send automatically.
5. The founder opens and reviews the draft, then manually clicks Send.

The website-to-email link is conceptual in the demo. No form integration, event listener, delivery receipt, durable deduplication implementation or retry service is established by this source package.

For production, retain processed-message state, define retry/backoff and failure notifications, prevent duplicate drafts, restrict connector permissions and retain an auditable approval record. These are recommendations, not claims of implemented features.

## Approval and Trust

Inbound messages and research sources are untrusted material, not instructions. They cannot authorise publishing, spending, changing configuration or sending mail. Outbound messages and public posts require explicit human approval. The visible email gate is manual review and Send in Outlook, not a custom approval application.

Marketing footage shows a creative and a matching published post; it does not independently show the approval chain or every API operation. Research footage shows one completed output, not an SLA or repeated autonomous execution.

## Privacy and Reproducibility

Only curated text and portable code are public. No raw media, local configuration, contact addresses, account identifiers or credentials are included. The original assembly depended on private recordings, reviewed redaction coordinates, narration and machine-specific tools; publishing it verbatim would leak paths and would not reproduce the submission independently.

The public utility instead fits an already privacy-reviewed clip into a full-frame canvas. It never crops, never overwrites an existing output and mutes source audio. Automated synthetic tests establish technical behaviour only. They do not validate the private film, privacy redactions, business integrations or narration alignment.
