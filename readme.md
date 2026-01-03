# My Blog: [https://zqw.ink](https://zqw.ink)

## Introduction

Generate by [Pelican](https://getpelican.com/).

Use Plugins:

- [sitemap](https://github.com/pelican-plugins/sitemap)

Use package:

- [jinja2](https://github.com/pallets/jinja/)

- [markdown-it-py](https://github.com/executablebooks/markdown-it-py)

- [nbformat](https://github.com/jupyter/nbformat)

## Acknowledge

[MathJax](https://www.mathjax.org/)

[highlight.js](https://highlightjs.org/)

## Usage

Parameters:

- `-r`: auto reloading
- `-l`: listen
- `-s`: with setting file

Publish with publish configure:

```shell
pelican -s publishconf.py
```

## TODO

- [ ] Fix the bug that toc in html render by markdown will jump to a location that the title will under the nav.
