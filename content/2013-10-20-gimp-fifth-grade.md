Date: 2013-10-20  
title: "小學生修圖 vol. 1" 
Author: Chen-Yen Lai
Category: Gimp

不知道大家是不是都有錢可以買Photoshop，或是總是可以找到ＯＯＸＸ。如果像我一樣怕死或是沒有時間去好好Google，可以試試看[Gimp](http://www.gimp.org)。唯一的缺點似乎是所謂「錄製某一些動作」然後「批次處理」沒有Photoshop來得方便！所以Gimp下只好學習如何使用python-fu以及script-fu。

今天跟大家分享一個讓照片變鮮豔的方法，當然如果你是清淡口味的話就請離開了！

概念很簡單，就是用圖層疊加的方法！其實四句話就說完了，還寫一篇blog？！

### Step-by-Step

+ 匯入照片。

![loadimage](https://dl.dropboxusercontent.com/u/165978/gimp-fifth-grade-1-fig0.png)

覺得已經很鮮豔了，那你趕快離開！

+ 拷貝圖層，`mode`改成`screen`，然後`opacity`調成50。(這是變亮的效果)

![screen](https://dl.dropboxusercontent.com/u/165978/gimp-fifth-grade-1-fig1.png)

+ 拷貝圖層，`mode`改成`overlay`。 (這是鮮豔的效果)

![overlay](https://dl.dropboxusercontent.com/u/165978/gimp-fifth-grade-1-fig2.png)

+ 針對`overlay`這個圖層，我們要來做`color mixer`！
	1. 到`Colors`選單裡面的`Components`選`Channel Mixer...`.
	2. 針對`Output channel: Red` - 把 `Red` 調成 150，把 `Green` 調成 -25，把 `Blue` 調成 -25。
	2. 針對`Output channel: Green` - 把 `Red` 調成 -25，把 `Green` 調成 150，把 `Blue` 調成 -25。
	2. 針對`Output channel: Blue` - 把 `Red` 調成 -25，把 `Green` 調成 -25，把 `Blue` 調成 150[^1]。

![colormix](https://dl.dropboxusercontent.com/u/165978/gimp-fifth-grade-1-fig3.png)

Preview就已經看到效果啦！

+ 到圖層的地方做`Merge Visible Layers...`

![mergelayer](https://dl.dropboxusercontent.com/u/165978/gimp-fifth-grade-1-fig4.png)

+ 輸出啦！

![sideside](https://dl.dropboxusercontent.com/u/165978/gimp-fifth-grade-1-fig5.png)

我應該不用說哪張是修改前吧！

### Python-fu

煩死了，我只要一個按鈕解決可以嗎？  
當然可以!

#### 下載安裝
+ 請到我的GitHub下載[這個python程式](https://github.com/chengyanlai/gimp_python/blob/master/My-Vivid.py)。  
+ 如果你也是OSX，恭喜你，請把這個檔案複製到`/Applications/Gimp.app/Contents/Resources/lib/gimp/2.0/plug-ins/`[^4]。然後到該路徑下執行`chmod 755 *py`。[^2]  
+ 重開`Gimp`，你應該可以在選單`Filters`->`ChenYen`看到`Color Mix`

#### 執行

+ 匯入照片。
+ 選擇`Filters`->`ChenYen`->`Color Mix`! 這不是廢話嗎？

![mypy](https://dl.dropboxusercontent.com/u/165978/gimp-fifth-grade-1-fig6.png)

+ 視窗出來了，有三個值可以設定
	1. Screen Opacity: 就是`screen layer`的`opacity`，預設是50。
	1. Overlay Opacity: 就是`overlay layer`的`opacity`，預設是100。
	3. Base Color: 就是在[Step-byStep](#step)裡面的150(/100)，預設是1.5(對應到150喔)。
+ 剩下的就自動處理啦！


[^1]: 是不是(150,-25,-25)不是重點，重點是加起來是100！
[^2]: 把它改成可以被執行。
[^4]: 你的python plugin路徑。