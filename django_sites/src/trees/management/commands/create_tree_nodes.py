#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
import logging

from django.core.management import BaseCommand

from trees.models import TreeNode

logger = logging.getLogger(__name__)

tree_nodes_data = [
    {'key': 'CEO', 'parent_key': '', 'name': '总经理', 'is_leaf': False},
    {'key': 'developDep', 'parent_key': 'CEO', 'name': '研发部经理', 'is_leaf': False},
    {'key': 'salesDep', 'parent_key': 'CEO', 'name': '销售部经理', 'is_leaf': False},
    {'key': 'financeDep', 'parent_key': 'CEO', 'name': '财务部经理', 'is_leaf': False},
    {'key': 'k', 'parent_key': 'CEO', 'name': '总经理秘书', 'is_leaf': True},
    {'key': 'a', 'parent_key': 'developDep', 'name': '员工A', 'is_leaf': True},
    {'key': 'b', 'parent_key': 'salesDep', 'name': '员工B', 'is_leaf': True},
]

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        logger.info('开始创建树节点')
        for node_data in tree_nodes_data:
            tree_node = TreeNode(**node_data)
            tree_node.save()
        logger.info('创建树节点结束')