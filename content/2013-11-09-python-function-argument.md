Date: 2013-11-09 21:00  
Modified: 2014-01-10 12:29
title: Python function *arg and **kwarg  
Author: Chen-Yen Lai
Category: Python

In python, we can use this special syntax to pass a number of arguments to a function. There are two kinds of them, choose the  best fit for your code.

### The single asterisk form (`*arg`)

This form gives you to pass several variables into a function. This following example pass one formal argument `x=1.0` and three non-keyword arguments, `2.0,3.0,4.0`,

	:::python Non keyword argument - arg.py
    def func(x,*args):  
        print x  
        for arg in args:
            print "non-keyword argument:", arg
        print "first argument is:", args[0]

    func(1.0,2.0,3.0,4.0)  

Run this code is going to give you the result

	:::python
    1.0
    non-keyword argument: 2.0
    non-keyword argument: 3.0
    non-keyword argument: 4.0
    first argument is: 2.0

### The double asterisk form (`**kwarg`)

The keyword argument needs you to specify the keyword. Look the following example.

	:::python keyword argument - kwarg.py
    def func(x,**kwargs):
        print "x = ", x
        a = 1.0
        b = 1.0
        c = 1.0
        for key in kwargs:
            if key == 'c':
                c = kwargs[key]
            elif key == "b":
                b = kwargs[key]
            elif key == "a":
                a = kwargs[key]
        print "keyword argument: a=",a,"b=",b,"c=",c

    print "Test-1"
    func(1.0)
    print "\nTest-2"
    func(2.0,a=3.0)
    print "\nTest-3"
    func(3.0,b=4.0,c=5.0)
    print "\nTest-4"
    func(4.0,a=3.0,b=4.0,c=5.0)

I set the default value as `a=1.0 b=1.0` and `c=1.0`.  
We then run it to test.  

Result shows

	:::python
    Test-1
    x = 1.0
    keyword argument: a= 1.0 b= 1.0 c= 1.0

    Test-2
    x = 2.0
    keyword argument: a= 3.0 b= 1.0 c= 1.0

    Test-3
    x = 3.0
    keyword argument: a= 1.0 b= 4.0 c= 5.0

    Test-4
    x = 4.0
    keyword argument: a= 3.0 b= 4.0 c= 5.0

Enjoy powerful python.

### The order of arguments - Python Syntax

Be careful when you call a function, we always put non-keyword argument in front of keyword argument. 