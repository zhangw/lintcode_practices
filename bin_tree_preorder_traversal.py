# -*- coding: utf-8 -*-
"""
bin_tree_preorder_traversal.py
------------------------------
给出一棵二叉树，返回其节点值的前序遍历。

样例:
给出一棵二叉树 {1,#,2,3}
1
 \
  2
 /
3
返回[1,2,3]
----------
Created by <jimokanghanchao@gmail.com> on Jan 20,2016
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        #the nodes collection
        nodes = []
        #the nodes which have both of left and right children
        branchnodes = []
        while True:
            if root != None:
                #firstly add the node into collection, whatever leaf node or not
                nodes.append(root.val)
                if root.left != None and root.right != None:
                    #push the node which have both of left and right children into stack
                    branchnodes.append(root)
                if root.left != None or root.right != None:
                    #left child first, if left child not exists, right child as root node
                    root = root.left if root.left != None else root.right
                    continue
                else:
                    #the leaf node founded
                    if len(branchnodes) >= 1:
                        #pop the stack to get the parent node which have two children,
                        #and use the right child as root node
                        root = branchnodes.pop().right
                        continue
                    else:
                        return nodes
            else:
                return nodes

class RecursiveSolution:
    """
    using recursive method to implement preorder traversal
    """
    def __init__(self):
        #the nodes collection
        self.nodes = []

    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        if root != None:
            #firstly add the node into collection, whatever leaf node or not
            self.nodes.append(root.val)
            if root.left != None:
                #left child node as root node
                self.preorderTraversal(root.left)
            if root.right != None:
                #right child node as root node
                self.preorderTraversal(root.right)
        return self.nodes

def main():
    tree = TreeNode(1)
    tree.left = TreeNode(4)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    solution = RecursiveSolution()
    print solution.preorderTraversal(tree)
    solution = Solution()
    print solution.preorderTraversal(tree)

if __name__ == '__main__':
    main()