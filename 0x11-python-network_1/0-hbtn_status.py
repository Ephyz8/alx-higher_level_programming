#!/usr/bin/python3
import urllib.request
"""Fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
   try:
      req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
      with urllib.request.urlopen(req) as response:
        body = response.read().decode('utf-8')
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
   except urllib.error.URLError as e:
       print("Error fetching URL:", e)
