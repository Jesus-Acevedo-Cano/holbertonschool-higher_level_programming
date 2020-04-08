#!/bin/bash
# request with the contents of a file, passed with the filename
curl -sX POST -H "Content-type: application/json" -d @"$2" "$1"
