---
title: 博客第三次改版
date: 2026-01-03
category: coding
tags:
  - blog
  - 'vibe coding'
---



本博客首版于 2018 年 9 月 7 日，用 [Hexo](https://hexo.io) 从 markdown 生成静态页面，发表了第一篇文章：[Typora 使用笔记](./2018-09-07-coding-typora_note.md)。

2022 年 4 月 16 日进行了[第一次改版](./2022-04-16-thinking-blog_evolution.md) 用 python 重写生成引擎和主题。

2024 年 10 月 24 日进行了[第二次改版](./2024-10-24-pelican_blog.md)后，采用了 Pelican 引擎。

在 2025 末，2026 初，这是对本博客进行了第三次改版。下面详细解释具体的更改。

目录：

- [更改主题](#更改主题)
- [增加风格指南](#增加风格指南)
- [优化博客内部的博文引用](#优化博客内部的博文引用)
- [改用 markdown-it-py 渲染 markdown](#改用-markdown-it-py-渲染-markdown)
- [更改导向栏](#更改导向栏)
- [增加 RSS 订阅](#增加-rss-订阅)
- [提高标签的用途](#提高标签的用途)
- [决定放弃 Org Mode 格式](#决定放弃-org-mode-格式)

-------------------------------------------------------------------------------

## 更改主题

在 AI 的帮助下，利用 vibe coding，去掉了 banner，增加明暗两套本色。更改后，感观更加“平凡”，易于阅读。

## 增加风格指南

为了格式统一，提升博客质量，便于迁移，增加了一系列[风格指南](./2025-12-30-coding-style_guide.md)。

## 优化博客内部的博文引用

之前的博客应该可用在不同博文之间引用，但没有统一的格式，我也没有用过。现在在 markdown 格式的博文中统一格式为 `[comment](./xxxx-xx-xx-xx-xxxx.md)` 的格式。在渲染时用正则替换，将相对引用替换为网址绝对引用。这样能保证在本地的 markdown 编辑器中，能很好的预览和跳转，生成 html 后也能支持链接跳转。

此外，增加不同博文之间的引用，可以提升关联性，以此提升写作体验和读者体验，也利于搜索引擎的索引。

## 改用 markdown-it-py 渲染 markdown

之前用的 [Python-Markdown](https://python-markdown.github.io/)，并用 [markdown_math_escape](https://github.com/sgryjp/markdown_math_escape) 处理数学公式。但是 Python-Markdown 与一些现代的 markdown 格式（[比如用两个空格区分不同级别的列表](https://github.com/DavidAnson/markdownlint/blob/v0.40.0/doc/md007.md)）兼容性不好，因此换用支持更灵活的 [CommonMark spec](https://spec.commonmark.org/) 的 [markdown-it-py](https://github.com/executablebooks/markdown-it-py)。

其实这些都无所谓，重要的是博客的内容。而目前 markdown-it-py 刚好实现了我的需要。

## 更改导向栏

一些博客文章的质量一般，但是也不应该删除，至少做为记录。所以改版后的导航栏分成以下几部分

- Home：主页，显示本博客的引言。
- Physics：物理，或者科研相关的内容。是筛选过质量过后的列表。
- Blog：生活相关的内容。是筛选过质量过后的列表。
- Coding：编程相关的内容。是筛选过质量过后的列表。
- All：所有的博客文章列表。

## 增加 RSS 订阅

受到 [Wiwi](https://wiwi.blog/blog/you-should-use-rss) 的影响，我现在自己也重新用起了 RSS，所以本站也应该支持 RSS 订阅。

## 提高标签的用途

一些成系列的内容，可以用一个标签连起来，放到首页展示。

## 决定放弃 Org Mode 格式

作为一名前 Emacs 用户，我曾经用 [Org Mode](https://orgmode.org/) 记录和组织一些内容。但是它和可移植性显然没有 markdown 强。
