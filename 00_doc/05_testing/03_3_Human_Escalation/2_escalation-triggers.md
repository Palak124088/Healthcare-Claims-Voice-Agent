*# Human Escalation Triggers

The following scenarios require the conversation to be transferred to a human representative.

| Trigger ID | Scenario | Action |
|------------|----------|--------|
| HE-001 | Authentication failed after maximum retry attempts | Human Escalation |
| HE-002 | User explicitly requests a human agent | Human Escalation |
| HE-003 | Low confidence after clarification attempts | Human Escalation |
| HE-004 | Backend API unavailable after retry | Human Escalation |
| HE-005 | Claim requires manual verification | Human Escalation |
| HE-006 | Compliance or sensitive request | Human Escalation |
| HE-007 | Unexpected system error | Human Escalation |

---

## Escalation Information

Before transferring the conversation, the system should provide the following information to the human representative:

- Authenticated member details
- Current conversation summary
- Identified intent
- Journey reached
- Error or escalation reason*
