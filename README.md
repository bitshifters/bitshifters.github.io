BitShifters Jekyll website
==========================



## Preamble
This repo is the website for [BitShifters](http://bitshifters.github.io), which is hosted using [GitHub pages](https://pages.github.com/).

Since GitHub pages serves only static html content, we can use [Jekyll](http://jekyllrb.com/) to "compile" templated content into a live static HTML website.

Jekyll typically builds the website into an output folder in the root of the repo called **_site**, however, GitHub helpfully does this build for us when new files are committed into a GitHub pages repo, so that is why there is no _site folder committed in the repo.

The site uses the [Bootstrap](http://www.w3schools.com/bootstrap/default.asp) HTML/CSS framework. This makes it very easy to add responsive and well designed components to pages within minimum fuss.


## Developer notes
It is easy to modify the website, just clone the repo and make the desired changes. To reflect the changes live, simply push changes back to the GitHub repo.

If you want to test locally before pushing to the live site repo, you need to install Jekyll. 

A guide for installing Jekyll on windows can be found [here](https://davidburela.wordpress.com/2015/11/28/easily-install-jekyll-on-windows-with-3-command-prompt-entries-and-chocolatey/).

`sudo apt-get install jekyll` should do the trick on Ubuntu.

To build the site:
```
jekyll build
```

To run a local http server to see the site:
```
jekyll serve
```

To run a local http server that automatically rebuilds the site when any changes are made (very useful!):
```
jekyll serve --watch
```


## Site structure
The overall site is designed to be a simple CMS to make it easy for us to add new content (such as productions or competitions). Since the site is static only, there is no backend database, so things like search and dynamic filters for content are not easy to achieve.

The site has 4 main pages, each with a custom layout:
 - home (default.html)
 - archive (archive.html)
 - info (info.html)
 - support (support.html)
 - art (art.html)

 
 The site currently supports 6 types of post:
  - **Productions** (`prods` category, `_posts/prods`) - pieces of work created by the Bitshifters collective
  - **Competitions** (`compo` category, `_posts/compos`) - competitions we've entered productions into
  - **Archives** (`compos` category, `_posts/archives`) - pieces of work created by anyone else. They are treated by the site as productions also, but just categorised differently
  - **Team** (`team` category, `_posts/team`) - one post per team member that wants to be listed in the `.NFO` page
  - **Support** (`support` category, `_posts/support`) - one post per support topic that will be listed in the `support.html` page


Some files (templates, layouts, includes etc.) are mostly HTML, with embedded Liquid templating commands that are compiled by Jekyll. 

Some files (pages, posts, data) are YAML style configuration files, with embedded variables and markdown formatted content.


## How to use

**THE FOLLOWING IS OUT OF DATE, BEWARE!**

### Productions (eg. new demos created by BitShifters)
To add a new production:
 - Place a image and a disk image file (SSD or DSD) in `/content/`
 - Create a .md file in the `_posts/prods/` folder with the correct filename convention, and the content you wish to publish
 - Apply the correct category and tags, and the new production will automatically be listed in the right place when the site is rebuilt

Post Filename format:
 - `yyyy-mm-dd-team-prodname.md`

```txt
---
layout: prods_post
category: [posts, prods]
tags: whatever tags you like. For compo entries, add a tag that matches a compo_id

title: name of the production
img: filename of the image in /content/ for this production (no need for any path) eg. TheMaster-Demo128.png
alt: text describing the image
team: name of the team that created the production
authors: members of the team
year: year that the production was created
type: type of the production (whatever text you like)
platform: name of the target platform
download: filename of the SSD or DSD disk image in /content/ for this production
source: link to the source code for this production (if any)
pouet: link to the pouet page for this production (if any)
video: link to a video for this production (if any)


---
PUT YOUR MARKDOWN FORMATTED POST CONTENT HERE
```

### Archives (eg. demos or cool stuff created by any other teams that we want to archive on the site)
To add a new archive:
 - Place an image and a disk image file (SSD or DSD) for the archive in `/content/`
 - Create a .md file in the `_posts/archives/` folder with the correct filename convention, and the content you wish to publish
 - Apply the correct category and tags, and the new production will automatically be listed in the right place when the site is rebuilt

Post Filename format:
 - `yyyy-mm-dd-team-prodname.md`

```txt
---
layout: prods_post
category: [posts, archives]
tags: whatever tags you like

... (same properties as productions above)
```


### Compos 
To add a new competition:
 - Place an image for the archive in `/content/`
 - Create a .md file in the `_posts/compos/` folder with the correct filename convention, and the content you wish to publish
 - Apply the correct category and tags, and the new compo will automatically be listed in the right place when the site is rebuilt

Post Filename format:
 - `yyyy-mm-dd-compo-name.md`

```txt
---
layout: prods_post
category: [posts, compos]
tags: whatever tags you like
compo_id: The id of this compo. Tag any posts with this ID so that they are filtered as submissions.

year: year the competition started
title: name of the competition
img: filename of the image in /content/ for this competition (no need for any path)
platform: suitable formats for the competition
---
PUT YOUR MARKDOWN FORMATTED POST CONTENT HERE

```

Credits
=======
The Jekyll theme for the Bitshifters site was based on [Freelancer bootstrap theme ](http://startbootstrap.com/templates/freelancer/)
