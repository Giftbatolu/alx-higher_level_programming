#!/bin/bash
# A script that send post request to url
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" $1
