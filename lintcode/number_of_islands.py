# -*- coding: utf-8 -*-
"""
number_of_islands.py
--------------------
岛屿的个数
给一个01矩阵，求不同的岛屿的个数。
0代表海，1代表岛，如果两个1相邻，那么这两个1属于同一个岛。我们只考虑上下左右为相邻。

样例:
矩阵
[
  [1, 1, 0, 0, 0],
  [0, 1, 0, 0, 1],
  [0, 0, 0, 1, 1],
  [0, 0, 0, 0, 0],
  [0, 0, 0, 0, 1]
]
中有 3 个岛.
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 06,2016
"""
class Solution:
    """
    使用深度遍历和标零法，记录可以遍历的"1"的路径，遍历的次数就是岛屿的个数
    参考:
    https://segmentfault.com/a/1190000003753307
    http://www.jiuzhang.com/problem/82/
    """
    def init(self):
        self.row = 0
        self.column = 0

    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        if grid != None:
            row = len(grid)
            if row > 0:
                column = len(grid[0])
                if column > 0:
                    i = 0
                    counter_islands = 0
                    self.row = row
                    self.column = column
                    while i < row:
                        j = 0
                        while j < column:
                            start = grid[i][j]
                            if start == 1:
                                #DFS
                                counter_islands += 1
                                self.traverseIsland(grid, i, j)
                            j += 1
                        i += 1
                    return counter_islands
        return 0

    def traverseIsland(self, grid, x, y):
        """
        DFS travesal and make all the visited islands as 0
        """
        if grid[x][y] == 1:
            grid[x][y] = 0
            if x > 0 and grid[x-1][y] == 1:
                #upward
                self.traverseIsland(grid, x-1, y)
            if x < self.row - 1 and grid[x+1][y] == 1:
                #downward
                self.traverseIsland(grid, x+1, y)
            if y > 0 and grid[x][y-1] == 1:
                #leftward
                self.traverseIsland(grid, x, y-1)
            if y < self.column - 1 and grid[x][y+1] == 1:
                #rightward
                self.traverseIsland(grid, x, y+1)

def main():
    """
    matrix01 = [
    [0,1,0,0,1,1,1,0,0,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,0,0,1,1,0,0,1,0,1,0,1,0,1,1,0,0,0],
    [0,1,0,0,0,1,1,1,1,0,0,0,0,0,1,1,1,1,0,1],
    [1,1,0,0,0,1,1,0,0,0,1,1,1,0,0,1,0,1,1,0],
    [0,1,0,1,1,0,1,0,0,0,1,0,0,1,0,0,0,0,0,1],
    [1,0,0,1,0,1,0,0,0,1,1,0,1,0,0,1,0,0,0,0],
    [1,0,0,0,1,1,0,0,0,0,0,1,0,0,1,0,0,0,0,1],
    [1,0,0,0,1,0,1,1,1,0,1,0,1,1,1,1,0,0,0,1],
    [1,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,0,1],
    [0,0,0,1,0,1,1,1,1,1,1,1,1,1,0,0,0,0,1,0],
    [1,0,1,0,1,0,0,1,1,1,0,1,1,0,0,1,1,0,0,0],
    [0,1,0,0,1,0,0,0,0,0,0,1,1,1,1,0,0,0,1,0],
    [1,0,0,0,1,1,1,0,1,0,0,0,1,0,1,0,1,0,0,1],
    [0,0,0,0,1,0,1,1,0,1,0,1,0,1,1,1,1,0,0,0],
    [0,1,1,0,0,0,0,1,0,0,1,1,1,0,0,1,1,0,1,0],
    [1,0,1,1,1,1,1,1,0,1,1,0,1,0,0,1,0,0,0,1],
    [1,0,0,0,1,0,1,0,0,1,0,1,0,0,1,0,0,1,1,1],
    [0,0,1,0,0,0,0,1,0,0,1,1,0,1,1,1,0,0,0,0],
    [0,0,1,0,0,0,0,0,0,1,1,0,1,0,1,0,0,0,1,1],
    [1,0,0,0,1,0,1,1,1,0,0,1,0,1,0,1,1,0,0,0]
    ]
    """
    """
    matrix01 = [
    [1,1,1,1,1,1],
[1,0,0,0,0,1],
[1,0,1,1,0,1],
[1,0,0,0,0,1],
[1,1,1,1,1,1]
    ]
    """
    matrix01 = [
 [0,1,1,1,1,0,0,1,0,1,1,1,1,1,1,0,0,1,1,0],
 [0,0,0,0,0,0,1,0,1,0,1,0,0,1,1,0,0,0,1,0],
 [0,1,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,0,1],
 [1,0,0,1,1,1,1,1,0,1,0,0,0,0,1,0,1,0,1,0],
 [0,1,0,0,0,0,1,0,0,0,0,1,0,0,1,0,1,1,1,0],
 [0,0,0,0,0,0,0,1,0,1,1,0,0,1,1,0,0,1,0,1],
 [0,0,1,1,1,1,0,1,1,1,1,0,0,0,1,0,1,0,1,1],
 [1,1,1,1,0,0,1,0,1,0,0,0,0,0,0,1,1,1,0,1],
 [1,0,0,0,1,1,0,0,1,0,1,1,0,0,0,1,0,0,0,0],
 [1,0,0,1,0,1,0,1,0,0,1,1,1,0,0,0,0,0,1,0],
 [0,0,0,1,0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,1],
 [0,1,0,0,1,1,1,0,1,1,1,0,0,0,1,0,1,0,0,0],
 [1,1,1,0,1,1,0,1,0,1,0,1,1,0,0,0,1,0,0,0],
 [0,1,1,0,1,0,0,1,1,0,1,1,0,1,1,0,1,1,0,0],
 [0,1,1,0,0,1,0,0,0,1,0,1,0,0,0,0,0,0,1,1],
 [0,0,1,0,0,0,1,1,0,1,1,1,1,0,1,0,1,0,1,0],
 [1,0,0,0,1,0,1,0,1,0,0,0,0,1,1,0,0,0,0,0],
 [1,0,0,1,1,0,0,1,1,0,0,0,1,0,0,0,1,1,1,0],
 [0,1,0,1,1,0,0,0,1,1,0,0,1,1,1,0,0,1,1,0],
 [0,0,1,0,1,0,0,0,0,0,0,0,0,1,0,1,0,0,1,0]]
    print "01矩阵,0表示海洋,1表示岛屿:\n", "\n".join([str(row) for row in matrix01])
    solution = Solution()
    print "岛屿的个数:%d" % solution.numIslands(matrix01)

if __name__ == '__main__':
    main()