# -*- coding: utf-8 -*-
"""
remove_nth_node_from_end_of_list.py
-----------------------------------
删除链表中倒数第n个节点
给定一个链表，删除链表中倒数第n个节点，返回链表的头节点。

样例:
给出链表1->2->3->4->5->null和 n = 2.
删除倒数第二个节点之后，这个链表将变成1->2->3->5->null.

注意:
链表中的节点个数大于等于n

挑战:
O(n)时间复杂度
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
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """
    def removeNthFromEnd(self, head, n):
        if head != None:
            nodes = []
            while head != None:
                nodes.append(head)
                head = head.next
            length = len(nodes)
            #get the nth number from beginning
            index = length - n
            #delete the head
            if index == 0:
                del nodes[0]
                length -= 1
                if length:
                    return nodes[0]
                else:
                    return None
            #delete the tail
            elif index == length - 1:
                del nodes[-1]
                length -= 1
                nodes[-1].next = None
                return nodes[0]
            #delete nothing
            elif index == length:
                return nodes[0]
            #delete other nodes
            else:
                nodes[index-1].next = nodes[index+1]
                del nodes[index]
                length -= 1
                return nodes[0]
        return head

def main():
    linkedlist = ListNode(1)
    linkedlist.next = ListNode(2)
    linkedlist.next.next = ListNode(3)
    linkedlist.next.next.next = ListNode(7)
    linkedlist.next.next.next.next = ListNode(9)
    print "原链表:", linkedlist
    solution = Solution()
    nth = raw_input("请输入要删除的倒数第几个节点?\n")
    nth = int(nth) 
    print "倒数第%d个节点被删除后的链表:%s" % (nth, solution.removeNthFromEnd(linkedlist,nth)) 

if __name__ == '__main__':
    main()