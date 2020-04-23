from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import os
import datetime 
from rfeed import *
app = Flask(__name__)
import json
import webbrowser
import urllib.parse as urlparse
from urllib.parse import parse_qs

@app.route('/')
def hello():
    return redirect("/rss", code=302)

@app.route('/jsonfeed',methods=["GET"])
def jsonfeed():
    abcd = {
        "uid": "urn:uuid:1335c695-cfb8-4ebb-abbd-80da344efa6b",
        "updateDate": "2020-03-23T22:34:51.0Z",
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
        link = "https://developer.salesforce.com/docs/atlas.en-us.lightning.meta/lightning/components_config_for_flow_actions.htm", 
        description = "Create Flow Local Actions Using Aura Components. <speak > Check out the developer docs in alexa app </speak> ",
        author = "Saranyan Narayanan",
        guid = Guid("https://developer.salesforce.com"),
        pubDate = datetime.datetime(2015, 4, 16, 14, 15)
    
    )

    item2 = Item(
        title = "LWC Hub",
        link = "https://www.lwchub.com/techtalk/lwc-common", 
        description = "LWC Hub is a great resource for LWC",
        author = "Saranyan Narayanan",
        guid = Guid("https://www.lwchub.com/"),
        pubDate = datetime.datetime(2015, 4, 16, 14, 15))
    
    
    item3 = Item(
        title = "Mulesoft Anypoint Studio",
        link = "https://www.youtube.com/watch?v=mzwIwahqkYM", 
        description = "How to install anypoint studio , get the link in  your alexa app",
        author = "Saranyan Narayanan",
        guid = Guid("https://anypoint.mulesoft.com"),
        pubDate = datetime.datetime(2012, 4, 16, 14, 15))

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
        title = "Salesforce Service  Cloud",
        link = "https://www.Salesforce.com", 
        description = "Salesforce Service Cloud in Lightning <speak > My service is call center </speak>",
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
