# -*- coding: utf-8 -*-
"""
sqrtx.py
--------
x的平方根
实现 int sqrt(int x) 函数，计算并返回 x 的平方根。

样例:
sqrt(3) = 1
sqrt(4) = 2
sqrt(5) = 2
sqrt(10) = 3

挑战:
O(log(x))

参考:
1.求0x5f3759df的数学原理:http://m.blog.csdn.net/article/details?id=42921601
2.开平方的7种方法:http://m.blog.csdn.net/article/details?id=8217866
3.整数开平方:http://m.blog.csdn.net/article/details?id=11537587
4.如何用牛顿法求一个数的平方根:http://www.nowamagic.net/librarys/veda/detail/2268
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 17,2016
"""
class Solution:
    """
    牛顿法
    """
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        if x > 0:
            guess = 10.0**(len(str(x))/2)
            error = 1e-3
            while True:
                temp = (x/guess + guess)/2.0
                if abs(temp**2 - x) < error:
                    break
                guess = temp
                print guess
            return int(guess)
        elif x == 0:
            return 0
        else:
            return None

def main():
    solution = Solution()
    print "使用牛顿法开平方:"
    n = raw_input("请输入需要开平方的整数:\n")
    n = int(n)
    print solution.sqrt(n)

if __name__ == '__main__':
    main()
