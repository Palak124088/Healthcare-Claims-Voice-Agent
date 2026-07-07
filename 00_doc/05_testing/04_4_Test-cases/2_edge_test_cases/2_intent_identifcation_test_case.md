# ET-002 – Intent Identification Failure

## Objective

Validate that the Healthcare Claims Voice Agent handles vague or unclear user requests without making assumptions.

## Scenario

The user provides a generic request that does not clearly indicate whether they need help with claim status, eligibility, provider information, or pre-authorization.

## Sample Interaction

| Speaker | Message                                                                                                                                       |
| ------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| User    | I have a problem.                                                                                                                             |
| Agent   | I'd be happy to help. Could you please tell me whether you're calling about a claim, eligibility, provider information, or pre-authorization? |
| User    | I don't know.                                                                                                                                 |

## Expected Behaviour

* The agent should recognize that the user's request is too vague.
* The agent should not assume the user's intent.
* The agent should ask a clarification question.
* The conversation should remain active.
* The user should be given another opportunity to provide more information.

## Expected Outcome

The conversation continues without incorrect routing, and the agent waits for a clearer user response.
