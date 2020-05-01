#!/bin/bash
NAME=link_$1
docker rm -f $NAME
docker rmi -f $NAME
