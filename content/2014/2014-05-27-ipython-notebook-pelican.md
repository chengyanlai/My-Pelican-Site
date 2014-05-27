Date: 2014-5-27 10:00  
Title: IPython Notebook and Blogging
Author: Chen-Yen Lai
Category: Python
Tags: WebsiteBuilder
Slug: ipython-notebook-pelican
Summary: 建立 Pelican Blog 發佈 IPython notebook
Status: draft

## 安裝 Pelican

這裡的步驟是基於有使用 `virtualenv` 跟 `virtualenvwrapper` 的人。有關虛擬環境，請詳閱[這裡](|filename|./2014-05-21-python-virtualenv.md)

    ::bash
    # 建立一個叫 pelican 的環境，我們不需要任何 site-packages
    $ mkvirtualenv pelican
    # 安裝需要的元件
    (pelican) $ pip install pelican Markdown
    # 現在我們就可以開始使用！
    (pelican) $ mkdir to/the/path/of/your/site
    (pelican) $ cd to/the/path/of/your/site
    (pelican) $ setvirtualenvproject

### Pelican Site 初始化

快速建立一個 blog，Pelican 提供了以下的指令...

    ::bash
    (pelican) $ pelican-quickstart

執行之後，他會問一些有關這個 blog 的訊息，就據實以答吧！錯了也不會怎樣，了不起再重來就好了XD  
其實這些之後也都可以在調整，基本上是 generate 出 `peliconconf.py` 還有 `publishconf.py` 。  
我是選擇使用 `Makefile` ， 你也可以選擇使用 `Fabric`......  
現在，你就已經有了基本 blog 的 elements 了～
可以先預覽一下

    ::bash
    (pelican) $ make html
    (pelican) $ make devserver

開啟瀏覽器連到 `localhost:8000` ，這就是剛剛建立的 blog！

    ::bash
    (pelican) $ ./develop_server.sh stop

就可以停止 localhost。

### Basic Post and Page

To be updated......

## 安裝 Pelican Theme

其實說安裝，也只不過把它下載下來而已......  
請一併參閱[這裡](https://github.com/getpelican/pelican-themes)  
想要看預覽，可以連[這裡](http://pelican-themes-gallery.place.org)  

    ::bash
    (pelican) $ git clone --recursive https://github.com/getpelican/pelican-themes ~/pelican-themes

使用 Theme 比需要修改 `pelicanconf.py`

    ::python
    THEME = "/to/path/of/pelican-themes/theme-name"

這樣就可以來看一下成果了

    ::bash
    (pelican) $ make html
    (pelican) $ make devserver

## 安裝 Pelican Plugin

其實說安裝，也只不過把它下載下來而已......(again)  
請一併參閱[這裡](https://github.com/getpelican/pelican-plugins)

    ::bash
    (pelican) $ git clone https://github.com/getpelican/pelican-plugins

### Configure Plugin

要讓 plugin 順利運作，必須修改 `pelicanconf.py`

    ::python
    # For Plugins
    PLUGIN_PATH = './plugins' # This is the path to your plugins!
    # Then we list all plugins we need.
    PLUGINS = ['liquid_tags.img', 'liquid_tags.video',
               'liquid_tags.youtube', 'liquid_tags.include_code',
               'liquid_tags.notebook','render_math','googleplus_comments']

基本上，這裡用了很多 `liquid tag` plugins ， 還有 `render_math` 是用來顯示 $\LaTeX$.

### Publish IPython notebook by Liquid Tag

Configure Notebook path in `pelicanconf.py`

    ::python
    STATIC_PATHS = ['images', 'code', 'pdf']
    NOTEBOOK_DIR = 'code/python/notebooks'

然後把要發佈的 notebook 存在 `to/the/path/of/your/site/content/code/python/notebooks` 
或是你設定的 `NOTEBOOK_DIR` 就可以了～  

以下就是使用 `liquid tag` 嵌入 IPython notebook 的實例......  
只需要加上 `{ % notebook blogging-with-the-ipython-notebook-example.ipynb %}` 在 post 裡面就可以了！  
請注意上面 `{ %` 的空格必需要拿掉！  

{% notebook blogging-with-the-ipython-notebook-example.ipynb %}
