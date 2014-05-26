Date: 2014-5-21 11:00  
Title: Python Virtual Environment
Author: Chen-Yen Lai
Category: Python
Slug: python-virtualenv
Summary: 如何根據 Project 管理 Python 使用環境

如何根據 Project 管理 Python 使用環境?

## Homebrew python

### 使用 virtualenv 以及 virtualenvwrapper

確定你已經安裝了這兩個套件，如果還沒

    ::bash
    $ pip install virtualenv
    $ pip install virtualenvwrapper

`virtualenvwrapper` 並不一定是需要的，但是可以讓管理env更省時省力！  

#### 設定 virtualenvwrapper

加入下列兩行在 `.bash_profile`

	::bash
	export WORKON_HOME=~/.virtualenvs
	source /usr/local/bin/virtualenvwrapper.sh

第一行裡的 `.virtualenvs` 是管理所有環境的資料夾，必須手動建立！資料夾名稱可以自行決定。  
設定好了之後，請重新開一個視窗或是 `source ~/.bash_profile`.

#### 建立環境

我們這裡介紹的是有使用 virtualenvwrapper 的方法！

    ::bash
    $ mkvirtualenv {ENV name}

以上指令就建立了一個 virtual environment，而且會被啟用！  

切換環境也很簡單，如下：

    ::bash
    $ workon
    # all available ENV names will be shown here
    $ workon {ENV name}
    (ENV name) $ which python
    # Now, you know this is an enviroment python!
    # something like /Users/.../.virtualenvs/{ENV name}/bin/python

這樣建立的環境只會有你原本的 python，其他的 site packages 並不會進來！  
如果你想要建立一個擁有所以已經安裝的 site packages 的環境，只需要加上 `--system-site-packages` 像是

    ::bash
    $ mkvirtualenv --system-site-packages {ENV name}

就可以了！  

如果是要建立不同 python 版本的環境，我們也可以指定，首先，你要知道那個 python 版本的路徑，我們用 python3 為例  

    ::bash
    # find python3 path
    $ which python3
    # Here is the path!
    $ mkvirtualenv -p {the path shown above} {ENV name}

這樣就可以建立 python3 專屬的環境了！  

在建立環境的同時，通常(!) `pip` 跟 `setuptools` 也會一起被安裝，所以我們可以根據不同用途的環境安裝不同用途的 packages!  
舉一個簡單的例子，像是用 `pelican` 建立blog.

    ::bash
    # 建立一個叫 pelican 的環境，我們不需要任何 site-packages
    $ mkvirtualenv pelican
    # 安裝需要的元件
    (pelican) $ pip install pelican Markdown
    # 現在我們就可以開始使用！
    (pelican) $ mkdir to/the/path/of/your/site
    (pelican) $ cd to/the/path/of/your/site
    (pelican) $ setvirtualenvproject
    
最後一步非常方便，這樣可以建立專屬環境的初始路徑(cwd)，一切換到那個環境就會在那個路徑下！  

    ::bash
    (pelican) $ pelican-quickstart

這樣就可以開始建立一個 pelican site!

#### 移除環境

在有 virtualenvwrapper 的情形下非常簡單，只需要

    ::bash
    $ rmvirtualenv {ENV name}

Nice!

## Anaconda

Anaconda 提供了 `conda create` 的指令來建立環境，基本用法如下：

    ::bash
    $ conda create -n py27 python=2.7 anaconda

`-n {name}` 這裡的 name 是環境的名字，上面的例子名字就是 `py27`，後面接上了 python version `2.7` 以及package_spec `anaconda`.

To be continued......

## Canopy

To be continued......
