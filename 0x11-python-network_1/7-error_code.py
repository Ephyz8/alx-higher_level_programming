#!/usr/bin/python3
"""Python Script that takes in a URL, sends a request to the URL
& displays the body of the response
"""
import requests
from sys import argv

if __name__ == '__main__':
    url = requests.get(argv[1])
    status = url.status_code
    print(url.text) if status < 400 else print(
        "Error code: {}".format(url.status_code))
