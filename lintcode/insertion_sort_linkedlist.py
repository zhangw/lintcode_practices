# -*- coding: utf-8 -*-
"""
insertion_sort_linkedlist.py
----------------------------
链表插入排序
用插入排序对链表排序

插入排序参考:
https://zh.wikipedia.org/wiki/%E6%8F%92%E5%85%A5%E6%8E%92%E5%BA%8F

样例:
Given 1->3->2->0->null, return 0->1->2->3->null
-----------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 25,2016
"""
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        values = []
        head = self
        while True:
            if head != None:
                values.append(str(head.val))
                head = head.next
            else:
                break
        return "->".join(values)

class Solution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.

    NOTE:performace test result:
        =============================
        | length | execution time(s)|
        -----------------------------
        | 1000   | 0.039391040802   |
        -----------------------------
        | 2000   | 0.154845952988   |
        -----------------------------
        | 4000   | 0.621329069138   |
        -----------------------------
        | 8000   | 2.49966096878    |
        -----------------------------
        | 10000  | 3.73059010506    |
        -----------------------------
    """
    def insertionSortList(self, head):
        array = []
        linkedlist = head
        while True:
            #It is more faster that sorting a simple array object than the ListNode object
            if head != None:
                array.append(head.val)
                head = head.next
            else:
                break
        if len(array) == 0:
            return None
        elif len(array) == 1:
            return linkedlist
        else:
            #the elements need to sort
            for i in range(1,len(array)):
                temp = array[i]
                #the elements have been sorted
                for j in range(i-1,-1,-1):
                    if temp < array[j]:
                        #move elements
                        array[j+1] = array[j]
                    else:
                        #IMPORTANT:don't forget to update value of j
                        j += 1
                        break
                #insertion
                array[j] = temp
            head = linkedlist
            i = 0
            while True:
                #use the sorted array to update the ListNode object
                if head != None:
                    head.val = array[i]
                    head = head.next
                    i += 1
                else:
                    break
            return linkedlist

class AnotherSolution:
    """
    @param head: The first node of linked list.
    @return: The head of linked list.
    
    NOTE:performace test result:
        =============================
        | length | execution time(s)|
        -----------------------------
        | 100    | 0.0366117954254  |
        -----------------------------
        | 200    | 0.216373205185   |
        -----------------------------
        | 400    | 1.62983512878    |
        -----------------------------
        | 800    | 12.8778920174    |
        -----------------------------
        | 1000   | 28.583534956     |
        -----------------------------
    """ 
    def insertionSortList(self, head):
        if head != None:
            if head.next == None:
                return head
            else:
                linkedlist = head
                #已经排序的链表的表头
                sorted = head
                while head.next != None:
                    #当前待排序的链表元素
                    temp = head.next
                    while True:
                        #从已经排序的表头位置寻找插入点
                        if sorted.val <= temp.val:
                            sorted = sorted.next
                            if sorted == temp:
                                #查找完毕，待排序的元素和查找的节点是同一个
                                sorted = linkedlist
                                #更新待排序元素的链表头
                                head = head.next
                                break
                            continue
                        #insertion sort
                        else:
                            #更新待排序元素的链表,移除准备排序的元素节点
                            head.next = temp.next
                            #新增一个节点代替当前sorted节点
                            node = ListNode(sorted.val,sorted.next)
                            #插入排序
                            sorted.val = temp.val
                            sorted.next = node
                            #更新待排序元素的链表头
                            head = node
                            del temp
                            #更新已经排序的链表的表头
                            sorted = linkedlist
                            break
                return linkedlist
        else:
            return head

def main():
    n = raw_input("使用随机数生成链表,请输入链表的长度N,比如50:\n")
    N = n = int(n)
    linkedlist, head = None, None
    import random, time
    while n > 0:
        value = int(random.random()*n*10)
        n -= 1
        if head == None:
            linkedlist = ListNode(value)
            head = linkedlist
            continue
        head.next = ListNode(value)
        head = head.next
    print "排序前链表:\n", linkedlist
    solution = Solution()
    start = time.time()
    print "插入法排序后链表:\n", solution.insertionSortList(linkedlist)
    end = time.time()
    print "%d长度的链表插入排序时间:%s second" % (N, end-start)

if __name__ == '__main__':
    main()
