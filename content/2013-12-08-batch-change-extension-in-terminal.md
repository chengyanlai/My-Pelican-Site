Title: Terminal下批次更改(副)檔名
Date: 2013-12-08 17:00
Author: Chen-Yen Sîn-gān Lai
Category: OSX
Status: draft

## 批次更改副檔名

    :::bash
    $ for file in *.html; do
    >   mv "$file" "`basename $file .html`.txt"
    > done

