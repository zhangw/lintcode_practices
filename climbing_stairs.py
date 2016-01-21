# -*- coding: utf-8 -*-
"""
climbing_stairs.py
------------------
爬楼梯
假设你正在爬楼梯，需要n步你才能到达顶部。但每次你只能爬一步或者两步，你能有多少种不同的方法爬到楼顶部？

样例:
比如n=3，1+1+1=1+2=2+1=3，共有3中不同的方法
返回 3
-----
Created by <jimokanghanchao@gmail.com> on Jan 21,2016
"""
class Solution:
    """
    这个问题可以转化成求斐波纳契数列的第N项
    """
    def __init__(self):
        #cache the result to avoid duplicate calculation
        self.caches = {1:1,2:2}

    """
    @param n: An integer
    @return: An integer
    """
    def climbStairs(self, n):
        if n <= 0:
            return 1
        if n == 1 or n == 2:
            return self.caches[n]
        if n >= 3:
            if self.caches.has_key(n-1):
                n_1 = self.caches[n-1]
            else:
                n_1 = self.climbStairs(n-1)
            if self.caches.has_key(n-2):
                n_2 = self.caches[n-2]
            else:
                n_2 = self.caches[n-2]
            self.caches[n] = n_1 + n_2
        return self.caches[n]

def main():
    pass

if __name__ == '__main__':
    main()