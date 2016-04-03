# -*- coding: utf-8 -*-
"""
subtree.py
----------
子树
有两个不同大小的二进制树： T1 有上百万的节点； T2 有好几百的节点。请设计一种算法，判定 T2 是否为 T1的子树。

样例:
下面的例子中 T2 是 T1 的子树：

       1                3
      / \              / 
T1 = 2   3      T2 =  4
        /
       4
下面的例子中 T2 不是 T1 的子树：

       1               3
      / \               \
T1 = 2   3       T2 =    4
        /
       4
注意:
若 T1 中存在从节点 n 开始的子树与 T2 相同，我们称 T2 是 T1 的子树。也就是说，如果在 T1 节点 n 处将树砍断，砍断的部分将与 T2 完全相同。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 18,2016
"""
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        """BFS traverse"""
        root = self
        if root != None:
            nodes = []
            current = [root]
            next = []
            while True:
                for node in current:
                    if node == None:
                        nodes.append(None)
                        continue
                    nodes.append(node.val)
                    if node.left != None:
                        next.append(node.left)
                    else:
                        next.append(None)
                    if node.right != None:
                        next.append(node.right)
                    else:
                        next.append(None)
                if len(next):
                    current = next
                    next = []
                    continue
                break
            if nodes[-1] == None:
                j = len(nodes)-1
                while j >= 0:
                    if nodes[j] == None:
                        j -= 1
                        continue
                    break
                nodes = nodes[:j+1]
            return str(nodes)
        
class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        def cmp(T1, T2):
            """recursively compare the two trees"""
            if T1 and T2:
                if T1.val == T2.val:
                    #the and operator
                    return cmp(T1.left, T2.left) and cmp(T1.right, T2.right)
                return False
            return not T1 and not T2
        
        def traverse(T1, T2):
            """recursively traverse subtrees of T1 and compare each subtree with T2"""
            if T2 == None:
                #always return True in this case
                return True
            if T1 != None:
                if not cmp(T1, T2):
                    #the or operator
                    return traverse(T1.left, T2) or traverse(T1.right, T2)
                return True
            #always return False in this case
            return False
        
        return traverse(T1, T2)

def main():
    T1 = TreeNode(1)
    T1.left = TreeNode(2)
    T1.right = TreeNode(3)
    T1.right.left = TreeNode(4)
    print "T1:", T1
    T2 = TreeNode(3)
    T2.right = TreeNode(4)
    print "T2:", T2
    T3 = TreeNode(3)
    T3.left = TreeNode(4)
    print "T3:", T3
    solution = Solution()
    print "T2 is%ssubtree of T1" % (' ' if solution.isSubtree(T1, T2) else ' not ')
    print "T3 is%ssubtree of T1" % (' ' if solution.isSubtree(T1, T3) else ' not ')

if __name__ == '__main__':
    main()
