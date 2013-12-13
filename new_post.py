import os, sys
from datetime import datetime, date

try:
    blog_title = sys.argv[1]
except IndexError:
    blog_title = "test"

try:
    if sys.argv[2]:
        blog_author = "Chen-Yen Lai"
except IndexError:
    blog_author = "Yao-An Chan"

filename = str(date.today()) + "-" + blog_title + ".md"

f = open('content/'+filename, 'w')

f.write("Date: " + str(datetime.today()))
f.write("\nTitle: " + blog_title)
f.write("\nAuthor: " + blog_author)
f.write("\nCategory: ")
f.write("\nTags: ")
f.write("\nSlug: ")
f.write("\nSummary: ")
f.write("\nStatus: draft")
f.write("\n\n")
f.close()