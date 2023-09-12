#!/usr/bin/env bash

# Used to force the correct platform for the build (in case you are using a M1 Mac)
# export DOCKER_DEFAULT_PLATFORM=linux/amd64

docker build . -t 477091544114.dkr.ecr.eu-north-1.amazonaws.com/demo/helloworld:latest
docker push 477091544114.dkr.ecr.eu-north-1.amazonaws.com/demo/helloworld:latest