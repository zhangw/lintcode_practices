# -*- coding: utf-8 -*-
"""
remove_element.py
-----------------
删除元素
给定一个数组和一个值，在原地删除与值相同的数字，返回新数组的长度。
元素的顺序可以改变，并且对新的数组不会有影响。

样例:
给出一个数组 [0,4,4,0,0,2,4,4]，和值 4
返回 4 并且4个元素的新数组为[0,0,0,2]
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 15,2016
"""
class Solution:
    """
    @param A: A list of integers
    @param elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        if A != None:
            length = len(A)
            i = 0
            while i < length:
                if A[i] == elem:
                    del A[i]
                    length -= 1
                    continue
                i += 1
            return length
        return 0

def main():
    n = raw_input("输入整数数组的长度,比如10:\n")
    n = int(n) if n != '' else 10
    import utils.RandomOrg.RandomOrgApi as random
    api = random.RandomOrgApi()
    array = api.integers.generate(num=n,min=0,max=n/2,col=1,base=10,format="plain",rnd="new")
    print "随机生成的数组:", array
    deleted = raw_input("输入要删除的数字值:\n")
    deleted = int(deleted)
    solution = Solution()
    solution.removeElement(array,deleted)
    print "%d被删除后的数组:%s" % (deleted, array) 

if __name__ == '__main__':
    main()