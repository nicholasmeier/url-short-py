#!/bin/python3
import hashlib, base64
import random
import pyshorteners
import sys

#
# Script version for shortening urls using existing apis / services
# Limitations: 
#   - relies on external resources not effective for internal/private endpoints 
#   - no control over external apis
# Benefits:
#   - less developer overhead
#   - simple code
#   - No need for a whole stack for existing services
#
# 

def main():
    if len(sys.argv) == 2:
        long_url = sys.argv[1]

        shortener_tu = pyshorteners.Shortener()
        short_url = shortener_tu.tinyurl.short(long_url)

        print("Short URL = " + short_url)
    elif len(sys.argv) == 1:
        long_url = input("Enter long url: ")
    else:
        print("err: incorrect format")
        print("example usage: ./url-short.py <longurl>")
        exit(1)

if __name__ == "__main__":
    main()
