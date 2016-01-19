# -*- coding: utf-8 -*-
"""
binary_tree_paths.py
---------------------
给一棵二叉树，找出从根节点到叶子节点的所有路径。

样例:
给出下面这棵二叉树：
  1
 / \
2   3
 \
  5
所有根到叶子的路径为：
[
  "1->2->5",
  "1->3"
]
-------------
Created by <jimokanghanchao@gmail.com> on Jan 19,2016
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    using a loop to build the binary tree paths, not by recursion
    """
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        #the paths collection
        paths = []
        #the current path of root-to-one-leaf
        currentpath = ''
        #a node that have both of left and right children, push the node and the current path of it into stack
        branchpaths_and_nodes = []
        while True:
            if root != None:
                #update the current path
                if currentpath == '':
                    currentpath = str(root.val)
                else:
                    currentpath = currentpath + '->' + str(root.val)
                if root.left != None or root.right != None:
                    if root.left != None and root.right != None:
                        #pop the stack if a leaf node founded
                        branchpaths_and_nodes.append((root,currentpath))
                    #left first, if left child not exists, right child as root node
                    root = root.left if root.left != None else root.right
                    continue
                else:
                    #a leaf node founded, add a new path into paths collection
                    paths.append(currentpath)
                    if len(branchpaths_and_nodes) >= 1:
                        #pop the latest node which have two children and the path of it
                        node, currentpath = branchpaths_and_nodes.pop()
                        #use the right child of the node as root node, the left child has been visited
                        root = node.right
                        continue
                    else:
                        return paths
            else:
                return paths

class RecursiveSolution:
    """
    using recursive method to build the binary tree paths
    """
    def __init__(self):
        #the paths collection
        self.paths = []
        #the current path of root-to-one-leaf
        self.currentpath = ''
        #a node that have both of left child and right child, must push the current path of the node into stack
        self.branchpaths = []
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        if root != None:
            if self.currentpath == '':
                self.currentpath = str(root.val)
            else:
                self.currentpath = self.currentpath + '->' + str(root.val)
            if root.left != None or root.right != None:
                if root.left != None and root.right != None:
                    #in order to pop the stack if a leaf node founded
                    self.branchpaths.append(self.currentpath)
                if root.left != None:
                    #always left first
                    self.binaryTreePaths(root.left)
                if root.right != None:
                    self.binaryTreePaths(root.right)
            #a leaf node founded
            else:
                #add a new path into paths collection
                self.paths.append(self.currentpath)
                if len(self.branchpaths) >= 1:
                    #pop the path of latest node which have two children
                    self.currentpath = self.branchpaths.pop()
                #return the paths when a leaf node founded
                return self.paths
            #end of recursion
            return self.paths
        else:
            return self.paths

def main():
  tree = TreeNode(1)
  tree.left = TreeNode(2)
  tree.right = TreeNode(3)
  tree.left.right = TreeNode(5)
  solution = RecursiveSolution()
  print '递归方法生成所有根到叶子的路径：',solution.binaryTreePaths(tree)
  solution = Solution()
  print '循环方法生成所有根到叶子的路径：',solution.binaryTreePaths(tree)

if __name__ == '__main__':
  main()