#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#

def get_no_duplicate_pai_list(paizu):
    result = []
    for pai in paizu:
        if pai not in result:
            result.append(pai)
    for p in result:
        paizu.remove(p)
    return result


def put_pai_back(lst, paizu):
    paizu.extend(lst)
    paizu.sort()


def find_shunzi(paizu):
    shunzi = []
    skip = 0
    shunzi_num = 0
    for index in range(0, len(paizu) - 2):
        if skip:
            skip -= 1
            continue
        if paizu[index + 2] - paizu[index + 1] == 1 and paizu[index + 1] - \
                paizu[index] == 1:
            shunzi.extend(paizu[index: index + 3])
            skip = 2
    for pai in shunzi:
        paizu.remove(pai)
    shunzi_num = len(shunzi) / 3
    if not shunzi_num:
        return 0
    if len(paizu) >= 3:
        shunzi_num += find_shunzi(paizu)
    return shunzi_num


def find_all_shunzi(paizu):
    no_duplicate_list = get_no_duplicate_pai_list(paizu)
    while find_shunzi(no_duplicate_list):
        put_pai_back(no_duplicate_list, paizu)
        no_duplicate_list = get_no_duplicate_pai_list(paizu)
    put_pai_back(no_duplicate_list, paizu)
    print paizu

def find_multi_pai(paizu, _type):
    result = []
    skip = 0
    num = (2 if _type == 'duizi' else 3)
    for index in range(0, len(paizu)):
        if paizu.count(paizu[index]) == num:
            result = paizu[index: index + num - 1]


if __name__ == '__main__':
    paizu = [1, 1, 1, 1, 2, 2, 2, 2, 3, 4, 4, 5, 6, 7]
    find_all_shunzi(paizu)
    # tri_list = find_tri(paizu)
    # duizi_list = find_duizi(paizu)
    # print 'shunzi:{},tri:{},duizi:{},paizu:{}'.format(shunzi_list, tri_list,
    #                                                   duizi_list, paizu)
