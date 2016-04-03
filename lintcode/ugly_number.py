# -*- coding: utf-8 -*-
"""
ugly_number.py
----------
Write a program to check whether a given number is an ugly number`.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 
For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

注意事项:
Note that 1 is typically treated as an ugly number.

样例:
Given num = 8 return true
Given num = 14 return false
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Apr 04,2016
"""

class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, num):
        if num <= 0:
            return False
        while True:
            if num == 1:
                return True
            if num % 2 == 0:
                num = num / 2
            elif num % 3 == 0:
                num = num / 3
            elif num % 5 == 0:
                num = num / 5
            else:
                return False

def main():
    pass

if __name__ == '__main__':
    main()