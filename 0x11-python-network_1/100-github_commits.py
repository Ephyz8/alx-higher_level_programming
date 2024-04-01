#!/usr/bin/python3
"""List 10 commits (from the most recent to oldest) of the repository
“rails” by the user “rails”
Uses the GitHub API,https://developer.github.com/v3/repos/commits/
Print all commits by: `<sha>: <author name>` (one by line)
"""


if __name__ == '__main__':
    from requests import get
    from sys import argv

    repos = argv[1]
    own = argv[2]
    j = 0

    URL = "https://api.github.com/repos/{}/{}/commits".format(own, repos)

    resp = get(URL)
    json = resp.json()

    for element in json:
        if j > 9:
            break
        sha = element.get('sha')
        author = element.get('commit').get('author').get('name')
        print("{}: {}".format(sha, author))
        j += 1
        