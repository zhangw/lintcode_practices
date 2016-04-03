# -*- coding: utf-8 -*-
"""
reverse_linked_list.py
----------------------
翻转链表
翻转一个链表

样例:
给出一个链表1->2->3->null，这个翻转后的链表为3->2->1->null

挑战:
在原地一次翻转完成
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 16,2016
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
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list. 
                  Reverse it in-place.
    """
    def reverse(self, head):
        if head != None:
            linkedlist = head
            #move the head of original linked list to the tail of the reversed linked list
            while head.next != None:
                temp = head.next
                #remove the next node from original linked list
                head.next = temp.next
                #the next node as the new head of reversed linked list
                temp.next = linkedlist
                linkedlist = temp
            return linkedlist
        return head

def main():
    linkedlist = ListNode(1)
    linkedlist.next = ListNode(2)
    linkedlist.next.next = ListNode(3)
    linkedlist.next.next.next = ListNode(7)
    linkedlist.next.next.next.next = ListNode(9)
    print "原链表:", linkedlist
    solution = Solution()
    print "翻转后的链表:", solution.reverse(linkedlist)
    
if __name__ == '__main__':
    main()
