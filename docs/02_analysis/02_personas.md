# User Personas

## Overview

The Healthcare Claims Voice Agent is designed to support different users within the healthcare ecosystem. Each user interacts with the system based on their role, responsibilities, and business requirements. Understanding these personas helps design secure, user-centric, and efficient conversational journeys.

---

## Persona 1 – Member

### Description

A healthcare plan member who interacts with the voice agent to access healthcare services and information.

### Primary Goals

- Check claim status
- Submit a new claim
- Verify eligibility
- Understand plan benefits
- Find in-network providers
- Check pre-authorization status

### Authentication Required

- Member ID
- Date of Birth
- ZIP Code / Address
- Last 4 digits of SSN

---

## Persona 2 – Healthcare Provider

### Description

A healthcare provider, hospital, or clinic requesting information on behalf of a member.

### Primary Goals

- Verify member eligibility
- Check pre-authorization requirements
- Confirm provider network participation

### Authentication Required

- Provider Credentials *(Future Scope)*
- Member Verification Details

---

## Persona 3 – Customer Support Representative

### Description

A human support representative responsible for handling conversations that require manual intervention.

### Primary Responsibilities

- Resolve escalated conversations
- Handle claim disputes
- Assist with authentication failures
- Review conversation history
- Complete unresolved requests

### Information Available During Escalation

- Member ID
- Authentication Status
- Detected Intent
- Conversation Summary
- Available API Responses

---

## Summary

The Healthcare Claims Voice Agent supports multiple user groups, each with different objectives and interaction requirements. These personas help define authentication needs, conversation design, healthcare journeys, and escalation strategies throughout the solution.
