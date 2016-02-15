# -*- coding: utf-8 -*-
"""
remove_duplicates_from_sorted_array.py
--------------------------------------
删除排序数组中的重复数字
给定一个排序数组，在原数组中删除重复出现的数字，使得每个元素只出现一次，并且返回新的数组的长度。
不要使用额外的数组空间，必须在原地没有额外空间的条件下完成。

样例
给出数组A =[1,1,2]，你的函数应该返回长度2，此时A=[1,2]。
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
                if i < length-1:
                    if A[i] == A[i+1]:
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
    array = api.integers.generate(num=n,min=0,max=n,col=1,base=10,format="plain",rnd="new")
    array.sort()
    print "随机生成的数组:", array
    solution = Solution()
    solution.removeDuplicates(array)
    print "删除重复数字后的数组:",array

if __name__ == '__main__':
    main()