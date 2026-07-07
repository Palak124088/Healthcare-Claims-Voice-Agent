# ET-003 – Consent Declined

## Objective

Validate that the Healthcare Claims Voice Agent explains the purpose of consent and securely ends the conversation when consent is not provided.

## Scenario

The member declines consent when the agent requests permission to access healthcare information.

## Sample Interaction

| Speaker | Message                                                                                              |
| ------- | ---------------------------------------------------------------------------------------------------- |
| Agent   | Before I access your healthcare information, I need your consent. Do you agree?                      |
| User    | No.                                                                                                  |
| Agent   | Your consent is required to securely access your healthcare information. Would you like to continue? |
| User    | No.                                                                                                  |

## Expected Behaviour

* The purpose of consent should be clearly explained.
* The agent should not proceed to authentication without consent.
* No member details should be collected.
* No backend healthcare services should be invoked.
* The conversation should end securely if the user declines consent again.

## Expected Outcome

The session ends securely without collecting member information or accessing healthcare data.
