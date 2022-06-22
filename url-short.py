#!/bin/python3
import hashlib, base64
import random

baseuri = "https://somedomain-temp.com/"

def gen_short_url(long_url):
    #init
    short_url = ""
    noise = ""

    #make sure short url doesn't already exist
    do:
        short_url = hashlib.sha1(long_url + noise).encode("UTF-8")).hexdigest(5)
        noise = noise + random.choice("qwertyuiopasdfghjklzxcvbnm1234567890")
    while (check_db(short_url))
    
    # temp line change later for actual db
    db.add(long_url, short_url)
    
    return baseuri + short_url


# just an outline, use real vars + db later
def check_db(short_url):
    if (short_url in db.short_urls):
        return True
    else:
        return False
