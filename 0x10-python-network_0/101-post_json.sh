#!/bin/bash
# A script that send a POST request with the content of a file, passed as second argument to a URL passed as first argument
curl -sX POST -H "Content-Type: application/json" -d @"$2" "$1"
