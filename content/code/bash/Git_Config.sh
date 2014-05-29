#!/bin/bash  
git config --global user.name "chenyenlai"
git config --global user.email "chengyanlai@gmail.com"
git config --global color.ui true
git config --global color.log auto
git config --global core.editor "mate -w"
git config --global alias.st status
git config --global alias.ci commit
git config --global alias.co checkout
git config --global alias.bh branch
git config --global alias.last 'log -1 HEAD'
git config --global alias.slog 'log --oneline -20'
git config --global alias.clni 'clean -i'
git config --global commit.template path/to/the/file/gitmessage.txt
git config --global core.excludesfile path/to/the/file/gitignore_global
git config --global push.default simple
git config --global merge.tool opendiff
