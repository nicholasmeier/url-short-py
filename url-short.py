#!/bin/python3
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import hashlib, base64
import random

#short_url = db_var
#shorturl = app_var


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/url-shortener.db'
db = SQLAlchemy(app)


#URL DB object
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

        #Conditionals for formatting longurl:
        if (longurl[:4] == "www."):
            longurl = "https://" + longurl
        elif (longurl[:8] != "https://" and longurl[:7] != "http://"):
            return render_template('index.html', display_shorturl="Err: check formatting for your url input")

        shorturl = gen_short_url(longurl)
        # Conditional for db check timeout
        if shorturl == -1:
            print("error with url gen")
            return render_template('index.html', display_shorturl="Err: Could not generate shortURL")

        # create new db entry
        newurlpair = UrlDBE(shorturl, longurl)
        db.session.add(newurlpair)
        db.session.commit()
        
        # return shortened link
        dispshort = request.base_url + shorturl
        return render_template('index.html', display_shorturl=dispshort)

    # default index
    elif (request.method == "GET"):
        return render_template('index.html', display_shorturl=" ")

@app.route('/<shorturl>')
def redirect_shorturl(shorturl):
    urldb_entry = UrlDBE.query.filter_by(short_url=shorturl).first()
    if urldb_entry:
        return redirect(urldb_entry.long_url)
    else:
        return "Err: Broken link, sorry :("


def gen_short_url(longurl):
    shorturl = ""
    noise = ""
    # is there a better way to do this? maybe?
    infinitybreaker = 0
    while(True):
        #generate shorturl from hashfunction
        shorturl = hashlib.sha1((longurl + noise).encode("UTF-8")).hexdigest()[:7]

        #check if hashfunction already exists in db
        if ( (bool(UrlDBE.query.filter_by(short_url=shorturl).first())) == False):
            #if not then just return
            return shorturl
        #else create some noise
        noise = noise + random.choice("qwertyuiopasdfghjklzxcvbnm1234567890")

        #make sure this only runs for x loops
        infinitybreaker += 1
        if infinitybreaker == 600:
            break
    return -1

if (__name__ == '__main__'):
    app.run(port=5000, debug=True)
