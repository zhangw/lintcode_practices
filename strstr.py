# -*- coding: utf-8 -*-
"""
strstr.py
----------
字符串查找
对于一个给定的 source 字符串和一个 target 字符串，你应该在 source 字符串中找出 target 字符串出现的第一个位置(从0开始)。如果不存在，则返回-1。

样例:
如果 source = "source" 和 target = "target"，返回 -1。
如果 source = "abcdabcdefg" 和 target = "bcd"，返回 1。

挑战:
O(n2)的算法是可以接受的。如果你能用O(n)的算法做出来那更加好。（提示：KMP

参考:
KMP算法的介绍:http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 21,2016
"""
class Solution:
    def strStr(self, source, target):
        # write your code here
        return -1

class RegularSolution:
    def strStr(self, source, target):
        if source != None and target != None:
            length_of_src = len(source)
            length_of_tgt = len(target)
            if length_of_tgt == 0:
                return 0
            if length_of_src and length_of_tgt:
                if length_of_src >= length_of_tgt:
                    i = 0
                    j = 0
                    #notice that plus 1
                    while i < length_of_src - length_of_tgt + 1:
                        if source[i] == target[j]:
                            k = i
                            while j < length_of_tgt:
                                if j == length_of_tgt - 1:
                                    #notice that plus 1
                                    return i - length_of_tgt + 1
                                i += 1
                                j += 1
                                if source[i] == target[j]:
                                    continue
                                else:
                                    j = 0
                                    #just move backward with 1 step
                                    i = k+1
                                    break
                            continue
                        else:
                            i += 1
        return -1

def main():
    source = raw_input("输入一个字符串作为源字符串:\n")
    target = raw_input("输入一个需要在源字符串中进行匹配的目标字符串:\n")
    print "使用常规方法查找目标字符串:"
    print "%s在%s中的位置是%d" % (target, source, RegularSolution().strStr(source, target))

if __name__ == '__main__':
    main()
