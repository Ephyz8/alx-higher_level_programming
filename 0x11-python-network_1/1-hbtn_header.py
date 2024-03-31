#!/usr/bin/python3
"""
Displays the value of the variable X-Request-Id
found in the header of the response.
"""


if __name__ == "__main__":
    import sys
    import urllib.request

    with urllib.request.urlopen(sys.argv[1]) as response:
        resp = response.headers["X-Request-Id"]
        print(resp) 