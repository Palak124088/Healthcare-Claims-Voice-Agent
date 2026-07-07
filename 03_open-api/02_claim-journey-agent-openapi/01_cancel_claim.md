openapi: 3.0.1
info:
  title: Cancel Claim
  version: "1.0.0"
servers:
  - url: https://healthcare-backend-686458672300.us-central1.run.app
paths:
  /claims/{claim_id}:
    delete:
      operationId: cancel_claim
      summary: Cancel Claim
      description: Cancels an existing claim for the member.
      parameters:
        - name: claim_id
          in: path
          required: true
          schema:
            type: string
          example: CLM1001
      responses:
        "200":
          description: Claim cancelled.
        "404":
          description: Claim not found.