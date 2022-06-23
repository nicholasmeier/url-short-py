#!/bin/python3
import hashlib, base64
import random
import boto3


baseuri = "https://somedomain-temp.com/"

def gen_short_url(long_url):
    #init
    short_url = ""
    noise = ""

    #make sure short url doesn't already exist
    do:
        short_url = hashlib.sha1((long_url + noise).encode("UTF-8")).hexdigest()[:7]
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


def generate_html(short_url):
    f = open("temp.html","w")
    f.write("<html><head><title>Redirecting...</title><meta http-equiv=\"refresh\" content=\"0; url=" + short_url + "\"/></head><body><a>Redirecting</a></html>")

