#!/usr/bin/python3

import urllib.request

""" script that fetches https://alx-intranet.hbtn.io/status """

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    line_read = response.read()
    print("Body response:")
    print(f"\t- type: {type(line_read)}")
    print(f"\t- content: {line_read}")
    print(f"\t- utf8 content: {line_read.decode('utf-8')}")
