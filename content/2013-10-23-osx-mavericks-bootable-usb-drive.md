Date: 2013-10-23 21:00  
Title: OSX Mavericks bootable USB drive
Author: Chen-Yen Lai
Category: OSX

I don't know if you like to do the clean install, but it is always good to have the bootable usb drive. If you have multiple MACs, you can take advantage for not downloading the 5.5G Mavericaks installer.

OSX Marvericks provides a very easy way to create the bootable USB drive.

	:::ruby

### Format your USB drive
Make sure you have a USB which is larger than 5.5G(I use 8G), and format it into Mac OS Extended (Journaled).
Here I just name it `Untitled`. Earaed it!
![osx-mavericks-bootable-usb-drive-fig0.png](https://dl.dropboxusercontent.com/u/165978/osx-mavericks-bootable-usb-drive-fig0.png)

### Make the drive
Once it is done, and you have the Mavericks installer in you `Application` folder.
Type the following in the terminal

    :::bash
	sudo /Applications/Install\ OS\ X\ Mavericks.app/Contents/Resources/createinstallmedia --volume /Volumes/Untitled --applicationpath /Applications/Install\ OS\ X\ Mavericks.app --nointeraction

You will see this on your terminal

![osx-mavericks-bootable-usb-drive-fig1.png](https://dl.dropboxusercontent.com/u/165978/osx-mavericks-bootable-usb-drive-fig1.png)

It takes about 20 mins to complete, be patient.

Read more at this [site](http://www.gottabemobile.com/2013/10/22/perform-clean-install-os-x-mavericks/#iA8WYhaBRRRieeGl.99).