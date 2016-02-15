# -*- coding: utf-8 -*-
"""
reverse_integer.py
------------------
反转整数
将一个整数中的数字进行颠倒，当颠倒后的整数溢出时，返回 0 (标记为 32 位整数)。

样例:
给定 x = 123，返回 321
给定 x = -123，返回 -321
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 15,2016
"""
class Solution:
    # @param {int} n the integer to be reversed
    # @return {int} the reversed integer
    def reverseInteger(self, n):
        if n == 0:
            return 0
        negative = False
        if n < 0:
            negative = True
            n *= -1
        temp = []
        #reverse digits from original integer
        while n > 0:
            temp.append(n%10)
            n = n/10
        length = len(temp)
        sum = 0
        #get the new integer with the reverse digits
        for i in range(0,length):
            sum += 10**(length-1-i)*temp[i]
        if negative == True:
            sum *= -1
        if sum > 2**31-1 or sum < -2**31:
            return 0
        return sum

def main():
    str_integer = raw_input("请输入一个整数:\n")
    if str_integer == '' or str_integer.isalpha():
        print "输入格式错误"
    else:
        if str_integer.isdigit():
            integer = int(str_integer, 10)
        else:
            strs = str_integer.split('-')
            if len(strs) == 2 and strs[0] == '' and strs[1].isdigit():
                integer = int(str_integer, 10)
            else:
                print "输入格式错误"
                return
        solution = Solution()
        print "%d反转之后的整数是%d(如果溢出32位,返回0)" % (integer, solution.reverseInteger(integer))

if __name__ == '__main__':
    main()