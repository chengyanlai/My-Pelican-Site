Title: Git
Date: 2014-05-29 09:00
slug: 8-git

Here is my favorite Git command and some git related posts.  
Some prior setups needed, please see [Git Setup](|filename|../2013/2013-10-17-git-setup.markdown).

### Commands

Super basic ...

    ::bash
    $ git ci [--amend] # Don't amend published commit!
    $ git add [-u] [-A]
    $ git st # status
    $ git bh # branch
    $ git remote add <remote> <url>

Tags

    ::bash
    # To add
    $ git tag -a <tag name> {SHA}
    # To delete
    $ git tag -d <tag name>
    # To push all tags
    $ git push origin --tags
    # To list all tags
    $ git tag
    # pattern?
    $ git tag -l <pattern>
    # To check out tag into new branch
    $ git checkout -b <new_branch_name> <tag name>

Branch

    ::bash
    # create
    $ git branch <branch name>
    # or
    $ git co -b <branch name>
    # delete
    $ git branch -d <branch name>
    # update
    $ git rebase master
    # rename
    $ git branch -m <oldname> <newname>

Rebase/Merge tool

    ::bash
    $ git mergetool

Stash

    ::bash
    $ git stash
    $ git stash pop

See log

    ::bash
    $ git slog # git log --oneline -20
    # or
    $ git last # git log -1 HEAD
    # on specific file
    $ git log -p <filename>

Reset

    ::bash
    $ git reset --soft HEAD^{some number}
    $ git reset --hard HEAD # remove all changes

List files under version control

    ::bash
    $ git ls-files

### Posts
[Git Setup](|filename|../2013/2013-10-17-git-setup.markdown)  
[Git Branch](|filename|../2013/2013-10-18-git-branch.markdown)  
[Git Tag](|filename|../2013/2013-12-16-git-tag.md)  
[Git Stash](|filename|../2014/2014-01-06-git-stash.md)  
[Git Subtree](|filename|../2014/2014-02-06-git-subtree.md)  
