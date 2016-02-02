# -*- coding: utf-8 -*-
"""
median.py
----------
中位数
给定一个未排序的整数数组，找到其中位数。
中位数是排序后数组的中间值，如果数组的个数是偶数个，则返回排序后数组的第N/2个数。

样例:
给出数组[4, 5, 1, 2, 3]， 返回 3
给出数组[7, 9, 4, 5]，返回 5

挑战:
时间复杂度为O(n)
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 02,2016
"""

class Solution:
    def middleNumber(self, nums, start, last, nth):
        """
        @param nums, the integer array
        @param start, the start index of the array
        @param last, the end index, but not include itself.
            for example: a = [1,2,3,4]
            a[0:4] means a[0],a[1],a[2],a[3]
            in this case start is 0, and last is 4
        @parem nth, the nth number in array that this number is greater or equal than the first number (include the first number)
            for example: a = [1,2,3,4]
            the number 1 is the 1st big number
            the number 4 is the 4th big number
            if nth == (N+1)/2 (N is length of the array), the nth number is the median of the array
        @return median of the sorted array
        """
        if nums != None:
            length = len(nums)
            if length == 0:
                return None
            elif length == 1:
                return nums[0]
            else:
                #the numbers of elements required to sort
                if last - start < 2:
                    #only one element, do nothing
                    return nums
                pivot = nums[start]
                i = start + 1
                j = last - 1
                #put the smaller on the left, put the bigger on the right
                while i <= j:
                    if nums[i] < pivot:
                        i += 1
                        continue
                    if nums[j] >= pivot:
                        j -= 1
                        continue
                    #swap the position when the smaller on the right and the bigger on the left
                    nums[i],nums[j] = nums[j],nums[i]
                #index of i-1 indicates the last number less than pivot
                #swap pivot and the number
                #index of i-1 indicates the pivot number
                #index of i indidates the first number not less than pivot
                nums[i-1], nums[start] = pivot, nums[i-1]
                nth_of_pivot = i - start
                if nth_of_pivot == nth:
                    #in this case, pivot is just the nth number
                    return pivot
                elif nth_of_pivot < nth:
                    #must on the right
                    return self.middleNumber(nums, i, last, nth - nth_of_pivot)
                else:
                    #must on the left
                    return self.middleNumber(nums, start, i, nth)
        else:
            return None
    
    """
    @param nums: A list of integers.
    @return: An integer denotes the middle number of the array.
    """
    def median(self, nums):
        middle = (len(nums) + 1)/2
        return self.middleNumber(nums, 0, len(nums), middle)

def main():
    n = raw_input("使用random.org生成随机正数数组,请输入数组的长度,比如10:")
    n = int(n) if n != '' else 10
    import utils.RandomOrg.RandomOrgApi as random
    array = random.RandomOrgApi().integers.generate(num=n,min=1,max=n,col=1,base=10,format="plain",rnd="new")
    print array
    solution = Solution()
    median = solution.median(array)
    print "数组中位数:%d" % median

if __name__ == '__main__':
    main()

