---
title: 个人博客风格指南（备忘）
date: 2025-12-30
category: coding
tags:
  - 'style guide'
---

## 博客文件名：`yyyy-mm-dd-category-blog_slug.md`

- 日期（yyyy-mm-dd）
- 分类（category）：一篇博客只有一个分类，且为英文，全部小写
- Blog slug（blog_slug）:一般全部小写，用下划线连接。如果有些词习惯大小，则可大写，例如：AMO_note

## YAML metadata

示例如下：

```yaml
---
title: 个人博客风格指南
date: yyyy-mm-dd
category: category
tags:
  - 'first tag'
  - 'second tag'
  - tag3
---
```

- title：无要求。
- date: yyyy-mm-dd 应与文件名一致。
- category: 唯一，应与文件名一致。
- tags:
  - 中英文皆可。
  - 写成 [YAML](https://zh.wikipedia.org/zh-cn/YAML) 清单的形式。
  - 空，一个，或多个。
  - 用空格连接，不用下划线。如果有空格则加单引号引起来，没有空格不必加单引号。
  - 一般全部小写，如果有些词习惯大小，则可大写。
  - 一些形成系列的博客，可以用同一个 tag 组织，如“总结”系列。

## 正文内容

参考 [markdownlint](https://github.com/DavidAnson/markdownlint/tree/v0.40.0?tab=readme-ov-file)

内容超过两页，可考虑生成目录。

中英混输且中文为主：

- 使用中文标点。
- 英文或阿拉伯数字与汉字用空格隔开。
- 中文括号中为英文，不加空格。如：风格指南（Style guide）。
- 逗号，句号等后为英文，按英文的习惯，加一个空格。
