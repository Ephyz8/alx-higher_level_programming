#!/usr/bin/python3
"""Sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)
"""

if __name__ == '__main__':
    import urllib.request
    import urllib.parse
    import sys

    argv = sys.argv
    url = argv[1]
    email = {"email": argv[2]}
    DATA = urllib.parse.urlencode(email).encode('ascii')

    with urllib.request.urlopen(url, DATA) as response:
        resp = response.read().decode('utf-8')
        print(resp)
