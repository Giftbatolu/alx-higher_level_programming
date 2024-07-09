#!/usr/bin/python3

""" A script that takes in a url and email,
    send a POST request to the passed url and display
    the body responsein utf-8
"""

import sys
import urllib.request

url = sys.argv[1]
email = {"email": sys.argv[2]}

data = urllib.parse.urlencode(email)
data = data.encode('utf-8')

with urllib.request.urlopen(url) as res:
    res_body = res.read().decode('utf-8')

print(res_body)
