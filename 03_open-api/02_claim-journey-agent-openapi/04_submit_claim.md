openapi: 3.0.1
info:
  title: Submit Claim
  version: "1.0.0"
servers:
  - url: https://healthcare-backend-686458672300.us-central1.run.app
paths:
  /claims/submit:
    post:
      operationId: submit_claim
      summary: Submit New Claim
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              required: [memberId, claimType, provider, serviceDate, diagnosisCode, amount]
              properties:
                memberId:
                  type: string
                  example: MEM1001
                claimType:
                  type: string
                  example: Medical
                provider:
                  type: string
                  example: City Medical Center
                serviceDate:
                  type: string
                  example: "2026-06-18"
                diagnosisCode:
                  type: string
                  example: I10
                amount:
                  type: number
                  example: 150
      responses:
        "200":
          description: Claim submitted.
        "422":
          description: Missing or invalid fields.