# Use Cases

## Overview

The Healthcare Claims Voice Agent enables members to complete common healthcare requests through a secure conversational interface. Each use case represents a supported member journey from authentication to successful request completion.

---

## UC-01 Claim Status

**Actor:** Member

**Description:**
The member checks the current status of an existing healthcare claim.

**Preconditions:**

- Member provides consent.
- Member authentication is successful.
- Valid Claim ID is available.

**Flow**

<img width="1024" height="1536" alt="ChatGPT Image Jul 7, 2026, 06_56_15 PM" src="https://github.com/user-attachments/assets/2aae3374-b5d0-4ac3-af83-ebe0b2e2100f" />


**Expected Outcome**

The member receives the latest claim status.

---

## UC-02 Eligibility Verification

**Actor:** Member

**Description:**
The member verifies healthcare plan eligibility and coverage.

**Flow**

<img width="1024" height="1536" alt="ChatGPT Image Jul 7, 2026, 06_58_12 PM" src="https://github.com/user-attachments/assets/c1ca2c8f-e21e-4a25-8f54-3f32a9d2c896" />


**Expected Outcome**

The member receives eligibility and coverage information.

---

## UC-03 Benefits Inquiry

**Actor:** Member

**Description:**
The member requests information about healthcare benefits available under their plan.

**Expected Outcome**

The agent retrieves and explains the member's available benefits.

---

## UC-04 Provider Lookup

**Actor:** Member

**Description:**
The member searches for an in-network healthcare provider.

**Expected Outcome**

The agent provides matching provider information based on the member's location or ZIP code.

---

## UC-05 Pre-Authorization Status

**Actor:** Member

**Description:**
The member checks whether a medical service requires pre-authorization and its current approval status.

**Expected Outcome**

The member receives the current pre-authorization status.

---

## UC-06 Claim Submission

**Actor:** Member

**Description:**
The member submits a new healthcare claim through the conversational agent.

**Expected Outcome**

The claim is successfully submitted and a confirmation is provided.

---

## UC-07 Human Agent Escalation

**Actor:** Member

**Description:**
The conversation is transferred to a human representative when the issue cannot be resolved automatically or when requested by the member.

**Expected Outcome**

The conversation is handed over with the available context.
