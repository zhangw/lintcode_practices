# -*- coding: utf-8 -*-
"""
valid_palindrome.py
-------------------
有效回文串
给定一个字符串，判断其是否为一个回文串。只包含字母和数字，忽略大小写。

样例:
"A man, a plan, a canal: Panama" 是一个回文。
"race a car" 不是一个回文。

注意:
你是否考虑过，字符串有可能是空字符串？这是面试过程中，面试官常常会问的问题。
在这个题目中，我们将空字符串判定为有效回文。

挑战:
O(n) 时间复杂度，且不占用额外空间。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 19,2016
"""
class Solution:
    # @param {string} s A string
    # @return {boolean} Whether the string is a valid palindrome
    def isPalindrome(self, s):
        if s != None:
            if s == '':
                return True
            i = 0
            length = len(s)
            j = length-1
            #traverse from the beginning and end
            while i < j:
                if not s[i].isalnum():
                    i += 1
                    continue
                if not s[j].isalnum():
                    j -= 1
                    continue
                if s[i].lower() == s[j].lower():
                    i += 1
                    j -= 1
                    continue
                #in this case, must not be a valid palindrome
                else:
                    return False
            #in this case, must be a valid palindrome
            return True
        return False

def main():
    s = raw_input("请输入一个字符串:\n")
    solution = Solution()
    print "%s is%sa valid palindrome." % (s, ' ' if solution.isPalindrome(s) else ' not ')

if __name__ == '__main__':
    main()
