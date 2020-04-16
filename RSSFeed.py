from flask import Flask, request, redirect, session, url_for
from flask.json import jsonify
import os
import datetime 
from rfeed import *
app = Flask(__name__)

import webbrowser
import urllib.parse as urlparse
from urllib.parse import parse_qs

@app.route("/rss", methods=["GET"])

def rss():
    item1 = Item(
        title = "First article",
        link = "http://www.example.com/articles/1", 
        description = "This is the description of the first article",
        author = "Santiago L. Valdarrama",
        guid = Guid("http://www.example.com/articles/1"),
        pubDate = datetime.datetime(2014, 12, 29, 10, 00))

    item2 = Item(
        title = "Second article",
        link = "http://www.example.com/articles/2", 
        description = "This is the description of the second article",
        author = "Santiago L. Valdarrama",
        guid = Guid("http://www.example.com/articles/2"),
        pubDate = datetime.datetime(2014, 12, 30, 14, 15))

    feed = Feed(
        title = "Sample RSS Feed",
        link = "http://localhost:5000/rss",
        description = "This is an example of how to use rfeed to generate an RSS 2.0 feed",
        language = "en-US",
        lastBuildDate = datetime.datetime.now(),
        items = [item1, item2])

    return feed.rss()

if __name__ == "__main__":
    # This allows us to use a plain HTTP callback
    #os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = "1"

    app.secret_key = os.urandom(24)
    app.run(debug=True)