# Intent Entity Mapping

The following mapping identifies the entities required for each supported intent.

| Intent | Required Entities |
|----------|----------|
| Claim Status | member_id, claim_id |
| Claim Submission | member_id, claim_amount, service_date |
| Eligibility Check | member_id, plan_type |
| Benefits Inquiry | member_id, plan_type |
| Provider Lookup | zip_code, provider_specialty |
| Pre Authorization Status | member_id, authorization_id |
| Service Request | member_id, issue_type |
| Agent Escalation | member_id, escalation_reason |

## Authentication Related Entities

The following entities may be used during authentication and identity verification:

- member_id
- date_of_birth
- zip_code
- address
- ssn_last4

## Journey Related Entities

Different healthcare journeys may require different entity combinations based on the user's request and verification status.
