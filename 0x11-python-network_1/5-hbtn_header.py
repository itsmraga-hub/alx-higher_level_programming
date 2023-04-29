#!/usr/bin/python3
"""
    A python script that takes in a URL, sends a request to the URL and
    displays the variable X-Request-Id
"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]

    res = requests.get(url)
    x_req_id = res.headers.get('X-Request-Id')
    print(x_req_id)
