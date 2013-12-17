title: Git branch for dummy
date: 2013-10-18 15:13  
Author: Chen-Yen Lai
Category: Git
Tags: 
Slug: git-branch
Summary: Basic git-branch usage

俗話說：用Git不開brach乾脆不要用！
Opening a new branch in Git is like nothing, comparing to svn! It is a good habit to working on the branch other than `master` in order to keep `mater` intact.
## Check your current branch
Let's try it. To check what brach you currently have

    :::bash
    $ git branch
     * master

for now, we are still doing nothing!

## Open New brach
Using the following command, we can create a new branch and switch to it.

	:::bash
	$ git checkout -b newmodel

Above command is the shorthand of the two

	:::bash
	$ git branch newmodel
    $ git checkout newmodel

After that, we get

	:::bash
     Switched to a new branch 'newmodel'

What's left now?

	:::bash
	$ git branch

and see

    :::bash
     master
     * newmodel

That is what I am talking about.

## Fifth grade Merge back
If I just change README.md file

	:::bash
	$ git status

I will see

    :::bash
    On branch newmodel
    Changes not staged for commit:
    (use "git add <file>..." to update what will be committed)
    (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   README.md

    no changes added to commit (use "git add" and/or "git commit -a")

so let's add and commit it to the branch `mewmodel`

	:::bash
	$ git commit -a -m "Test branch function in README.md file."

Now, I go back to `master` branch and see what's going on

	:::bash
	$ git checkout master
    $ Switched to branch 'master'
    $ git status
     On branch master
     nothing to commit (working directory clean)

Oops, this is the idea and power of branch! Suppose you open a branch and create some bugs, you can just abandon it!(OMG)
If you want to keep the changes, I will need to merge it by

	:::bash
	$ git merge newmodel
     Updating 69007a5..6a71d52
     Fast-forward
     README | 2 ++
     1 file changed, 2 insertions(+)

Therefore,

	:::bash
	$ git st
     On branch master
     Your branch is ahead of 'origin/master' by 1 commit.
     nothing to commit (working directory clean)

## Delete branch
Once you finish with the modify and merge, than you can delete the branch by

	:::bash
	$ git branch -d newmodel

## Make it a remote branch and delete it

### You need to try this before you merge them!
So far, the branch is local on your computer and is not tracked with server.
If you want to add it to remote, you will need to do

	:::bash
	$ git push --set-upstream origin newmodel

Then you create a new branch on server!

## Do following with caution
Make sure what you are doing now. This is going to delete the branch on remote server.

	:::bash
	$ git push origin :newmodel

## Update branch from mater
If someone update the `master` branch and you want to that part of change in your own branch. You will need to update it. First, check your current branch

	:::bash
	$ git branch

If you are on the branch you want to update, simply try

	:::bash
	$ git rebase master

to get updated.