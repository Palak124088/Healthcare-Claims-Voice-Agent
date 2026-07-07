# ET-006 – API Failure

## Objective

Validate that the Healthcare Claims Voice Agent handles backend API failures gracefully by retrying the request and escalating to a human representative if the issue continues.

## Scenario

The member requests eligibility information, but the backend eligibility service is unavailable.

## Sample Interaction

| Speaker | Message                                                                                                                    |
| ------- | -------------------------------------------------------------------------------------------------------------------------- |
| User    | I'd like to check my eligibility.                                                                                          |
| Agent   | Please wait while I retrieve your eligibility information.                                                                 |
| System  | Backend service is unavailable.                                                                                            |
| Agent   | I'm experiencing a temporary technical issue while accessing your information.                                             |
| Agent   | Let me try once again.                                                                                                     |
| System  | Retry also fails.                                                                                                          |
| Agent   | I'm sorry, I'm unable to retrieve your information at this time. I'll connect you with one of our support representatives. |

## Expected Behaviour

* The API request should be retried once.
* The member should be informed about the temporary technical issue.
* The agent should not expose backend error details to the member.
* If the retry succeeds, the conversation should continue normally.
* If the retry also fails, the conversation should be transferred to Human Escalation.

## Expected Outcome

The API failure is handled safely, and the member is transferred to a human support representative when the system cannot retrieve the requested information.
