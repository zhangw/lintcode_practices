# -*- coding: utf-8 -*-
"""
flatten_bin_tree_to_linked_list.py
----------------------------------
将二叉树拆成链表
将一棵二叉树按照前序遍历拆解成为一个假链表。
所谓的假链表是说，用二叉树的 right 指针，来表示链表中的 next 指针。
样例:
              1
               \
     1          2
    / \          \
   2   5    =>    3
  / \   \          \
 3   4   6          4
                     \
                      5
                       \
                        6
注意:
不要忘记将左儿子标记为 null，否则你可能会得到空间溢出或是时间溢出。
挑战:
不使用额外的空间耗费。
------------------
Created by <jimokanghanchao@gmail.com> on Jan 23,2016
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __repr__(self):
        values = []
        while self != None:
            values.append(str(self.val))
            self = self.right
        return "->".join(values)

class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        #if the new tree should be returned, return tree_linkedlist
        tree_linkedlist = root
        if root != None:
            #the stack used to save all the right nodes should be visited
            #the parents of these nodes all have left nodes
            rightnodes = []
            while True:
                left = root.left
                right = root.right
                if left != None and right != None:
                    #in this case, push the right node into stack
                    rightnodes.append(right)
                if left != None or right != None:
                    #firstly left child
                    #if left child not exists, use right child
                    next = left if left != None else right
                    #del left child and update right child to build linkedlist
                    root.left = None
                    root.right = next
                    #continue the loop
                    root = next
                else:
                    #a leaf node
                    if len(rightnodes) >= 1:
                        #return the next right node should be visited
                        node = rightnodes.pop()
                        #update right child for tail node of linkedlist
                        root.right = node
                        #continue the loop with the right child as new root node
                        root = node
                    else:
                        #end the loop when all the nodes have been visited
                        break

def main():
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(5)
    tree.left.left = TreeNode(3)
    tree.left.right = TreeNode(4)
    tree.right.right = TreeNode(6)
    solution = Solution()
    solution.flatten(tree)
    print "转换成假链表的二叉树:", tree
if __name__ == '__main__':
    main()

