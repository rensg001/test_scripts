#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#


def gen():
    n = 0
    while True:
        m = yield n
        if m is None:
            break
        n += m
    return n


def dele_gen():
    result = yield from gen()
    print("result:{}".format(result))
    yield result

if __name__ == '__main__':
    d_gen = dele_gen()
    next(d_gen)
    for i in range(5):
        d_gen.send(i)
    print("caller get result:{}".format(d_gen.send(None)))
    try:
        next(d_gen)
    except StopIteration:
        d_gen.close()