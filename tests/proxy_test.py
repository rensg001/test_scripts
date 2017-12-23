#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

class Proxy(object):

    def foo(self):
        print('foo')

    def __getattribute__(self, method_name):
        if method_name == 'foo':
            print('call before foo')
            return super(Proxy, self).__getattribute__(method_name)
        else:
            raise AttributeError()

if __name__ == '__main__':
    proxy = Proxy()

    proxy.foo()