# ET-001 – Authentication Failure

## Objective

Validate that the Healthcare Claims Voice Agent securely handles failed authentication attempts without exposing sensitive information.

## Scenario

The member provides authentication details that do not match the system records.

## Sample Interaction

| Speaker | Message                                                                                 |
| ------- | --------------------------------------------------------------------------------------- |
| Agent   | Please provide your Member ID.                                                          |
| User    | MBR123456                                                                               |
| Agent   | Please provide your Date of Birth.                                                      |
| User    | 15 January 1995                                                                         |
| Agent   | Please provide your ZIP Code.                                                           |
| User    | 110011                                                                                  |
| Agent   | Please provide the last four digits of your SSN.                                        |
| User    | 9876                                                                                    |
| Agent   | I'm sorry, I couldn't verify your information. Please check your details and try again. |

## Expected Behaviour

* The authentication request should fail.
* The agent should not indicate which field was incorrect.
* The member should be prompted to retry authentication.
* No sensitive member information should be disclosed.
* The failed authentication attempt should be handled using a neutral error message.

## Expected Outcome

The authentication attempt fails securely, and the member is asked to retry without being told which authentication detail was incorrect.
