#!/usr/bin/python3
"""
    A script that takes a URL, sends a request to the URL
    and displays the body of the response
"""

if __name__ == "__main__":
    import urllib.request
    import urllib.error
    import sys
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            res = response.read().decode('utf-8')
            print(res)
    except urllib.error.HTTPError as e:
        print('Error code:', e.get('code'))
