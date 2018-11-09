#!/bin/bash

docker rm -f simple_api && \
docker rmi -f lcarneirofreitas/simple_api:latest && \
docker run --network="host" --restart=unless-stopped --name=simple_api -d lcarneirofreitas/simple_api:latest

