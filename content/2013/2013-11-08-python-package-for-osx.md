Date: 2013-11-08 21:00  
title: Python package for OSX
Author: Chen-Yen Lai
Category: Python
Summary: 在 OSX 上安裝 Python 的選擇

## First word, I am running OSX 10.8
There are several choices on the market, including the apple one within the os. In order to get all I need at once, I usually choose one from the following. Of cause, you can download the source code and install from it. The advantage of using those packages is that they are well maintained. Thus, the update and upgrade are easier!

### [Anaconda](http://www.continuum.io/)
I feel it is slower than EPD.

### [Enthough Python Distribution(EPD)](https://www.enthought.com/products/epd/)
It is now provided with the Canopy. I had hard time on installing it on a remote server which has no x-sesssion provided. Basically, I had hard time on setting up the environment on a remote server. If you know how, please leave a comment!  
I think both Anaconda and EPD provide the installer for Windows and Linux[^1].

### [Scipy Superpack](http://fonnesbeck.github.io/ScipySuperpack/)
This is the first thing I have tried and succeeded, easy and fast[^2]. 

### [Homebrew](http://brew.sh/)

UPDATED 05/20/2014: We have another post regarding [Homebrew Python installation](|filename|../2014/2014-05-20-python-homebrew-package.md).

The similar alternatives are [Macport](http://www.macports.org/) and [Fink](http://fink.thetis.ig42.org/). Th detail difference are compared by [Ted Wise](http://tedwise.com/2010/08/28/homebrew-vs-macports/)
Example(Homebrew):
Installation is super easy, it is depended on ruby and git.   
Please check the Software Installation section in [my another post]({{ root_url }}/blog/2013/10/24/osx-mavericks/) for installation.  
Xcode command-line tool(CLT) and XQartz(X11) are beforehand.  

#### Installation
Once installation success, check this before we start

	:::bash
    $ brew doctor


If everything looks good(no error message), let's get started.

Set the right path in `.bash_profile`.

	:::bash
    $ export PATH=/usr/local/bin:$PATH

`/usr/local/bin/` is the default path for everything installed from Homebrew[^3].

We need these prerequisites

	:::bash
    $ brew install gfortran python

Tap those to add formula

	:::bash
    $ brew tap homebrew/science
    $ brew tap samueljohn/python
    $ brew tap michaelwimmer/kwant

The last one is not need unless you want it like me.

Install Numpy, Scipy

	:::bash
    $ pip install nose
    $ brew install numpy scipy matplotlib

You may need other packages (use `pip`), just follow the message from Homebrew!  
It is not as difficult as you think.

#### Update and Upgrade
Using the following command,

	:::bash
    $ brew update

, and you will see, for example

![update](https://dl.dropboxusercontent.com/u/165978/python-package-for-osx-fig0.png) 

. If the update fails, you need to reset it by `git` command. The following command might help

	:::bash
    $ cd /usr/local/
    $ git reset --hard FETCH_HEAD

Let's assume the update is good. If you find anything you want to upgrade on the update list, just run

	:::bash
    $ brew upgrade {package name}

As easy as it!

## Last word, Python conflict!
I have installed the Anaconda, EPD Canopy, and Homebrew python on my '09 Macbook Pro. I am not using anaconda because I feel slow. I am running the Homebrew version on my Terminal, and EPD Canopy on TextMate. So far, I didn't discover any conflict, or I am too stupid to find out. All my python codes can be executed well on both TextMate or on terminal command `python -i whatever.py`. 


[^2]: I haven't try to use the Scipy Superpack for a while, but I think it is still working.
[^1]: I have installed both Anaconda and EPD on Debian already. I never use Windows, sorry.
[^3]: The actual files are in the folder called `Cellar`, but a symbolic link is created in the `/usr/local/bin/`.