# -*- coding: utf-8 -*-
"""
compare_strings.py
------------------
比较字符串
比较两个字符串A和B，确定A中是否包含B中所有的字符。字符串A和B中的字符都是大写字母。
样例:
给出 A = "ABCD" B = "ACD"，返回 true
给出 A = "ABCD" B = "AABC"， 返回 false
注意:
在 A 中出现的 B 字符串里的字符不需要连续或者有序。
-------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 21,2016
"""

class Solution:
    """
    @param A : A string includes Upper Case letters
    @param B : A string includes Upper Case letters
    @return :  if string A contains all of the characters in B return True else return False
    """
    def compareStrings(self, A, B):
        for char in B:
            char_count_B = B.count(char)
            char_count_A = A.count(char)
            if char_count_A < char_count_B:
                return False
            else:
                continue
        return True

def main():
    strA = raw_input("输入字符串A:\n")
    strA = strA.upper()
    strB = raw_input("输入字符串B:\n")
    strB = strB.upper()
    solution = Solution()
    print "result:%s" % solution.compareStrings(strA,strB) 

if __name__ == '__main__':
    main()

