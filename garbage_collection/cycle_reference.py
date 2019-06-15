#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

import time
import weakref
import gc

class A(object):
    def __init__(self, class_B):
        self._b = class_B(self)

    def __del__(self):
        print('delete A')

class B(object):
    def __init__(self, obj_a):
        self._a = obj_a

    def __del__(self):
        print('delete B')

def foo():
    A(B)

if __name__ == '__main__':
    foo()
    while True:
        time.sleep(3)
        gc.collect()