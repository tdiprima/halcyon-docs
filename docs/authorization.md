# Authorization

https://yourserver.com:/auth/realms/Halcyon/protocol/openid-connect/token

Method: POST
Content-Type: application/x-www-form-urlencoded

Body content:
client_id=account&username=<username>&password=<password>&grant_type=password&credentialId=

Accessing SPARQL endpoint

https://yourserver.com:/rdf

Method: POST
Headers:
Authorization: Bearer <your token retrieved from above>
Accept: text/plain
Content-Type: application/x-www-form-urlencoded

form values:
query: select * where {graph ?g {?s ?p ?o}} limit 10
