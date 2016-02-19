# -*- coding: utf-8 -*-
"""
valid_parentheses.py
--------------------
有效的括号序列
给定一个字符串所表示的括号序列，包含以下字符： '(', ')', '{', '}', '[' and ']'， 判定是否是有效的括号序列。

样例:
括号必须依照 "()" 顺序表示， "()[]{}", "{([])}" 是有效的括号，但 "([)]"则是无效的括号。

挑战:
O(n)的时间，n为括号的个数
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 19,2016
"""
class Solution:
    # @param {string} s A string
    # @return {boolean} whether the string is a valid parentheses
    def isValidParentheses(self, s):
        if s != None:
            length = len(s)
            stack = []
            i = 0
            while i < length:
                if len(stack) == 0:
                    stack.append(s[i])
                else:
                    if (s[i] == ")" and stack[-1] == "(") \
                    or (s[i] == "}" and stack[-1] == "{") \
                    or (s[i] == "]" and stack[-1] == "["):
                        stack.pop()
                    else:
                        stack.append(s[i])
                i += 1
                continue
            return len(stack) == 0
        return False

def main():
    parentheses = raw_input("输入只包含([{}])这6个字符的字符串:\n")
    parentheses = parentheses.replace(' ','')
    for c in parentheses:
        if c not in list("([{}])"):
            raise Exception("输入字符串格式错误!")
    solution = Solution()
    print "%s is%sa valid parentheses" % (parentheses, ' ' if solution.isValidParentheses(parentheses) else ' not ')

if __name__ == '__main__':
    main()
