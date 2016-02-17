# -*- coding: utf-8 -*-
"""
trailing_zeros.py
-----------------
设计一个算法，计算出n阶乘中尾部零的个数

样例
11! = 39916800，因此应该返回 2
挑战
O(logN)的时间复杂度
-------------------
Created by <jimokanghanchao@gmail.com> on Jan 08,2016
"""

class Solution:
  # @param n a integer
  # @return ans a integer
  def trailingZeros(self, n):
    #the trailing zeros only depends on the numbers of fator which is mutiples of 5.
    #for examples:
    #10! => 1*5,2*5, zeros:2 == 10/5
    #20! => 1*5,2*5,3*5,4*5, zeros:4 == 20/5
    #25! => 1*5,2*5,3*5,4*5,5*5, zeros:6 == 25/5+5/5
    #100! => ...,20*5, zeros:24 == 100/5 + 20/5
    #1000! => ...,200*5, zeros:249 = 1000/5 + 200/5 + 40/5 + 8/5
    #or:
    #10! => zeros:2 == 10/5
    #20! => zeros:4 == 20/5
    #25! => zeros:6 == 25/5 + 25/25
    #100! => zeros:24 == 100/5 + 100/25
    #1000! => zeros:249 == 1000/5 + 1000/25 + 1000/125 + 1000/625
    ret = 0
    if n < 1:
      return ret
    n /= 5
    while n >= 1:
      ret += n
      n /= 5
    return ret

def main():
  n = raw_input('输入n!阶乘的n值,比如11\n')
  n = int(n)
  solution = Solution()
  print '尾部的零有%d个' % solution.trailingZeros(n)

if __name__ == '__main__':
  main()
