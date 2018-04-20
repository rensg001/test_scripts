#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import copy

class ProtoType(object):
    def __init__(self, a, obj):
        self._a = a
        self._obj = obj

    def clone(self):
        return copy.copy(self)

    def deep_clone(self):
        return copy.deepcopy(self)

    def show_a(self):
        print(id(self._a))

    def show_obj(self):
        print(id(self._obj))

def main():
    pt = ProtoType(1, [])
    pt.show_obj()
    pt.show_a()
    pt2 = pt.clone()
    pt2.show_obj()
    pt2.show_a()
    pt3 = pt.deep_clone()
    pt3.show_obj()
    pt3.show_a()

if __name__ == '__main__':
    main()
