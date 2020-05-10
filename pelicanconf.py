#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Engineerang'
SITENAME = 'Engineerang'
SITESUBTITLE = 'Planning makes perfect'
SITEURL = 'engineerang.github.io'
GITHUB_URL = 'https://github.com/engineerang'
PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = 'en'

# Pelican Theme
THEME = 'pelican-bootstrap3'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

# Pelican Plugins
# https://github.com/getpelican/pelican-plugins/tree/master/series
# https://github.com/getpelican/pelican-plugins/tree/master/related_posts
# https://github.com/getpelican/pelican-plugins/tree/master/i18n_subsites
# https://github.com/getpelican/pelican-plugins/tree/master/tag_cloud

PLUGINS = ['i18n_subsites', 'related_posts', 'series', 'tag_cloud', 'gist_directive']
PLUGIN_PATHS = ['./pelican-plugins/']
I18N_TEMPLATES_LANG = 'en'

# Markdown settings
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'markdown_markup_emoji.markup_emoji': {},
    },
    'output_format': 'html5',
}

# Bootstrap Settings
BOOTSTRAP_THEME = 'darkly'
PYGMENTS_STYLE = 'solarizeddark'
BOOTSTRAP_FLUID = False
DISPLAY_BREADCRUMBS = True
DISPLAY_CATEGORY_IN_BREADCRUMBS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/engineerang'),
          ('github', 'https://github.com/engineerang'),
          ('reddit', 'https://www.reddit.com/user/engineerang'),
          )

DELETE_OUTPUT_DIRECTORY = True
USE_PAGER = True
DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = False
RELATED_POSTS_MAX = 5
DISPLAY_SERIES_ON_SIDEBAR = True
DISPLAY_ARTICLE_INFO_ON_INDEX = True
DISQUS_DISPLAY_COUNTS = True
DISPLAY_TAGS_ON_SIDEBAR = True
TAG_CLOUD_MAX_ITEMS = 10
DISPLAY_CATEGORIES_ON_SIDEBAR = True
DISPLAY_RECENT_POSTS_ON_SIDEBAR = True
DISQUS_SITENAME = 'engineerang'
CC_LICENSE = 'CC-BY-SA'


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
