# -*- coding: utf-8 -*-
"""
nth_to_last_node_in_list.py
---------------------------
链表倒数第n个节点
找到单链表倒数第n个节点，保证链表中节点的最少数量为n。

样例:
给出链表 3->2->1->5->null和n = 2，返回倒数第二个节点的值1.
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 04,2016
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: Nth to last node of a singly linked list. 
    """
    def nthToLast(self, head, n):
        #n should be greater than 0
        if n <= 0:
            return None
        array = []
        while head != None:
            array.append(head)
            head = head.next
        last = -1
        nth = last * n
        #check whether the nth index out of range
        if nth + len(array) >= 0:
            return array[nth]
        return None

def main():
    pass

if __name__ == '__main__':
    main()

