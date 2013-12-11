Date: 2013-10-01 21:00  
title: "Fusion Drive on OSX" 
Author: Chen-Yen Lai
Category: OSX
Tags: Fusion


## Setup Fusion Drive
First of all, you will need to reinstall os and everything you needed, so start backup your files.
You need to boot from a flash drive or the installation dmg, then you need to go to the terminal to do the following.

### Check your storage
First to check your storage and find their Volume ID by entering the following in terminal

	:::bash
    $ diskutil list

### Create CoreStorage
After obtaining the two storage you want to setup as a single Fusion drive, you can use the command
	:::bash
    $ diskutil cs create {drivename} {driveIDs}

. This command can be broken down into

1. diskutil - the command-line version of Disk Utility.
2. cs -  Core Storage in short, which is necessary for Fusion.
3. creat - creates a Core Storage group.
4. drivername -  this is the name of the drive and how you want it to appear in Disk Utility (not the Finder – that comes later). You can call it whatever you want!
5. driveIDs - these are the drive IDs of the drives you want as part of your Fusion, separated by a space.

### Format CoreStorage
Then, we need to obtain the {groupString} to format the Fusion drive. Using the following command

	:::bash
    $ diskutil cs list

. Once you obtain it, we can start to format it by

	:::bash
    $ diskutil cs createVolume {groupString} jhfs+ {volumeName} {size}

, where

1. jhfs+ – the format of the drive. This is Apple Extended Format (journaled), which is recommended for drives with an OS installed on it.
2. volumeName - the actual name of the volume, how it should appear underneath the icon.
3. size - this is the size of the volume.

### Reboot and Install OSX!

## Split up Fusion drive
First step, you need to find the unique identifier for the logical volume group. You can do this by typing

	:::bash
    $ diskutil coreStorage list

, so you might see following

![corelist](https://dl.dropboxusercontent.com/u/165978/osx-fusion-drive-fig0.png)

. In the above example, you can find the ID is 7B6B........
If you want to split this logic volume, type the following

	:::bash
    $ diskutil coreStorage delete {Logic Volume ID}

After destroying the CoreStorage Logical Volume Group, system formats the drives for you as normal OSX Extended (Journaled) volumes (JHFS+). This is the normal type of volume that you would install OS X on or use to format an external drive.