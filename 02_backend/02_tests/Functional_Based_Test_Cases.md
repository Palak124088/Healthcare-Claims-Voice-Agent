# Test Case Register: Functional Test Cases

## Section 1: Root Agent and Conversation Management

| TC ID | Journey    | Scenario                                          | Test Type  | Priority | Expected Result                               | Semantic Similarity | Tool Correctness | Hallucination | Actual Result               | Status |
| ----- | ---------- | ------------------------------------------------- | ---------- | -------- | --------------------------------------------- | ------------------: | ---------------: | ------------- | --------------------------- | ------ |
| F-001 | Root Agent | Handle Out-of-Scope Request                       | Negative   | High     | Appropriate fallback response is provided.    |                 4/4 |             100% | No            | Fallback response returned. | Pass   |
| F-002 | Root Agent | Escalate After Three Consecutive Unclear Requests | Escalation | High     | Conversation is transferred to a human agent. |                 4/4 |             100% | No            | Escalated successfully.     | Pass   |
| F-003 | Root Agent | Transfer to Human Representative on Request       | Positive   | High     | User is transferred immediately.              |                 4/4 |              N/A | No            | Transfer successful.        | Pass   |
| F-004 | Root Agent | Root Agent Identifies Claim Status Intent         | Positive   | High     | User is routed to the Claims Journey Agent.   |                 4/4 |             100% | No            | Routed successfully.        | Pass   |

## Section 2: Consent Management

| TC ID | Journey | Scenario                                | Test Type | Priority | Expected Result                                                         | Semantic Similarity | Tool Correctness | Hallucination | Actual Result        | Status |
| ----- | ------- | --------------------------------------- | --------- | -------- | ----------------------------------------------------------------------- | ------------------: | ---------------: | ------------- | -------------------- | ------ |
| F-005 | Consent | Consent Granted                         | Positive  | High     | Authentication process starts.                                          |                 4/4 |             100% | No            | Routed successfully. | Pass   |
| F-006 | Consent | Consent Declined                        | Negative  | High     | Conversation ends successfully without accessing protected information. |                 4/4 |             100% | No            | Session ended.       | Pass   |
| F-007 | Consent | Grant Consent After Initially Declining | Edge Case | Medium   | User proceeds after granting consent later in the conversation.         |                 4/4 |             100% | No            | Flow resumed.        | Pass   |

## Section 3: Authentication and Identity Verification

| TC ID | Journey        | Scenario                                                | Test Type  | Priority | Expected Result                                                                  | Semantic Similarity | Tool Correctness | Hallucination | Actual Result                   | Status |
| ----- | -------------- | ------------------------------------------------------- | ---------- | -------- | -------------------------------------------------------------------------------- | ------------------: | ---------------: | ------------- | ------------------------------- | ------ |
| F-008 | Authentication | Valid Member ID                                         | Positive   | High     | Valid Member ID is accepted.                                                     |                 4/4 |             100% | No            | Authentication started.         | Pass   |
| F-009 | Authentication | Invalid Member ID                                       | Negative   | High     | Retry prompt is returned.                                                        |                 4/4 |             100% | No            | Prompt returned.                | Pass   |
| F-010 | Authentication | Accept Valid Member ID After Invalid Member ID          | Edge Case  | High     | Authentication continues after the valid Member ID is entered.                   |                 4/4 |             100% | No            | Authentication resumed.         | Pass   |
| F-011 | Authentication | Different DOB Formats                                   | Edge Case  | Medium   | Supported DOB formats are accepted.                                              |                 4/4 |             100% | No            | DOB validated.                  | Pass   |
| F-012 | Authentication | DOB in MM/DD/YYYY Format                                | Positive   | Medium   | DOB is validated successfully.                                                   |                 4/4 |             100% | No            | DOB accepted.                   | Pass   |
| F-013 | Authentication | User Asks an Invalid Question During Authentication     | Edge Case  | Medium   | Authentication flow is maintained without losing progress.                       |                 4/4 |             100% | No            | Flow continued.                 | Pass   |
| F-014 | Authentication | Handles Credentials Refusal                             | Negative   | High     | Credential refusal is handled gracefully.                                        |                 4/4 |             100% | No            | Conversation handled correctly. | Pass   |
| F-015 | Authentication | Incorrect Verification Credentials                      | Negative   | High     | Authentication is denied.                                                        |                 4/4 |             100% | No            | Access denied.                  | Pass   |
| F-016 | Authentication | Re-entering Correct Credentials                         | Edge Case  | High     | Authentication is completed successfully after correct credentials are provided. |                 4/4 |             100% | No            | Authentication completed.       | Pass   |
| F-017 | Authentication | Agent Does Not Reveal Information Before Authentication | Security   | Critical | No PHI is exposed before successful verification.                                |                 4/4 |             100% | No            | Information protected.          | Pass   |
| F-018 | Authentication | Three Failed Authentication Attempts                    | Escalation | Critical | Human escalation is triggered after the maximum number of attempts.              |                 4/4 |             100% | No            | Escalated successfully.         | Pass   |
| F-019 | Authentication | Three Invalid Member ID Attempts                        | Escalation | Critical | Human escalation is triggered after three invalid Member ID attempts.            |                 4/4 |             100% | No            | Escalated successfully.         | Pass   |

## Section 4: Claims Journey

| TC ID | Journey        | Scenario                           | Test Type | Priority | Expected Result                                       | Semantic Similarity | Tool Correctness | Hallucination | Actual Result                 | Status |
| ----- | -------------- | ---------------------------------- | --------- | -------- | ----------------------------------------------------- | ------------------: | ---------------: | ------------- | ----------------------------- | ------ |
| F-020 | Claims Journey | Displays Claim History             | Positive  | High     | Claim history is provided to the authenticated user.  |                 4/4 |             100% | No            | Claim history retrieved.      | Pass   |
| F-021 | Claims Journey | Submits New Claim                  | Positive  | Medium   | Claim submission assistance is provided successfully. |                 4/4 |             100% | No            | Request handled successfully. | Pass   |
| F-022 | Claims Journey | Handles Claim Cancellation Request | Negative  | Medium   | Appropriate claim-cancellation response is provided.  |                 4/4 |             100% | No            | Cancellation handled.         | Pass   |

## Section 5: Eligibility and Benefits

| TC ID | Journey     | Scenario                              | Test Type | Priority | Expected Result                                       | Semantic Similarity | Tool Correctness | Hallucination | Actual Result                      | Status |
| ----- | ----------- | ------------------------------------- | --------- | -------- | ----------------------------------------------------- | ------------------: | ---------------: | ------------- | ---------------------------------- | ------ |
| F-023 | Eligibility | Retrieves Eligibility Information     | Positive  | High     | Eligibility details are provided.                     |                 4/4 |             100% | No            | Eligibility information retrieved. | Pass   |
| F-024 | Eligibility | Handles No Eligibility Record Found   | Negative  | Medium   | Appropriate no-record-found message is provided.      |                 4/4 |             100% | No            | Appropriate message provided.      | Pass   |
| F-025 | Benefits    | Retrieves Benefits Information        | Positive  | High     | Benefits information is provided.                     |                 4/4 |             100% | No            | Benefits information retrieved.    | Pass   |
| F-026 | Benefits    | Handles No Benefits Information Found | Negative  | Medium   | Appropriate no-information-found message is provided. |                 4/4 |             100% | No            | Appropriate message provided.      | Pass   |

## Section 6: Provider Lookup and Preauthorization

| TC ID      | Journey          | Scenario                                 | Test Type | Priority | Expected Result                                       | Semantic Similarity | Tool Correctness | Hallucination | Actual Result                   | Status |
| ---------- | ---------------- | ---------------------------------------- | --------- | -------- | ----------------------------------------------------- | ------------------: | ---------------: | ------------- | ------------------------------- | ------ |
| F-027 (I)  | Provider Lookup  | Retrieves Assigned Provider              | Positive  | High     | Assigned provider information is provided.            |               3.7/4 |             100% | No            | Not recorded.                   | Fail   |
| F-027 (II) | Provider Lookup  | Retrieves Assigned Provider              | Positive  | High     | Assigned provider information is provided.            |                 4/4 |             100% | No            | Provider information retrieved. | Pass   |
| F-028 (I)  | Provider Lookup  | Provider Search by City                  | Positive  | Medium   | Providers are listed based on the specified city.     |                 4/4 |             100% | Yes           | Not recorded.                   | Fail   |
| F-028 (II) | Provider Lookup  | Provider Search by City                  | Positive  | Medium   | Providers are listed based on the specified city.     |                 4/4 |             100% | No            | Providers retrieved.            | Pass   |
| F-029      | Provider Lookup  | Provider Search by ZIP Code              | Positive  | Medium   | Providers are listed based on the specified ZIP code. |               3.7/4 |             100% | No            | Providers retrieved.            | Pass   |
| F-030 (I)  | Provider Lookup  | Provider Search by Provider Name         | Positive  | Medium   | Matching provider is found.                           |               3.9/4 |             100% | Yes           | Not recorded.                   | Fail   |
| F-030 (II) | Provider Lookup  | Provider Search by Provider Name         | Positive  | Medium   | Matching provider is found.                           |               3.9/4 |             100% | No            | Provider information retrieved. | Pass   |
| F-031      | Preauthorization | Verify Preauthorization Status Retrieval | Positive  | High     | Current preauthorization status is provided.          |                 4/4 |             100% | No            | Preauthorization status shared. | Pass   |

## Section 7: Cross-Agent Routing and Security

| TC ID | Journey       | Scenario                                                                          | Test Type | Priority | Expected Result                                | Semantic Similarity | Tool Correctness | Hallucination | Actual Result                           | Status |
| ----- | ------------- | --------------------------------------------------------------------------------- | --------- | -------- | ---------------------------------------------- | ------------------: | ---------------: | ------------- | --------------------------------------- | ------ |
| F-032 | Agent Routing | Claims Request Transfers from Provider and Preauthorization Agent to Claims Agent | Positive  | High     | Request is routed to the Claims Journey Agent. |               3.9/4 |             100% | No            | Routing successful.                     | Pass   |
| F-033 | Security      | Provider and Preauthorization Agent Refuses to Share Internal System Details      | Security  | Critical | Internal system information remains protected. |                 4/4 |             100% | No            | Internal information was not disclosed. | Pass   |
