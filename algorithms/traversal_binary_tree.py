#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author rsg
#
from collections import deque


class Node(object):

    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data


node_f = Node(data='f')
node_d = Node(data='d')
node_c = Node(data='c')
node_e = Node(left=node_f, data='e')
node_b = Node(left=node_d, right=node_e, data='b')
node_a = Node(left=node_b, right=node_c, data='a')
root = node_a


def inorder_traversal(root):
    stack = list()
    current = root
    done = 0

    while not done:
        if current:
            stack.append(current)
            current = current.left
        else:
            if stack:
                current = stack.pop()
                print(current.data)
                current = current.right
            else:
                done = 1

class Node2(object):

    def __init__(self, data):
        self.data = data
        self.sub = []

# node_f = Node2(data='f')
# node_d = Node2(data='d')
# node_c = Node2(data='c')
# node_e = Node2(data='e')
# node_e.sub.append(node_f)
# node_b = Node2(data='b')
# node_b.sub.append(node_d)
# node_b.sub.append(node_e)
# node_a = Node2(data='a')
# node_a.sub.append(node_b)
# node_a.sub.append(node_c)
# root = node_a

def depth_first_search(root):
    "Traverses through a tree depth-first by putting nodes on a stack"
    stack = deque()
    result_list = []
    stack.append(root)
    while len(stack) != 0:
        # Take off the node at the top of the stack, add it to the list
        temp_node = stack.pop()
        result_list.append(temp_node.data)
        # Add the children of that node to the top of the stack
        if temp_node.right is not None:
            stack.append(temp_node.right)
        if temp_node.left is not None:
            stack.append(temp_node.left)
    return result_list


if __name__ == '__main__':
    print(depth_first_search(root))