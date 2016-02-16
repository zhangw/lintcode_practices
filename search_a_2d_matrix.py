# -*- coding: utf-8 -*-
"""
search_a_2d_matrix.py
---------------------
搜索二维矩阵

写出一个高效的算法来搜索 m × n矩阵中的值。
这个矩阵具有以下特性：
每行中的整数从左到右是排序的。
每行的第一个数大于上一行的最后一个整数。

样例
考虑下列矩阵:
[
  [1, 3, 5, 7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
给出 target = 3，返回 true

挑战:
O(log(n) + log(m)) 时间复杂度
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 16,2016
"""
class Solution:
    """
    1.先使用二分法查找元素可能出现的行
    2.如果行存在,再使用二分法查找元素可能出现的列
    """
    """
    @param matrix, a list of lists of integers
    @param target, an integer
    @return a boolean, indicate whether matrix contains target
    """
    def searchMatrix(self, matrix, target):
        if matrix != None and len(matrix):
            m = len(matrix)
            n = len(matrix[0])
            if n == 0:
                return False
            while m > 1:
                m_middle = (m-1)/2
                temp = matrix[m_middle][-1]
                if temp == target:
                    return True
                elif temp > target:
                    matrix = matrix[:m_middle+1]
                else:
                    matrix = matrix[m_middle+1:]
                m = len(matrix)
            if m == 1:
                matrix = matrix[0]
                while n > 1:
                    n_middle = (n-1)/2
                    temp = matrix[n_middle]
                    if temp == target:
                        return True
                    elif temp > target:
                        matrix = matrix[:n_middle]
                    else:
                        matrix = matrix[n_middle+1:]
                    n = len(matrix)
                if n == 1:
                    return matrix[0] == target
                else:
                    return False
            else:
                return False
        return False

def main():
    matrix = [
        [1, 3, 5, 7],
        [10, 11, 16, 20],
        [23, 30, 34, 50]
    ]
    print "被搜索的矩阵:"
    print "\n".join([str(row) for row in matrix])
    target = raw_input("输入要搜索的元素值:\n")
    target = int(target)
    solution = Solution()
    print "%d在矩阵中%s存在" % (target, "" if solution.searchMatrix(matrix, target) else "不")

if __name__ == '__main__':
    main()
