Title: Terminal
Date: 2014-10-10 09:00
slug: 7-termianl

# Bash/Zsh

## Very handy shell - [Oh-my-zsh](http://ohmyz.sh)
Useful plugins:
* gitfast
* rsync
* brew
* autopep8

## Terminal shortcut
* 'ctrl-a': Cursor to start of line  
* 'ctrl-e': Cursor to end of line  
* 'ctrl-u': Delete left of the cursor  
* 'ctrl-k': Delete right of the cursor  

## Batch rename

    ::bash
    $ rename 's/{old string}/{new string}/' {file pattern}

## multiple copy

    ::bash
    $ echo {folder pattern} | xargs -n 2 cp foo1.txt foo2.txt

, which will copy foo1.txt and foo2.txt to {folder pattern}

## wird search - ack
to give exact match

    ::bash
    $ ack -w {PATTERN}

## check linked library
on an exacutable or dynamical linked library
### OSX

    ::bash
    $ otool -L {target}

### Linux

    ::bash
    $ ldd {target}

## free linux cache

    ::bash
    $ sudo sh -c 'echo 1 >/proc/sys/vm/drop_caches'

, which might cost several minutes. Check result by

    ::bash
    $ free -g

# Grid Engine
## change queue

    ::bash
    $ qalter -q {quene.q} {job id}

## batch delete queue

    ::bash
    $ qdel `seq {from job id} {to job id}`

# Posts
[Multiple copy](|filename|../2014/2014-03-14-bash-tips.md)  
[SSH](|filename|../2013/2013-10-15-ssh-without-password.md)  
