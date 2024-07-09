#!/usr/bin/python3
"""
    - A script that takes in a URL,
    - sends a request to the URL
    - Displays the value of the X-Request-Id variable
    - found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":

    url = sys.argv[1]

    with urllib.request.urlopen(url) as res:
        print(dict(res.headers).get('X-Request-Id'))
