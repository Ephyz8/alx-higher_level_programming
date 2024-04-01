#!/usr/bin/python3
"""Python script that takes Github credentials (username and password)
and uses the Github API to display id
"""
import requests
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == '__main__':
    url = 'https://api.github.com/users/{}'.format(argv[1])
    resp = requests.get(url,
                     auth=HTTPBasicAuth(argv[1], argv[2]))
    print(resp.json().get('id'))
