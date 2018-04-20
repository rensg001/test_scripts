# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import absolute_import

import json

data = [
    {'id': 1, 'pid': 0, 'key': 'A'},
    {'id': 2, 'pid': 0, 'key': 'B'},
    {'id': 3, 'pid': 0, 'key': 'C'},
    {'id': 4, 'pid': 1, 'key': 'D'},
    {'id': 5, 'pid': 1, 'key': 'E'},
    {'id': 6, 'pid': 2, 'key': 'F'},
    {'id': 7, 'pid': 3, 'key': 'G'},
    {'id': 8, 'pid': 4, 'key': 'H'},
    {'id': 9, 'pid': 5, 'key': 'J'},
    {'id': 10, 'pid': 7, 'key': 'K'},
]

dictionary = {node['id']: node for node in data}


def create_tree(data):
    # out = {0: {'id': 0, 'pid': 0, 'key': 'root', 'sub': []}}
    tree = {}
    for p in data:
        # out.setdefault(p['pid'], {'sub': []})
        tree.setdefault(p['pid'], {'sub': []})
        tree.setdefault(p['id'], {'sub': []})
        tree[p['id']].update(p)
        tree[p['pid']]['sub'].append(tree[p['id']])

    return tree[0]['sub']


if __name__ == '__main__':
    tree = create_tree(data)
    print(json.dumps(tree))
