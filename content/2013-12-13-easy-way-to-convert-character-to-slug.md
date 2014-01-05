Date: 2013-12-13 15:50:01
Title: 繁體中文slug
Author: Chen-Yen Lai
Category: Python
Tags: WebsiteBuilder
Slug: easy-way-to-convert-character-to-slug
Summary: 轉換中文字體成unicode編碼拼音

通常，網頁連結不支持中文字體，所以我們需要拼音跟unicode的協助來把我們的中文標題換成unicode或是ascii！  
這裡介紹如何使用`Python`來做這件事情！

## 安裝 django and uuslug

這個方法需要用到兩個套件，都可以由`pip`來安裝

    :::bash
    $ pip install django
    $ pip install django-uuslug

在我們的程式裡，我們直接用`uuslug`的function - `slugify`!

#### 測試
用一個簡單的測試，就可以知道如何使用！雖然這樣的轉換有點不是很清楚，但是作為網頁的slug已經夠用了。

    :::python slugify-example.py
    from uuslug import slugify
    text = "中文"
    print(text)
    slug = slugify(text)
    print(slug)

得到結果

    :::bash
    $ python slugify-example.py 
    中文
    zhong-wen

## Create Pelican New Post
如果你跟我一樣用過octopress，那有一個功能就是利用`Rakefile`來建立新文章，

    :::bash
    $ rake new_post["Title"]

但是這是Pelican所沒有的，不過這很容易辦到，而且可以使用中文的title！像下面這樣的程式就可以了

{% include_code python/new_post.py %}