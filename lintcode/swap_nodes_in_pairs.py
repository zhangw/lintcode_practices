# -*- coding: utf-8 -*-
"""
swap_nodes_in_pairs.py
----------------------
两两交换链表中的节点
给一个链表，两两交换其中的节点，然后返回交换后的链表。

样例:
给出 1->2->3->4, 你应该返回的链表是 2->1->4->3。

挑战:
你的算法只能使用常数的额外空间，并且不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 18,2016
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        values = []
        while self != None:
            values.append(str(self.val))
            self = self.next
        return "->".join(values)

class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        #the head of new list
        linkedlist = None
        #the last node swapped 
        prev = None
        while head != None:
            #the pair of nodes can be swapped
            if head.next != None:
                temp = head.next
                head.next = temp.next
                temp.next = head
                if linkedlist == None:
                    #build the new list
                    linkedlist = temp
                else:
                    #make the last node swapped point to the new node
                    prev.next = temp
                #the node has been swapped
                prev = head
                #the node need to swap
                head = head.next
                continue
            #the single node not need to swap
            else:
                if linkedlist == None:
                    linkedlist = head
                break
        return linkedlist

def main():
    linkedlist = ListNode(1)
    current = linkedlist
    for i in range(2,8):
        current.next = ListNode(i)
        current = current.next
    print "给定链表:", linkedlist
    solution = Solution()
    linkedlist = solution.swapPairs(linkedlist)
    print "链表节点两两交换后:", linkedlist

if __name__ == '__main__':
    main()
