title: Hello World - Using Pelican and GitHub to create a blog.
Category: Tech
Tags: pelican, blogging, python
Slug: hello-world
date: 18/04/2020
author: Engineerang
Summary: The birth of a blog using Pelican and GitHub.
 
I've been thinking about writing a blog for a while now and have wanted to do so for a number of reasons. The most notable being that I want to give back to the open source community that has so selflessly helped me grow and learn. Coming in at a close second is that during my journey, there have been occasions where I've had to collate A LOT of resources and dumpster-dive obscure parts of the internet to find answers.
 
With these reasons in mind, my intention is to provide an informative space to write down my thoughts, journal my projects as they're being developed, and share interesting/helpful snippets that I find along the way.
 
This article will be no exception to the aforementioned intention and thus I will inaugurate my blog with why I chose Pelican and Github and how I went about setting it all up.
 
## Why use Pelican? 🤔
 
I knew coming into this project that I would have a list of things I wanted, and some things that I could compromise on when choosing a solution. These broadly fell in to the following categories:
 
*Blog Application:*
 
1.  MUST be lightweight requiring no additional infrastructure (e.g. a database)
2.  MUST be able to create content in a straightforward way (i.e. not raw HTML)
 
*Blog integrations:*
 
1.  MUST include the ability to customize 'themes' for a personalized experience.
2.  MUST support a comments section
3.  MUST support 'Single Sign On' (i.e i don't want to manage users)
4.  SHOULD support site analytics
5.  SHOULD support language translation
 
*Hosting:*
 
1. MUST be hosting agnostic (i.e. many options for hosting)
2. MUST have TLS/SSL termination (i.e. some way to get the https Green Lock)
3. MUST support DNS (i.e. some way to point a URL at my blog)
4. SHOULD be free to host
 
*Personal Constraints:*
 
1. MUST maintain control of the content
2. SHOULD be created using Python
 
For me, Pelican ticked all of these boxes and some! ✅
 
## Pelican
 
Honestly, I had intended to write a post on how I built my blog step-by-step for others to follow along. However, due to general life and procrastination I haven't put something together and in the spirit of just getting something published (and thus starting my blog!) I've decided to share the resources that I used to get started. 😀
 
### Guides 📋
Matthew and Erik's step-by-step guides (links below) are brilliant. I started with Erik's to get a general idea of how Pelican works before using Matthew's to polish up my own blog that you see now. Matthew's guide covers everything from GitHub publishing to integrating Disqus and Google analytics.
 
* [Matthew Davaney's blog](https://matthewdevaney.com/posts/2019/03/10/deploying-a-static-website-to-github-pages/)
* [Erik O'Shaughnessy' blog](https://opensource.com/article/19/5/run-your-blog-github-pages-python)
 
### Adding Emoji Support 🤪
Ok, so I took the easy route and just linked a bunch of guides... In penitence I will offer a critical feature not mentioned in the guides above, **Emoji support**.

To add Emoji support to your blog all you have to do is the following:

Add the [Markdown emoji module](https://pypi.org/project/markdown-markup-emoji/) to your ```requirements.txt```
````txt
...
markdown-markup-emoji
...
````
and install with pip, ```pip install -r requirements.txt```.

Next, add the emoji Markdown extension to your ```pelicanconf.py```
````python
...
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
...
````

Now you're all set to use Emoji's in your Markdown! 👌

A full list of Unicode Emoji's can be found [here](https://unicode.org/emoji/charts/full-emoji-list.html)

### Themes 🖼
 
When I first started looking at themes I couldn't decide which one I wanted and so instead cloned the entire Pelican theme project into my project's root directory:
 
````bash
git clone https://github.com/getpelican/pelican-themes.git
````
 
I ended up using ```THEME = 'pelican-bootstrap3'```, playing with the theme until I arrived at:
````ini
BOOTSTRAP_THEME = 'darkly'
PYGMENTS_STYLE = 'solarizeddark'
````
 
### Plugins 🔌
Similar to themes, I cloned the entire Pelican plugin project into my project's root directory:
 
````bash
git clone https://github.com/getpelican/pelican-plugins.git
````
 
I then played around with the plugins that suited my needs and ended up with:
````ini
PLUGINS = ['i18n_subsites', 'related_posts', 'series', 'tag_cloud']
````

## Helpful Pelican tips 🧐

### Drafting Markdown
As mentioned in my requirements for a static HTML generator, Markdown was my preferred static markup language. Producing Markdown can be a bit tedious because you can't see the end results until you generate it. Another downside to using Markdown is that most plaintext editors generally don't come with spellchecking..

To resolve these problems I used the following [Visual Studio Code](https://code.visualstudio.com/Download) extensions to preview Markdown as I produced it, and prompt me when there's a grammatical error:

* [Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)
* [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker)

### Blog preview
Before I publish to Github Pages I always preview a local copy of my changes to make sure I'm happy with the formatting and contents. To do this you can run the following:

````bash
pelican content -o output -s publishconf.py # Generate the static files
pelican --listen                            # Serve the files locally
````

Now go to ```127.0.0.1:8000``` in your browser for a preview of your newly added article or updated theme. 

Note: things like Disqus comments won't work locally.

### Publishing to GitHub Pages
Everything looks awesome and now you're ready to push your changes and publish your blog!

````bash
# Generate the static files in the output directory
pelican content -o output -s publishconf.py                        

# Add the output directory to the master branch using ghp-import
ghp-import -m "Generate Pelican site" --no-jekyll -b master output 

# Push the master branch (output directory files) to the remote repo
git push origin master

# Commit and push the new content to the content branch
git add content
git commit -m 'Updated Pelican site!'
git push origin content
````
Now it's time to view your changes in all their glory!

## Summary
Hopefully this article was useful and pointed you in the direction of some really helpful resources. I'd like to extend my gratitude to Erik and Matthew for the awesome posts! Couldn't have done it without you.

Thanks for taking the time to stop by and I hope to continue bringing you helpful/interesting content going forward. 🍻

P.S. I have no regrets for the amount of emoji's used in this article. 😂
