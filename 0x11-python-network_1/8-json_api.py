#!/usr/bin/python3
# takes in a letter and sends a POST request
import requests
from sys import argv


if __name__ == '__main__':
    try:
        data = [("q", argv[1])]
    except Exception:
        data = [("q", "")]
    r = requests.post("http://0.0.0.0:5000/search_user", data)
    try:
        json = r.json()
        if json:
            print("[{}] {}".format(json['id'], json['name']))
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")
