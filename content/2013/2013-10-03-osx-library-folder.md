Date: 2013-10-03 21:00  
Title: OSX Library folder
Author: Chen-Yen Lai
Category: OSX


The `~/Library/` folder is default hidden in your finder and other place in OSX. If you are terminal user, there is no trouble for you to access it. However, you can let it appear in Finder by just several simple tips.

#### `Go to` function

When you are in Finder, simply just use `Command-Shift-g`. There will be a pop-up on your finder, we then type `~/Library/`, the library folder will be opened.

#### In the `Go` menu

On the top menu, you can see there is a `Go` menu. You can not see the `Library` button until you hit `Alt`.

#### Keyboard shortcut

You can set up the keyboard shortcut in the `Preference`.  
Go to `Preference`->`Keyboard`->`Shortcuts`. On the left, choose `App shortcuts`. After that, you can see the `+` button appears. Click it, it would show you

![image](https://dl.dropboxusercontent.com/u/165978/osx-library-folder-fig0.png)

Choose `Finder` in the `Application`, then type `Library` in the `Menu Title`. Finally, set up the shortcut you want in `Keyboard Shortcut`.  
Next time, you can use that shortcut to open `Library` folder just like we open the `Application` folder by `Command-Alt-A`.

#### Make it appear in other App

If you need to save file directly in to subfolder of library folder, you need to change the flag to make it no hidden!  
Open your terminal and type

	:::bash
    $ chflags nohidden ~/Library


, you then can see it at save menu in other applications.

If you want to go back to the hidden mode, just type[^1]

	:::bash
    $ chflags hidden ~/Library

in terminal.

[^1]: BSD command `chflags` -- change file flags.