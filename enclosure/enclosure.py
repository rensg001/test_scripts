#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

def a():
    lst = [lambda : 2 * i for i in range(0, 10)]
    return [i() for i in lst]

if __name__ == '__main__':
    print(a())