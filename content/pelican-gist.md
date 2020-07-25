title: Code Snippets
Category: Tech
Tags: pelican, blogging, python
Slug: pelican-gist
date: 05/10/2020
author: Engineerang
Summary: Adding Code Snippets to Pelican from GitHub Gists

As I continue to grow my blog/tech diary I wanted a place to feature useful code snippets or commands I often forget. I'm already using GitHub's Gist to source control a number of code snippets so why not use that as the basis of my snippets here. Luckily enough, Pelican supports Gists in the [pelican-plugins repo](https://github.com/getpelican/pelican-plugins) giving us two options for implementation.

1. [gist_directive](https://github.com/getpelican/pelican-plugins/tree/master/gist_directive); and
2. [pelican-gist](https://github.com/streeter/pelican-gist/tree/395e619534b404fb2b94456dc400dc2a8a2f934a)

After playing around with both of these plugins, I settled on using gist_directive. Although gist_directive is a restructured-text plugin (previously I mentioned I'm a MarkDown fan), its feature set satisfied the functionality I was after. The main advantages it has over streeter's pelican-gist is that it's able to directly target a GitHub user's Gist and that you can configure the code highlighting. The obvious disadvantage is that I've introduced restructured-text in to a pretty much exclusive MarkDown environment. But hey, it's only one page and the shoe fits.

All that's required is to add gist_directive to your ```pelicanconf.py``` like so:

````
PLUGINS = ['i18n_subsites', 'related_posts', 'series', 'tag_cloud', 'gist_directive']
````
----------------------
Modify the plugin module file, ```gist_directive/__init__.py```, so that it can be loaded locally.

before:
````python
from gist_directive import *
````
after:
````python
from .gist_directive import *
````
----------------------
and create your restructured-text file:

````
Code Snippets
#############

Code snippets from my personal gist: https://gist.github.com/engineerang

Pelican
*******
.. gist:: engineerang/72286b20f138a9aeecac7ec3905203a1 publish-pelican.sh bash
````
----------------------

__From now on you can find any Code Snippets I find handy or useful here: [Code Snippets](https://engineerang.github.io/pages/code-snippets.html)__ 👌

