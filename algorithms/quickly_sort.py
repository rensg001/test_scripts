# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import


def exchange(data, i, j):
    tmp = data[i]
    data[i] = data[j]
    data[j] = tmp


def quickly_sort(data):
    if not data:
        return []
    i = 0
    j = len(data) - 1
    key = data[0]
    while i != j:
        while i < j:
            if data[j] < key:
                exchange(data, i, j)
                break
            j -= 1
        while i < j:
            if data[i] > key:
                exchange(data, i, j)
                break
            i += 1
    left = quickly_sort(data[:i])
    right = quickly_sort(data[i + 1:])
    sorted_data = []
    sorted_data.extend(left)
    sorted_data.append(key)
    sorted_data.extend(right)
    return sorted_data


if __name__ == '__main__':
    data = [4, 2, 7, 1, 6, 9, 3, 0, 2]
    data = quickly_sort(data)
    print(data)
