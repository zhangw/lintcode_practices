# -*- coding: utf-8 -*-
"""
minimum_depth_of_bin_tree.py
----------------------------
二叉树的最小深度
给定一个二叉树，找出其最小深度。
二叉树的最小深度为根节点到最近叶子节点的距离。
样例:
给出一棵如下的二叉树:
      1
     / \ 
    2   3
       / \
      4   5
这个二叉树的最小深度为 2
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 04,2016
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    use preorder traversal to calculate minimum depth of binary tree.
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def minDepth(self, root):
        if root != None:
            depth = 0
            mindepth = None
            rightnodes = []
            while True:
                if root.left != None or root.right != None:
                    depth += 1
                    if root.left != None and root.right != None:
                        #save the depth of current node and its right child node
                        rightnodes.append((depth, root.right))
                    #traverse left children
                    root = root.left if root.left != None else root.right
                else:
                    depth += 1
                    if mindepth == None:
                        mindepth = depth
                    elif depth < mindepth:
                        mindepth = depth
                    #traverse right children
                    if len(rightnodes) > 0:
                        depth, root = rightnodes.pop()
                    else:
                        break
            return mindepth
        else:
            return 0

def main():
    pass

if __name__ == '__main__':
    main()

