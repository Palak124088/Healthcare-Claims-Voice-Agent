# ET-007 – Eligibility Information Not Found

## Objective

Validate that the Healthcare Claims Voice Agent handles unavailable eligibility information safely without displaying incorrect or assumed coverage details.

## Scenario

The member requests eligibility information, but no eligibility record is found for the member’s account.

## Sample Interaction

| Speaker | Message                                                                                          |
| ------- | ------------------------------------------------------------------------------------------------ |
| User    | Am I eligible for dental treatment?                                                              |
| Agent   | Let me check your eligibility information.                                                       |
| System  | System searches the eligibility database.                                                        |
| Agent   | I couldn't find any eligibility information associated with your account.                        |
| Agent   | Would you like me to connect you with one of our support representatives for further assistance? |

## Expected Behaviour

* The agent should inform the member that no eligibility record is available.
* The agent should not display incorrect or assumed eligibility information.
* The agent should not expose backend or database details.
* The agent should offer additional assistance.
* Human Escalation should be offered if the member needs further support.

## Expected Outcome

The eligibility lookup ends safely without showing incorrect information, and the member is offered additional support or Human Escalation.
