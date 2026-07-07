# ET-004 – Authentication Retry Limit Reached

## Objective

Validate that the Healthcare Claims Voice Agent stops authentication attempts after the configured retry limit and safely transfers the conversation to a human representative.

## Scenario

The member enters incorrect authentication details multiple times during the verification process.

## Sample Interaction

| Speaker | Message                                                                                                               |
| ------- | --------------------------------------------------------------------------------------------------------------------- |
| Agent   | I'm sorry, I couldn't verify your information. Please try again.                                                      |
| User    | Enters incorrect authentication details again.                                                                        |
| Agent   | I'm sorry, I still couldn't verify your information. Please try again.                                                |
| User    | Enters incorrect authentication details for the third time.                                                           |
| Agent   | I'm unable to verify your identity after multiple attempts. I'll connect you with one of our support representatives. |

## Expected Behaviour

* Retry attempts should stop after the configured retry limit.
* The agent should not allow unlimited authentication attempts.
* The conversation should be transferred to Human Escalation.
* No member information should be disclosed.
* The agent should use a safe and neutral message without revealing which credential was incorrect.

## Expected Outcome

The authentication process stops securely after multiple failed attempts, and the member is transferred to a human support representative.
