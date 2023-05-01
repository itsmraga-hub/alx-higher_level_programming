#!/usr/bin/python3
"""
    A python script that takes in a URL and an email address, sends a POST
    request to the passed URL with email as a parameter
"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    res = requests.post(url, data=payload)
    print(res.text)
