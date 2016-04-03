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

    def __repr__(self):
        #use preorder way to traverse the tree
        from bin_tree_preorder_traversal import RecursiveSolution
        recursivePreorderTraversal = RecursiveSolution()
        nodes = recursivePreorderTraversal.preorderTraversal(self)
        return "先序遍历:" + str(nodes)

class Solution:
    """
    use a loop to invert tree
    """
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def invertBinaryTree(self, root):
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
                    #end the loop
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
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(4)
    print "反转前二叉树=>\n", tree
    solution = Solution()
    solution.invertBinaryTree(tree)
    print "使用循环反转后的二叉树=>\n", tree
    solution = RecursiveSolution()
    solution.invertBinaryTree(tree)
    print "使用递归再次反转后的二叉树=>\n", tree

if __name__ == '__main__':
    main()