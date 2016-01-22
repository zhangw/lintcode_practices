# -*- coding: utf-8 -*-
"""
count_1_in_binary.py
--------------------
二进制中有多少个1
计算在一个 32 位的整数的二进制表式中有多少个 1.

样例:
给定 32 (100000)，返回 1
给定 5 (101)，返回 2
给定 1023 (1111111111)，返回 10
-----------------------------
Created by <jimokanghanchao@gmail.com> on Jan 22,2016
"""

class Solution:
    # @param num: an integer
    # @return: an integer, the number of ones in num
    def countOnes(self, num):
        if num >= 0:
            count = 0
            while num !=0:
                if num%2 != 0:
                    count += 1
                num = num/2
            #only 0 has 0 number of 1, at least 1 for the other values
            if count == 0 and num != 0:
                return 1
            return count
        else:
            MIN_NEGATIVE_32bit = -2**(32-1)
            if num < MIN_NEGATIVE_32bit:
                print 'error: out of range'
                return -1
            #IMPORTANT:sign bit is one, all the other bits is zero
            #this kind of compliment bits represent negative value of the positive value 
            #represented by the same bits but without sign bit
            elif num == MIN_NEGATIVE_32bit:
                #the representation of compliment bits:10000000000000000000000000000000
                return 1
            #the sign bit must be 1
            count = 1
            #convert the negative integer to representation of compliment bits
            #firstly return the bits of positive value
            original_bits = bin(num * -1)[2:]
            #exclude sign bit
            bits_without_sign = original_bits.zfill(32-1)
            #invert bits
            invert_bits = bits_without_sign.replace('0','r').replace('1','0').replace('r','1')
            #the result if invert bits add 1
            if invert_bits.count('0') == 0:
                return count
            elif invert_bits[-1] == '0':
                count += invert_bits.count('1') + 1
                return count
            else:
                carry_bit = 0
                for i in range(31-1,-1,-1):
                    if i == 30:
                        carry_bit = 1
                    if carry_bit == 1:
                        if invert_bits[i] == '0':
                            count += 1
                            carry_bit = 0
                    else:
                        if invert_bits[i] == '1':
                            count += 1
                return count

def main():
    i = raw_input('输入一个整数:\n')
    i = int(i)
    solution = Solution()
    count = solution.countOnes(i)
    print '2进制表示法(补码)中含有1的个数:%d' % count

if __name__ == '__main__':
    main()

