# -*- coding: utf-8 -*-
"""
recover_rotated_sorted_array.py
-------------------------------
恢复旋转排序数组
给定一个旋转排序数组，在原地恢复其排序。

样例:
[4, 5, 1, 2, 3] -> [1, 2, 3, 4, 5]

挑战:
使用O(1)的额外空间和O(n)时间复杂度

说明:
什么是旋转数组？
比如，原始数组为[1,2,3,4], 则其旋转数组可以是[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 15,2016
"""
class Solution:
    """
    @param nums: The rotated sorted array
    @return: nothing
    """
    def recoverRotatedSortedArray(self, nums):
        if nums != None:
            length = len(nums)
            if length > 1:
                temp = nums[0]
                i = 1
                while i < length:
                    #search the pivot element which is the max number
                    if nums[i] >= temp:
                        temp = nums[i]
                        i += 1
                        continue
                    else:
                        #recover
                        for j in range(i,length):
                            #the pivot element of which index is i-1
                            temp = nums[j]
                            #move the sub sequence backward
                            for k in range(j-1,j-i-2,-1):
                                nums[k+1] = nums[k]
                            #move the small number in front of the array
                            nums[j-i] = temp
                        break
def main():
    n = raw_input("输入整数数组的长度,比如10:\n")
    n = int(n) if n != '' else 10
    import utils.RandomOrg.RandomOrgApi as random
    api = random.RandomOrgApi()
    array = api.integers.generate(num=n,min=0,max=n,col=1,base=10,format="plain",rnd="new")
    array.sort()
    rotated = array[n/2:]+array[:n/2]
    print "随机生成的旋转排序数组:", rotated
    solution = Solution()
    solution.recoverRotatedSortedArray(rotated)
    print "恢复排序的数组:", rotated

if __name__ == '__main__':
    main()

