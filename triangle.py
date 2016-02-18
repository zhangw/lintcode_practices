# -*- coding: utf-8 -*-
"""
triangle.py
-----------
给定一个数字三角形，找到从顶部到底部的最小路径和。每一步可以移动到下面一行的相邻数字上。

样例:
比如，给出下列数字三角形：
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
从顶到底部的最小路径和为11 ( 2 + 3 + 5 + 1 = 11)。

注意:
如果你只用额外空间复杂度O(n)的条件下完成可以获得加分，其中n是数字三角形的总行数。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 18,2016
"""
class Solution:
    """
    简单的动态规划，3角形两条斜边的求和值是初始值
    formula of state transfer:S[i,j] = A[i,j] + min(S[i-1,j], S[i-1][j-1]), i>1,j>0
    """
    def __init__(self):
        self.dp = None
    """
    @param triangle: a list of lists of integers.
    @return: An integer, minimum path sum.
    """
    def minimumTotal(self, triangle):
        if triangle != None:
            height = len(triangle)
            if height:
                #init dp
                dp = [[0] * len(row) for row in triangle]
                dp[0][0] = triangle[0][0]
                for i in range(1,height):
                    dp[i][0] = triangle[i][0] + dp[i-1][0]
                    dp[i][-1] = triangle[i][-1] + dp[i-1][-1]
                #use formula of state transfer
                for j in range(2,height):
                    for k in range(1,j):
                        dp[j][k] = triangle[j][k] + min(dp[j-1][k], dp[j-1][k-1])
                self.dp = dp
                return min(dp[-1])
        return None

def main():
    triangle = [
        [2],
        [3,4],
        [6,5,7],
        [4,1,8,3]
    ]
    print "给定一个三角形:"
    print "\n".join([str(row) for row in triangle])
    solution = Solution()
    minimum = solution.minimumTotal(triangle)
    print "三角形顶部到底部的最小路径和:%d" % minimum
    print "动态规划的计算过程:"
    print "\n".join([str(row) for row in solution.dp])

if __name__ == '__main__':
    main()
