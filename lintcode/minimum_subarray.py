# -*- coding: utf-8 -*-
"""
minimum_subarray.py
-------------------
最小子数组
给定一个整数数组，找到一个具有最小和的子数组。返回其最小和。

样例:
给出数组[1, -1, -2, 1]，返回 -3

注意:
子数组最少包含一个数字
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 04,2016
"""

class Solution:
    """
    @param nums: a list of integers
    @return: A integer denote the sum of minimum subarray
    """
    def minSubArray(self, nums):
        if nums != None and len(nums) > 0:
            #initialize minimum value
            min_sum = current_sum = nums[0]
            i = 1
            while i < len(nums):
                temp = nums[i]
                if current_sum < 0 and current_sum + temp < 0:
                    #update sum of current subarray
                    current_sum += temp
                else:
                    #reinitialize the subarray 
                    current_sum = temp
                #update the minimum sum value
                min_sum = min(min_sum, current_sum)
                i += 1
            return min_sum
        else:
            return None

def main():
    pass

if __name__ == '__main__':
    main()

