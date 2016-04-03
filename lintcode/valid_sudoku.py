# -*- coding: utf-8 -*-
"""
valid_sukudou.py
----------------
判断数独是否合法
请判定一个数独是否有效。
该数独可能只填充了部分数字，其中缺少的数字用 . 表示。

样例:
下列就是一个合法数独的样例。
http://www.lintcode.com/media/problem/valid-sudoku.png

注意:
一个合法的数独（仅部分填充）并不一定是可解的。我们仅需使填充的空格有效即可。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 19,2016
"""
class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def isduplicate(sequence):
            """
            whether duplicate digits in the sequence, for example:
            "....5..1." => false,
            ".2..3.7.2" => true
            """
            digits = [0]*10
            for i in sequence:
                if i != '.':
                    if digits[int(i)] == 0:
                        digits[int(i)] = i
                    else:
                        return True
            return False
            
        if board != None:
            #whether duplicate digits in horizontal line
            for i in range(0,9):
                if isduplicate(board[i]):
                    return False
            #whether duplicate digits in vertical line
            for j in range(0,9):
                vertical = [row[j] for row in board]
                if isduplicate(vertical):
                    return False
            #whether duplicate digits in 3*3 square
            for m in range(0,7,3):
                for n in range(0,7,3):
                    square = []
                    for row in board[m:m+3]:
                        square += row[n:n+3]
                        if isduplicate(square):
                            return False
            return True
        return False

def main():
    sudoku = [".87654321","2...1....",".3....6..","..4...7..","5.....28.","6.....1.3","....7.5..","......8..","9.....4.."]
    print u"给定数独:"
    print "\n".join([" ".join(list(s)) for s in sudoku])
    solution = Solution()
    print u"该数独是%s法的." % u"合" if solution.isValidSudoku(sudoku) else u"非"

if __name__ == '__main__':
    main()
