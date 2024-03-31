#!/usr/bin/python3
"""Fetches https://alx-intranet.hbtn.io/status"""
import urllib.request


if __name__ == "__main__":
  req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
  with urllib.request.urlopen(req) as response:
    bd = response.read().decode('utf-8')
    print("Body response:")
    print("\t- type: {}".format(type(bd)))
    print("\t- content: {}".format(bd))
    print("\t- utf8 content: {}".format(bd.decode("utf-8")))