#!/usr/bin/env python
#coding=utf-8

"""
    __init__.py
    ~~~~~~~~~~~

    :license: BSD, see LICENSE for more details.
"""

from os.path import exists

from flask import Flask, render_template

from cnfuyu_blog import views

DEAFAULT_APP_NAME = "cnfuyu_blog"

DEAFAULT_MODULES = (
    (views.index, ""),
    (views.home, "/blog"),
    (views.article, "/blog"),
    (views.feed, "/blog"),
)

def create_app(config = None, modules = None):
    
    if exists(config) == False:
        return False

    if modules is None:
        modules = DEAFAULT_MODULES
      
    app = Flask(DEAFAULT_APP_NAME)

    #config
    app.config.from_pyfile(config)
    
    configure_errorhandlers(app)

    #register module
    configure_modules(app, modules)

    return app

def configure_errorhandlers(app):
    
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html")

def configure_modules(app, modules):
    
    for module, url_prefix in modules:
        app.register_module(module, url_prefix = url_prefix)

