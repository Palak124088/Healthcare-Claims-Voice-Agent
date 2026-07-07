# Authentication Flow

## Overview

Authentication is mandatory before accessing any Protected Health Information (PHI). The Healthcare Claims Voice Assistant verifies the user's identity using multiple factors before routing the request to the appropriate domain agent.

---

## Authentication Parameters

| Parameter | Purpose |
|-----------|---------|
| Member ID | Identify the member record |
| Date of Birth (DOB) | Verify member identity |
| ZIP Code | Additional identity verification |
| Last 4 Digits of SSN | Final authentication check |

---

## Authentication Flow

<img width="1024" height="1536" alt="ChatGPT Image Jul 7, 2026, 09_41_16 PM" src="https://github.com/user-attachments/assets/4b73492f-b063-42e4-9fd8-9944d9dedecb" />


---

## Authentication Rules

- Authentication is required before accessing healthcare information.
- All user inputs are validated before verification.
- Protected Health Information (PHI) is never shared before successful authentication.
- Failed authentication allows up to two retry attempts before escalation.

---

## Expected Outcomes

- Successful authentication routes the request to the Supervisor Agent.
- Repeated authentication failures trigger escalation to a human support representative.
