# -*- coding: utf-8 -*-
"""
identical_bin_tree.py
---------------------
等价二叉树
检查两棵二叉树是否等价。等价的意思是说，首先两棵二叉树必须拥有相同的结构，并且每个对应位置上的节点上的数都相等。

样例:
    1             1
   / \           / \
  2   2   and   2   2
 /             /
4             4
就是两棵等价的二叉树。

    1             1
   / \           / \
  2   3   and   2   3
 /               \
4                 4
就不是等价的。
------------
Created by <jimokanghanchao@gmail.com> on Jan 24,2016
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Solution:
    """
    use a loop to implement.
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        a_rightnodes = []
        b_rightnodes = []
        while True:
            if a == None and b == None:
                return True
            if a != None and b != None:
                if a.val == b.val:
                    if a.left != None and a.right != None:
                        a_rightnodes.append(a.right)
                    if b.left != None and b.right != None:
                        b_rightnodes.append(b.right)
                    if a.left == None and a.right == None:
                        if b.left == None and b.right == None:
                            if len(a_rightnodes) == len(b_rightnodes):
                                if len(a_rightnodes) >= 1:
                                    a = a_rightnodes.pop()
                                    b = b_rightnodes.pop()
                                else:
                                    return True
                            else:
                                return False
                        else:
                            return False
                    else:
                        if a.left != None:
                            a = a.left
                            b = b.left
                            continue
                        if a.right != None:
                            a = a.right
                            b = b.right
                            continue
                else:
                    return False
            else:
                return False

class RecursiveSolution:
    """
    use recursive way to implement.
    @param a, b, the root of binary trees.
    @return true if they are identical, or false.
    """
    def isIdentical(self, a, b):
        if a == None and b == None:
            return True
        if a != None and b != None:
            if a.val == b.val:
                return self.isIdentical(a.left,b.left) and self.isIdentical(a.right,b.right)
            else:
                return False
        else:
            return False

def main():
    treeA = TreeNode(1)
    treeA.left = TreeNode(2)
    treeA.right = TreeNode(3)
    treeB = TreeNode(1)
    treeB.left = TreeNode(2)
    treeB.right = TreeNode(3)
    solution = Solution()
    print '使用循环比较treeA,treeB的结果:%s' % "等价" if solution.isIdentical(treeB,treeA) else "不等价"
    solution = RecursiveSolution()
    print '使用递归比较treeA,treeB的结果:%s' % "等价" if solution.isIdentical(treeB,treeA) else "不等价"
    
if __name__ == '__main__':
    main()

