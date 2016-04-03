# -*- coding: utf-8 -*-
"""
space_replacement.py
--------------------
空格替换
设计一种方法，将一个字符串中的所有空格替换成 %20 。你可以假设该字符串有足够的空间来加入新的字符，且你得到的是“真实的”字符长度。
你的程序还需要返回被替换后的字符串的长度。

样例:
对于字符串"Mr John Smith", 长度为 13
替换空格之后的结果为"Mr%20John%20Smith"

注意:
如果使用 Java 或 Python, 程序中请用字符数组表示字符串。

挑战:
在原字符串(字符数组)中完成替换，不适用额外空间
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 17,2016
"""
class Solution:
    # @param {char[]} string: An array of Char
    # @param {int} length: The true length of the string
    # @return {int} The true length of new string
    def replaceBlank(self, string, length):
        if string != None:
            i = 0
            while i < length:
                temp = string[i]
                if temp == ' ':
                    string[i] = '%'
                    if i < length-1:
                        #move backward
                        for j in range(length-1,i,-1):
                            string[j+2] = string[j]
                        #extend the length
                        length += 2
                        string[i+1] = '2'
                        string[i+2] = '0'
                        i += 3
                        continue
                    #consider if the whitespace in the end
                    else:
                        length += 2
                        string[i+1] = '2'
                        string[i+2] = '0'
                        break
                else:
                    i += 1
            return length

def main():
    strings = raw_input("请输入一个字符串(至少包含一个空格):\n")
    length = len(strings)
    whitespaces = strings.count(' ')*2
    strings = list(strings) + ['']*whitespaces
    solution = Solution()
    solution.replaceBlank(strings, length)
    print "字符串的空格被替换为%20:"
    print strings
    print "".join(strings)

if __name__ == '__main__':
    main()
