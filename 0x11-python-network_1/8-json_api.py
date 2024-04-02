#!/usr/bin/python3
"""Python script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter
"""


if __name__ == '__main__':
    from requests import post
    from sys import argv

    URL = 'http://0.0.0.0:5000/search_user'
    data = {'q': argv[1] if len(argv) >= 2 else ""}
    resp = post(URL, data)

    t_resp = resp.headers['content-type']

    try:
        t_resp == 'application/json'
        result = resp.json()
        id = result.get('id')
        name = result.get('name')
        if (result != {} and id and name):
          print("[{}] {}".format(id, name))
        else:
          print('No result')
    except Exception:
        print("Not a valid JSON")
