#!/usr/bin/env python
#coding=utf-8

"""
    home.py
    ~~~~~~~

    :license: BSD, see LICENSE for more details.
"""

from flask import Module, render_template, redirect, url_for, current_app as app

from cnfuyu_blog.helpers import get_articles, translate_article

home = Module(__name__)

@home.route("/")
@home.route("/home")
@home.route("/page/<int:page>")
def home_page(page = 1):
    
    articles, page_num = get_articles(page)
    
    prevpage = page - 1
    if prevpage <= 0:
        prevpage = False
    nextpage = page + 1
    if nextpage > page_num:
        nextpage = False

    return render_template("home.html",
                           articles = articles,
                           prevpage = prevpage,
                           nextpage = nextpage)
