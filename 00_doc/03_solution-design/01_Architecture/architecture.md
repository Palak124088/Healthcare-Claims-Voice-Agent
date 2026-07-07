## High-Level Architecture

The Healthcare Claims Voice Agent follows a secure-first Agentic AI Orchestration architecture designed to handle healthcare inquiries through specialized AI agents while ensuring authentication, privacy, and compliance requirements are enforced.

The architecture follows a layered approach where every user request passes through Input Guardrails and a Mandatory Authentication Layer before any business workflow is executed. Once the user is verified, a centralized Supervisor Agent is responsible for understanding the request, managing conversation context, determining confidence scores, and routing the request to the appropriate healthcare domain agent.

This architecture separates orchestration responsibilities from domain-specific business logic, enabling scalability, maintainability, and accurate decision-making across healthcare workflows such as claims, eligibility, benefits, provider lookup, pre-authorization, and escalation management.

### High-Level Agentic AI Orchestration Architecture

<img width="941" height="603" alt="Architecture" src="https://github.com/user-attachments/assets/73032358-efcf-40fb-a2b6-a3855fc45c19" />


The architecture consists of the following key layers:

### Voice Interaction Layer

The Voice Interface acts as the primary interaction channel between the user and the system. It supports:

- Incoming voice calls
- Speech-to-text conversion
- Text-based processing
- Voice response generation

This layer serves as the entry and exit point of the healthcare journey.

### Input Guardrails Layer

Before any healthcare workflow begins, user input is validated through the Input Guardrails Layer.

This layer is responsible for:

- Detecting malicious prompts
- Preventing prompt injection attempts
- Filtering unsupported requests
- Detecting abusive or harmful language
- Enforcing conversation policies

Only validated requests are allowed to proceed further into the system.

### Mandatory Authentication Layer

Healthcare information is highly sensitive and requires identity verification before access.

The Authentication Layer verifies:

- Member ID
- Date of Birth (DOB)
- ZIP Code
- Last Four Digits of SSN
- Address Validation (when required)

No business workflow or healthcare data retrieval can occur until authentication is successfully completed.

### Agentic AI Orchestrator

The Agentic AI Orchestrator acts as the coordination layer of the system.

Its responsibilities include:

- Request understanding
- Intent pre-processing
- Context awareness
- Conversation state management
- Policy and compliance enforcement
- Workflow coordination

The orchestrator determines how requests should be processed before passing control to the Supervisor Agent.

### Supervisor Agent

The Supervisor Agent serves as the central decision-making component of the architecture.

Key responsibilities include:

- Intent classification
- Confidence score evaluation
- Context management
- Human-in-loop decisioning
- Agent coordination
- Tool selection

Based on confidence levels, the Supervisor Agent determines whether a request should continue automatically, require clarification, or be escalated to a human representative.

### Domain Sub-Supervisor Agents

Specialized Sub-Supervisor Agents manage healthcare-specific workflows independently.

These include:

#### Claims Sub-Supervisor
Handles claim status inquiries, claim submissions, and claim-related information.

#### Eligibility Sub-Supervisor
Manages member eligibility and coverage verification workflows.

#### Benefits Sub-Supervisor
Provides benefit details and coverage information.

#### Provider Lookup Sub-Supervisor
Assists members in locating in-network providers and healthcare facilities.

#### Pre-Authorization Sub-Supervisor
Handles pre-authorization requirements and authorization status requests.

#### Escalation Sub-Supervisor
Manages complex situations requiring human intervention.

### Tool and API Layer

Sub-Supervisor Agents invoke backend tools and APIs to retrieve or update information.

Examples include:

- Eligibility Verification APIs
- Claim Status APIs
- Benefits APIs
- Provider Lookup APIs
- Pre-Authorization APIs
- Service Request APIs

This layer provides real-time access to healthcare data while maintaining security and compliance controls.

### Response Generation Layer

Once information is retrieved and validated, responses are returned through the Voice Interface.

The system delivers:

- Accurate healthcare information
- Verified member-specific responses
- Context-aware communication
- Secure voice interactions

### Platform and Security Layer

The solution is built on Google Cloud technologies including:

- Google Cloud Platform
- CX Agent Studio
- Vertex AI
- Cloud Functions
- Cloud Storage
- Security & IAM
- HIPAA Compliance Controls

These services provide scalability, reliability, security, and compliance for healthcare operations.
