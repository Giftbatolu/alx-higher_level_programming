#!/bin/bash
#A script that display HTTP methods the server will accept
curl -sI "$1" | grep "Allow" | cut -d " " -f2-
