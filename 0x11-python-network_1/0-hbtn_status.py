#!/usr/bin/python3

import urllib.request

""" script that fetches https://alx-intranet.hbtn.io/status """

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    line_read = response.read()
    print('-', line_read)
