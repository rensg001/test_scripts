#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


class MyContext(object):

    def __init__(self):
        print('init')
        # raise RuntimeError

    def __enter__(self):
        print('enter')
        # raise RuntimeError
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exit')
        print(exc_type, exc_val)

if __name__ == '__main__':
    with MyContext() as mc:
        print('body')
        raise RuntimeError