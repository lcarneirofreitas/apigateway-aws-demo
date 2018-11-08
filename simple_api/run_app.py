#!/bin/bash

docker build -t lcarneirofreitas/simple_api .
docker rm -f simple_api
docker run --network="host" --restart=unless-stopped --name=simple_api -d lcarneirofreitas/simple_api
docker push lcarneirofreitas/simple_api
