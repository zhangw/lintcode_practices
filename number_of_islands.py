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
class AnotherSolution:
    """
    此方法按行扫描的方式进行遍历，但是效率低下，会引起LintCode执行时间超出限制的异常
    """
    # @param {boolean[][]} grid a boolean 2D matrix
    # @return {int} an integer
    def numIslands(self, grid):
        if grid != None:
            row = len(grid)
            if row > 0:
                column = len(grid[0])
                if column > 0:
                    i = 0
                    islands = []
                    current_island = []
                    while i < row:
                        j = 0
                        while j < column:
                            temp = grid[i][j]
                            if temp == 1:
                                current_island.append((i, j))
                            else:
                                if len(current_island):
                                    islands.append(current_island)
                                    current_island = []
                                    self.mergeIslands(islands, i)
                            j += 1
                        i += 1
                        #IMPORTANT:initialize a new island object when before beginning of the new row
                        if len(current_island):
                            islands.append(current_island)
                            current_island = []
                            self.mergeIslands(islands, i)
                    if len(current_island):
                        islands.append(current_island)
                        self.mergeIslands(islands, i)
                    self.islands = islands
                    return len(islands)
        return 0

    def mergeIslands(self, islands, row_index):
        if len(islands) > 1:
            last_island = islands[-1]
            for i in range(0, len(islands)-1):
                    merged = self.mergeTwoIslands(islands[i], last_island)
                    if merged:
                        islands[i] = merged
                        del islands[-1]
                        return True
        return False

    def mergeTwoIslands(self, island, newisland):
        for m in range(0, len(newisland)):
            a = newisland[m]
            if island.count((a[0]-1,a[1])) >= 1:
                return island + newisland
        return False

def main():
    matrix01 = [[1,0,0,1,1,1,0,1,1,0,0,0,0,0,0,0,0,0,0,0],[1,0,0,1,1,0,0,1,0,0,0,1,0,1,0,1,0,0,1,0],[0,0,0,1,1,1,1,0,1,0,1,1,0,0,0,0,1,0,1,0],[0,0,0,1,1,0,0,1,0,0,0,1,1,1,0,0,1,0,0,1],[0,0,0,0,0,0,0,1,1,1,0,0,0,0,0,0,0,0,0,0],[1,0,0,0,0,1,0,1,0,1,1,0,0,0,0,0,0,1,0,1],[0,0,0,1,0,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1],[0,0,0,1,0,1,0,0,1,1,0,1,0,1,1,0,1,1,1,0],[0,0,0,0,1,0,0,1,1,0,0,0,0,1,0,0,0,1,0,1],[0,0,1,0,0,1,0,0,0,0,0,1,0,0,1,0,0,0,1,0],[1,0,0,1,0,0,0,0,0,0,0,1,0,0,1,0,1,0,1,0],[0,1,0,0,0,1,0,1,0,1,1,0,1,1,1,0,1,1,0,0],[1,1,0,1,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,1],[0,1,0,0,1,1,1,0,0,0,1,1,1,1,1,0,1,0,0,0],[0,0,1,1,1,0,0,0,1,1,0,0,0,1,0,1,0,0,0,0],[1,0,0,1,0,1,0,0,0,0,1,0,0,0,1,0,1,0,1,1],[1,0,1,0,0,0,0,0,0,1,0,0,0,1,0,1,0,0,0,0],[0,1,1,0,0,0,1,1,1,0,1,0,1,0,1,1,1,1,0,0],[0,1,0,0,0,0,1,1,0,0,1,0,1,0,0,1,0,0,1,1],[0,0,0,0,0,0,1,1,1,1,0,1,0,0,0,1,1,0,0,0]]
    print "01矩阵,0表示海洋,1表示岛屿:\n", "\n".join([str(row) for row in matrix01])
    solution = AnotherSolution()
    print "岛屿的个数:%d" % solution.numIslands(matrix01)
    islands = solution.islands
    print "岛屿的组成:\n", "\n".join([str(island) for island in islands])

if __name__ == '__main__':
    main()