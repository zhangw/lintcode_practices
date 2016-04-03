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

class BetterSolution:
    """
    参考:http://blog.csdn.net/wutingyehe/article/details/46635767

    xor_ab = a ^ b
    如果xor_ab是负数，那么求解负数(补码)中1的个数等价于:
        xor_ab ^= -2**31(32位整数中的最小的负数,其补码为:10000000000000000000000000000000),
    xor_ab 此时除了符号位变成了0，其它位不变，所以xor_ab这个正数二进制中1的个数 + 1(负数符号位),
    就是负数二进制中1的个数
    求一个正数a的二进制1的个数除了使用bin和count函数，可以使用:
    while a > 0:
        counter += a % 2
        a /= 2
    
    综上:
    0:      00000000000000000000000000000000
    -1:     11111111111111111111111111111111
    -2**31: 10000000000000000000000000000000
    2**31-1:01111111111111111111111111111111
    使用这几个数，配合^ | &进行位运算，可以简化计算
    """
    pass

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

