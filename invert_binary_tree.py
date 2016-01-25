# -*- coding: utf-8 -*-
"""
invert_binary_tree.py
---------------------
翻转一颗二叉树

样例:
  1         1
 / \       / \
2   3  => 3   2
   /       \
  4         4

挑战:
不适用递归
---------
Created by <jimokanghanchao@gmail.com> on Jan 25,2016
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    use a loop to invert tree
    """
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        #save the root node of tree
        tree = root
        #the right child nodes
        rightnodes = []
        while root != None:
            if root.left != None or root.right != None:
                root.left, root.right = root.right, root.left
                if root.left != None and root.right != None:
                    #push the right child nodes into stack
                    rightnodes.append(root.right)
                #firstly use left child node as root node, if not exists, right node as root node
                #continue the loop
                root = root.left if root.left != None else root.right
            else:
                if len(rightnodes) >= 1:
                    #pop the right child node from stack, and use it as root node
                    #continue the loop
                    root = rightnodes.pop()
                else:
                    #restore the root node of tree and end the loop
                    root = tree
                    break

class RecursiveSolution:
    """
    use recursive way to invert tree
    """
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
        if root != None:
            if root.left != None or root.right != None:
                root.left, root.right = root.right, root.left
                if root.left != None:
                    self.invertBinaryTree(root.left)
                if root.right != None:
                    self.invertBinaryTree(root.right)

def main():
    

if __name__ == '__main__':
    main()