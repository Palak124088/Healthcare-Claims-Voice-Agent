openapi: 3.0.1
info:
  title: Get Claim Status
  version: "1.0.0"
servers:
  - url: https://healthcare-backend-686458672300.us-central1.run.app
paths:
  /claims/status:
    post:
      operationId: get_claim_status
      summary: Get Claim Status
      description: Returns the claim status for the authenticated member.
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [memberId]
              properties:
                memberId:
                  type: string
                  example: MEM1001
      responses:
        "200":
          description: Claim status retrieved successfully.
        "401":
          description: Authentication required.
        "404":
          description: Member or claim not found.
        "422":
          description: Invalid request.