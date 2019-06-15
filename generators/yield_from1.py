#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from collections import namedtuple
from inspect import getgeneratorstate

Result = namedtuple('Result', 'count average')


def averager():  # <1>
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # <2>
        if term is None:  # <3>
            break
        total += term
        count += 1
        average = total / count
    return Result(count=count, average=average)  # <4>


def grouper(results, key):  # <5>
    while True:  # <6>
        print('grouper: key:{}'.format(key))
        results[key] = yield from averager()  # <7>


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)  # <8>
        for value in values:
            group.send(value)
        group.send(None)  # <9>
        print('group type:{}'.format(getgeneratorstate(group)))
    report(results)


def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(";")
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group,
                                                    result.average, unit))


data = {
    'girls;kg':
        [40.9, 38.5, 44.3],
    'girls;m':
        [1.6, 1.51, 1.4],
    'boys;kg':
        [39.0, 40.8],
    'boys;m':
        [1.38, 1.5],
}
if __name__ == '__main__':
    main(data)