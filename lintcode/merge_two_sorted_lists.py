# -*- coding: utf-8 -*-
"""
merge_two_sorted_lists.py
-------------------------
合并两个排序链表
将两个排序链表合并为一个新的排序链表

样例:
给出 1->3->8->11->15->null，2->null， 返回 1->2->3->8->11->15->null。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 04,2016
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        valus = []
        while self != None:
            valus.append(str(self.val))
            self = self.next
        return "->".join(valus)

class Solution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        rst = ListNode(val=None)
        rst_head = rst
        while l1 != None and l2 != None:
            if l1.val <= l2.val:
                rst.val = l1.val
                l1 = l1.next
            else:
                rst.val = l2.val
                l2 = l2.next
            rst.next = ListNode(val=None)
            rst = rst.next
        if l1 != None:
            rst.val = l1.val
            rst.next = l1.next
        if l2 != None:
            rst.val = l2.val
            rst.next = l2.next
        return rst_head

class AnotherSolution:
    """
    @param two ListNodes
    @return a ListNode
    """
    def mergeTwoLists(self, l1, l2):
        array1 = []
        array2 = []
        while l1 != None:
            array1.append(l1.val)
            l1 = l1.next
        while l2 != None:
            array2.append(l2.val)
            l2 = l2.next
        array = []
        while len(array1) and len(array2):
            first_1 = array1[0]
            first_2 = array2[0]
            if first_1 <= first_2:
                array.append(first_1)
                array1 = array1[1:]
            else:
                array.append(first_2)
                array2 = array2[1:]
        if len(array1):
            array += array1
        if len(array2):
            array += array2
        if len(array) > 0:
            rst = ListNode(array[0])
            rst_head = rst
            for i in range(1,len(array)):
                rst.next = ListNode(array[i])
                rst = rst.next
            return rst_head
        else:
            return None
        

def main(): 
    l1 = ListNode(1)
    l1.next = ListNode(3)
    print "l1:", l1
    l2 = ListNode(2)
    print "l2:", l2
    solution = Solution()
    print "merge l1 and l2:", solution.mergeTwoLists(l1,l2)

if __name__ == '__main__':
    main()

