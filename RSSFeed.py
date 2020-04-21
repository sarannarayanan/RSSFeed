from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import os
import datetime 
from rfeed import *
app = Flask(__name__)

import webbrowser
import urllib.parse as urlparse
from urllib.parse import parse_qs

@app.route('/')
def hello():
    return redirect("/rss", code=302)

@app.route('/json')
def jsonret():
    abcd = {
        "uid": "urn:uuid:1335c695-cfb8-4ebb-abbd-80da344efa6b",
        "updateDate": "2016-05-23T22:34:51.0Z",
        "titleText": "Amazon Developer Blog, week in review May 23rd",
        "mainText": "",
        "streamUrl": "https://developer.amazon.com/public/community/blog/myaudiofile.mp3",
        "redirectionUrl": "https://developer.amazon.com/public/community/blog"
        }
    return json.dumps(abcd, sort_keys=True, indent=2, separators=(',', ': '))

@app.route("/rss", methods=["GET"])

def rss():
    item1 = Item(
        title = "Salesforce Best practice",
        link = "https://www.Salesforce.com", 
        description = " Triggers are to be bulkified, else they will trigger failuers  ",
        author = "Saranyan Narayanan",
        guid = Guid("https://www.Salesforce.com"),
        pubDate = datetime.datetime(2020, 4, 16, 14, 15)
    
    )

    item2 = Item(
        title = "LWC Hub",
        link = "https://www.lwchub.com/techtalk/lwc-common", 
        description = "LWC Hub is a great resource for LWC",
        author = "Saranyan Narayanan",
        guid = Guid("https://www.lwchub.com/"),
        pubDate = datetime.datetime(2020, 4, 16, 14, 15))
    
    
    item3 = Item(
        title = "LWC Hub",
        link = "https://www.youtube.com/watch?v=mzwIwahqkYM", 
        description = "How to install anypoint studio , get the link in  your alexa app",
        author = "Saranyan Narayanan",
        guid = Guid("https://anypoint.mulesoft.com"),
        pubDate = datetime.datetime(2020, 4, 16, 14, 15))

    feed = Feed(
        title = "Sample RSS Feed",
        link = "https://herokuhero-sharan.herokuapp.com/rss",
        description = "This is an example of how to use rfeed to generate an RSS 2.0 feed",
        language = "en-IN",
        lastBuildDate = datetime.datetime.now(),
        items = [item1, item2, item3])

    return feed.rss()

@app.route("/crmrss", methods=["GET"])

def crmrss():
    item1 = Item(
        title = "Salesforce Sales Cloud",
        link = "https://www.Salesforce.com", 
        description = "Salesforce Sales Cloud in Lightning",
        author = "Saranyan Narayanan",
        guid = Guid("https://www.Salesforce.com"),
        pubDate = datetime.datetime(2020, 4, 16, 14, 15)
    
    )



    feed = Feed(
        title = "Sample RSS Feed",
        link = "https://herokuhero-sharan.herokuapp.com/crmrss",
        description = "This is an example of how to use rfeed to generate an RSS 2.0 feed",
        language = "en-IN",
        lastBuildDate = datetime.datetime.now(),
        items = [item1])

    return feed.rss()


if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    #os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

    app.secret_key = os.urandom(24)
    app.run(debug=True)
