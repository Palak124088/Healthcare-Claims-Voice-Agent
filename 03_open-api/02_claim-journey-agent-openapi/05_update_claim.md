openapi: 3.0.1
info:
  title: Update Claim
  version: "1.0.0"
servers:
  - url: https://healthcare-backend-686458672300.us-central1.run.app
paths:
  /claims/{claim_id}:
    put:
      operationId: update_claim
      summary: Update Claim
      parameters:
        - name: claim_id
          in: path
          required: true
          schema:
            type: string
          example: CLM1001
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                claimType:
                  type: string
                amount:
                  type: number
      responses:
        "200":
          description: Claim updated.
        "404":
          description: Claim not found.