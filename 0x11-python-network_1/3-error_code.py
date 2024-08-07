#!/usr/bin/python3

""" A script that takes in a URL, sends a request to the URL
    Displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as res:
            print(res.read().decode('utf-8'))
    except urllib.error.HTTPError as error:
        print(f"Error code: {error.status}")
