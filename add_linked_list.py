# -*- coding: utf-8 -*-
"""
add_linked_list.py
------------------
你有两个用链表代表的整数，其中每个节点包含一个数字。
数字存储按照在原来整数中相反的顺序，使得第一个数字位于链表的开头。
写出一个函数将两个整数相加，用链表形式返回和。

样例:
给出两个链表 3->1->5->null 和 5->9->2->null
```
3+5->8
1+9->10(进位1)
5+2->7,7+1->8(进位+1)
```
返回 8->0->8->null
------------------
Created by <jimokanghanchao@gmail.com> on Jan 10,2016
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def printSelf(self):
        vals = []
        vals.append(self.val)
        next = self.next
        while True:
            if next != None:
                vals.append(next.val)
                next = next.next
            else:
                break
        print vals

class Solution:
  def addLists(self, l1, l2):
    """
     @param l1: the first list
     @param l2: the second list
     @return: the sum list of l1 and l2
    """
    ret_link = ListNode(None)
    ret_link_current = ret_link
    carry_num = 0
    while True:
      if l1 == None and l2 == None and carry_num == 0:
        break
      if l1 != None and l1.val != None:
        num1 = l1.val
      else:
        num1 = 0
      if l2 != None and l2.val != None:
        num2 = l2.val
      else:
        num2 = 0
      num1_add_2 = num1 + num2 + carry_num
      if num1_add_2 >= 10:
        carry_num = 1
        num1_add_2 -= 10
      else:
        carry_num = 0
      ret_link_current.val = num1_add_2
      if l1 != None and l1.next != None:
        l1 = l1.next
      else:
        l1 = None
      if l2 != None and l2.next != None:
        l2 = l2.next
      else:
        l2 = None
      if l1 == None and l2 == None and carry_num == 0:
        ret_link_current.next = None
      else:
        ret_link_current.next = ListNode(None)
        ret_link_current = ret_link_current.next
    return ret_link

def main():
  def _convert_str_to_link(link_str):
    chars = ('0','1','2','3','4','5','6','7','8','9')
    items = link_str.split('->')
    if len(items) >= 1:
      if items[0] not in chars:
        return None
      link = ListNode(int(items[0]))
      plink = link
      for item in items[1:]:
        if item not in chars:
          return None
        plink.next = ListNode(int(item))
        plink = plink.next
      return link
    else:
      return None
  link1 = raw_input('输入链表1的结构，比如1->2->2->1->4->9\n')
  link2 = raw_input('输入链表2的结构，比如9->8->7->9->0\n')
  link1 = _convert_str_to_link(link1)
  link1.printSelf()
  link2 = _convert_str_to_link(link2)
  link2.printSelf()
  if link1 != None and link2 != None:
    solution = Solution()
    ret_link = solution.addLists(link1,link2)
    ret_link.printSelf()
  else:
    print '输入有错误，请重新输入'

if __name__ == '__main__':
  main()
