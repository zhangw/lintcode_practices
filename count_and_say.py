# -*- coding: utf-8 -*-
"""
count_and_say.py
----------------
报数指的是，按照其中的整数的顺序进行报数，然后得到下一个数。如下所示：
1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211...
1 读作 "one 1" -> 11.
11 读作 "two 1s" -> 21.
21 读作 "one 2, then one 1" -> 1211.
给定一个整数 n, 返回 第 n 个顺序。
样例:
给定 n = 5, 返回 "111221".
给定 n = 6, 返回 "312211".
注意:
整数的顺序将表示为一个字符串.
-------------------------
Created by <jimokanghanchao@gmail.com> on Jan 23,2016
"""
class Solution:
    """
    使用递归的方法计算报数序列
    """
    def __init__(self):
        #cache the result to reduce duplicate calculation
        self.caches = {1:"1"}

    # @param {int} n the nth
    # @return {string} the nth sequence
    def countAndSay(self, n):
        if n <= 0:
            return ""
        if n == 1:
            return self.caches[n]
        #use recursive way to get the last string in sequence
        if self.caches.has_key(n-1):
            #return item from caches
            last_str = self.caches[n-1]
        else:
            last_str = self.countAndSay(n-1)
        #push every result of counting into it
        ret = []
        index = 0
        length = len(last_str)
        last_char = last_str[0]
        last_char_count = 0
        #use a loop to build the counter
        while index < length:
            current_char = last_str[index]
            if current_char == last_char:
                last_char_count += 1
            else:
                ret.append(str(last_char_count) + last_char)
                last_char = current_char
                last_char_count = 1
            if index == length - 1:
                ret.append(str(last_char_count) + last_char)
            index += 1
        #update the caches
        self.caches[n] = "".join(ret)
        return self.caches[n]

def main():
    n = raw_input("输入报数序列的第N项的N值:\n")
    n = int(n)
    solution = Solution()
    print solution.countAndSay(n)
    pass

if __name__ == '__main__':
    main()

