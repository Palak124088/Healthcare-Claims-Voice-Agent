# Use Cases

## Overview

The Healthcare Claims Voice Assistant supports multiple healthcare use cases through secure authentication and intent-based routing.

| Use Case | Actor | Description | Outcome |
|----------|-------|-------------|---------|
| UC-01 | Healthcare Member | Check claim status | Current claim status is retrieved |
| UC-02 | Healthcare Member | Verify eligibility | Coverage and eligibility details are displayed |
| UC-03 | Healthcare Member | View benefits | Healthcare benefits and coverage information are provided |
| UC-04 | Healthcare Member | Find provider | In-network provider details are retrieved |
| UC-05 | Healthcare Member | Check pre-authorization | Pre-authorization status is displayed |
| UC-06 | Healthcare Member | Request human assistance | Conversation is transferred to a support representative |

## Common Flow

1. User initiates a request.
2. User provides consent.
3. User completes authentication.
4. Supervisor Agent identifies the intent.
5. Request is routed to the appropriate domain agent.
6. Tool/API is invoked.
7. Response is returned or the conversation is escalated if required.
