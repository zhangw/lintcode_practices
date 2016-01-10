# -*- coding: utf-8 -*-
"""
binary_sum.py
-------------
给定两个二进制字符串，返回他们的和（用二进制表示）。
样例:
a = 11
b = 1
返回 100
--------
Created by <jimokanghanchao@gmail.com> on Jan 08,2016
"""

class Solution:
  def addBinary(self, a, b):
    """
    @param {string} a a number
    @param {string} b a number
    @return {string} the result  
    """
    a_bits = self._convert_binary_bits(a)
    b_bits = self._convert_binary_bits(b)
    ret = self._sum_by_plus_operator(a_bits,b_bits)
    return bin(ret)[2:]
  
  def _convert_binary_bits(self,num):
    #suppose without sign bit
    return '0b' + num

  def _sum_by_plus_operator(self,a_bits,b_bits):
    if a_bits != None and b_bits != None:
      return int(a_bits,2) + int(b_bits,2)
    else:
      return None

class SolutionWithoutPlusOperator(Solution):
  """
  Calculate the sum of two binary numbers without plus(+) operator.
  """
  def addBinary(self, a, b):
    a_bits = self._convert_binary_bits(a)
    b_bits = self._convert_binary_bits(b)
    a_bits = self._align_bits(a_bits)
    b_bits = self._align_bits(b_bits)
    ret = self._sum_without_plus_operator(a_bits,b_bits)
    return bin(ret)[2:]

  def _align_bits(self,bits):
    import sys
    #suppose without sign bit
    len_bits = int.bit_length(sys.maxint) + 1
    bits = bits[2:].zfill(len_bits)
    return bits

  def _sum_without_plus_operator(self,a_bits,b_bits):
    len_bits = len(a_bits)
    carry_bit = 0
    ret_bits = list('0'*len_bits)
    for pos in range(len_bits-1, -1, -1):
      a_bit = int(a_bits[pos])
      b_bit = int(b_bits[pos])
      bit_added = a_bit ^ b_bit
      if carry_bit == 1:
        bit_added ^= carry_bit
      ret_bits[pos] = str(bit_added)
      if (a_bit & b_bit == 1) or (a_bit & carry_bit == 1) or (b_bit & carry_bit == 1):
        carry_bit = 1
      else:
        carry_bit = 0
    if carry_bit == 1:
      warning = 'overflow the length of max unsigned integer'
      print warning
    #suppose without sign bit
    ret_bits = '0b' + ''.join(ret_bits)
    #int method can return long integer type if needed
    return int(ret_bits,2)

def main():
  a = raw_input("input the first binary,like 1010\n")
  b = raw_input("input the second binary,like 11\n")
  solution = Solution()
  solutionWithoutPlusOperator = SolutionWithoutPlusOperator()
  ret1 = solution.addBinary(a,b)
  ret2 = solutionWithoutPlusOperator.addBinary(a,b)
  if ret1 == ret2:
    print 'correct'
    print 'the sum is %s' % ret2
  else:
    print ret1
    print ret2
    print 'the two results of calculation not matched'

if __name__ == '__main__':
  main()

