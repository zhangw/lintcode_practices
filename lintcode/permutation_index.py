# -*- coding: utf-8 -*-
"""
permutation_index.py
--------------------
排列序号
给出一个不含重复数字的排列，求这些数字的所有排列按字典序排序后该排列的编号。其中，编号从1开始。

样例:
例如，排列[1,2,4]是第1个排列。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 05,2016
"""
class Solution:
    """
    对于[a1,a2,a3...an]组成的所有排列，按字典序排序后，每个排列的编号有如下计算公式:
    s = (n-1)!*a1_index + (n-2)!*a2_index + (n-3)!*a3_index + ... + 1!*a(n-1)_index
    s 的值从0开始，如果编号从1开始，s = s + 1。
    
    其中(n-1)!,(n-2)!...1!表示阶乘，a1_index, a2_index...a(n-1)_index表示a1,a2...a(n-1)
    各自在以各自为数组首项的有序子序列之中的索引值，索引值从0开始，比如:
    [1,3,4,2]在所有排列中的编号计算过程为: 
    s = 3!*0 + 2!*2 + 1!*1 + 1 => 6
        其中1在[1,3,4,2]有序的情况下，索引是0
        其中3在[3,4,2]有序的情况下，索引是2
        其中4在[4,2]有序的情况下，索引是1
    [4,3,2,1]的编号为: s = 3!*3 + 2!*2 + 1!*1 + 1 => 24
    [1,4,2,3]的编号为：s = 3!*0 + 2!*2 + 1!*0 + 1 => 5
    """
    # @param {int[]} A an integer array
    # @return {long} a long integer
    def permutationIndex(self, A):
        if A != None and len(A) > 0:
            if len(A) == 1:
                return 1
            else:
                length = len(A)
                permutation_index = 1
                for i in range(0, length-1):
                    #calculate the factorial value
                    f = self.factorial(length-1-i)
                    #sort the subarray by quick sort method
                    subarray_of_A = A[i:]
                    self.quickSort(subarray_of_A, 0, length-i)
                    #get the index of current number in sorted subarray
                    position = subarray_of_A.index(A[i])
                    #update the sum
                    permutation_index += f * position
                return permutation_index
        return None

    def factorial(self, n):
        caches = {0:1,1:1}
        def recurrence(n):
            if n < 0:
                return None
            if caches.has_key(n-1):
                n_1 = caches[n-1]
            else:
                n_1 = recurrence(n-1)
            rst = n_1 * n
            caches[n] = rst
            return rst
        return recurrence(n)

    def quickSort(self, A, start, last):
        if A != None and len(A) > 1:
            if last - start <= 1:
                return
            pivot = A[start]
            i = start + 1
            j = last - 1
            while i<=j:
                if A[i] <= pivot:
                    i += 1
                    continue
                if A[j] > pivot:
                    j -= 1
                    continue
                A[i],A[j] = A[j],A[i]
            A[start],A[i-1] = A[i-1],pivot
            self.quickSort(A, start, i)
            self.quickSort(A, i, last)

def main():
    array = [0,1,2,3,5,4]
    solution = Solution()
    print array
    print "当前排列在所有排列序列中的序号值:%d" % solution.permutationIndex(array)

if __name__ == '__main__':
    main()

