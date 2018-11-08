# apigateway-aws-demo
Demo api gateway aws

# como buscar os deploys da api
aws apigateway get-deployments --rest-api-id XXXXXXXXXX


# get json swagger aws gateway
aws apigateway get-export --parameters extensions='integrations' --rest-api-id XXXXXXXXX --stage-name v1 --export-type swagger v1-swagger-apigateway.yaml


# put json swagger aws gateway
aws apigateway put-rest-api --rest-api-id XXXXXXXXXX --mode overwrite --body 'file://v1-swagger-apigateway.yaml

# create deploy
aws apigateway create-deployment --rest-api-id XXXXXXXXX --stage-name v1 --description testeapi1
