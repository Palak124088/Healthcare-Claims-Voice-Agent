# Guardrails

## Overview

Guardrails ensure that the Healthcare Claims Voice Assistant provides secure, reliable, and compliant interactions while protecting sensitive healthcare information.

---

## Input Guardrails

- Detect unsupported requests
- Handle invalid or incomplete user input
- Prevent prompt injection attempts
- Detect abusive or inappropriate language

---

## Security Guardrails

- Require authentication before accessing PHI
- Validate user identity using Member ID, DOB, ZIP Code, and SSN
- Prevent unauthorized access to healthcare information
- Restrict backend tool execution to authenticated users

---

## Conversation Guardrails

- Route requests only to supported healthcare journeys
- Trigger fallback for unsupported intents
- Preserve conversation context across agent handoffs
- Retry failed authentication and API requests within configured limits

---

## Escalation Guardrails

Escalate the conversation when:

- Authentication repeatedly fails
- User requests a human agent
- Backend services are unavailable
- Claim disputes are raised
- Tool or API failures cannot be recovered

---

## AI Safety

The assistant does not:

- Provide medical diagnosis
- Recommend treatments or medications
- Interpret healthcare policies
- Generate information not returned by authorized backend systems
