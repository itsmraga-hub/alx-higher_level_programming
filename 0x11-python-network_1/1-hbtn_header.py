#!/usr/bin/python3
"""
    A python script that takes in a URL, sends a request and displays the
    value of the X-Request-Id variable found in the header of the response
"""


if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        x_req_id = response.headers.get('X-Request-Id')
        print(x_req_id)
