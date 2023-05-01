#!/usr/bin/python3
"""
    Python script that fetches https://alx-intranet.hbtn.io/status
"""

if __name__ == "__main__":
    import requests

    res = requests.get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type:", str(type(res.text)))
    print("\t- content:", str(res.text))
