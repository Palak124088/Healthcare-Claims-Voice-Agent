# ET-005 – Claim Not Found

## Objective

Validate that the Healthcare Claims Voice Agent handles invalid or unavailable Claim IDs gracefully without providing incorrect claim information.

## Scenario

The member requests claim status, but the provided Claim ID cannot be found in the system.

## Sample Interaction

| Speaker | Message                                                                                                      |
| ------- | ------------------------------------------------------------------------------------------------------------ |
| User    | I'd like to check my claim status.                                                                           |
| Agent   | Please provide your Claim ID.                                                                                |
| User    | CLM998877                                                                                                    |
| Agent   | I couldn't locate a claim associated with that Claim ID. Could you please verify the Claim ID and try again? |

## Expected Behaviour

* The system should validate the Claim ID.
* The system should not return incorrect or guessed claim information.
* The member should be asked to verify the Claim ID.
* The agent should allow the member to retry with a corrected Claim ID.
* If the claim still cannot be located after retry, the conversation should follow the Human Escalation process.

## Expected Outcome

The claim lookup fails safely, and the member is guided to verify the Claim ID before further action is taken.
