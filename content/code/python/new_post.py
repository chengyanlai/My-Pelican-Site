#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os, sys
from datetime import datetime, date
from uuslug import slugify

try:
    blog_title = sys.argv[1]
    blog_slug = slugify(sys.argv[1])
except IndexError:
    blog_title = "test"
    blog_slug = blog_title

try:
    if sys.argv[2]:
        blog_author = "Chen-Yen Lai"
except IndexError:
    blog_author = "Yao-An Chan"

time_now = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

filename = str(date.today()) + "-" + blog_slug + ".md"

f = open('content/'+filename, 'w')

f.write("Date: " + time_now)
f.write("\nTitle: " + blog_title)
f.write("\nAuthor: " + blog_author)
f.write("\nCategory: ")
f.write("\nTags: ")
f.write("\nSlug: " + blog_slug)
f.write("\nSummary: ")
f.write("\nStatus: draft")
f.write("\n\n")
f.close()