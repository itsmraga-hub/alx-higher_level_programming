#!/usr/bin/python3
"""
    Fetch rails github commits from the rails user
    last 10 commits and print the commit sha
"""

if __name__ == "__main__":
    import requests
    import sys

    name = sys.argv[1]
    repo = sys.argv[2]

    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        name, repo))
    for i in range(1, 11):
        print("{}: {}".format(
            r.json()[i]['sha'], r.json()[i]['commit']['author']['name']))
