# -*- coding: utf-8 -*-
"""
maximum_subarray.py
-------------------
最大子数组
给定一个整数数组，找到一个具有最大和的子数组，返回其最大和。

样例:
给出数组[−2,2,−3,4,−1,2,1,−5,3]，符合要求的子数组为[4,−1,2,1]，其最大和为6

注意:
子数组最少包含一个数

挑战:
要求时间复杂度为O(n)
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 28,2016
"""

class Solution:
    """
    @param nums: A list of integers
    @return: An integer denote the sum of maximum subarray
    """
    def maxSubArray(self, nums):
        if nums == None:
            return None
        else:
            length = len(nums)
            if length == 0:
                return None
            i = 1
            #the child array must have at least one number
            #so initialize them with nums[0] value
            subarray_max_sum = nums[0]
            #the sum of current sub array
            subarray_sum = nums[0]
            while i < length:
                temp = nums[i]
                if subarray_sum < 0:
                    #reinitialize the sub array
                    subarray_sum = temp
                else:
                    if subarray_sum + temp <= 0:
                        #reinitialize the sub array
                        subarray_sum = temp
                    else:
                        #update the sum of current sub array
                        subarray_sum += temp
                #update the maximum value if needed
                if subarray_sum > subarray_max_sum:
                    subarray_max_sum = subarray_sum
                i += 1
            return subarray_max_sum

def main():
    n = raw_input("正在随机生成一个整数数组,数值范围[-10,10],请输入数组的长度N,比如10:\n")
    n = int(n) if n != '' else 10
    array = []
    import random
    for i in range(0,n):
        array.append(int(random.random()*20)-10)
    print array
    solution = Solution()
    print "子数组的最大和:%d" % solution.maxSubArray(array)

if __name__ == '__main__':
    main()

