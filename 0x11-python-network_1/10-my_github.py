#!/usr/bin/python3
# takes in a letter and sends a POST request
import requests
from sys import argv


if __name__ == '__main__':
    r = requests.get('https://api.github.com/user', auth=(argv[1], argv[2]))
    print(r.json().get("id"))
