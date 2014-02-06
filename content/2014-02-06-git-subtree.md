Date: 2014-02-06 07:38:29
Title: Git subtree for dummy
Author: Chen-Yen Lai
Category: Git
Slug: git-subtree-split
Summary: Basic git-subtree-split usage

## Submodule

If you have some sub-programs like plotting tool, which only produces visuals of data generated from original main program, 
you can make it as a submodule.

Just make a folder and initialize, then add your remote (you need to create it somewhere like GitHub)

    :::bash
    $ mkdir foo
    $ cd foo
    $ git init
    $ git remote add origin git@github.com:my-user/new-project.git

This is nothing like create a project.   
However, you would need to do one more step for the submodule. Go back to the project folder and add it. 

    :::bash
    $ cd ..
    $ git submodule add git@github.com:my-user/new-project.git foo

Here, `git` is going to create a file named `.gitmodules` indicates `path` and `url`.

## Split Super-project

Let's say if you didn't do it as a submodule at the beginning, then you want to separate it from super-project.  
We would need `git subtree split`!

Go into the project root

    :::bash
    $ cd path-to-my-project

Create a branch which only contains commits of 'foo'

    :::bash
    $ git subtree split --prefix=foo --branch=foo-only

Remove folder 'foo' from the super-project

    :::bash
    $ git rm -rf ./foo

Create a git repo for new folder 'foo' (you need to create a repo somewhere like GitHub). In project folder,

    :::bash
    $ mkdir foo
    $ pushd foo
    $ git init
    $ git remote add origin git@github.com:my-user/new-project.git
    $ git pull ../ foo-only
    $ git push origin -u master
    $ popd

Add folder as a git submodule to super-project

    :::bash
    $ git submodule add git@github.com:my-user/new-project.git foo
    
For detailed documentation (man page), please read [git-subtree.txt](https://github.com/apenwarr/git-subtree/blob/master/git-subtree.txt).  
Thanks to [this post at StackOverflow](http://stackoverflow.com/a/1307969/3011790).
