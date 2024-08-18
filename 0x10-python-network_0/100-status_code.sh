#!/bin/bash
# A script that display only the response code of the url passed to it without using any pipe and redirection
curl -sI -o /dev/null -w %{response_code} "$1"
