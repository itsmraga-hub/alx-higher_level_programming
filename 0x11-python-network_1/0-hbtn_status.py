#!/usr/bin/python3
"""
  Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":

    import urllib.request
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        body = res.read()
        print("Body response:")
        print("\t- type: " + str(type(body)))
        print("\t- content: " + str(body))
        print("\t- utf8 content: " + str(body.decode('utf-8')))
