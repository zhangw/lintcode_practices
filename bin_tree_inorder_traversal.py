# -*- coding: utf-8 -*-
"""
bin_tree_inorder_traversal.py
-----------------------------
给出一棵二叉树,返回其中序遍历
使用递归和非递归算法实现
二叉树使用宽度优先遍历(BFS)来表示:
    1
   / \
  2   3
 / \   \
4   5   6
   / \
  7   8
二叉树可以表示为[1,2,3,4,5,#,6,#,#,7,8]
中序遍历返回[4,2,7,5,8,1,3,6]
-----------------------------
Created by <jimokanghanchao@gmail.com> on Jan 10,2016
"""

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


class Solution:
  def inorderTraversal(self, root):
    """
    build a loop to implement inorder traversal.
    @param root: The root of binary tree.
    @return: Inorder in ArrayList which contains node values.
    """
    nodes = []
    rootnodes = []
    rootnode = root
    while True:
      if rootnode != None:
        #如果根节点右左子树，优先遍历左子树
        if rootnode.left != None:
          #把根节点入栈，在遍历右子树时出栈
          rootnodes.append(rootnode)
          rootnode = rootnode.left
          continue
        if rootnode.left == None and rootnode.right == None:
          #记录叶子节点
          nodes.append(rootnode.val)
          if len(rootnodes) >= 1:
            #叶子节点的根节点出栈
            rootnode = rootnodes.pop()
            #记录根节点
            nodes.append(rootnode.val)
            #如果根节点是双子节点，此时应该遍历右子树
            if rootnode.left != None and rootnode.right != None:
              rootnode = rootnode.right
              continue
            else:
              #当前根节点没有右子树需要遍历，继续出栈，找寻最近一个有右子树的根节点
              while True:
                if len(rootnodes) >= 1:
                  rootnode = rootnodes.pop()
                  nodes.append(rootnode.val)
                  if rootnode.right != None:
                    #找到有右子树的节点
                    rootnode = rootnode.right
                    break
                else:
                  #没有节点有右子树，结束遍历，返回
                  return nodes
              #返回有右子树的节点，继续遍历
              continue
          else:
            #没有未遍历的根节点了，结束遍历，返回
            break
        #根节点没有左子树，只有右子树
        if rootnode.right != None:
          #记录根节点
          nodes.append(rootnode.val)
          #继续遍历右子树
          rootnode = rootnode.right
          continue
      else:
        break
    return nodes

class RecursiveSolution(Solution):
  """use the recursive method to implement the inorder traversal"""
  def __init__(self):
    self.nodes = []

  def inorderTraversal(self, root):
    if root != None:
      #only left child exists
      #traversal left child as root, after that, the root
      if root.left != None and root.right == None:
        self.inorderTraversal(root.left)
        self.nodes.append(root.val)
      #only right child exists
      #firstly the root, after that, traversal right child as root
      elif root.right != None and root.left == None:
        self.nodes.append(root.val)
        self.inorderTraversal(root.right)
      #both children exist
      #traversal left child as root, after that, the root, and then traversal right child as root
      elif root.left != None and root.right != None:
        self.inorderTraversal(root.left)
        self.nodes.append(root.val)
        self.inorderTraversal(root.right)
      #both children not exist
      #just only the root
      else:
        self.nodes.append(root.val)
    return self.nodes

def main():
  """
  tree = TreeNode(1)
  tree.left = TreeNode(2)
  tree.right = TreeNode(3)
  tree.right.right = TreeNode(6)
  tree.left.left = TreeNode(4)
  tree.left.right = TreeNode(5)
  tree.left.right.left = TreeNode(7)
  tree.left.right.right = TreeNode(8)
  """
  """
  tree = TreeNode(1)
  tree.right = TreeNode(2)
  tree.right.left = TreeNode(3)
  """
  tree = TreeNode(1)
  tree.left = TreeNode(2)
  tree.right = TreeNode(3)
  tree.left.left = TreeNode(4)
  tree.left.left.left = TreeNode(6)
  tree.left.left.left.left = TreeNode(8)
  tree.right.right = TreeNode(5)
  tree.right.right.right = TreeNode(7)
  tree.right.right.right.right = TreeNode(9)
  solution = RecursiveSolution()
  print solution.inorderTraversal(tree)
  solution = Solution()
  print solution.inorderTraversal(tree)

if __name__ == '__main__':
  main()

