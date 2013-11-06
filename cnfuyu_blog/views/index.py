#!/usr/bin/env python
#coding=utf-8

"""
    index.py
    ~~~~~~~~

    :license: BSD, see LICENSE for more details.
"""

from flask import Module, render_template

index = Module(__name__)

@index.route("/")
def index_page():
    
    return render_template("index.html")

@index.route("/resume")
def resume():
    
    return render_template("resume.html")
