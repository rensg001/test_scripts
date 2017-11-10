#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


def binary_search(a, n, key):
    font = 0
    back = n - 1
    while font <= back:
        mid = int((font + back) / 2)
        if a[mid] == key:
            return mid
        elif a[mid] > key:
            back = mid - 1
        else:
            font = mid + 1
    return -1


if __name__ == "__main__":
    l = [1, 2, 3, 4, 5, 6, 7]
    index = binary_search(l, len(l), 3)
    if index != -1:
        print("find. index is %s" % index)
    else:
        print("does not find.")
