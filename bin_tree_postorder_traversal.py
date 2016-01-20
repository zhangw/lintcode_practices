# -*- coding: utf-8 -*-
"""
bin_tree_postorder_traversal.py
-------------------------------
给出一棵二叉树，返回其节点值的后序遍历。

样例:
给出一棵二叉树 {1,#,2,3}
1
 \
  2
 /
3
返回[3,2,1]
----------
Created by <jimokanghanchao@gmail.com> on Jan 20,2016
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    using a loop to implement postorder traversal
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        #the nodes collection
        nodes = []
        #the nodes which not leaf nodes
        branchnodes = []
        while True:
            if root != None:
                if root.left != None or root.right != None:
                    #push the parent node into stack
                    branchnodes.append(root)
                    #left child first
                    root = root.left if root.left != None else root.right
                    continue
                else:
                    #the leaf node founded, add the leaf node into collection
                    nodes.append(root.val)
                    #a loop used to find right child tree or node
                    while True:
                        if len(branchnodes) >= 1:
                            parent = branchnodes[-1]
                            if parent.left != None and parent.right != None and parent.left == root:
                                #right tree or node founded, use it as root node
                                root = parent.right
                                break
                            else:
                                #both of left and right children have been visited, so add the parent node of them into collection
                                nodes.append(parent.val)
                                #IMPORTANT:pop the parent node from stack and use it to recover the root node, continue to find the right child of it
                                root = branchnodes.pop()
                                continue
                        else:
                            return nodes
                    #the new root node founded, continue the loop
                    continue
            else:
                return nodes

class RecursiveSolution:
    """
    using recursive method to implement postorder traversal
    """
    def __init__(self):
        #the nodes collection
        self.nodes = []

    """
    @param root: The root of binary tree.
    @return: Postorder in ArrayList which contains node values.
    """
    def postorderTraversal(self, root):
        if root != None:
            if root.left != None or root.right != None:
                #left child first
                if root.left != None:
                    self.postorderTraversal(root.left)
                #right child 
                if root.right != None:
                    self.postorderTraversal(root.right)
                #after left and right children, push the parent node into collection
                self.nodes.append(root.val)
            else:
                #the leaf node founded, push the leaf node into collection
                self.nodes.append(root.val)
        return self.nodes

def main():
    tree = TreeNode(1)
    tree.left = TreeNode(5)
    tree.left.right = TreeNode(6)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(4)
    solution = RecursiveSolution()
    print solution.postorderTraversal(tree)
    solution = Solution()
    print solution.postorderTraversal(tree)

if __name__ == '__main__':
    main()

