#!/usr/bin/python3
# script that fetches an url only request pack
import requests


if __name__ == "__main__":
    r = requests.get('https://intranet.hbtn.io/status')
    print("Body response:")
    print("\t- type: {}".format(type(r.content.decode("utf-8"))))
    print("\t- content: {}".format(r.content.decode("utf-8")))
