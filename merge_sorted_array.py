# -*- coding: utf-8 -*-
"""
merge_sorted_array.py
---------------------
合并排序数组 II
合并两个排序的整数数组A和B变成一个新的数组。

样例:
给出A = [1, 2, 3, empty, empty] B = [4,5]
合并之后A将变成[1,2,3,4,5]

注意:
你可以假设A具有足够的空间（A数组的大小大于或等于m+n）去添加B中的元素。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 03,2016
"""

class Solution:
    """
    @param A: sorted integer array A which has m elements, 
              but size of A is m+n
    @param B: sorted integer array B which has n elements
    @return:  void
    """
    def mergeSortedArray(self, A, m, B, n):
        result = []
        if A != None and B != None:
            if m != 0 and n != 0:
                if A[m-1] <= B[0]:
                    for i in range(0,n):
                        A[m+i] = B[i]
                else:
                    _A = A[:m]
                    result = []
                    while len(_A) > 0 and len(B) > 0:
                        min_A = _A[0]
                        min_B = B[0]
                        if min_A <= min_B:
                            result.append(min_A)
                            _A = _A[1:]
                        else:
                            result.append(min_B)
                            B = B[1:]
                    if len(_A) > 0:
                        result += _A
                    if len(B) > 0:
                        result += B
                    for i in range(0,len(result)):
                        A[i] = result[i]
            else:
                if m == 0:
                    for i in range(0,n):
                        A[i] = B[i]
def main():
    pass

if __name__ == '__main__':
    main()

