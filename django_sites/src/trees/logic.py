#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from trees.models import TreeNode


def create_node(node_list):
    for node in node_list:
        tree_node = TreeNode(parent_id=node['parent_id'],
                             key=node['key'])
        tree_node.save()


def main():
    node_list = [
        {'parent_id': 0, 'key': 'a'},
        {'parent_id': 1, 'key': 'b'},
        {'parent_id': 1, 'key': 'c'},
        {'parent_id': 2, 'key': 'd'}
    ]
    create_node(node_list)

class Node(object):

    def __init__(self, _id, pid, key):
        self.id = _id
        self.pid = pid
        self.key = key

        self.children = []

    def print_key(self):
        print(self.key)

def create_tree(tree_node_dict):
    for _id, node in tree_node_dict.items():
        if node.pid == 0:
            continue
        tree_node_dict[node.pid].children.append(node)

def fetch_tree_nodes() -> dict:
    tree_nodes = TreeNode.objects.all()
    return {node.id: Node(node.id, node.parent_id, node.key)
            for node in tree_nodes}

def client():
    d = fetch_tree_nodes()
    create_tree(d)
    for key, value in d.items():
        print(key)
        print(value.children)

if __name__ == '__main__':
    client()
