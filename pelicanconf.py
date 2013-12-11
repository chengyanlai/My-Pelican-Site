#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Chen-Yen Lai'
SITENAME = u'Little Things about Everything'
SITESUBTITLE = u'Never Stop Learning'
SITEURL = 'http://chengyanlai.github.io'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  (('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('Chen-Yen\'s Facebook', 'http://www.facebook.com/chenyenlai'),
          ('Chen-Yen\'s Flickr', 'http://www.flickr.com/photos/xavierweathertoplai/'),
          ('Yao-An\'s Facebook', 'http://www.facebook.com/yaoanchan'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MD_EXTENSIONS = (['codehilite(css_class=highlight)','extra'])

MENUITEMS = (('Archives',SITEURL+'/archives.html'),)

ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

STATIC_PATHS = ['images', 'code']

#THEME = "/Users/Shared/Git_repo/GitHub/my-blog/pelican-octopress-theme"

# For Theme - gum
THEME = "/Users/Shared/Git_repo/GitHub/my-blog/gum"
TWITTER_URL = "https://twitter.com/chenyenlai"
GITHUB_URL = "https://github.com/chengyanlai"
FACEBOOK_URL = "https://www.facebook.com/chenyenlai"
GOOGLEPLUS_URL = "https://plus.google.com/+ChenYenLai"

# For Plugins
PLUGIN_PATH = '/Users/Shared/Git_repo/GitHub/my-blog/plugins'
PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.include_code',
           'liquid_tags.notebook','latex','googleplus_comments']