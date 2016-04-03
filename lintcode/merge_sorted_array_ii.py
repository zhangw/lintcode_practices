# -*- coding: utf-8 -*-
"""
merge_sorted_array_ii.py
------------------------
合并两个排序的整数数组
合并两个排序的整数数组A和B变成一个新的数组。

样例:
给出A=[1,2,3,4]，B=[2,4,5,6]，返回 [1,2,2,3,4,4,5,6]

挑战:
你能否优化你的算法，如果其中一个数组很大而另一个数组很小？
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 03,2016
"""

class Solution:
    #@param A and B: sorted integer array A and B.
    #@return: A new sorted integer array
    def mergeSortedArray(self, A, B):
        if A != None and B != None:
            length_A = len(A)
            length_B = len(B)
            if length_A > 0 and length_B > 0:
                if A[-1] <= B[0]:
                    return A + B
                if A[0] >= B[-1]:
                    return B + A
                else:
                    sorted = []
                    while len(A) and len(B):
                        first_of_A = A[0]
                        first_of_B = B[0]
                        if first_of_A <= first_of_B:
                            sorted.append(first_of_A)
                            A = A[1:]
                        else:
                            sorted.append(first_of_B)
                            B = B[1:]
                    if len(A):
                        sorted += A
                    if len(B):
                        sorted += B
                    return sorted
            else:
                if length_A > 0:
                    return A
                if length_B > 0:
                    return B
                return None
        else:
            return None

def main():
    pass

if __name__ == '__main__':
    main()

