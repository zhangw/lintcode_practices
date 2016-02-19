# -*- coding: utf-8 -*-
"""
two_strings_are_anagrams.py
---------------------------
两个字符串是变位词
写出一个函数 anagram(s, t) 去判断两个字符串是否是颠倒字母顺序构成的

样例:
给出 s="abcd"，t="dcab"，返回 true
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 19,2016
"""
class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        if s and t:
            l1 = len(s)
            l2 = len(t)
            if l1 == l2:
                i = 0
                while i < l1:
                    char = s[i]
                    if s.count(char) == t.count(char):
                        i += 1
                        continue
                    return False
                return True
            return False
        return False

def main():
    pass

if __name__ == '__main__':
    main()
