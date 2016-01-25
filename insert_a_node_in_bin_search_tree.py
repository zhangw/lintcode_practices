# -*- coding: utf-8 -*-
"""
insert_a_node_in_bin_search_tree.py
-----------------------------------
在二叉查找树中插入节点
给定一棵二叉查找树和一个新的树节点，将节点插入到树中。
你需要保证该树仍然是一棵二叉查找树。

样例:
给出如下一棵二叉查找树，在插入节点6之后这棵二叉查找树可以是这样的：

  2             2
 / \           / \
1   4   ==>   1   4
   /             / \ 
  3             3   6

挑战:
能否不使用递归？
-------------
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
    use a loop to implement the insertion.
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        tree = root
        if root != None and node != None:
            while True:
                if root.val == node.val:
                    #ignore this case
                    return tree
                elif root.val < node.val:
                    #insert on the right
                    if root.right == None:
                        root.right = node
                        return tree
                    else:
                        root = root.right
                else:
                    #insert on the left
                    if root.left == None:
                        root.left = node
                        return tree
                    else:
                        root = root.left
        else:
            if node == None:
                return tree
            else:
                return node

class RecursiveSolution:
    """
    use recursive way to implement the insertion.
    """
    def __init__(self):
        self.tree = None

    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """
    def insertNode(self, root, node):
        if root != None and node != None:
            if self.tree == None:
                self.tree = root
            if root.val == node.val:
                #ignore this case
                return self.tree
            elif root.val < node.val:
                if root.right == None:
                    root.right = node
                    return self.tree
                else:
                    #recursively with right child
                    return self.insertNode(root.right, node)
            else:
                if root.left == None:
                    root.left = node
                    return self.tree
                else:
                    #recursively with left child
                    return self.insertNode(root.left, node)
        else:
            if node == None:
                return root
            else:
                return node

def main():
    tree = TreeNode(2)
    tree.left = TreeNode(1)
    tree.right = TreeNode(4)
    print "初始的二叉搜索树=>", tree
    node = TreeNode(3)
    solution = Solution()
    solution.insertNode(tree, node)
    print "增加了数值为3的节点=>", tree
    node = TreeNode(6)
    solution = RecursiveSolution()
    solution.insertNode(tree, node)
    print "增加了数值为6的节点=>", tree

if __name__ == '__main__':
    main()

