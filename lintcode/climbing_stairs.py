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
                n_2 = self.climbStairs[n-2]
            self.caches[n] = n_1 + n_2
        return self.caches[n]

class AnotherSolution():
    """
    使用排列的方法进行计算，假如楼梯数有N层，那么爬楼的方法等价于求解：
    没有2出现的组合+一个2出现在不同位置的组合+2个2出现在不同位置的组合+3个2...
    比如楼梯数为3:
    3可以包含的2的个数为3/2=1，那么没有2出现的组合为C(3,0)，一个2出现在不同位置的组合为C(2,1)
    结果为C(3,0)+C(2,1)
    同理，楼梯数为4时：
    结果为C(4,0)+C(3,1)+C(2,2)
    楼梯数为5时：
    结果为C(5,0)+C(4,1)+C(3,2)
    """
    def climbStairs(self, n):
        if n>= 1:
            m = n/2
            if m >= 1:
                ret = 0
                for s in range(0, m+1):
                    ret += self.c(n,s)
                    n -= 1
                return ret
            else:
                return 1
        else:
            return 1
        
    def c(self, m, n):
        """
        计算组合C(m,n)的值
        """
        if m >= 1 and n >= 0:
            if n == 0:
                return 1
            if n == 1:
                return m
            if m < n:
                return None
            else:
                #C(m,n) == C(m,m-n)
                if n*2 > m:
                    n = m - n
                #a = m * m-1 * m-2 ...
                a, b = 1, 1
                for value in range(m, m-n, -1):
                    a *= value
                #b = n!
                for value in range(n, 0, -1):
                    b *= value
                #C(m,n) == a/b
                return a/b
        else:
            return None

def main():
    solution = AnotherSolution()
    stairs = raw_input("请输入楼梯数:\n")
    stairs = int(stairs)
    print "爬楼的方法有%d种" % solution.climbStairs(stairs)

if __name__ == '__main__':
    main()
