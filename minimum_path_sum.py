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
    """
    使用循环的方式替换递归实现对所有求和路径的遍历
    此实现只返回路径和最小值，不保存求和路径
    这个实现在数据量小的情况下(m*n <= 10 * 10)，可以运行。
    数据量大时，LintCode的执行环境会抛出"Memory Limit Exceeded"的异常
    """
    
    """
    @param grid: a list of lists of integers.
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        nodes_with_current_sum = []
        min_sum = None
        current_sum = 0
        while True:
            if grid != None:
                row = len(grid)
                if row > 0:
                    column = len(grid[0])
                    if column > 0:
                        if row > 1 and column > 1:
                            #update the sum value
                            current_sum += grid[0][0]
                            #push the current sum and the downward node into stack
                            nodes_with_current_sum.append((current_sum, grid[1:]))
                            #firstly towards the right if it is possible
                            grid = [row[1:] for row in grid]
                            continue
                        else:
                            #just towards the right
                            if row == 1:
                                current_sum += sum(grid[0])
                            #just downward
                            if column == 1:
                                current_sum += sum([row[0] for row in grid])
                            #update the minimum sum value
                            if min_sum == None:
                                min_sum = current_sum
                            else:
                                min_sum = min(min_sum, current_sum)
                            #recover the sum value and start the new path from the downward node
                            if len(nodes_with_current_sum) > 0:
                                current_sum, grid = nodes_with_current_sum.pop()
                                continue
                            else:
                                #all paths have been visited, return the minimum sum
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
    grid = [[i for i in range(0,5)]] * 5
    print "需要求最小路径和的网格:"
    print "\n".join([str(row) for row in grid])
    solution = AnotherSolutionWithoutPaths()
    print "所有路径的最小和:%d" % solution.minPathSum(grid)
    print "此递归实现不返回求和路径"
    solution = AnotherSolution()
    print "所有路径的最小和:%d" % solution.minPathSum(grid)
    print "递归实现返回所有的求和路径:", solution
    solution = Solution()
    print "所有路径的最小和:%d" % solution.minPathSum(grid)
    print "此非递归实现不返回求和路径"

if __name__ == '__main__':
    main()

