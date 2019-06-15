#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


def access_list(lst):
    for item in lst:
        if isinstance(item, list):
            access_list(item)
        else:
            print(item)


lst = [1, 1, 2, [5, 2, [8, 2, [443]]]]


if __name__ == '__main__':
    access_list(lst)
