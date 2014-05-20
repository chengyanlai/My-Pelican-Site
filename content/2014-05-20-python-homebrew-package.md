Date: 2014-5-20 11:00  
Title: Python package for OSX - Update!
Author: Chen-Yen Lai
Category: Python
Slug: homebrew-python
Summary: 在 OSX 上使用 Homebrew 安裝 Python - Updated!

在 OSX 上使用 Homebrew 安裝 Python - Updated!  

The following steps are referenced from [Jorn's blog](http://joernhees.de/blog/2014/02/25/scientific-python-on-mac-os-x-10-9-with-homebrew/).

## Set up some taps and update Homebrew

    ::bash
    $ brew doctor
    # fix the error shown here
    $ brew tap homebrew/science # a lot of cool formulae for scientific tools
    $ brew tap homebrew/python # numpy, scipy
    $ brew update && brew upgrade

## Install Homebrew python

    ::bash
    $ brew install python
    
## Check the python you are using

To make sure that you are using the Homebrew python, not system python.

    ::bash
    $ which python
    # should be /usr/local/bin/python
    $ echo $PATH
    
`/usr/local/bin` should be in front of `/usr/bin`!

## Install PIL, imagemagick, graphviz and other

Image generating stuff (qt is nice for viewing).

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

    ::bash
    $ pip install sympy q

[IPython](http://ipython.org) and IPython notebook support.  
If you are a theoretical physicist, you must try ipython notebook!

    ::bash
    $ brew install zmq
    $ pip install ipython[zmq,qtconsole,notebook,test]

HTML stuff (parsing),

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