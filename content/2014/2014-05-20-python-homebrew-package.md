Date: 2014-5-20 11:00  
Title: Python package for OSX - Update!
Author: Chen-Yen Lai
Category: Python
Slug: homebrew-python
Summary: 在 OSX 上使用 Homebrew 安裝 Python - Updated!

在 OSX 上使用 Homebrew 安裝 Python - Updated!  
安裝順序是重要的！如果發現有問題，請重新安裝。

## Set up some taps and update Homebrew

確保 Homebrew 運作正常，加入安裝 Python 需要的 repo。 並且更新 Homebrew！

    ::bash
    $ brew doctor
    # fix the error shown here
    $ brew tap homebrew/science # a lot of cool formulae for scientific tools
    $ brew tap homebrew/python # numpy, scipy
    $ brew update && brew upgrade

## Install Homebrew python

安裝 Homebrew 的 python。

    ::bash
    $ brew install python
    
## Check the python you are using

確認你的 python 是 Homebrew 的，不是系統提供的.

    ::bash
    $ which python
    # should be /usr/local/bin/python
    $ echo $PATH
    
`/usr/local/bin` should be in front of `/usr/bin`!  
若是系統提供的 python，必須修改 `~/.bash_profile` 裡面的 `PATH`，像是加入`export PATH="/usr/local/bin:$PATH"`.

## Install PIL, imagemagick, graphviz and other

Image generating stuff (qt is nice for viewing).  
一些圖形界面的 package。

    ::bash
    $ ln -s /usr/local/include/freetype2 /usr/local/include/freetype # seems freetype can't be found on some systems otherwise
    $ brew install pillow imagemagick graphviz
    $ brew install cairo --without-x
    $ brew install py2cairo # this will ask you to download xquartz and install it
    $ brew install qt pyqt  # qt 經常是其他元件的 requirement 像是 ipython

## Install nose and Virtual Environment

    ::bash
    $ pip install virtualenv virtualenvwrapper nose

請看[另一篇 post](|filename|./2014-05-21-python-virtualenv.md) 有關如何使用 virtualenv

## Install numpy and scipy

You can choose to use `openblas` or not. If so, run

    ::bash
    # This is optional!
    $ brew install openblas

then,

    ::bash
    # If you use openblas, please comment out below.
    $ brew install numpy # --with-openblas
    $ brew install scipy # --with-openblas

### Test the numpy and scipy installation

測試是否已經安裝完成...

    ::bash
    $ brew test numpy
    $ brew test scipy

### Some cool python libraries

一些科學用途的套件！

Python Data Analysis Library ([pandas](http://pandas.pydata.org)), especially time series stuff, and natural language toolkit ([nltk](http://www.nltk.org)).

    ::bash
    $ pip install pandas nltk
    
Math Plot Library ([matplotlib](http://matplotlib.org)) for plotting.

    ::bash
    $ brew install matplotlib

This is Symbolic python ([SymPy](http://sympy.org/en/index.html)).  
I hope this can beat Mathematica in the future!

    ::bash
    $ pip install sympy q

[IPython](http://ipython.org) and IPython notebook support.  
If you are a theoretical physicist, you must try ipython notebook!

    ::bash
    $ brew install zmq
    $ pip install ipython[zmq,qtconsole,notebook,test]
    
#### 使用 ipython notebook

在終端機下直接執行

    ::bash
    $ ipython notebook

就會開啟網頁版 ipython ，建議搭配 GitHub 跟 [nbviewer](http://nbviewer.ipython.org) 一起使用，可以快速上線筆記！
    
### HTML stuff

基本上我使用 python 使科學用途，比較少用網頁元件，以下只是參考。

Parsing,

    ::bash
    $ pip install html5lib cssselect pyquery lxml BeautifulSoup

, webapps / apis

    ::bash
    $ pip install Flask Django

, and semantic web stuff: `rdf` and `sparql`.

    ::bash
    $ pip install rdflib SPARQLWrapper
    
Run python scripts in the cloud

    ::bash
    $ pip install cloud
    

Those steps are referenced from [Jorn's blog](http://joernhees.de/blog/2014/02/25/scientific-python-on-mac-os-x-10-9-with-homebrew/).