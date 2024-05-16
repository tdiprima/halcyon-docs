# Authorization

This describes authenticating to get a token and then using this token to make authorized requests to the SPARQL endpoint to query RDF data.

## 1. Authentication
   
**URL:** `https://yourserver.com:<port>/auth/realms/Halcyon/protocol/openid-connect/token`

**Method:** POST

**Content-Type:** application/x-www-form-urlencoded

**Body content:**

```
client_id=account&username=<username>&password=<password>&grant_type=password&credentialId=
```

The response from this request, if successful, will include an access token.

## 2. Accessing SPARQL Endpoint

**URL:** `https://yourserver.com:<port>/rdf`

**Method:** POST

**Headers:**

```
Authorization: Bearer <your token retrieved from above>
Accept: text/plain
Content-Type: application/x-www-form-urlencoded
```

**Form values:**

```
query=select * where {graph ?g {?s ?p ?o}} limit 10
```

The results will be returned in plain text.
