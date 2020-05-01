#!/bin/bash
NAME=link_$1
docker build -t $NAME --build-arg USER_NAME=$2 --build-arg USER_PASSWORD=$3 --build-arg CITY=$4  --build-arg JOB_TITLE=$5 --build-arg BLACK_LIST=$6 .
docker run -name $NAME --rm $NAME
