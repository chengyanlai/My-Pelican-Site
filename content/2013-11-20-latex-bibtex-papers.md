Title: "LaTeX and BibTeX from Papers"
Date: 2013-11-21 16:14:35
Author: Chen-Yen Lai
Category: OSX
Tags: Latex

This is just convenient if you are using LaTeX and BibTex, also you have a lot of references.

You need to pay for the Paper app, it only has OSX and Windows(WTF!) version, sorry.

### Export bib from Papers
Papers allow you to export your entire library to single file 

![InPapers](https://dl.dropboxusercontent.com/u/165978/papers-bibtex-latex-fig0.png)

Next, you would need to put the file to the right PATH(It is painful in some way)

### Put bib to the right PATH
I know nothing about Windows for these days. For OSX, I am using the [MacTex](http://www.tug.org/mactex/) distribution, and I figure it out that the right path is 

	:::bash
    ${HOME}/Library/texmf/bibtex/bib/

If the folder is not there, please create it! Then copy your file to that path. Remember you need to update your bibtex file every time you update your library(I mean when you are going to use .bib).

### In LaTeX
So, the only thing you need to do in `.tex` file is

	:::bash
    \bibliographystyle{apsrev4-1}
    \bibliography{My_Ref}

. This is just an example. Because I am using RevTex, so the style is `apsrev4-1`. Second line means you have a file called and located at `${HOME}/Library/texmf/bibtex/bib/My_Ref.bib`

### Maintain the title
If You import an article which has some latex form, for example, name of compound like
`La_2CuO_4` or atoms `^{40}K` should appear like $La_2CuO_4\text{ or } ^{40}K$.  

This would, however, cause error message during compile of Bibtex. We need to manually edit it in 
the `Papers` to become `La$_2$CuO$_4$` or `$^{40}$K`. The small edit would ease the problem that you need to edit the `.bib` every time Bibtex compile.

#### Style list

You can choose different kinds of styles in reference. You need to find different `.bst` files for it. For each journal, they have corresponding style. For example, you can search `nature.bst` to find the the style for [Nature](http://nature.com).

Once you have the `bst` files you want, you need to put it into right path to let `latex` to find it. For OSX and MacTex installed, the path is located at

	:::bash
    ${HOME}/Library/texmf/bibtex/bst/


. Just copy all `.bst` files into it and `LaTeX` will find find it. All you need to do in `.tex` file is the following

	:::bash
    \bibliographystyle{nature}
