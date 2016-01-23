# -*- coding: utf-8 -*-
"""
flip_bits.py
------------
将整数A转换为B
如果要将整数A转换为B，需要改变多少个bit位？

样例:
如把31转换为14，需要改变2个bit位。
(31)10=(11111)2
(14)10=(01110)2
挑战:
你能想出几种方法？
---------------
Created by <jimokanghanchao@gmail.com> on Jan 24,2016
"""

class Solution:
    """
    use xor result of a, b to calculate.
    @param a, b: Two integer
    return: An integer
    """
    def bitSwapRequired(self, a, b):
        xor_ab = a ^ b
        #count '1' in bits of xor result if the result is positive value
        if xor_ab >= 0:
            return bin(xor_ab).count('1')
        else:
            #suppose 32 bits integer
            MAX_BITS_LEN = 32
            #use compliment bits to represent negative value
            bits_without_sign = bin(xor_ab)[3:].zfill(MAX_BITS_LEN - 1)
            bits_inverted = bits_without_sign.replace('1','r').replace('0','1').replace('r','0')
            carry_bit = None
            #the sign bit must be '1', so initialize the counter with 1
            count_1_of_compliment_bits = 1
            #calculate the compliment bits by adding 1 to bits_inverted
            for i in range(len(bits_inverted)-1,-1,-1):
                if carry_bit == None:
                    if bits_inverted[i] == '1':
                        carry_bit = 1
                        continue
                else:
                    if bits_inverted[i] == '1' and carry_bit == 1:
                        continue
                    if bits_inverted[i] == '0' and carry_bit == 0:
                        continue
                count_1_of_compliment_bits += 1
                carry_bit = 0
            return count_1_of_compliment_bits

def main():
    ab = raw_input("请输入两个整数a和b，比如:-1,1\n")
    ab = ab.split(',')
    a = int(ab[0])
    b = int(ab[1])
    solution = Solution()
    print "把%d转换为%d，需要改变%d个bit位" % (a,b,solution.bitSwapRequired(a,b))

if __name__ == '__main__':
    main()

