Title: My Octopress and Heroku - 3
Date: 2013-11-17 15:14
Author: Chen-Yen Lai
Category: misc
Tags: WebsiteBuilder  
Summary: 從Blogspot匯入Octopress!

## Blogspot Posts 到 Octopress
如果你已經有Blog，而且並不想要放棄你的心血結晶，在GitHub可以找到一個Ruby程式，基本上你只需要匯出你的posts！  
Run一行Command，複製匯出的檔案到octopress的`_post`檔案夾！你就可成功從Blogspot轉換到octopress！  

到你的Blogspot control center，匯出你的Blog！  
![Blogspot Control](https://dl.dropboxusercontent.com/u/165978/blog-to-octopress/fig0.png)  

下載這個 [Ruby程式](https://gist.github.com/chengyanlai/7492278).  
把匯出的`blog-xxxx-xx-xx.xml`檔案跟剛剛下載的`Ruby`程式放在一起，開啟你的Terminal，執行  

    :::bash
    $ ruby import.rb blog-xxxx-xx-xx.xml
    
基本上它會產生兩個資料夾，`_post` and `_draft`！你可以在`_post`裡面找到你所有的published posts，`_draft`裡面找到你所有的unpublished posts！所有的檔案都是`html`  
所有你要做的就是把`_post`跟`_draft`裡面的files拷貝到你的`path/to/octopress/source/_post` and `path/to/octopress/source/_draft`  
最後就是

	:::bash
    $ rake generate
    $ rake preview

就大功告成了！
