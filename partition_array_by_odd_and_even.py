# -*- coding: utf-8 -*-
"""
partition_array_by_odd_and_even.py
----------------------------------
奇偶分割数组
分割一个整数数组，使得奇数在前偶数在后。

样例:
给定 [1, 2, 3, 4]，返回 [1, 3, 2, 4]。

挑战:
在原数组中完成，不使用额外空间。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 06,2016
"""
class Solution:
    # @param nums: a list of integers
    # @return: nothing
    def partitionArray(self, nums):
        if nums != None and len(nums):
            i = 0
            #prev_number_is_even = None
            last_odd_index = None
            length = len(nums)
            while i < length:
                temp = nums[i]
                temp_is_even = temp % 2 == 0
                if not temp_is_even:
                    if last_odd_index == None:
                        #initialize last_odd_index
                        nums[0],nums[i] = nums[i],nums[0]
                        last_odd_index = 0
                    elif nums[i-1] % 2 == 0:
                        #swap odd and even
                        last_odd_index += 1
                        nums[last_odd_index], nums[i] = nums[i], nums[last_odd_index]
                    else:
                        last_odd_index += 1
                i += 1

def main():
    n = raw_input("正在随机生成整数数组,请输入数组的长度,比如10:\n")
    n = int(n) if n != '' else 10
    import utils.RandomOrg.RandomOrgApi as random
    array = random.RandomOrgApi().integers.generate(num=n,min=-1*n,max=2*n,col=1,base=10,format="plain",rnd="new")
    print array
    solution = Solution()
    solution.partitionArray(array)
    print "奇偶分割的结果:", array

if __name__ == '__main__':
    main()
