# -*- coding: utf-8 -*-
"""
remove_duplicates_from_sorted_array_ii.py
-----------------------------------------
删除排序数组中的重复数字 II
跟进“删除重复数字“：
如果可以允许出现两次重复将如何处理？

样例:
给出数组A =[1,1,1,2,2,3]，你的函数应该返回长度5，此时A=[1,1,2,2,3]。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 15,2016
"""
class Solution:
    """
    @param A: a list of integers
    @return an integer
    """
    def removeDuplicates(self, A):
        if A != None:
            i = 0
            length = len(A)
            while i < length:
                if i < length-2:
                    if A[i] == A[i+1] and A[i+1] == A[i+2]:
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
    array.sort()
    print "随机生成的数组:", array
    solution = Solution()
    solution.removeDuplicates(array)
    print "允许出现两次重复,删除重复数字后的数组:",array

if __name__ == '__main__':
    main()

