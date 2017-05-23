# -*- coding: utf-8 -*-
"""
flatten_list.py
----------
给定一个列表，该列表中的每个要素要么是个列表，要么是整数。
将其变成一个只包含整数的简单列表。

样例
给定 [1,2,[1,2]]，返回 [1,2,1,2]。
给定 [4,[3,[2,[1]]]]，返回 [4,3,2,1]。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on May 22,2017
"""

import pdb
class Solution(object):
    # @param nestedList a list, each element in the list 
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        prev_nested_list = []
        ret = []
        if nestedList is not None:
            if type(nestedList) == int:
                ret.append(nestedList)
            else:
                current_list = nestedList
                current_index = 0
                current_list_len = len(current_list)
                #深度优先遍历
                while len(prev_nested_list) or current_index < current_list_len:
                    #深度遍历结束，恢复之前的遍历
                    if current_index == current_list_len:
                        current_list = prev_nested_list.pop()
                        current_index = 0
                        current_list_len = len(current_list)
                        continue
                    current = current_list[current_index]
                    if type(current) == int:
                        #广度遍历
                        ret.append(current)
                    else:
                        if len(current):
                            #保存当前尚未遍历的节点
                            prev_nested_list.append(current_list[current_index+1:])
                            #开始新的深度遍历
                            current_list = current
                            current_index = 0
                            current_list_len = len(current_list)
                            continue
                    current_index += 1
        return ret
class RecursiveSolution(object):
    def __init__(self):
        self.ret = []

    def flatten(self, nestedList):
        if nestedList is not None:
            if type(nestedList) == int:
                self.ret.append(nestedList)
            else:
                index = 0
                count = len(nestedList)
                while index < count:
                    current = nestedList[index]
                    self.flatten(current)
                    index += 1
        return self.ret

def main():
    solution = RecursiveSolution()
    print solution.flatten([0,1,[2],3,[4,[5],[[6]]]])
    print solution.flatten(7)

    solution = Solution()
    print solution.flatten([0,1,[2],3,[4,[5],[[6]]]])
    print solution.flatten(7)

if __name__ == '__main__':
    main()
