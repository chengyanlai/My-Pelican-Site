Date: 2013-12-13 15:50:01
Title: 繁體中文slug
Author: Chen-Yen Lai
Category: Python
Tags: Static Site Builder
Slug: easy-way-to-convert-character-to-slug
Summary: 轉換中文字體成unicode編碼拼音
Status: draft

通常，網頁連結不支持中文字體，所以我們需要拼音跟unicode的協助來把我們的中文標題換成unicode或是ascii！  
這裡介紹如何使用`Python`來做這件事情！

## 安裝 django and uuslug

這個方法需要用到兩個套件，都可以由`pip`來安裝

    :::bash
    $ pip install django
    $ pip install uuslug

在我們的程式裡，我們直接用`uuslug`的function - `slugify`!

{% include_code python/new_post.py %}