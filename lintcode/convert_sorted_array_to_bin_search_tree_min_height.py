# -*- coding: utf-8 -*-
"""
convert_sorted_array_to_bin_search_tree_min_height.py
-----------------------------------------------------
把排序数组转换为高度最小的二叉搜索树
给一个排序数组（从小到大），将其转换为一棵高度最小的排序二叉树。

样例:
给出数组 [1,2,3,4,5,6,7], 返回
     4
   /   \
  2     6
 / \    / \
1   3  5   7

挑战:
可能有多个答案，返回任意一个即可
---------------------------
Created by <jimokanghanchao@gmail.com> on Jan 21,2016
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    convert sorted array to binary tree with minimal height by binary search way.
    @param A: a list of integer
    @return: a tree node
    """
    def sortedArrayToBST(self, A):
        length = len(A)
        array = A
        rootnodes_with_rightarray = []
        tree = None
        if length == 0:
            return None
        while True:
            if length/2 > 0:
                leftarray = array[:length/2]
                rightarray = array[length/2+1:]
                if tree == None:
                    rootnode = TreeNode(array[length/2])
                    tree = rootnode
                #always push parent node with the right array into stack
                rootnodes_with_rightarray.append((rootnode,rightarray))
                #build the left and right children for the parent node
                if len(leftarray)/2 > 0:
                    rootnode.left = TreeNode(leftarray[len(leftarray)/2])
                if len(rightarray)/2 > 0:
                    rootnode.right = TreeNode(rightarray[len(rightarray)/2])
                #leftarray first
                array = leftarray
                length = len(leftarray)
                rootnode = rootnode.left if rootnode.left != None else rootnode
                continue
            else:
                #this element of array should be a leaf node in tree
                leafnode = TreeNode(array[0])
                if len(rootnodes_with_rightarray) > 0:
                    parentnode, rightarray = rootnodes_with_rightarray.pop()
                    #add the leaf node as left child
                    parentnode.left = leafnode
                    #add the right node as right child if it exists
                    if len(rightarray) == 1:
                        parentnode.right = TreeNode(rightarray[0])
                    #find the next right child tree or node
                    while True:
                        if len(rootnodes_with_rightarray) > 0:
                            parentnode, array = rootnodes_with_rightarray.pop()
                            #the next right child tree founded, use the right node as root, rightarray as array
                            if len(array)/2 > 0:
                                length = len(array)
                                rootnode = parentnode.right
                                break
                            else:
                                if len(array) == 1:
                                    #the next right leaf node founded, add it as right child of its parent
                                    parentnode.right = TreeNode(array[0])
                                #continue to find the next right child tree 
                                continue
                        else:
                            return tree
                    continue
                else:
                    if tree == None:
                        tree = leafnode
                    return tree
def main():
    array_str = raw_input('输入从小到大排序的数组,比如1,2,3,4,5,6,7\n')
    if array_str == '':
        array_str = '1,2,3,4,5,6,7'
    sorted_array = [int(c) for c in array_str.split(',')]
    sorted_array.sort()
    solution = Solution()
    tree = solution.sortedArrayToBST(sorted_array)
    print '使用中序遍历返回tree的节点'
    from bin_tree_inorder_traversal import Solution as BinTreeInorderTraversal
    solution = BinTreeInorderTraversal()
    print solution.inorderTraversal(tree)

if __name__ == '__main__':
    main()
