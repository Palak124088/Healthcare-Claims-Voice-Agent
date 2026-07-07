# Fallback Flow

## Objective

The Fallback Flow is triggered when the AI agent is unable to confidently understand the user's request or when the conversation cannot continue through the normal routing process.

The objective is to recover the conversation by requesting clarification before escalating to a human representative.

---

## Flow

<img width="1086" height="1448" alt="ChatGPT Image Jun 29, 2026, 11_00_48 PM" src="https://github.com/user-attachments/assets/cb7e0f68-d371-4a36-9feb-5aaa5a0ddfd1" />

---

## Business Rules

- Do not assume the user's intent.
- Ask only one clarification question at a time.
- Allow a maximum of two clarification attempts.
- Maintain the conversation context during clarification.
- If clarification fails after the retry limit, transfer the conversation to Human Escalation.

---

## Trigger Conditions

The fallback flow is initiated when one of the following conditions occurs:

- Unknown intent
- Low intent confidence
- Ambiguous request
- Multiple intents detected
- Incomplete user input

---

## Expected Behaviour

| Scenario | System Behaviour |
|----------|------------------|
| Low confidence | Ask clarification question |
| Unknown intent | Ask user to rephrase |
| Multiple intents | Ask user to complete one request at a time |
| Retry limit reached | Human Agent Escalation |
