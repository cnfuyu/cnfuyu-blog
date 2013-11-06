#!/usr/bin/env python
#coding=utf-8

"""
    run.py
    ~~~~~~

    :license: BSD, see LICENSE for more details.
"""

from os.path import abspath, dirname, join

from cnfuyu_blog import create_app  

curpath = abspath(dirname(__file__))

app = create_app(join(curpath, "config.cfg"))

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
