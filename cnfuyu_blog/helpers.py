#!/usr/bin/env python
#coding=utf-8

"""
    helpers.py
    ~~~~~~~~~~

    :license: BSD, see LICENSE for more details.
"""

import os
import codecs
import math
import markdown
from os import path, listdir

from flask import current_app as app

def file_filter(files, filters):
    
    return filter(lambda x: (x in filters) is False, files)

def get_articles(page = 1, ret_page_num = True):
    
    posts_dir = app.config["POSTS_DIR"]
    per_page_num = app.config["PER_PAGE_NUM"]

    files = listdir(posts_dir)
    files = file_filter(files, [".svn", ".git"])

    file_num = len(files)
    page_num = math.ceil(file_num / float(per_page_num))
    files.sort(reverse = True)

    file_list = [path.join(posts_dir, f) for f in files]
    articles = [translate_article(f) for f in file_list[(page - 1) * per_page_num : page * per_page_num]]

    if ret_page_num is True:
        return articles, page_num
    else:
        return articles

def translate_article(file_path):
    
    f = codecs.open(file_path, "r", "utf-8")
    
    lines = f.readlines()
    
    f.close()
    
    response = {}

    for n, line in enumerate(lines[1 : ]):
        if "update: " in line:
            response["update"] = line.replace("update: ", "")
            continue
        elif "date: " in line:
            response["date"] = line.replace("date: ", "")
            continue
        elif "title: " in line:
            response["title"] = line.replace("title: ", "")
            continue
        elif "```" in line:
            break
    
    content = "".join(lines[n + 2 : ])

    response["content"] = markdown.markdown(content)
    response["name"] = file_path.split(os.sep)[-1].split(".")[0]
    response["update"] = response["update"] if response.get("update", None) is not None else response["date"] 

    return response
