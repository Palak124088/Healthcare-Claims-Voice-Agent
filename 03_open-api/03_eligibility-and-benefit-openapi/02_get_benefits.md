openapi: 3.0.1
info:
  title: Get Benefits
  version: 1.0.0
servers:
- url: https://healthcare-backend-686458672300.us-central1.run.app
paths:
  /benefits/:
    post:
      operationId: get_benefits
      summary: Get Member Benefits
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
          description: Benefits result.
        '404':
          description: Member not found.