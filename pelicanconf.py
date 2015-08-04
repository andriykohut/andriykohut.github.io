#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andriy Kogut'
SITENAME = u'HOKAI!'
SITEURL = 'http://andriykohut.github.io'
SITETITLE = 'Hokai!'
SITESUBTITLE = "Just some python hacker"
SITEDESCRIPTION = "Stuff I find interesting and useful"
SITELOGO = 'https://lh3.googleusercontent.com/D_nTcNrJlLAGy7N4yNuUkGo6TNqIqolUW3J2sOyZJAU=w680-h861-no'
FAVICON = 'img/favicon.ico'
ROBOTS = 'index, follow'

COPYRIGHT_YEAR = 2015
CC_LICENSE = {'name': 'Creative Commons Attribution-ShareAlike',
              'version': '4.0', 'slug': 'by-sa'}
MAIN_MENU = True

PATH = 'content'
PAGE_URL = 'pages/{slug}/'

TIMEZONE = 'Europe/Kiev'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DISQUS_SITENAME = 'andriykohutgithubio'

# Blogroll
LINKS = (('about', '/about'),
         ('contact', '/contact'),
         )

# Social widget
SOCIAL = (('linkedin', 'https://ua.linkedin.com/in/akohut'),
          ('github', 'https://github.com/andriykohut'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = "Flex"

STATIC_PATHS = ['img']
