# -*- coding: utf-8 -*-
"""
remove_linked_list_elements.py

Created by <jimokanghanchao@gmail.com> on Jan 06,2016
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
        print "->".join(vals)

class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        if head == None:
            return None
        h = head
        if h.next == None:
            if h.val == val:
                return None
            return h
        else:
            current = head
            prev = head
            while True:
                if current.val == val:
                    if current == h:
                        #删除的元素是链表头
                        prev = current.next
                        current = current.next
                        h = current.next
                        if current != None:
                            continue
                        else:
                            return h
                    else:
                        #删除的元素不是链表头
                        prev.next = current.next
                        if prev.next != None:
                            current = current.next
                            continue
                        else:
                            return h
                else:
                    #不需要删除元素，如果链表已经遍历结束，返回；否则继续遍历
                    if current.next != None:
                        prev = current
                        current = current.next
                        continue
                    else:
                        return h
            return h

if __name__ == '__main__':
    link = raw_input('输入链表的结构，比如1->2->2->1->m->0\n')
    val = raw_input('输入要删除的链表元素，比如2\n')
    items = link.split('->')
    if len(items) >= 1:
        link = ListNode(items[0])
        plink = link
        for item in items[1:]:
            plink.next = ListNode(item)
            plink = plink.next
        print '未删除元素前的链表:'
        link.printSelf()
        solution = Solution()
        solution.removeElements(link,val)
        print '删除元素后的链表:'
        link.printSelf()

