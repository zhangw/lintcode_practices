# -*- coding: utf-8 -*-
"""
single_number.py
----------------
落单的数
给出2*n + 1 个的数字，除其中一个数字之外其他每个数字均出现两次，找到这个数字。

样例:
给出 [1,2,2,1,3,4,3]，返回 4

挑战:
一次遍历，常数级的额外空间复杂度
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 16,2016
"""
class Solution:
    """
    一开始想用加减法把重复的数消去,但由于数组无序,用异或xor才是消除重复数的王道!
    xor使用的例子:
    1.a==b, a ^ b => 0, 相等性判断,重复数想消
    2.0 ^ a = a, 0和任何数异或返回本身
    3.-1 ^ -2**31-1 == 2**31-1, 对于int32,-1和最小的数异或,等于最大的正数,可以把一个负数转换成正数,求解其二进制中有多少个1.
    """
    """
    @param A : an integer array
    @return : a integer
    """
    def singleNumber(self, A):
        if A != None:
            length = len(A)
            #use xor operator to eliminate all the duplicates
            xor_ret = 0
            for i in range(0, len(A)):
                xor_ret ^= A[i]
            return xor_ret
        return None

def main():
    array = [1,2,2,1,3,4,3]
    print "消除重复项目之前的数组:", array
    solution = Solution()
    print "使用求异或和的方法消除所有重复项:", solution.singleNumber(array)

if __name__ == '__main__':
    main()
