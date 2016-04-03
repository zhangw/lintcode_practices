# -*- coding: utf-8 -*-
"""
subarray_sum.py
---------------
子数组之和
给定一个整数数组，找到和为零的子数组。你的代码应该返回满足要求的子数组的起始位置和结束位置

样例:
给出 [-3, 1, 2, -3, 4]，返回[0, 2] 或者 [1, 3].
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 18,2016
"""
class Solution:
    """
    @param nums: A list of integers
    @return: A list of integers includes the index of the first number 
             and the index of the last number
    """
    def subarraySum(self, nums):
        if nums != None:
            length = len(nums)
            rst = []
            i = 0
            while i < length:
                sum = nums[i]
                if i == length-1:
                    if nums[i] == 0:
                        rst = [i,i]
                    return rst
                else:
                    j = i+1
                    last = None if sum != 0 else i
                    while j < length:
                        sum += nums[j]
                        if sum == 0:
                            last = j
                        j += 1
                    if last != None:
                        rst = [i,last]
                        return rst
                    i += 1

def main():
    pass

if __name__ == '__main__':
    main()

