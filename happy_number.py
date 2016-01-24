# -*- coding: utf-8 -*-
"""
happy_number.py
---------------
快乐数
写一个算法来判断一个数是不是"快乐数"。
一个数是不是快乐是这么定义的：对于一个正整数，每一次将该数替换为他每个位置上的数字的平方和，
然后重复这个过程直到这个数变为1，或是无限循环但始终变不到1。如果可以变为1，那么这个数就是快乐数。

样例：
19 就是一个快乐数。
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1

参考:
http://segmentfault.com/a/1190000003481340
http://jandan.net/2012/08/19/nemesis-of-happy.html
不是快乐数的数称为不快乐数（unhappy number），所有不快乐数的数位平方和计算，
最后都会进入 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 的循环中。
-------------------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 24,2016
"""

class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        if n == 0:
            return False
        else:
            #use a list to save all the numbers during the loop
            numbers = [n]
            while True:
                strn = str(n)
                #if number == 10**i(i=0,1,2,...n)
                if strn[0] == '1' and strn[1:].count('0') == len(strn)-1:
                    print 'happy number founded', numbers
                    return True
                else:
                    #recalculate the number
                    n = sum([int(s)**2 for s in strn])
                    if n in numbers:
                        #infinite loop
                        print 'encounter an infinite loop:\n', '%s => %d is already in %s' % (strn, n, numbers)
                        return False
                    else:
                        numbers.append(n)
def main():
    n = raw_input("输入一个正整数，判断其是否为快乐数\n")
    n = int(n)
    solution = Solution()
    if solution.isHappy(n):
        print "%d is a happy number" % n
    else:
        print "%d isn't a happy number" % n

if __name__ == '__main__':
    main()