#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

def a():
    lst = [lambda : 2 * i for i in range(0, 10)]
    return [i() for i in lst]

def outer():
    n = []
    for i in range(0, 10):
        def inner():
            n.append(i)
            return n
    return inner



if __name__ == '__main__':
    l = []
    l.append(outer())
    l.append(outer())
    l.append(outer())
    a = outer()
    a()
    a()
    print(a())
    # print([id(func()) for func in l])