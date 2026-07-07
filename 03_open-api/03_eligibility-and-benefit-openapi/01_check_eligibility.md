openapi: 3.0.1
info:
  title: Check Eligibility
  version: 1.0.0
servers:
- url: https://healthcare-backend-686458672300.us-central1.run.app
paths:
  /eligibility/:
    post:
      operationId: check_eligibility
      summary: Check Eligibility
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required:
              - memberId
              properties:
                memberId:
                  type: string
                  example: MEM1001
      responses:
        '200':
          description: Eligibility result.
        '404':
          description: Member not found.