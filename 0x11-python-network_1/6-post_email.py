#!/usr/bin/python3
"""Python Script that takes in a URL and an email address,
sends a POST request to the passed URL
with the email as a parameter,
and finally displays the body of the response"""


if __name__ == "__main__":
    from sys import argv
    from requests import post

    url = argv[1]
    email = argv[2]
    respns = post(url, {'email': email})
    print(respns.text)
