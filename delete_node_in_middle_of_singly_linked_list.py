# -*- coding: utf-8 -*-
"""
delete_node_in_middle_of_singly_linked_list.py
----------------------------------------------
在O(1)时间复杂度删除链表节点

给定一个单链表中的表头和一个等待被删除的节点(非表头或表尾).
请在在O(1)时间复杂度删除该链表节点.

样例:
给定 1->2->3->4，和节点 3，返回 1->2->4.
-------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 23,2016
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        linkedlist = self
        linkedlist_values = []
        while True:
            if linkedlist != None:
                linkedlist_values.append(str(linkedlist.val))
                linkedlist = linkedlist.next
            else:
                break
        return "->".join(linkedlist_values)

class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):
        next = node.next
        #use next node instead of the node will be deleted
        if next != None:
            node.val = next.val
            node.next = next.next
            del next

def main():
    linkedlist = ListNode(1)
    linkedlist.next = ListNode(2)
    linkedlist.next.next = readytodeleted = ListNode(3)
    linkedlist.next.next.next = ListNode(4)
    print "the old linkedlist:", str(linkedlist)
    print "delete node of which value is 3"
    solution = Solution()
    solution.deleteNode(readytodeleted)
    print "the new linkedlist:", str(linkedlist)

if __name__ == '__main__':
    main()

