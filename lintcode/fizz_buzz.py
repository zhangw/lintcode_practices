# -*- coding: utf-8 -*-
"""
fizz_buzz.py
------------
给你一个整数n. 从 1 到 n 按照下面的规则打印每个数：
如果这个数被3整除，打印fizz.
如果这个数被5整除，打印buzz.
如果这个数能同时被3和5整除，打印fizz buzz.
样例:
比如 n = 15, 返回一个字符串数组：
["1", "2", "fizz","4", "buzz", "fizz","7", "8", 
"fizz","buzz", "11", "fizz","13", "14", "fizz buzz"]
----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 23,2016
"""
class Solution:
    """
    @param n: An integer as description
    @return: A list of strings.
    For example, if n = 7, your code should return
        ["1", "2", "fizz", "4", "buzz", "fizz", "7"]
    """
    def fizzBuzz(self, n):
        ret = []
        for value in range(1,n+1):
            if value%15 == 0:
                ret.append("fizz buzz")
            elif value%3 == 0:
                ret.append("fizz")
            elif value%5 == 0:
                ret.append("buzz")
            else:
                ret.append(str(value))
        return ret

def main():
    n = raw_input("输入一个整数:\n")
    n = int(n)
    solution = Solution()
    print solution.fizzBuzz(n)
if __name__ == '__main__':
    main()

