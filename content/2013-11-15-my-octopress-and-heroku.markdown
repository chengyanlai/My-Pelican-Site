Title: My Octopress and Heroku - 2
Date: 2013-11-15 21:00
Author: Chen-Yen Lai
Category: misc
Tags: Static Site Builder


Octopress的好處就是可以隨意的更改以及裝自己想要的plugin，或是你熟`Ruby`，你也可以自己寫plugin，剛設置好的blog其實已經很夠用，但是當你的blog漸漸壯大或是你要匯入你之前的文章(數百篇)，那加一些有用的plugin就變得很必要了！

### 建立中文 Categories Sidebar
`Octopress 2.1` 已經提供中文category，我們只要使用正確的url就可以了！  
有幾件事必須要先完成  

加入這個`ruby` plugin在你的 `plugins` 路徑下。

	:::ruby plugins/category_sidebar.rb mark:9
    module Jekyll
    class CategoryListTag < Liquid::Tag
    def render(context)
        html = ""
        categories = context.registers[:site].categories.keys
        categories.sort.each do |category|
            posts_in_category = context.registers[:site].categories[category].size
            category_dir = context.registers[:site].config['category_dir']
            html << "<li class='category'><a href='/#{category_dir}/#{category.to_url}/'>#{category} (#{posts_in_category})</a></li>\n"
            end
            html
            end
        end
    end

    Liquid::Template.register_tag('category_list', Jekyll::CategoryListTag)

加入下面這個 `categories.html` 在 `source/_includes/custom/asides/` 路徑下。

    :::html
    <section>
      <h1>Categories</h1>
      <ul id="categories">
        {% category_list %}
      </ul>
    </section>

把`custom/asides/categories.html`加入你的`_config.yml`，`rake generate`之後就可以顯示你的Categories Sidebar.

	:::ruby _config.yml mark:3
    # list each of the sidebar modules you want to include, in the order you want them to appear.
    # To add custom asides, create files in /source/_includes/custom/asides/ and add them to the list like 'custom/asides/custom_aside_name.html'
    default_asides: [custom/asides/about.html, asides/googleplus.html, custom/asides/flickr.html, asides/recent_posts.html, custom/asides/categories.html, asides/github.html, asides/delicious.html, asides/pinboard.html]

    # Each layout uses the default asides, but they can have their own asides instead. Simply uncomment the lines below

### 建立 Monthly Archives 
這是一個很經典的Blogspot有的功能，但是Octopress並沒有內建，因為不實用吧！
但是你想要他出現也是很簡單，有一個[現成的Plugin](https://github.com/rcmdnk/monthly-archive). 按照他的`README.md`，做就可以了！

### 建立 Author's archives for multiple authors
如果你要建立多人編輯的blog，而且想要可以區分出誰Post了哪些東西，這裡提供一個簡單的方法，我只是增加一個page，並沒有生產出一個folder放某個作者的Posts。我想，但是我不會寫Ruby。而且我在GitHub上找到的plugin沒有辦法使用!  
首先，建立作者的Page

	:::bash
    $ rake new_page[author_name/index.markdown]

按照下面的方法編輯剛剛產生的檔案，這是我的範例，請按照你的方式修改！至少你要改掉Front matter裡的`author` and `title`吧

    :::html
    ---
    layout: page
    title: Chen-Yen's Archives
    author: chengyanlai
    comments: false
    sharing: false
    footer: false
    ---
    <div id="blog-archives">
    	{% assign index = true %}
        {% for post in site.posts %}
            {% if post.author contains page.author %}
                {% capture this_year %}{{ post.date | date: "%Y" }}{% endcapture %}
                {% unless year == this_year %}
                {% assign year = this_year %}
                <h2>{{ year }}</h2>
                {% endunless %}
                {% assign content = post.content %}
                <article>
                    {% include archive_post.html %}
                </article>
            {% endif %}
        {% endfor %}

### Google web font and FontFace

#### Google Web Font
Octopress提供了一個可以簡易更改字體的方法，先到[Google Fonts](http://www.google.com/fonts)找你要的字體！

![find fonts](https://dl.dropboxusercontent.com/u/165978/blog-to-octopress/octopress_font-fig0.png)

選好之後選擇右下角的`Use`，接下來你看到這兩個有用的欄位

![font code](https://dl.dropboxusercontent.com/u/165978/blog-to-octopress/octopress_font-fig1.png)

把第三個欄位的`code`，就是那個 `<link href='.....'>` 加到你的`source/_includes/custom/head.html`  
然後第四個欄位的`code`，就是那個 `font-family: 'Doppio One', sans-serif`，就可以直接用在你的`sass/custom/_fonts.scss`  
像是

    :::bash
    $sans: 'Doppio One', sans-serif;

可以試試看各個欄位是什麼，畢竟這是Octopress的樂趣之一啊！

#### FontFace
事實上，Octopress也可以直接用FontFace，只要你提供正確的WebFont files!  
可以到這個網頁[Fonts Squirrel](http://www.fontsquirrel.com)找到你要的字體，他也提供`Webfont Generator`(在 Navigation bar上！)  
找到你要的字體，下載下來它會是`.ttf`，但這是不夠的！你必須要用他的`WEBFONT GENERATOR`，他會要求你上傳，然後做成一個package給你！(Sweet)，
這個package裡面只有某些檔案是必要的，而你必須在你的`source`裡面找到一個folder存放他們！  
我是建立了一個資料夾`source/assets/fontface`，以`New Circle`當例子的話，你需要把下面的檔案存進去`source/assets/fontface`

    :::bash
    new_cicle_gordita_italic-webfont.eot
    new_cicle_gordita_italic-webfont.svg
    new_cicle_gordita_italic-webfont.ttf
    new_cicle_gordita_italic-webfont.woff

另外一個需要用到的檔案就是`stylysheet.css`，首先更改裡面的內容，replace `url('` by `url('/assets/fontface/`，對路徑的修正！

{% include_code css/_typography.css %}

再來就是把這個檔案的內容加到`sass/custom/_typography.css`，如果你沒有這個檔案就建立他吧！  
現在你已經建立了自己的FontFace，使用的話就跟上面用WebFont一樣，更改`sass/custom/_fonts.scss`就可以了！
