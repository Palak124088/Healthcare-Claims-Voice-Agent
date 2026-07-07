# Conversation Flow

## Overview

The Healthcare Claims Voice Assistant follows a standardized conversation flow for all supported healthcare services. Every request is authenticated before being routed to the appropriate domain agent.

---

## Master Conversation Flow
<img width="1024" height="1536" alt="ChatGPT Image Jul 7, 2026, 09_18_44 PM" src="https://github.com/user-attachments/assets/7f78019a-0c80-4ebb-b263-3de821f186f3" />


---

## Conversation Steps

1. User initiates a healthcare request.
2. Agent requests user consent.
3. User is authenticated using Member ID, DOB, ZIP Code, and SSN.
4. Supervisor Agent identifies the user's intent.
5. Request is routed to the appropriate domain agent.
6. Domain agent invokes the required tool/API.
7. Agent presents the response.
8. Conversation ends or escalates to a human agent if required.

---

## Exception Handling

- Authentication failure → Retry → Escalation
- Invalid Claim ID → Retry
- Unsupported request → Fallback response
- API timeout → Retry → Escalation
- User requests human agent → Immediate escalation
