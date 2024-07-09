#!/usr/bin/python3
"""
A script that takes in a URL, sends a request to the URL
Display the value of X-Request-Id variable found in the header of the response.
"""

import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as res:
    print(dict(res.headers).get('X-Request-Id'))
