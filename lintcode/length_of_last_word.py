# -*- coding: utf-8 -*-
"""
length_of_last_word.py
----------------------
最后一个单词的长度
给定一个字符串， 包含大小写字母、空格' '，请返回其最后一个单词的长度。
如果不存在最后一个单词，请返回 0 。

样例:
给定 s = "Hello World"，返回 5。

注意:
一个单词的界定是，由字母组成，但不包含任何的空格。
------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 26,2016
"""
class Solution:
    # @param {string} s A string
    # @return {int} the length of last word
    def lengthOfLastWord(self, s):
        if s == None:
            return 0
        else:
            splits = s.split(' ')
            while True:
                if len(splits) >= 1:
                    w = splits.pop()
                    if w.isalpha():
                        return len(w)
                    continue
                else:
                    return 0

def main():
    s = raw_input("请输入一个字符串，允许包含小大写字母和空格:\n")
    solution = Solution()
    length = solution.lengthOfLastWord(s)
    if length == 0:
        print "不存在最后一个单词"
    else:
        print "最后一个单词长度为:%d" % length

if __name__ == '__main__':
    main()

