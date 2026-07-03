# Constraints

## Overview

The following constraints define the known limitations and boundaries considered during the design and implementation of the Healthcare Claims Voice Agent. These constraints influence the project's functionality, implementation approach, and overall scope.

---

## Business Constraints

### CN-01 HIPAA Compliance

The solution must protect sensitive healthcare information and ensure that member data is only shared after successful authentication.

---

### CN-02 Secure Authentication

Protected healthcare information cannot be accessed unless the member successfully completes the required authentication process.

---

### CN-03 Mock Backend Services

The current implementation uses mock APIs for healthcare services instead of live insurance or hospital systems.

---

### CN-04 Limited Business Scope

The project focuses only on selected healthcare services, including claim status, claim submission, eligibility verification, benefits inquiry, provider lookup, pre-authorization, and service requests.

---

### CN-05 Voice-Based Interaction

The solution is designed primarily for voice conversations through Google CX Agent Studio and does not include web or mobile interfaces.

---

### CN-06 Project Timeline

The project is developed within the internship timeline, limiting the implementation of advanced production features such as live system integration, multilingual support, and analytics dashboards.

---

## Summary

These constraints define the boundaries of the current implementation and ensure that the project remains aligned with business objectives, available resources, and internship deliverables.
