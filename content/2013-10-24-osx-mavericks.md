Date: 2013-10-24 21:00  
title: "OSX Mavericks Installation and Setup"  
Author: Chen-Yen Lai
Category: OSX

I run all the following in order to setup my OSX Mavericks. I prefer clean install!

Since I have remove my SuperDrive on my 2009 Macbook Pro, I have two harddrives. One is the SSD shipped with Apple, the other HD is installed on the slot of old SuperDrive. I would like to move my home folder to the 2nd HD.

The following setup is also worked if you try to do partition on single harddrive.

The details on how to do bootable USB drive and clean install, please refer to [my another post]({{ root_url }}/blog/2013/10/23/osx-mavericks-bootable-usb-drive/).



## Move Home Folder
After clean install, there is basically nothing new on home folder. You still have to move it, however, due to the reason that the Library folder.

### Copy the home folder to the other drive
Use the following command to check the drive

	:::bash
    $ ls /Volume/

![findvol](https://dl.dropboxusercontent.com/u/165978/osx-mavericks-from-scratch-fig0.png)

I install my Mavericks on the SSD called `Mavericks`. I want to move my home folder to HD call `HD`.  
Using the following command on terminal

	:::bash
    $ sudo ditto -v /Users/{Username}/ /Volumes/HD/Users/{Username}/

, where `ditto` is `cp` for OSX. It will copy entire home folder of {Username} to the `HD`. Your old home folder still intact.

### Relocate the home folder for system
Go to the `System Preference` => `Users & Groups`, then right click on {Username} => choose `Advanced Options`
![AdjustPath](https://dl.dropboxusercontent.com/u/165978/osx-mavericks-from-scratch-fig1.png)

. Click `Choose` on the `Home directory`, and choose the `/Volumes/HD/Users/{Username}/`. After this the system is going to restart because you change the home folder. Let's do it.

### Test the result
Open Terminal and type

	:::bash
    $ echo ${HOME}

, and it shows

![EchoHome](https://dl.dropboxusercontent.com/u/165978/osx-mavericks-from-scratch-fig2.png)

. It is DONE!

### Delete the old home folder
If you wish to delete the old home folder, you can go ahead an do it the following command

	:::bash
    $ cd /Users/
    $ sudo rm -rf {Username}

### Software Installation

Here is the software list I will definitely install on my OSX.
This is not a complete list, but other things are easy to find.

### Xcode
You can do this via `App Store`. After download, simply just install it. All I need is the command line tool(CLT), like `make`. 
To make sure the CLT is install, do the following

	:::bash
    $ xcode-select --install

### XQartz
Apple no longer provide the X11, but we still can get it by clicking the X11 in `Utilities` folder. It will guide you to the XQartz site.  
Download it and install it.

### [Homebrew](http://brew.sh)
I need some library like `boost` to run my code, and I plan to get it here. Also it provide the python, numpy, scipy, and matplotlib etc..  
To install, basically run

	:::bash
    $ ruby -e "$(curl -fsSL https://raw.github.com/mxcl/homebrew/go)"

, then you will be ready to brew.
Here is my list to do

1. `brew install wget` - the missing command in osx.
2. `brew install gfortran` - the fortran compiler.
3. `brew install boost` - the library used by fci.

The following is for python, numpy, scipy, matplotlib, and [kwant](http://kwant-project.org/)

Add `export PATH=/usr/local/bin:$PATH` in the `~/.bash_profile` to make sure system find the correct python.  
`brew install python` - the python maintained by homebrew.  
Tap the three followings

	:::bash
    $ brew tap homebrew/science
    $ brew tap samueljohn/python
    $ brew tap michaelwimmer/kwant

Install `numpy` and `scipy` first

	:::bash
    $ pip install nose
    $ brew install numpy scipy

Before going to `matplolib`, I need to do this due to the error message I got when installing `matplolib`

	:::bash
    $ pip-2.7 install python-dateutil
    $ pip-2.7 install pyparsing
    $ brew install matplotlib
    $ brew install kwant

Now, I have all I need so far from Homebrew.
The alternatives are [Macport](http://www.macports.org/) or [Fink](http://fink.thetis.ig42.org/), and the detail difference is provided by [Ted Wise](http://tedwise.com/2010/08/28/homebrew-vs-macports/)

### [Anaconda](https://store.continuum.io/cshop/anaconda/)
This is the alternative way to have python, numpy, scipy, and matplotlib. Usually they provide the academic license for free.

This installer is going to modify the `$PATH` in `.~/.bash_profile`. You can manipulate the `$PATH` to choose which python you want to use. To know that, you can type `which python` in terminal.

### [EPD Canopy](https://www.enthought.com/products/epd/)
It is something like Anaconda, but I feel EPD is faster. I have both of them on my computer, also the one from Homebrew.

### [MacTeX](http://www.tug.org/mactex/)
My compiler and editor, TeXShop, for tex files.

### [TextMate](http://macromates.com/)
A very useful text editor. Make sure that only v2.0 support Mavericks(by date 10/23). You can install the command-line version of it in the preference, so you can use it in terminal by typing `mate`. 
If you like to use it as git (or svn) editor, remember to use `mate -w`. I usually do the following in gitconfig

	:::bash
    $ git config --global core.editor "mate -w"

, so Textmate will open when I commit.
The python command can be set in the `Variables` of `Preferences`. For example, I want to run EPD Canopy on TextMate I will modify my PATH to `/path/to/Canopy/enviroment/User/bin:$PATH`.

### [DTerm](http://decimus.net/DTerm)
A very useful command line tool if you only need one command.

### [Go2Shell](https://itunes.apple.com/us/app/go2shell/id445770608?mt=12)
Another terminal program which open a new terminal window in current finder path.

### [Gimp](http://www.gimp.org/)
My photoshop.

### [Inkscape](http://inkscape.org)
Vector figures editor. You need X11 to run this.

### [Hugin](http://hugin.sourceforge.net)
A free software to do panorama.

### [Luminance HDR](http://qtpfsgui.sourceforge.net)
Just like its name.

### [Alfread](http://www.alfredapp.com/)
Get it from `App Store`. Very easy to use and not cost a lot of resources.

### [VLC](http://www.videolan.org/vlc/index.html)
How can anyone miss this wonderful player?

### [OpenOffice](http://www.openoffice.org/)
I need this to open xls files used in iLearn (Fuck!).

### [Mackfuse](https://code.google.com/p/macfuse/)
The only purpose is to read NTFS files.