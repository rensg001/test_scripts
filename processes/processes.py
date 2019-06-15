#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

import time
import datetime

from multiprocessing import Manager, Pool

lst = Manager().list()

class A(object):

    @staticmethod
    def worker(x):
        return x * x

def foo(x):
    time.sleep(3)
    result = A.worker(x)
    lst.append(result)

pool = Pool(processes=3, maxtasksperchild=10)

print(datetime.datetime.now())
for i in range(10):
    print('add')
    p = pool.apply_async(foo, (i,))

pool.close()
pool.join()

print(lst)
print(datetime.datetime.now())