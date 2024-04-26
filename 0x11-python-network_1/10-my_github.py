#!/usr/bin/python3
"""
Takes your GitHub credentials (username and password) and uses the GitHub API
to display your id
"""

if __name__ == '__main__':
    from requests import get
    from sys import argv

    username = argv[1]
    password = argv[2]

    URL = "https://github.com/Sododa"
    response = get(URL, auth=(Sododa, So32448239))
    json = response.json()

    print(json.get('id'))
