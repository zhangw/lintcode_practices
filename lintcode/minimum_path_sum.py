# -*- coding: utf-8 -*-
"""
minimum_path_sum.py
-------------------
最小路径和
给定一个只含非负整数的m*n网格，找到一条从左上角到右下角的可以使数字和最小的路径。

注意:
你在同一时间只能向下或者向右移动一步
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 04,2016
"""

class Solution:
    def __init__(self):
        self.states = None

    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    参考:
    http://mioopoi.github.io/%E7%AE%97%E6%B3%95/lintcode-dynamic-programming-summary#lintcode-110-minimum-path-sum-%E6%9C%80%E5%B0%8F%E8%B7%AF%E5%BE%84%E5%92%8C
    http://www.hawstein.com/posts/dp-novice-to-advanced.html
    DP(动态规划)的状态转移公式为：
    S[i][j] = grid[i][j] + min(S[i-1][j],S[i][j-1])
    """
    def minPathSum(self, grid):
        if grid != None:
            if len(grid) and len(grid[0]):
                row, column = len(grid), len(grid[0])
                #init dp
                dp = [[0 for c in range(0,column)] for r in range(0,row)]
                dp[0][0] = grid[0][0]
                #calculate the values of first row
                for i in range(1,column):
                    dp[0][i] = grid[0][i] + dp[0][i-1]
                #calculate the values of first vertical row
                for j in range(1,row):
                    dp[j][0] = grid[j][0] + dp[j-1][0]
                #the formula of state transition: S[i][j] = grid[i][j] + min(S[i-1][j],S[i][j-1])
                for i in range(1,row):
                    for j in range(1,column):
                        dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
                self.states = dp
                return dp[row-1][column-1]
        return None

class AnotherSolutionWithoutPathsAndRecurrence:
    """
    使用循环的方式替换递归实现对所有求和路径的遍历
    此实现只返回路径和最小值，不保存求和路径
    这个实现在数据量小的情况下(m*n <= 10 * 10)，可以运行。
    数据量大时，LintCode的执行环境会抛出"Time Limit Exceeded"的异常
    """

    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        nodes_with_current_sum = []
        min_sum = None
        current_sum = 0
        if len(grid) and len(grid[0]):
            row = len(grid)
            column = len(grid[0])
            i = 0
            j = 0
            while True:
                current_sum += grid[i][j]
                if i < row - 1 and j < column - 1:
                    #save the current_sum and downward location into stack
                    nodes_with_current_sum.append((current_sum,(i+1,j)))
                    #firstly rightward
                    j += 1
                    continue
                if i < row - 1:
                    #just downward
                    i += 1
                    continue
                if j < column - 1:
                    #just rightward
                    j += 1
                    continue
                #the last element visited, update the mininum value
                if min_sum == None:
                    min_sum = current_sum
                else:
                    min_sum = min(min_sum, current_sum)
                #traverse with a new path
                if len(nodes_with_current_sum):
                    #recover the current sum value and the downward location
                    current_sum, location = nodes_with_current_sum.pop()
                    i, j = location[0], location[1]
                    continue
                else:
                    return min_sum
        return None


class AnotherSolutionWithoutPaths:
    """
    只返回路径和最小值，不保存求和路径
    这个实现在数据量小的情况下(m*n <= 10 * 10)，可以运行。
    数据量大时，LintCode的执行环境会抛出"Memory Limit Exceeded"的异常
    """
    def __init__(self):
        self.result = None

    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        return self.minPathSumRecurrence(grid, 0)

    def minPathSumRecurrence(self, grid, prev_sum):
        if grid != None:
            row = len(grid)
            if row > 0:
                column = len(grid[0])
                if row > 1 and column > 1:
                    #right
                    prev_sum += grid[0][0]
                    self.minPathSumRecurrence([row[1:] for row in grid], prev_sum)
                    #down
                    self.minPathSumRecurrence(grid[1:], prev_sum)
                else:
                    if row == 1:
                        prev_sum += sum(grid[0])
                    if column == 1:
                        prev_sum += sum([row[0] for row in grid])
                    if self.result == None:
                        self.result = prev_sum
                    else:
                        self.result = min(self.result, prev_sum)
                return self.result
        return None

class AnotherSolution:
    """
    除了路径和最小值，同时保存所有求和路径
    这个实现在数据量小的情况下(m*n <= 10 * 10)，可以运行。
    数据量大时，LintCode的执行环境会抛出"Memory Limit Exceeded"的异常
    """
    def __init__(self):
        #all the paths
        self.paths = []

    def __str__(self):
        return str(self.paths)

    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        all_paths = self.minPathSumRecurrence(grid, [])
        if all_paths != None and len(all_paths) > 0:
            min_sum = sum(all_paths[0])
            for i in range(1, len(all_paths)):
                temp_sum = sum(all_paths[i])
                min_sum = min(min_sum, temp_sum)
            return min_sum
        return None

    """
    use a recurrence to traverse all the paths.
    @param grid: a List of lists of integers.
    @param path: the prev path
    @return: all the paths by which from top left element to bottom right element in the grid
    """ 
    def minPathSumRecurrence(self, grid, path):
        if grid != None:
            row = len(grid)
            if row > 0:
                column = len(grid[0])
                newpath = [pitem for pitem in path]
                if row > 1 and column > 1:
                    #right
                    newpath.append(grid[0][0])
                    self.minPathSumRecurrence([row[1:] for row in grid], newpath)
                    #down
                    self.minPathSumRecurrence(grid[1:], newpath)
                else:
                    if row == 1:
                        newpath += grid[0]
                        self.paths.append(newpath)
                    if column == 1:
                        newpath += [row[0] for row in grid]
                        self.paths.append(newpath)
                return self.paths

def main():
    grid = [[0,4,3,1],[6,8,4,1],[10,2,1,9],[3,9,2,7]]
    print "需要求最小路径和的网格:"
    print "\n".join([str(row) for row in grid])
    solution = AnotherSolutionWithoutPaths()
    print "所有路径的最小和:%d" % solution.minPathSum(grid)
    print "此递归实现不返回求和路径"
    solution = AnotherSolution()
    print "所有路径的最小和:%d" % solution.minPathSum(grid)
    print "递归实现返回所有的求和路径:", solution
    solution = AnotherSolutionWithoutPathsAndRecurrence()
    print "所有路径的最小和:%d" % solution.minPathSum(grid)
    print "此非递归实现不返回求和路径"
    solution = Solution()
    print "所有路径的最小和:%d" % solution.minPathSum(grid)
    print "动态规划的状态转移公式的求解过程:"
    print "\n".join([str(row) for row in solution.states])

if __name__ == '__main__':
    main()

