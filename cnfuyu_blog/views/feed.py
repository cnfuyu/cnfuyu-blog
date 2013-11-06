#!/usr/bin/env python
#coding=utf-8

"""
    feed.py
    ~~~~~~~

    :license: BSD, see LICENSE for more details.
"""

import datetime

from flask import Module, url_for
from werkzeug.contrib.atom import AtomFeed

from cnfuyu_blog.helpers import get_articles

feed = Module(__name__)

@feed.route("/feed")
def index():
    
    title = "CNFUYU"
    author = {"name" : "Yu Fu", "email" : "cnfuyu@gmail.com"}
    
    feeds = AtomFeed(title = title,
                     feed_url = url_for("index", _external = True),
                     url = url_for("home.home_page", _external = True),
                     author = author,
                    )

    articles = get_articles(page = 1, ret_page_num = False)
    
    for article in articles:
        feeds.add(title = article["title"],
                 content = article["content"],
                 content_type = "html",
                 author = author,
                 url = url_for("article.show", name = article["name"]),
                 updated = datetime.datetime(int(article["update"][0 : 4]),
                                               int(article["update"][5 : 7]),
                                               int(article["update"][8 : 10]),
                                               int(article["update"][11 : 13]),
                                               int(article["update"][14 : 16]),
                                              ),
                 published = datetime.datetime(int(article["date"][0 : 4]),
                                               int(article["date"][5 : 7]),
                                               int(article["date"][8 : 10]),
                                               int(article["date"][11 : 13]),
                                               int(article["date"][14 : 16]),
                                              ),
                 )
    
    return feeds.get_response()
