#!/usr/bin/env python
#coding=utf-8

"""
    article.py
    ~~~~~~~~~~

    :license: BSD, see LICENSE for more details.
"""

from os import path

from flask import Module, render_template, current_app as app, abort

from cnfuyu_blog.helpers import translate_article

article = Module(__name__)

@article.route("/article/<name>")
def show(name):
    
    posts_dir = app.config["POSTS_DIR"]
    file_path = path.join(posts_dir, name) + ".md"
    
    if path.exists(file_path) == False:
        abort(404)
    
    article_content = translate_article(file_path)
    
    return render_template("article.html",
                           article = article_content)
