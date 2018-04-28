# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import


def exchange(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp


def quickly_sort(lst, left, right):
    if left > right:
        return
    l, r = left, right
    key = lst[left]
    while left < right:
        while left < right and lst[right] > key:
            right -= 1
        lst[left] = lst[right]
        while left < right and lst[left] <= key:
            left += 1
        lst[right] = lst[left]
    lst[left] = key
    quickly_sort(lst, l, left - 1)
    quickly_sort(lst, right + 1, r)


if __name__ == '__main__':
    data = [4, 2, 7, 1, 6, 9, 3, 0, 2]
    quickly_sort(data, 0, len(data) - 1)
    print(data)
