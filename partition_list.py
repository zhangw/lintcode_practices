# -*- coding: utf-8 -*-
"""
partition_list.py
-----------------
链表划分
给定一个单链表和数值x，划分链表使得所有小于x的节点排在大于等于x的节点之前。
你应该保留两部分内链表节点原有的相对顺序。

样例:
给定链表 1->4->3->2->5->2->null，并且 x=3
返回 1->2->2->4->3->5->null
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 05,2016
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
    @param x: an integer
    @return: a ListNode 
    """
    def partition(self, head, x):
        values = []
        while head != None:
            values.append(head.val)
            head = head.next
        if len(values) > 0:
            less_than_x = []
            max_number_in_less = None
            length = len(values)
            i = 0
            #push all the elements less than x into new array, and remove them from original array
            while i < length:
                temp = values[i]
                if temp < x:
                    less_than_x.append(temp)
                    if max_number_in_less == None:
                        max_number_in_less = temp
                    else:
                        max_number_in_less = max(max_number_in_less, temp)
                    del values[i]
                    length -= 1
                    #decrease length of original array and keep value of variable i
                    continue
                #increase value of variable i
                i += 1
            #original array is empty
            if len(values) == 0:
                values = less_than_x
            elif len(less_than_x):
                #regenerate the original array by inserting the new array at some index
                for j in range(0, len(values)):
                    if values[j] > max_number_in_less:
                        values = values[:j] + less_than_x + values[j:]
                        break
            #generate a new linkedlist with the elements in the array
            head_linked_list = ListNode(values[0])
            node = head_linked_list
            for k in range(1, len(values)):
                node.next = ListNode(values[k])
                node = node.next
            return head_linked_list
        else:
            return None

def main():
    head = ListNode(3)
    head.next = ListNode(3)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(2)
    head.next.next.next.next = ListNode(4)
    print "需要被划分的链表:", head
    solution = Solution()
    print "划分的数值为3,划分之后的链表:", solution.partition(head, 3)

if __name__ == '__main__':
    main()

