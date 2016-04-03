# -*- coding: utf-8 -*-
"""
rotate_string.py
----------------
旋转字符串
给定一个字符串和一个偏移量，根据偏移量旋转字符串(从左向右旋转)

样例:
对于字符串 "abcdefg",
offset=0 => "abcdefg"
offset=1 => "gabcdef"
offset=2 => "fgabcde"
offset=3 => "efgabcd"

挑战:
在数组上原地旋转，使用O(1)的额外空间
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 16,2016
"""
class Solution:
    # @param s: a list of char
    # @param offset: an integer 
    # @return: nothing
    def rotateString(self, s, offset):
        if s != None and len(s) and offset >= 0:
            length = len(s)
            offset = offset % length
            i = length-offset
            while i < length:
                temp = s[i]
                #move the elements one of which index that less than i backward
                for j in range(i-1,(i+offset)%length-1,-1):
                    s[j+1] = s[j]
                #move the element of which index that greater than i to the beginning
                s[j] = temp
                i += 1
def main():
    chars = raw_input("请输入一个字符串:\n")
    chars = list(chars)
    offset = raw_input("请输入用于旋转字符串的偏移量的值:\n")
    offset = int(offset)
    solution = Solution()
    print "旋转(从左向右)后的字符串:"
    solution.rotateString(chars, offset)
    print "".join(chars)

if __name__ == '__main__':
    main()
