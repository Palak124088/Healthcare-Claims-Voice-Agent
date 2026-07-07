# Sub-Agents

## Overview

The Healthcare Claims Voice Assistant uses specialized sub-agents to handle different healthcare workflows. Each sub-agent is responsible for a specific business function and invokes the required backend tool or API.

---

## Sub-Agents

| Agent | Responsibility | Tool | API |
|--------|----------------|------|-----|
| Claims Agent | Retrieve claim status | ClaimStatusTool | `getClaimStatus()` |
| Eligibility Agent | Verify member eligibility | EligibilityTool | `checkEligibility()` |
| Benefits Agent | Retrieve benefit details | BenefitsTool | `getBenefits()` |
| Provider Agent | Search in-network providers | ProviderTool | `providerLookup()` |
| Pre-Authorization Agent | Check authorization requirements | PreAuthTool | `getPreAuthorizationStatus()` |
| Escalation Agent | Transfer to human support | ServiceRequestTool | `createServiceRequest()` |

---

## Execution Flow

<img width="1536" height="1024" alt="ChatGPT Image Jul 7, 2026, 09_58_49 PM" src="https://github.com/user-attachments/assets/f6f1447a-3aa2-4c70-a700-dff8beb3f034" />

```

---

## Design Principles

- Each sub-agent handles a single healthcare workflow.
- Business logic is isolated to improve maintainability.
- Backend communication is performed through Python tools.
- The Supervisor Agent coordinates all routing decisions.
- Conversation context is preserved across agent handoffs.
