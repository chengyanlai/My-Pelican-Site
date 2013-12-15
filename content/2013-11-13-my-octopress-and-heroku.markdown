Title: My Octopress and Heroku - 1
Date: 2013-11-13 22:46
Author: Chen-Yen Lai
Category: misc  
Tags: Static Site Builder

## 前言
[Octopress](http://octopress.org) 是一套Blog Framework。也是這個 Blog 正在用的系統。  
可以參考名人xdite的[早期文章](http://blog.xdite.net/posts/2011/10/08/what-is-octopress)，市面上還有其他做static site的package，像是python做的[hyde](http://github.com/hyde/hyde)跟[Pelican](http://docs.getpelican.com/en/3.3.0/)，以及一樣是`Ruby`的[MIDDLEMAN](http://middlemanapp.com)    
這篇文章記錄我自己從零開始的設置，從clone octopress到把最基本的blog製造出來～

This entire process is not going to cost you more than 30 mins unless you meet trouble on `Ruby` dependencies.  

This is not going to hurt anything on your personal computer, why not give it a shot! Especially if you are already tired for Blogspot and WordPress,
you must try the Markdown blogging framework.  

If you are not ready for working with `git` and terminal, you can also try [Logdown](http://logdown.com) or [scriptogr.am](http://scriptogr.am/). 
Logdown is more convenient and support more syntax, but it is not free and/or flexible to edit. On the other hand, scriptogr.am is completely free,  editor for CSS and HTML provided, and sync to Dropbox (How awesome is that!). If one day, you decide to use Octopress. Moving from Logdown (or scriptogr.am) to octopress is super easy!

## Install ruby, gem, bundler
說實在我也是完全不懂`ruby`！但是這真的不難，只要你願意使用`Command line`。其實大部份的步驟跟octopress網頁上提供的相去不遠  
I follow the steps in the [Octopress](http://octopress.org/) page, and setup the deployment in [Heroku](http://www.heroku.com/). 
You can do the same.  

I fail to install octopress by using `rbenv` Ruby(`~/.rbenv/bin/ruby`) or Homebrew Ruby(`/usr/local/bin/ruby`). Eventually, 
I have to go back to the system Ruby(`/usr/bin/ruby`) to finish the job!  

If you never use `git`, you need to open your terminal and type

	:::bash
    $ git

It is going to check if you have this command installed. If not, Mavericks will ask you to install command line tool. 
Mavericks has system `ruby` and `gem` installed, so you only need to install `bundler`. Before we do so, we need 
to set up a `GEM_HOME`, which you have the right access.  
If you want to try

	:::bash
    $ gem install bundler

, this will fail because you do not have the right access to the system Library folder.  
Thus, you need to 

	:::bash
    $ sudo gem install bundler

The disadvantage is all these things are going to run under `root` permission. My way to resolve this is create a `.gems` folder under my `${HOME}` 
directory, and set the `GEM_HOME` there. I will do the following

	:::bash
    $ mkdir ~/.gems
    $ echo 'export GEM_HOME="$HOME/.gems"' >> ~/.bash_profile
    $ source ~/.bash_profile
    # Check ruby environment
    $ gem env

Now, you can check which command you are currently using, for me  

	:::bash
    $ which ruby
    /usr/bin/ruby
    $ which gem
    /usr/bin/gem
    $ which bundle
    /usr/bin/bundle

## Setup Your Static Blog Site
The sequence of my commands for successful installation is like  

	:::bash
    # Get the Octopress
    $ git clone git://github.com/imathis/octopress.git octopress
    $ cd octopress
    $ gem install bundler
    # If it shows the permission error, check your GEM_HOME
    # You need to have write permission
    $ bundle install
    $ rake install
    # Generate the website by using Jekyll
    $ rake generate
    # Preview your blog
    $ rake preview

Basically it is done. After the last command, you can open your browser link to `localhost:4000` to see it.
現在你建立了一個blog在你自己的電腦上，確切說是在一個folder裡面！  
下一步就是部署你的blog.

## Deploy Your Static Blog Site to Heroku - 1
第一種方法跟octopress網頁上的方法是一樣的！如果你沒有Heorku帳號，你必須先建立一個。  
You need to install [*Heroku toolkit*](https://toolbelt.heroku.com) before you proceed next. If you decide to deploy to other place, please skip this section and refer to others. This approach is provided in the octopress page. I think it is not a good one, so I provide another method to do it like deploy to GitHub pages at next section.  

	:::bash
    $ heroku create # Heroku is going to ask your account, and setup a ssh key.
    # Set heroku to be the default remote for push/fetch
    $ git config branch.master.remote heroku
    # Before you proceed next,
    # edit the .gitignore in the root of your repository and remove public.
    # Because that is the folder Heroku will need.
    $ git add .
    $ git commit -m 'first site updated'
    # Push files to remote(heroku) from local(master)
    $ git push heroku master

That's it, you just deployed to Heroku. You can go to your Heroku website and check it out!  

## Deploy Your Static Blog Site to Heroku - 2
概念很簡單，因為Heroku只需要知道用什麼語言(rack app)去部署你的網頁，以及你的網頁檔案放在`public`檔案夾裡！
The second method is credited to Joshua Wood[^3]. The idea is to copy entire `public` folder into a subfolder called `_heorku` (just like the `_deploy` for github page). Thus, all we need to push to Heroku is just this subfolder.  
The procedure is the following  

### Create the subfolder and put essentials
Let's say we use the subfolder name `_heroku`. In your octopuses root folder, do  

	:::bash
    $ mkdir _heroku
    $ cp Gemfile config.ru _heroku

. Then we need to modify the `Gemfile` to

    :::ruby
    source "http://rubygems.org"
    gem 'sinatra', '1.2.6'

, and this would be enough for Heroku to do deployment.

### Setup Heroku in the subfolder
Go to the subfolder and set up your Heroku app. You will need the [*Heroku toolkit*](https://toolbelt.heroku.com).  

	:::bash
    $ cd _heroku
    $ mkdir public # create this folder for later usage
    $ bundle install # in order to generate Gemfile.lock
    $ git init .
    $ git add .
    $ git commit -m "initial commit"
    $ heroku create
    $ git push heroku master

Now, you have your Heroku app setup. Before you proceed next, you can add an `public/index.html` to test the result.  

### Setup Rakefile to easily deploy  
This is the most difficult part. Open your `Rakefile` and change the following variables.

Tell Rakefile to find the function heroku to deploy

    :::ruby
    deploy_default = "heroku"

Pushing master(local) to heroku(remote)

    :::ruby
    deploy_branch  = "master"

Your website is located at `_heorku`

    :::ruby
    deploy_dir     = "_heroku"   # deploy directory (for Github pages deployment)

and add this function to the end of the Rakefile.

    :::ruby
    desc "deploy basic rack app to heroku"
    multitask :heroku do
        puts "## Deploying to Heroku "
        (Dir["#{deploy_dir}/public/*"]).each { |f| rm_rf(f) }
        system "cp -R #{public_dir}/* #{deploy_dir}/public"
        puts "\n## copying #{public_dir} to #{deploy_dir}/public"
        cd "#{deploy_dir}" do
            system "git add ."
            system "git add -u"
            puts "\n## Committing: Site updated at #{Time.now.utc}"
            message = "Site updated at #{Time.now.utc}"
            system "git commit -m '#{message}'"
            puts "\n## Pushing generated #{deploy_dir} website"
            system "git push heroku #{deploy_branch}"
            puts "\n## Heroku deploy complete"
        end
    end

Once it is all set, you can deploy just like people do to GihHub page

	:::bash
    $ rake generate # generate the site
    $ rake deploy # deploy to heroku

or just

	:::bash
    $ rake gen_deploy # This is rake integrate; rake generate; rake deploy

I think this is the better way to do it if you have backup in github because this only push the static site to Heroku. In such way that you can minimize the repo size on Heroku, and the deploy is faster than pushing entire repo to remote.  

## Custom Heroku App Name
If you do the deployment to Heroku like me, it will generate an App with random names. 
You can use your own domain name by following [the setting](https://devcenter.heroku.com/articles/custom-domains). 
You can actually just change the name for the app by doing[^1]  

	:::bash
    $ heroku apps:rename newname
    http://newname.heroku.com/ | git@heroku.com:newname.git
    Git remote heroku updated

This command will do everything for you, including the `git` remote address, so you can keep up with `git push heroku master` without any trouble. 
After this change, you can visit your site at `http://{newname}.herokuapp.com`.

## Backup Entire Repo to GitHub
If you want to keep your website a backup, you can do it on [GitHub](http://github.com/). The dark side is that will be opened to everyone!  
1. Go to the GitHub website and [Create a repo](https://help.github.com/articles/create-a-repo). Please do not add any file, including `README.mb`!  
2. Back to your terminal, and do the following

	:::bash
    # Add the GitHub repo to the remote list
    $ git remote add {Name Whatever You Want} git@github.com/username/{Name of repo on GitHub}.git
    # Suppose I name it github, and my repo name on GitHub is My_Octopress
    # You can check your git remote list
    $ git remote -v
    github	git@github.com:username/My_Octopress.git (fetch)
    github	git@github.com:username/My_Octopress.git (push)
    heroku	git@heroku.com:blogname.git (fetch)
    heroku	git@heroku.com:blogname.git (push)
    origin	git://github.com/imathis/octopress.git (fetch)
    origin	git://github.com/imathis/octopress.git (push)

The first two are the remote you just added. Second two are your website on Heroku. The last two you don't have the right to `push` are the source code of octopress. 

	:::bash
    # Push to GitHub remote(github) from local(master)
    $ git push github master

Here, you might learn about `git` a little more - Git supports multiple remotes, which is commonly used when forking a repo.

### Remember to backup regularly
This backup thing is not automatically, you need to push your master to the remote every time you want a backup. Just do

	:::bash
    # Back up to GitHub
    $ git push github master
    # Publish your blog
    $ git push heroku master #if you deploy by method 1
    $ rake gen_deploy #if you deploy by method 2

## Fix the preview blank page on Safari 7 of Mavericks
Somehow, WEBrick has problem with the safari, the issue is reported [here (closed)](https://github.com/imathis/octopress/issues/1395#issuecomment-28829065). Therefore, I decide to use `thin`. Here is how it woks.  
Add the gems to `Gemfile`, and install it.

	:::bash
    $ echo gem \"thin\" >> Gemfile
    $ bundle install

This would do all works for you. Now try

	:::bash
    $ rake preview

, and open `localhost:4000` on Safari!

[^1]: Official page [Here](https://devcenter.heroku.com/articles/renaming-apps).
[^3]: Please see original post [here](http://joshuawood.net/how-to-deploy-jekyll-slash-octopress-to-heroku/).