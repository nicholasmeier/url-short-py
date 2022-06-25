#!/bin/python3
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import hashlib, base64
import random

#short_url = db
#shorturl = appcode


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/url-shortener.db'
db = SQLAlchemy(app)


#URL DB class
class UrlDBE(db.Model):
    short_url = db.Column("shorturl", db.String(7), primary_key=True)
    long_url = db.Column("longurl", db.String())
    
    def __init__(self, short_url, long_url):
        self.short_url = short_url
        self.long_url = long_url

#init db
@app.before_first_request
def create_tables():
    db.create_all()

# index html page
@app.route('/', methods=['POST', 'GET'])
def index():
    if (request.method == "POST"):
        longurl = request.form["long_url_in"]
        shorturl = gen_short_url(longurl)
        
        # Conditional for db check timeout
        if shorturl == -1:
            print("error with url gen")
            return render_template('index.html', display_shorturl="Err: Could not generate shortURL")
        newurlpair = UrlDBE(shorturl, longurl)
        db.session.add(newurlpair)
        db.session.commit()
        return render_template('index.html', display_shorturl=shorturl)
    elif (request.method == "GET"):
        return render_template('index.html', display_shorturl=" ")

@app.route('/<shorturl>')
def redirect_shorturl(shorturl):
    urldb_entry = UrlDBE.query.filter_by(short_url=shorturl).first()
    if urldb_entry:
        return redirect(urldb_entry.long_url)
        #return render_template('redirect.html', redirectContent=contentstring)
        #return "<head><title>Redirecting...</title><meta http-equiv=\"refresh\" content=\"0; url=" + urldb_entry.long_url + "\"/></head><body><a>Redirecting</a>"
    else:
        return "Err: Broken link, sorry :("


def gen_short_url(longurl):
    shorturl = ""
    noise = ""
    #make sure short url doesn't already exist
    # is there a better way to do this? probably
    # gonna make this hacky and not infinitely loop
    infinitybreaker = 0
    while(True):
        shorturl = hashlib.sha1((longurl + noise).encode("UTF-8")).hexdigest()[:7]
        if ( (bool(UrlDBE.query.filter_by(short_url=shorturl).first())) == False):
            return shorturl
        noise = noise + random.choice("qwertyuiopasdfghjklzxcvbnm1234567890")
        infinitybreaker += 1
        if infinitybreaker == 600:
            break
    #while (bool(UrlDBE.query.filter_by(short_url=shorturl).first()))
    #return short_url
    return -1

#def generate_html(long_url):
    #return"<html><head><title>Redirecting...</title><meta http-equiv=\"refresh\" content=\"0; url=" + long_url + "\"/></head><body><a>Redirecting</a></html>"
    
# just an outline, use real vars + db later
#def check_db(short_url,):
 #   if (short_url in db.short_urls):
  #      return True
   # else:
    #    return False



if (__name__ == '__main__'):
    app.run(port=5000, debug=True)
