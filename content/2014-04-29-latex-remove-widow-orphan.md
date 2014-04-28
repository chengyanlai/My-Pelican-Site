Date: 2014-04-29 10:07:01
Title: How to prevent widows and orphans in LaTeX?
Author: Chen-Yen Lai
Category: OSX
Tags: Latex
Slug: latex-remove-widows-orphans
Summary: 如何移除 widows and orphans in LaTeX.

在某些文擋裡面，大家會避免某一句子落單在最後(widow)或是開頭(orphan)，在LaTeX裡面，我們可用下面的方式達到這個目的！

## 使用 widowpenalty

第一種方法是使用`\widowpenalty`以及`clubpenalty`，LaTeX的預設值是`150`，值越大，出現widow跟orphan的機會就越低。
在`\begin{document}`之前下下面的指令

    ::tex
    \widowpenalty500
    \clubpenalty500

如果想要完全移除可以把值設到10000。

