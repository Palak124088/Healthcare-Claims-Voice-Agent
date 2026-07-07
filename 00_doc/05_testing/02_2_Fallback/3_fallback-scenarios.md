# Fallback Scenarios

## Supported Fallback Scenarios

| ID | Scenario | Recovery Action |
|----|----------|-----------------|
| FB-001 | Unknown Intent | Ask the user to rephrase the request |
| FB-002 | Low Confidence Intent | Ask a clarification question |
| FB-003 | Ambiguous Request | Request additional information |
| FB-004 | Multiple Intents | Ask the user to complete one request first |
| FB-005 | Incomplete Request | Ask for missing information |
| FB-006 | Unsupported Request | Inform the user about supported services |
| FB-007 | Clarification Retry Limit Reached | Human Agent Escalation |

---

## Recovery Strategy

1. Request clarification.
2. Maintain conversation context.
3. Retry intent identification.
4. Continue the workflow if the intent is identified.
5. Escalate to a human representative if recovery is unsuccessful.
