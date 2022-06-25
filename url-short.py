#!/bin/python3
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import hashlib, base64
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////url-shortener.db'
db = SQLAlchemy(app)

class UrlDBE(db.model):
    short_url = db.Column("shorturl", db.String(7), primary_key=True)
    long_url = db.Column("longurl", db.String())
    
    def __init__(self, short_url, long_url):
        self.short_url = short_url
        self.long_url = long_url

@app.route('/', methods=['POST', 'GET'])
def index():
    if (request.method == "POST"):
        long_url = request.form["long_url_in"]
        # do more here
    if (request.method == "GET"):
        return render_template('index.html')

def gen_short_url(long_url):
    #init
    short_url = ""
    noise = ""
    #make sure short url doesn't already exist
    # is there a better way to do this? probably
    do:
        short_url = hashlib.sha1((long_url + noise).encode("UTF-8")).hexdigest()[:7]
        noise = noise + random.choice("qwertyuiopasdfghjklzxcvbnm1234567890")
    while (check_db(short_url))
    
    # temp line change later for actual db
    db.add(long_url, short_url)
    
    return short_url


#
# Name : generate_html
# Desc : Generate html with a built in redirect with given url
# Returns : string of html 
#
def generate_html(long_url):
    return"<html><head><title>Redirecting...</title><meta http-equiv=\"refresh\" content=\"0; url=" + long_url + "\"/></head><body><a>Redirecting</a></html>"
    
# just an outline, use real vars + db later
#def check_db(short_url):
#    if (short_url in db.short_urls):
#        return True
#    else:
#        return False







if (__name__ == '__main__'):
    app.run(port=5000, debug=True)
