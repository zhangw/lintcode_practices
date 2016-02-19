# -*- coding: utf-8 -*-
"""
unique_paths_ii.py
------------------
不同的路径 II
"不同的路径" 的跟进问题：
现在考虑网格中有障碍物，那样将会有多少条不同的路径？
网格中的障碍和空位置分别用 1 和 0 来表示。

样例:
如下所示在3x3的网格中有一个障碍物：
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
一共有2条不同的路径从左上角到右下角。

注意:
m 和 n 均不超过100
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 19,2016
"""
class Solution:
    """
    简单的动态规划
    formula of state transfer counter[i][j] = 0 if gird[i][j] == 1 else counter[i-1][j] + counter[i][j-1] i>0,j>0
    """
    """
    @param obstacleGrid: An list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid != None:
            row = len(obstacleGrid)
            if row:
                column = len(obstacleGrid[0])
                if obstacleGrid[0][0] == 1:
                    #no path exists
                    return 0
                dp = [[0]*column for r in obstacleGrid]
                dp[0][0] = 1
                flag = 1
                #if encounter an obstacle, the following paths is not exist
                for i in range(1,row):
                    if obstacleGrid[i][0] == 1:
                        flag = 0
                    dp[i][0] = flag
                flag = 1
                #if encounter an obstacle, the following paths is not exist
                for j in range(1,column):
                    if obstacleGrid[0][j] == 1:
                        flag = 0
                    dp[0][j] = flag
                if row > 1 and column > 1:
                    if dp[1][0] == 0 and dp[0][1] == 0:
                        #no path exists in this case
                        return 0
                i = 1
                while i < row:
                    j = 1
                    while j < column:
                        #use formula of state transfer
                        if obstacleGrid[i][j] == 1:
                            dp[i][j] = 0
                        else:
                            dp[i][j] = dp[i-1][j] + dp[i][j-1]
                        j += 1
                    i += 1
                self.dp = dp
                return dp[row-1][column-1]

def main():
    mn = raw_input("请输入M*N网格的M和N,使用逗号分割:\n")
    mn = mn.split(",")
    m = int(mn[0])
    n = int(mn[1])
    gird = [[0]*n for r in range(0,m)]
    import random
    for row in gird:
        for x in range(0,int(random.random()*(n>>1))):
            index = int(random.random()*(n-1))
            row[index] = 1
    print "含有障碍物(1)的网格:"
    print "\n".join([str(row) for row in gird])
    solution = Solution()
    print "使用动态规划计算网格左上角到右下角的路径数:%d" % solution.uniquePathsWithObstacles(gird)
    if hasattr(solution, 'dp'):
        print "动态规划的计算过程:"
        print "\n".join([str(row) for row in solution.dp])

if __name__ == '__main__':
    main()
