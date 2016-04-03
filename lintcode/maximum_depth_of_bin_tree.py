# -*- coding: utf-8 -*-
"""
maximum_depth_of_bin_tree.py
----------------------------
二叉树的最大深度 
给定一个二叉树，找出其最大深度。
二叉树的深度为根节点到最远叶子节点的距离。

样例:
给出一棵如下的二叉树:
  1
 / \ 
2   3
   / \
  4   5
这个二叉树的最大深度为3.
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 28,2016
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    use preorder traversal to calculate maximum depth of binary tree.
    @param root: The root of binary tree.
    @return: An integer
    """ 
    def maxDepth(self, root):
        #the right child nodes of whose parents both have left and right children
        rightnodes = []
        #the maximum depth of the tree
        max_depth = 0
        #the depth of current node
        depth = 0
        if root == None:
            return 0
        else:
            while True:
                #increase the depth value
                depth += 1
                if root.left != None or root.right != None:
                    if root.left != None and root.right != None:
                        #save the depth of current node and the its right child node
                        rightnodes.append((depth,root.right))
                    #firstly left child, if not exists, right child as root node
                    root = root.left if root.left != None else root.right
                #leaf node
                else:
                    #update the maximum depth value
                    max_depth = max(depth,max_depth)
                    if len(rightnodes) >= 1:
                        #right child node as root node
                        depth, root = rightnodes.pop()
                    else:
                        #all the nodes have been visited
                        return max_depth

def main():
    pass    

if __name__ == '__main__':
    main()

