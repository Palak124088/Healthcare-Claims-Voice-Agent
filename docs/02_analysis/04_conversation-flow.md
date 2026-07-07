# Conversation Flow

## Overview

The conversation flow defines the end-to-end interaction between the member and the Healthcare Claims Voice Agent. It ensures that every conversation follows a secure, structured, and consistent process while supporting authentication, intent routing, backend integration, fallback handling, and human escalation.

---

## Master Conversation Flow
<img width="864" height="1821" alt="ChatGPT Image Jul 7, 2026, 07_25_42 PM" src="https://github.com/user-attachments/assets/70687396-923f-425b-8788-8cfc3cde35e4" />


---

## Conversation Stages

### Stage 1 – Welcome

The agent greets the member and starts the conversation.

### Stage 2 – Consent

The member is asked for consent before collecting or processing personal healthcare information.

### Stage 3 – Authentication

The member's identity is verified using the required authentication details before accessing protected healthcare information.

### Stage 4 – Intent Identification

The agent determines the member's request and selects the appropriate healthcare journey.

### Stage 5 – Journey Execution

The selected healthcare agent retrieves the required information using backend tools or APIs.

### Stage 6 – Response Delivery

The requested information is presented to the member in a clear and conversational manner.

### Stage 7 – Conversation Closure

The agent asks if additional assistance is required. If not, the conversation is closed. If yes, the conversation returns to the Root Agent for another request.

---

## Exception Handling

If authentication fails, the member is allowed to retry based on the configured retry limit.

If the retry limit is reached or the request cannot be completed automatically, the conversation follows the human escalation process.

---

## Summary

The conversation flow provides a secure and structured approach for handling healthcare member requests while supporting authentication, intelligent routing, backend integration, fallback handling, and human escalation.
