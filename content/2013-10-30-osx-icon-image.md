Date: 2013-10-30 21:00  
title: OSX Folder Icon
Author: Chen-Yen Lai
Category: Gimp
Summary: 使用免費的 Gimp 自己製作 OSX 的 Folder Icon

Sometimes you just can't find the right folder icon for yourself. Why not make one from scratch?
	:::ruby
### Obtain the plain folder icon image

This is what we need. Click `Cmd-i` on a folder with bare folder icon.

![bare folder icon](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig0.png)

Click on the image of folder icon, then `Cmd-c` to copy it. Next, open `Preview`, and choose `New from Clipboard`

![new from clip board](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig1.png)

You will see an `Untitled` file with several folder images. Save it to somewhere you can find it.

### Gimp[^1]
Open that file by Gimp, choose `Page 3`, which is 512x512.

![512512](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig2.png)

This is the bare folder layer, and we need another layer which is the one we are going to add on the bare one. I just pick up any image I want. I provide a example in the following.

#### Text[^2]

1. Add the Text you want, and you will see a `text layer`.
2. Duplicate both `text layer` and `folder layer`.
![fig3](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig3.png)
3. Create a white layer, put it right after the color image layer, and merge down.
![fig4](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig4.png)
4. Blur it by choosing `Filters/Blur/Gaussian Blur`. Leave this layer here, it looks like useless but you will fail at step 8 if you didn't do it.
![fig5](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig5.png)
5. Hide all layers expect the `folder layer copy`. Right click on the original unblurred `text layer`, and choose `Alpha to Selection`. 
![fig6](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig6.png)
6. Invert the selection with `Selection/Invert,` and next right click `folder layer copy` and chose `Add Layer Mask` to add this inverted selection.
![fig7](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig7.png)
7. We need to make sure that the folder picture, not the mask is selected in the layers dialog. [Hint: Click on the folder image!]
8. Apply `Filters/Map/Bump map` to it. Set `azimuth` to around 90 (so light comes from top), and increase `ambient` as well to around 100. Once you are satisfied with the settings, click `OK`. [Hint:  If you see a black/white image here, you have not selected the correct layer or selected the channel instead of the actual layer.]
![fig8](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig8.png)
9. Make a second copy of the folder layer, we get `folder layer copy2`.
10. Make `folder layer copy2` visible behind our `folder layer copy`. You may have noticed that the folder shadow became darker. 
11. To remove the double shadow, use `Select Tool` to select the middle part of the folder icon that covers the `text layer` shape. Then select the `Select/Invert` menu item, and press `Delete`. The extra shadow should disappear. Remove the selection using `Select/None`.
![fig9](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig9.png)
12. Choose the `folder layer copy2`, and go to `Colors/Hue-Saturation`. Change both Lightness and Saturation to around -25. Adjust it until you are happy.
![fig10](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig10.png)
13. We should make a darker thin border in the inside area of the text. Here is How. Right click on the `text layer` select `Alpha to Selection`.
![fig11](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig11.png)
14. Create a new `transparent layer` between the `folder layer copy` and `folder layer copy2`. Go to `Select/Grow` with value 1 then `Select/Border` with value 3 and `feather border`. Then fill this new selection with color black by `Bucket Fill Tool`. Finally change this new `transparent layer` mode to `Overlay`.
![fig12](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig12.png)
![fig13](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig13.png)
![fig14](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig14.png)
15. Right click on any visible layer, and select `Merge Visible Layers`.
![fig15](https://dl.dropboxusercontent.com/u/165978/folder-icon-fig15.png)
16. Export it to `.png`!

#### Color/Black Image

If you want an image, instead of plain text, you can add the fig as a layer by just dragging the image file on the layer panel. Basically follow the same procedure and use the image layer not text layer.

### Img2icns[^3]
You can use this tool to convert any image file to an icon file.

[^1]: Download from [Here](http://gimp.org/).
[^2]: Reference from [Here](http://attila.tajti.info/creating-an-os-x-folder-icon-in-gimp).
[^3]: Download from [Here](http://www.img2icnsapp.com), free version is way enough.