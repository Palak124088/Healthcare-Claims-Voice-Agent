openapi: 3.0.1
info:
  title: Search Providers
  version: 1.0.0
servers:
- url: https://healthcare-backend-686458672300.us-central1.run.app
paths:
  /providers/search:
    get:
      operationId: search_providers
      summary: Search Providers
      description: Search for providers by name, city, state, or ZIP code. Provide
        at least one filter.
      parameters:
      - name: providerName
        in: query
        required: false
        schema:
          type: string
        example: City Medical Center
      - name: city
        in: query
        required: false
        schema:
          type: string
        example: New York
      - name: state
        in: query
        required: false
        schema:
          type: string
        example: NY
      - name: zipCode
        in: query
        required: false
        schema:
          type: string
        example: '10001'
      responses:
        '200':
          description: Matching providers.
        '404':
          description: No providers found.