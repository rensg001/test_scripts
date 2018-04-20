#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import copy
import json
import logging
import time

from collections import defaultdict

from django.core.management import BaseCommand
from django.forms import model_to_dict

from trees.models import TreeNode

logger = logging.getLogger(__name__)


def create_tree(root, tree_nodes):
    assert isinstance(root, dict)

    root['children'] = []
    children = filter(lambda n: n.parent_key == root['key'], tree_nodes)
    for child in children:
        child = model_to_dict(child)
        root.setdefault('children', []).append(child)
        if child['is_leaf']:
            continue
        create_tree(child, tree_nodes)

    root['children'] = sorted(root['children'],
                              key=lambda item: item['id'],
                              reverse=True)
class MakeTree(object):
    def __init__(self):
        tree_nodes = TreeNode.objects.all()
        self.tree_nodes = [model_to_dict(node) for node in tree_nodes]

        self.unsorted_children_map = {}
        self.node_dict = {}

    def make_tree(self, tree_nodes):
        # 在原树节点集合中生成树
        self.node_dict = {node['key']: node for node in tree_nodes}
        for node in tree_nodes:
            if not node['parent_key']:
                continue

            parent = self.node_dict[node['parent_key']]
            children = parent.setdefault('children', [])
            children.append(node)
            self.unsorted_children_map[parent['key']] = children

    def _sort_children(self, node_dict):
        for key, children in self.unsorted_children_map.items():
            children = sorted(children,
                              key=lambda child: child['id'],
                              reverse=True)
            node_dict[key]['children'] = children

    @property
    def trees(self):
        self.make_tree(self.tree_nodes)
        self._sort_children(self.node_dict)
        roots = list(filter(lambda tree_node: not tree_node['parent_key'],
                            self.tree_nodes))
        return roots


class MakeTree2(MakeTree):

    def __init__(self):
        self.tree = {}
        super(MakeTree2, self).__init__()

    def make_tree(self, root):
        # 产生副作用
        children = [tree_node for tree_node in self.tree_nodes
                    if tree_node['parent_key'] == root['key']]
        for child in children:
            root.setdefault('children', {}).update({child['key']: child})
            self.make_tree(child)

    @property
    def get_tree(self):
        roots = [tree_node for tree_node in self.tree_nodes
                 if not tree_node['parent_key']]
        for root in roots:
            self.make_tree(root)
        return roots




class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # root_list = []

        # start_time = time.time()
        # roots = filter(lambda tree_node: not tree_node.parent_key, tree_nodes)
        # print("--- %s seconds ---" % (time.time() - start_time))

        # for root in roots:
        #     root = model_to_dict(root)
        #     create_tree(root, tree_nodes)
        #     root_list.append(root)
            # logger.info(json.dumps(root_list))
        # roots = MakeTree().trees
        roots = MakeTree2().get_tree
        logger.info(json.dumps(roots))
