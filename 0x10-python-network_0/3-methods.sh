#!/bin/bash
#A script that display HTTP methods the server will accept
curl -s -X OPTIONS $1
