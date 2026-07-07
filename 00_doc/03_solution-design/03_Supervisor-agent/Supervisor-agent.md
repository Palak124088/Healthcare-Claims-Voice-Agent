# Supervisor Agent

## Overview

The Supervisor Agent acts as the central orchestrator of the Healthcare Claims Voice Assistant. It analyzes authenticated user requests, identifies the user's intent, and routes the conversation to the appropriate domain-specific agent.

---

## Responsibilities

- Receive requests after successful authentication
- Detect user intent
- Route conversations to the correct domain agent
- Maintain conversation context
- Coordinate tool and API execution
- Trigger escalation when required

---

## Routing Logic

| Detected Intent | Routed Agent |
|-----------------|--------------|
| Claim Status | Claims Agent |
| Eligibility Check | Eligibility Agent |
| Benefits Inquiry | Benefits Agent |
| Provider Lookup | Provider Agent |
| Pre-Authorization | Pre-Authorization Agent |
| Human Assistance | Escalation Agent |
| Unsupported Request | Fallback / Escalation |

---

## Decision Flow

<img width="1086" height="1448" alt="ChatGPT Image Jul 7, 2026, 09_54_44 PM" src="https://github.com/user-attachments/assets/2f3f1c41-68a6-40b1-b183-2e8ea79ab4ba" />


---

## Key Design Principles

- Authentication before intent routing
- Context-aware conversations
- Intent-based routing
- Modular agent architecture
- Human escalation for unsupported or complex requests
