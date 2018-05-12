#!/usr/bin/env sh
GITCOMMIT=$(git log --format="%h" -n 1)
IMAGETAG=${GITCOMMIT}
IMAGE=${IMAGENAME}:${IMAGETAG}

docker build -t ${IMAGE} .

if [ $? -ne 0 ]; then
    echo "docker build failed."
    exit 0
fi


docker tag ${IMAGE} ${IMAGENAME}:latest