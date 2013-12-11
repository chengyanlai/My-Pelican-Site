#!/bin/bash  
git config --global user.name "chengyanlai"
git config --global user.email "chengyanlai@gmail.com"
git config --global color.ui true
git config --global color.log auto
git config --global core.editor "mate -w"
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.last 'log -1 HEAD'
git config --global commit.template $HOME/Dropbox/File/git_files/gitmessage.txt
git config --global core.excludesfile $HOME/Dropbox/File/git_files/gitignore_global
git config --global push.default simple
