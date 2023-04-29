#!/usr/bin/python3
"""
    Script that takes a URL and email, sends a POST req to the passed URL
    with email as a parameter
"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url = sys.argv[1]
    value = {'email': sys.argv[2]}

    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)

    with urllib.request.urlopen(req) as res:
        res = res.read()
        res = res.decode('utf-8')
        print(res)
