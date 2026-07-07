openapi: 3.0.1
info:
  title: Get Claim History
  version: "1.0.0"
servers:
  - url: https://healthcare-backend-686458672300.us-central1.run.app
paths:
  /claims/history/{member_id}:
    get:
      operationId: get_claim_history
      summary: Get Claim History
      parameters:
        - name: member_id
          in: path
          required: true
          schema:
            type: string
          example: MEM1001
      responses:
        "200":
          description: Claim history retrieved.
        "404":
          description: Member not found.