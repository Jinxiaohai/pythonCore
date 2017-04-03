#!/usr/bin/env python
# _*_ coding: utf-8 _*_

"""Created by xiaohai"""


class Node(object):
    """Documentation for Node
    """
    def __init__( self, data = -1, lchild = None, rchild = None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild


class BinaryTree(object):
    """Documentation for Binary
    """
    def __init__(self):
        self.root = Node()

    def add(self, data):
        node = Node(data)
        if self.isEmpty():
            self.root = node
        else:
            tree_node = self.root
            queue = []
            queue.append(self.root)

            while queue:
                tree_node = queue.pop(0)
                if tree_node.lchild == Node:
                    tree_node.lchild = node
                    return
                elif tree_node.rchild == Node:
                    tree_node.rchild = node
                    return
                else:
                    queue.append(tree_node.lchild)
                    queue.append(tree_node.rchild)

    def pre_order(self, start):
        node = start
        if node == Node:
            return

        print node.data
        if node.lchild == Node and node.rchild == Node:
            return
        self.pre_order(node.lchild)
        self.pre_order(node.rchild)

    def pre_ordr_loop(self):
        if self.isEmpty():
            return

        stack = []
        node = self.root
        while node or stack:
            while node:
                print node.data
                stack.append(node)
                node = node.lchild
            if stack:
                node = stack.pop()
                node = node.rchild

    def in_order(self, start):
        node = start
        if node == None:
            return
        self.in_order(node.lchild)
        print node.data
        self.in_order(node, rchild)

    def in_order_loop(self):
        if self.isEmpty():
            return

        
        
    
