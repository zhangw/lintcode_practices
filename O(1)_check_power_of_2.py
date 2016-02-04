# -*- coding: utf-8 -*-
"""
O(1)_check_power_of_2.py
------------------------
O(1)时间检测2的幂次
用 O(1) 时间检测整数 n 是否是 2 的幂次。

样例:
n=4，返回 true;
n=5，返回 false.

注意:
O(1) 时间复杂度
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 04,2016
"""

class Solution:
    """
    @param n: An integer
    @return: True or false
    """
    def checkPowerOf2(self, n):
        #suppose the max integer is 64 bits
        m = 2**64
        #m must be exactly divisible by n if n is power of 2.
        #if n <= 1, return false
        return n >= 1 and m % n == 0

def main():
    pass

if __name__ == '__main__':
    main()