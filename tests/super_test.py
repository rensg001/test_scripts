#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
class A(object):
    def foo(self, x):
        print("x is {}".format(x))


class B(A):
    def __new__(cls, name):
        name = "A:" + name
        return super(B, cls).__new__(cls)

    def __init__(self, name):
        self._name = name

    def foo(self, x):
        print("I add some addional logic.")
        super(B, self).foo(x)

    @property
    def name(self):
        return self._name

class mytuple(tuple):
    def __new__(cls, name):
        obj = super(mytuple, cls).__new__(cls)
        obj.name = name
        return obj

    def __init__(self, name):
        self._name = name
        super(mytuple, self).__init__()


if __name__ == "__main__":
    b = B("b")
    b.foo(1)
    print(b.name)
    a = ()
    c = mytuple("fdfs")
    print(c._name)