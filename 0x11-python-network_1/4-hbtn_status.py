#!/usr/bin/python3

""" A script that fetches
    https://alx-intranet.hbtn.io/status using request package.
"""

import requests

if __name__ == "__main__":
    res = requests.get("https://alx-intranet.hbtn.io/status")
    res_body = res.text
    print("Body response")
    print(f"\t- type: {type(res_body)}")
    print(f"\t- content: {res_body}")
