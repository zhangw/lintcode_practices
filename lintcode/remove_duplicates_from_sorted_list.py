# -*- coding: utf-8 -*-
"""
remove_duplicates_from_sorted_list.py
-------------------------------------
删除排序链表中的重复元素
给定一个排序链表，删除所有重复的元素每个元素只留下一个。

样例:
给出1->1->2->null，返回 1->2->null
给出1->1->2->3->3->null，返回 1->2->3->null
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 15,2016
"""

class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        values = []
        while self != None:
            values.append(str(self.val))
            self = self.next
        return "->".join(values)

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
        if head != None:
            array = []
            while head != None:
                array.append(head.val)
                head = head.next
            length = len(array)
            i = 0
            while i < length:
                if i < length - 1:
                    if array[i] == array[i+1]:
                        del array[i]
                        length -= 1
                        continue
                i += 1
            if length:
                linkedlist = ListNode(array[0])
                prev = linkedlist
                i = 1
                while i < length:
                    prev.next = ListNode(array[i])
                    prev = prev.next
                    i += 1
                return linkedlist
            else:
                return None
        return head

def main():
    linkedlist = ListNode(1)
    linkedlist.next = ListNode(2)
    linkedlist.next.next = ListNode(3)
    linkedlist.next.next.next = ListNode(7)
    linkedlist.next.next.next.next = ListNode(7)
    print "原链表:", linkedlist
    solution = Solution()
    print "重复元素删除后链表:", solution.deleteDuplicates(linkedlist)

if __name__ == '__main__':
    main()