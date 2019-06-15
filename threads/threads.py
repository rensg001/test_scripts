#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

import threading
import time


class MyThread(threading.Thread):
    def __init__(self, func, *args, **kwargs):
        super(MyThread, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.result = self.func(*self.args, **self.kwargs)

    def get_result(self):
        threading.Thread.join(self)
        try:
            return self.result
        except:
            return None

def foo(a):
    time.sleep(2)
    print(a)
    return a + 1

if __name__ == '__main__':
    mt1 = MyThread(foo, 10)
    mt2 = MyThread(foo, 11)
    mt3 = MyThread(foo, 12)
    mt4 = MyThread(foo, 13)
    mt5 = MyThread(foo, 14)
    mt1.start()
    mt2.start()
    mt3.start()
    mt4.start()
    mt5.start()
    for mt in [mt1, mt2, mt3, mt4, mt5]:
        print(mt.get_result())
