# -*- coding: utf-8 -*-
"""
product_of_array_exclude_itself.py
----------------------------------
数组剔除元素后的乘积
给定一个整数数组A。
定义B[i] = A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]， 计算B的时候请不要使用除法。

样例:
给出A=[1, 2, 3]，返回 B为[6, 3, 2]
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 15,2016
"""
class Solution:
    """
    @param A: Given an integers array A
    @return: An integer array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, A):
        if A != None and len(A):
            length = len(A)
            #init
            B = [1] * length
            if length == 1:
                return B
            for i in range(0,length):
                temp = B[i]
                #exclude index i
                for k in range(0,i):
                    temp *= A[k]
                #exclude index i
                for j in range(i+1,length):
                    temp *= A[j]
                B[i] = temp
            return B
        return None

def main():
    n = raw_input("输入整数数组的长度,比如10:\n")
    n = int(n) if n != '' else 10
    import utils.RandomOrg.RandomOrgApi as random
    api = random.RandomOrgApi()
    array = api.integers.generate(num=n,min=-n,max=n,col=1,base=10,format="plain",rnd="new")
    print "随机生成的数组:", array
    solution = Solution()
    print "剔除元素后的乘积数组:", solution.productExcludeItself(array)

if __name__ == '__main__':
    main()

