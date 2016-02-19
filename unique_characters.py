# -*- coding: utf-8 -*-
"""
unique_characters.py
--------------------
判断字符串是否没有重复字符
实现一个算法确定字符串中的字符是否均唯一出现

样例:
给出"abc"，返回 true
给出"aab"，返回 false

挑战:
如果不使用额外的存储空间，你的算法该如何改变？
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 19,2016
"""
class Solution:
    # @param s: a string
    # @return: a boolean
    def isUnique(self, str):
        if str:
            length = len(str)
            if length:
                i = 0
                while i < length:
                    if str.count(str[i]) == 1:
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
