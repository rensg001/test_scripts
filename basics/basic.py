#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

class Test(object):

    def foo(self, x):
        print('Test %s' % x)


class SubTest(Test):

    def call_foo(self):
        super(SubTest, self).foo('aaaa')

    def foo(self, x):
        print('subtest %s' % x)

if __name__ == '__main__':
    st = SubTest()
    st.call_foo()