# Tools and APIs

## Overview

The Healthcare Claims Voice Assistant uses Python tools in CX Agent Studio to communicate with backend healthcare services. Each tool is responsible for executing a specific business function by invoking the corresponding API.

---

## Tool Mapping

| Tool | API | Purpose |
|------|-----|---------|
| AddressValidationTool | `validateAddress()` | Authenticate member identity |
| ClaimStatusTool | `getClaimStatus()` | Retrieve claim status |
| EligibilityTool | `checkEligibility()` | Verify healthcare eligibility |
| BenefitsTool | `getBenefits()` | Retrieve healthcare benefits |
| ProviderTool | `providerLookup()` | Find in-network providers |
| PreAuthTool | `getPreAuthorizationStatus()` | Check pre-authorization status |
| ClaimUpdateTool | `updateClaim()` | Update claim information *(Future Scope)* |
| ServiceRequestTool | `createServiceRequest()` | Create escalation requests |

---

## Tool Execution Flow

<img width="1024" height="1536" alt="ChatGPT Image Jul 7, 2026, 10_03_47 PM" src="https://github.com/user-attachments/assets/582f3543-25e3-47d8-abb9-b38ccc432d49" />


---

## API Response Handling

The assistant validates every API response before presenting information to the user.

Supported outcomes include:

- Successful response
- Invalid input
- Data not found
- API timeout
- Service unavailable

If an API call cannot be completed, the assistant follows the configured retry and escalation strategy.
