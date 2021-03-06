#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chen-Yen Lai'
SITENAME = u'Little Things about Everything'
SITESUBTITLE = u'Never Stop Learning'
SITEURL = ''

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (("老百姓HP的部落格", "http://hpwange.pixnet.net/blog"),
          ('La Casa de JimmyBlanca', 'http://jimmyblanca.blogspot.com'),
          ('A Free Seeker', 'http://thousandchen.blogspot.com'),
          ('sally\'s little world', 'http://marykey-all.blogspot.com'),
          ('Sentimental Reasons', 'http://vilina.blogspot.com/'),
          ('Markdown語法', 'http://markdown.tw/'),
          ('Dingus Tryout', 'http://daringfireball.net/projects/markdown/dingus'),
          ('PHP Markdown Extra', 'http://michelf.ca/projects/php-markdown/extra/'),)
#          ('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIALCY = (('facebook', 'http://www.facebook.com/chenyenlai'),
          ('flickr', 'http://www.flickr.com/photos/xavierweathertoplai/'),
          ('github', 'https://github.com/chengyanlai'),
          ('twitter', 'https://twitter.com/chenyenlai'),
          ('linkedin', 'http://www.linkedin.com/pub/chenyen-lai/52/568/901'),
          ('gplus', 'https://plus.google.com/+ChenYenLai'),
          ('email', 'mailto:chengyanlai@gmail.com'),)
SOCIALYA = (('facebook', 'http://www.facebook.com/yaoanchan'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = (['codehilite(css_class=highlight)','extra'])

MENUITEMS = ()

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

STATIC_PATHS = ['images', 'code', 'pdf']
NOTEBOOK_DIR = 'code/python/notebooks'

USE_FOLDER_AS_CATEGORY = False

#THEME = "./octopress"

# For Theme - gum
THEME = "./gum"
TWITTER_URL = "https://twitter.com/chenyenlai"
GITHUB_URL = "https://github.com/chengyanlai"
FACEBOOK_URL = "https://www.facebook.com/chenyenlai"
GOOGLEPLUS_URL = "https://plus.google.com/+ChenYenLai"
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = True
TAG_CLOUD_STEPS = 4

# For Plugins
PLUGIN_PATHS = ['./plugins',]
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.include_code',
           'liquid_tags.notebook','render_math','googleplus_comments']
