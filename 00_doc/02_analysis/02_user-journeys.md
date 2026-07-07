# User Journeys

## Overview

The Healthcare Claims Voice Assistant supports multiple healthcare journeys through a secure authentication process and intent-based routing.

---

## Supported Journeys

| Journey | Description | API |
|----------|-------------|-----|
| Claim Status | Retrieve the current status of a submitted claim | `getClaimStatus()` |
| Eligibility Check | Verify member eligibility and coverage | `checkEligibility()` |
| Benefits Inquiry | View healthcare benefits and coverage details | `getBenefits()` |
| Provider Lookup | Find in-network healthcare providers | `providerLookup()` |
| Pre-Authorization | Check pre-authorization requirements and status | `getPreAuthorizationStatus()` |
| Escalation | Transfer the conversation to a human support agent | `createServiceRequest()` |

---

## Standard Journey Flow
<img width="823" height="1912" alt="ChatGPT Image Jul 7, 2026, 09_09_26 PM" src="https://github.com/user-attachments/assets/ef922ff3-98b1-4f34-a30b-56cef855c336" />


---

## Journey Principles

- Authentication before accessing PHI
- Intent-based routing
- Tool/API-driven responses
- Context preservation across journeys
- Human escalation when required
