# -*- coding: utf-8 -*-
"""
first_position_of_target.py
---------------------------
二分查找
给定一个排序的整数数组（升序）和一个要查找的整数target，
用O(logn)的时间查找到target第一次出现的下标（从0开始），如果target不存在于数组中，返回-1。
样例:
在数组 [1, 2, 3, 3, 4, 5, 10] 中二分查找3，返回2。
挑战:
如果数组中的整数个数超过了2^32，你的算法是否会出错？
--------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 23,2016
"""

class Solution:
    # @param nums: The integer array
    # @param target: Target number to find
    # @return the first position of target in nums, position start from 0 
    def binarySearch(self, nums, target):
        length = len(nums)
        #position of target
        position = 0
        #the last search direction indicates whether increase position value
        isleft = None
        #binary search
        while True:
            if length/2 > 0:
                if target < nums[0] or target > nums[-1]:
                    return -1
                leftarray = nums[:length/2]
                rightarray = nums[length/2+1:]
                middle = nums[length/2]
                if isleft == None:
                    #initialize position value
                    position = length/2
                elif isleft == True:
                    #last direction is left, decrease position value
                    #{a1,a2}a3{a4}, in this case, change position of a3 to a2
                    position -= length/2
                    if length%2 == 1:
                        #{a1,a2,a3}a4{a5,a6}, in this case, change position of a4 to a2
                        position -= 1
                else:
                    #last direction is right, increase position value
                    #{a1,a2}a3{a4,a5}, in this case, change position of a3 to a5
                    #{a1,a2}a3{a4,a5,a6}, in this case, change position of a3 to a5
                    position += length/2 + 1
                #direction is left
                if middle > target:
                    nums = leftarray
                    length = len(nums)
                    isleft = True
                elif middle == target:
                    #in order to search the first position of target
                    #{a1=1,a2=2,a3=2}a4=2{a5=3...}, in this case ,position of a4 shouldn't returned
                    #position of a2 is correct, so continue to search with leftarray
                    if leftarray[-1] == target:
                        nums = leftarray
                        length = len(nums)
                        isleft = True
                    else:
                        #target founded
                        return position
                #direction is right
                elif middle < target:
                    nums = rightarray
                    length = len(nums)
                    isleft = False
            #the current array just only have 0 or 1 number, end the binary search
            else:
                #target not exists
                if length == 0:
                    return -1
                if nums[0] != target:
                    return -1
                else:
                    #target founded
                    position = position - 1 if isleft else position + 1
                    return position
def main():
    str_array = raw_input("输入一个整数数组，比如:1,2,3,3,5,8,8,10\n")
    array = [int(s) for s in str_array.split(',')]
    array.sort()
    target = raw_input("输入要查找的整数值，比如3\n")
    target = int(target)
    solution = Solution()
    position = solution.binarySearch(array,target)
    print 'use index method of Array type to validate this calculation...'
    if position == array.index(target):
        print 'correct! the first position of %d is %d' % (target,position)

if __name__ == '__main__':
    main()
