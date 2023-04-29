#!/usr/bin/python3
"""
    A python script takes in a letter and sends a POST request to
    http://0.0.0.0:5000/search_user with the letter as a parameter
"""

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) >= 2:
        data = {'q': sys.argv[1}
    else:
        data = {'q': ''}

    res = requests.get('http://0.0.0.0:5000/search_user')

    try:
        res = res.json()
        if len(res) == 0 or not res.get('id') or not res.get('name'):
            print("No result")
        else:
            print("[{}] {}".format(res.get('id'), res.get('name')))
    except:
        print("Not a valid JSON")
