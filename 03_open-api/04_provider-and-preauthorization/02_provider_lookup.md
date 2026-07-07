openapi: 3.0.1
info:
  title: Provider Lookup
  version: 1.0.0
servers:
- url: https://healthcare-backend-686458672300.us-central1.run.app
paths:
  /providers/:
    post:
      operationId: provider_lookup
      summary: Provider Lookup
      description: Returns the provider details for the authenticated member.
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
          description: Provider details returned.
        '404':
          description: No provider found for this member.