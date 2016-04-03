# -*- coding: utf-8 -*-
"""
reverse_words_in_a_string.py
----------------------------
翻转字符串
给定一个字符串，逐个翻转字符串中的每个单词。

样例:
给出s = "the sky is blue"，返回"blue is sky the"

说明:
单词的构成：无空格字母构成一个单词
输入字符串是否包括前导或者尾随空格？可以包括，但是反转后的字符不能包括
如何处理两个单词间的多个空格？在反转字符串中间空格减少到只含一个
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 16,2016
"""
class Solution:
    # @param s : A string
    # @return : A string
    def reverseWords(self, s):
        if s != None:
            if len(s):
                words = s.split(' ')
                reversed = ''
                length = len(words)
                i = length - 1
                #traverse words from the end
                while i >= 0:
                    #ignore all the whitespaces
                    if words[i] == '':
                        del words[i]
                        length -= 1
                    else:
                        #reverse words
                        reversed += words[i]
                        if i > 0:
                            reversed += ' '
                    i -= 1
                return reversed
            return s
        return None

def main():
    string = raw_input("请输入一个字符串,无空格字母构成一个单词:\n")
    solution = Solution()
    print "翻转字符串:"
    print solution.reverseWords(string)

if __name__ == '__main__':
    main()
