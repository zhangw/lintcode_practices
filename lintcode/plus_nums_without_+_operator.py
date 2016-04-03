# -*- coding: utf-8 -*-
"""
plus_nums_without_+.py

计算两正数数的和，但是不用+操作符
Created by <jimokanghanchao@gmail.com> on Jan 05,2016
"""

def main():
  a = raw_input('input integer a:')
  b = raw_input('input integer b:')
  try:
    a = int(a)
    b = int(b)
  except:
    print 'input error, please input integer' 
  else:
    if aplusb(a,b) == a+b:
      print 'correct'
    else:
      print 'wrong or an error occured'

def aplusb(a, b):
  """
  @param a: The first integer
  @param b: The second integer
  @return:  The sum of a and b
  """
  import sys
  sys_int_bit_length = len(bin(sys.maxint)[2:])+1#include the sign bit
  if int.bit_length(a) < sys_int_bit_length and int.bit_length(b) < sys_int_bit_length:
    a_complement_bits = _get_complement_bits(a,bit_length=sys_int_bit_length)
    b_complement_bits = _get_complement_bits(b,bit_length=sys_int_bit_length)
    print 'complement bits of a:%s' % a_complement_bits
    print 'complement bits of b:%s' % b_complement_bits
    a_plus_b = _plus_with_bits(a_complement_bits,b_complement_bits,bit_length=sys_int_bit_length)
    print 'a plus b:%d' % a_plus_b
    return a_plus_b
  else:
    print 'a or b is not an integer'
    return None

def _plus_with_bits(a_bits,b_bits,bit_length=32):
  """
  @return: convert the complement bits code to decimal value
  """
  ret_bits = _get_complement_plus_with_bits(a_bits,b_bits,bit_length)
  if ret_bits[0] == '1':
    #if the representation of negative bits
    positive_bits = _reverse_and_plus_one(ret_bits,bit_length)
    #exclude the sign bit and use '-0b' to represent the negative value
    ret_bits = "".join(['-0b',positive_bits[1:]])
    return int(ret_bits,2)
  #exclude the sign bit and directly to get the positive value
  return int(ret_bits[1:],2)

def _get_complement_plus_with_bits(a_bits,b_bits,bit_length=32):
  """
  @return: plus the complement bits code of the two integers
  """
  ret_bits = list('0'*bit_length)
  carry_bit = 0
  for pos in range(bit_length-1,-1,-1):
    cur_bit_a = int(a_bits[pos])
    cur_bit_b = int(b_bits[pos])
    cur_bit_plused = cur_bit_a ^ cur_bit_b#xor 
    if pos == bit_length - 1:
      ret_bits[pos] = str(cur_bit_plused)
      carry_bit = 1 if cur_bit_a == 1 and cur_bit_b == 1 else 0
    else:
      if carry_bit == 0:
        ret_bits[pos] = str(cur_bit_plused)
        carry_bit = 1 if cur_bit_a == 1 and cur_bit_b == 1 else 0
      else:
        cur_bit_plused_with_carry_bit = cur_bit_plused ^ carry_bit#xor
        ret_bits[pos] = str(cur_bit_plused_with_carry_bit)
        carry_bit = 1 if (cur_bit_plused == 1 or (cur_bit_a == 1 and cur_bit_b == 1)) and carry_bit == 1 else 0
  ret_bits = "".join(ret_bits)
  if carry_bit == 1:
    print "the plus operation overflowed"
  return ret_bits

def _get_complement_bits(integer_value,bit_length=32):
  """
  @return: the complement bits code of integer 
  """
  if integer_value >= 0:
    #remove '0b' and fill with '0000...'
    return bin(integer_value)[2:].zfill(bit_length)
  else:
    #remove '-0b' and fill with '0000...'
    #get the Sign-Magnitude
    positive_bits = bin(integer_value)[3:].zfill(bit_length)
    complement_bits = _reverse_and_plus_one(positive_bits,bit_length)
    return complement_bits

def _reverse_and_plus_one(bits,bit_length=32):
    #get the reverse bits
    reverse_bits = bits.replace('0','-').replace('1','0').replace('-','1')
    #reverse + 1
    complement_bits_one = _get_complement_bits(1,bit_length)
    complement_bits = _get_complement_plus_with_bits(reverse_bits,complement_bits_one,bit_length)
    return complement_bits

if __name__ == '__main__':
  main()
