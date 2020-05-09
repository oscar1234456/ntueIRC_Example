#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  8 16:19:09 2020

@author: chentaiyuan
"""

class treeNode(object):
    data = 0
    leftNode = None
    rightNode = None
    def __init__(self,val):
        self.data = val
        self.leftNode = None
        self.rightNode = None
    def addLeftNode(self, node):
        self.leftNode = node
    def addRightNode(self, node):
        self.rightNode = node
    def viewTree(self,root):
        if root == None:
            return
        self.viewTree(root.leftNode)
        print(root.data)
        self.viewTree(root.rightNode)
        
    
root = treeNode(0)
node1 = treeNode(1)
node2 = treeNode(2)
node3 = treeNode(3)
node4 = treeNode(4)

#level2
root.addLeftNode(node1)
root.addRightNode(node2)

#level3
node1.addLeftNode(node3)
#level4
node3.addRightNode(node4)


root.viewTree(root)


'''
        root
     /            \
   node1        node2  
  /     \       /   \
 node3
  /  \  
     node4
'''
        
    
