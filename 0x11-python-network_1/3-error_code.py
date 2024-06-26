#!/usr/bin/python3
"""Takes in a URL, send a request to the URL and displays the body of the
response (decoded in utf-8).
"""


if __name__ == '__main__':
    import sys
    from urllib import request, error

    url = sys.argv[1]
    try:
        with request.urlopen(url) as rsp:
            print(rsp.read().decode('utf-8'))
    except error.HTTPError as er:
        print("Error code: {}".format(er.status))
