#!/usr/bin/env python
# -*- coding: utf-8 -*- #
import os, sys
from datetime import datetime, date
from uuslug import slugify

try:
    rin = slugify(sys.argv[1])
    blog_title =  rin
except IndexError:
    blog_title = "test"

try:
    if sys.argv[2]:
        blog_author = "Chen-Yen Lai"
except IndexError:
    blog_author = "Yao-An Chan"

time_now = datetime.today().strftime("%Y-%m-%d %H:%M:%S")

filename = str(date.today()) + "-" + blog_title + ".md"

f = open('content/'+filename, 'w')

f.write("Date: " + time_now)
f.write("\nTitle: " + blog_title)
f.write("\nAuthor: " + blog_author)
f.write("\nCategory: ")
f.write("\nTags: ")
f.write("\nSlug: " + blog_title)
f.write("\nSummary: ")
f.write("\nStatus: draft")
f.write("\n\n")
f.close()