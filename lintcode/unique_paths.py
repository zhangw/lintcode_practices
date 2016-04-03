# -*- coding: utf-8 -*-
"""
unique_paths.py
---------------
不同的路径:
有一个机器人的位于一个M×N个网格左上角。
机器人每一时刻只能向下或者向右移动一步。机器人试图达到网格的右下角。
问有多少条不同的路径？

注意:
n和m均不超过100
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 19,2016
"""
class Solution:
    """
    简单的动态规划,到达每一个点的路径数取决于左边和上边相邻的点的路径数之和
    从左上角开始初始化，只向右走和只向下走的每个点的路径数都是1
    formula of state transfer:counter[i][j] = counter[i-1][j] + counter[i][j-1], i>0,j>0
    """
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        #init
        dp = []
        for i in range(0,m):
            dp.append([0]*n)
        dp[0][0] = 1
        for i in range(1,n):
            dp[0][i] = 1
        for j in range(1,m):
            dp[j][0] = 1
        #use formula of state transfer
        i = 1
        while i < m:
            j = 1
            while j < n:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
                j += 1
            i += 1
        self.dp = dp
        return dp[m-1][n-1]


class StupidSolution:
    """
    穷举所有路径
    """
    """
    @param n and m: positive integer(1 <= n , m <= 100)
    @return an integer
    """ 
    def uniquePaths(self, m, n):
        locations = []
        i = 0
        j = 0
        counter_paths = 0
        while i < m and j < n:
            if i+1 < m and j+1 < n:
                locations.append((i+1,j))
                j += 1
                continue
            if i == m-1 or j == n-1:
                counter_paths += 1
            if len(locations):
                i, j = locations.pop()
                continue
            return counter_paths

def main():
    solution = Solution()
    mn = raw_input("请输入M*N的M和N,使用逗号分割:\n")
    mn = mn.split(",")
    m = int(mn[0])
    n = int(mn[1])
    print "使用动态规划计算左上角到右下角的所有路径数:%d" % solution.uniquePaths(m,n)
    print "动态规划的计算过程:"
    print "\n".join([str(row) for row in solution.dp])
    import threading, time
    def stupid_calculate(m,n):
        rst = StupidSolution().uniquePaths(m,n)
        print "使用穷举法计算左上角到右下角的所有路径数:%d" % rst
    calculate_thread = threading.Thread(target=stupid_calculate, args=(m,n,))
    print "开始使用穷举法计算:"
    calculate_thread.start()
    s = time.time()
    e0 = s
    while True:
        e = time.time()
        if calculate_thread.is_alive():
            if e-e0 > 1:
                print str(e-s) + "sec..."
                e0 = e
        else:
            break

if __name__ == '__main__':
    main()
