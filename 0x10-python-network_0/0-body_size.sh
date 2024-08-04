#!/bin/bash
# A script that send a request to url and display the body in bytes

curl -s $1 | wc -c
