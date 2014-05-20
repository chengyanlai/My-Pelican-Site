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
    $ brew install qt pyqt

## Install nose and VirtualENV

    ::bash
    $ pip install virtualenv nose

## Install numpy and scipy

You can choose to use `openblas` or not. If so, run

    ::bash
    $ brew install openblas

then,

    ::bash
    $ brew install numpy # --with-openblas
    $ brew install scipy # --with-openblas

### Test the numpy and scipy installation

    ::bash
    $ brew test numpy
    $ brew test scipy

### Some cool python libraries

PANDAS (Python Data Analysis Library), especially time series stuff, and NITK (natural language toolkit).

    ::bash
    $ pip install pandas nltk
    
Math Plot Library ([matplotlib](http://matplotlib.org)) for plotting.

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

就會開啟網頁版ipython.
    
### HTML stuff

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