#!/usr/bin/python3
"""
    A python script that takes my GitHub credentials and uses the GitHub
    API to display my id
"""

if __name__ == "__main__":
    import requests
    import sys

    res = requests.get(
              'https://api.github.com/user',
              auth=(sys.argv[1], sys.argv[2]))
    print(res.json().get('id'))
