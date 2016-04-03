# -*- coding: utf-8 -*-
"""
matrix_zigzag_traversal.py
--------------------------
矩阵的之字型遍历
给你一个包含 m x n 个元素的矩阵 (m 行, n 列), 求该矩阵的之字型遍历。

样例:
对于如下矩阵：
[
  [1, 2,  3,  4],
  [5, 6,  7,  8],
  [9,10, 11, 12]
]
返回 [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]

参考:
A:http://blog.csdn.net/wutingyehe/article/details/46629087
    1.move right one step, if it is impossible, move down one step
    2.move to the lower left corner
    3.move down one step, if it is impossible, move right one step
    4.move to the top right corner
    5.repeat 1-4

B:http://kuchaguangjie.iteye.com/blog/792175
左斜切线法:
    1.m 行 n 列 矩阵，记为T
    2.左斜切线的条数N=m-1 + 1 + n-1 => N = m+n-1
    3.最长的左斜切线的长度为M,M=min(m,n)
    4.从左往右遍历左斜切线P(i),P(i)的长度记为L(i),i的取值是[0,N)
    5.斜切线P(i)超出矩阵行的高度，记为H(i)=i+1-m；超出矩阵列的长度，记为W(i)=i+1-n
    6.H(i)=0 if H(i)<=0 else H(i);W(i)=0 if W(i)<=0 else W(i), L(i)=i+1-H(i)-W(i)
    7.斜切线右上角元素，记为P(i) = T[H(i)][i-H(i)]，左下角元素，记为Q(i) = T[i-W(i)][W(i)]
    8.遍历所有左斜切线，对每一条切线，利用P(i)或者Q(i)和L(i)，遍历切线上的元素
    9.遍历的方向由i%2==0判断
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 27,2016
"""

class AnotherSolution:
    # @param: a matrix of integers
    # @return: a list of integers
    #
    # matrix T(4,5):
    # [ 1,  2,  3,  4] #  #  #  #
    # [ 5,  6,  7,  8] #  #  #
    # [ 9, 10, 11, 12] #  #
    # [13, 14, 15, 16] #
    # [17, 18, 19, 20]
    #   $   $   $
    #   $   $
    #   $
    # N = 4 + 5 - 1
    # all the lines(N), i in [0,N):
    # [ i=0:1,                                           W(i)=0,H(i)=0
    #   i=1:2-5,                                         ..     ..
    #   i=2:9-6-3,                                      
    #   i=3:4-7-10-13,                                   ..     ..
    #   i=4:17-14-11-8,(17-14-11-8-#)=>remove(#),        W(i)=1,H(i)=0        top_right:[W(i),i-W(i)], lower_left:[i-H(i),H(i)]
    #   i=5:12-15-18,(#-#-12-15-18-$)=>remove(#,#,$)     W(i)=2,H(i)=1
    #   i=6:19-16,($-$-19-16-#-#-#)=>remove($,$,#,#,#)   W(i)=3,H(i)=2
    #   i=7:20,(#-#-#-#-20-$-$-$)=>remove(#,#,#,#,$,$,$) W(i)=4,H(i)=3
    #  ]
    def printZMatrix(self, matrix):
        if matrix != None:
            #the height of matrix
            row = len(matrix)
            if row >= 1:
                #the width of matrix
                column = len(matrix[0])
                if column >= 1:
                    ret = []
                    #get the number of lines
                    N = row + column - 1
                    i = 0
                    while i < N:
                        h_extra = i + 1 - row
                        h_extra = 0 if h_extra <= 0 else h_extra
                        w_extra = i + 1 - column
                        w_extra = 0 if w_extra <= 0 else w_extra
                        #get the length of the current line
                        length = i + 1 - h_extra - w_extra
                        #the top right element of the line
                        top_right = [w_extra,i-w_extra]
                        #the lower left element of the line
                        lower_left = [i-h_extra,h_extra]
                        if i % 2 == 0:
                            #direction from lower left to top right 
                            while length > 0:
                                length -= 1
                                element = matrix[top_right[0]+length][top_right[1]-length]
                                ret.append(element)
                        else:
                            #direction from top right to lower left
                            while length > 0:
                                length -= 1
                                element = matrix[lower_left[0]-length][lower_left[1]+length]
                                ret.append(element)
                        i += 1
                    return ret
            else:
                return []
        return []


class Solution:
    # @param: a matrix of integers
    # @return: a list of integers
    def printZMatrix(self, matrix):
        if matrix != None:
            m = len(matrix)
            if m >= 1:
                n = len(matrix[0])
                if n >= 1:
                    ret = []
                    row,column = 0,0
                    length = m * n
                    i = 0
                    while i < length:
                        if i == 0:
                            ret.append(matrix[row][column])
                            i += 1
                        else:
                            """
                            1.move right one step, if it is impossible, move down one step
                            2.move to the lower left corner
                            3.move down one step, if it is impossible, move right one step
                            4.move to the top right corner
                            5.repeat 1-4
                            """
                            #step 1:
                            if i < length and column < n - 1:
                                i += 1
                                column += 1
                                ret.append(matrix[row][column])
                            else:
                                if i < length and row < m - 1:
                                    i += 1
                                    row += 1
                                    ret.append(matrix[row][column])
                            #step 2:
                            while i < length and row < m - 1 and column >= 1:
                                i += 1
                                row += 1
                                column -= 1
                                ret.append(matrix[row][column])
                            #step 3:
                            if i < length and row < m - 1:
                                i += 1
                                row += 1
                                ret.append(matrix[row][column])
                            else:
                                if i < length and column < n - 1:
                                    i += 1
                                    column += 1
                                    ret.append(matrix[row][column])
                            #step 4:
                            while i < length and row >= 1 and column < n - 1:
                                i += 1
                                row -= 1
                                column += 1
                                ret.append(matrix[row][column])
                    return ret
                else:
                    return []
            else:
                return []
        else:
            return []

def main():
    m_n = raw_input("正在生成一个自然数序列的矩阵[M x N],请输入M和N的值,比如3,4:\n")
    m_n = m_n.split(',')
    m = int(m_n[0])
    n = int(m_n[1])
    matrix = []
    rjust_width = len(str(m*n-1))
    for i in range(0,m*n):
        if i % n == 0:
            matrix.append([])
            matrix[-1].append(i)
        else:
            matrix[-1].append(i)
    for m in matrix:
        print "["+",".join([str(number).rjust(rjust_width) for number in m])+"]"
    solution = AnotherSolution()
    matrix_zigzag_traversal = solution.printZMatrix(matrix)
    print "之字形遍历矩阵=>", matrix_zigzag_traversal

if __name__ == '__main__':
    main()