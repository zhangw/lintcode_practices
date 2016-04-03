# -*- coding: utf-8 -*-
"""
paint_fence.py
----------
Paint Fence

There is a fence with n posts, each post can be painted with one of the k colors.
You have to paint all the posts such that no more than two adjacent fence posts have the same color.
Return the total number of ways you can paint the fence.

注意事项:
n and k are non-negative integers.

样例:
Given n=3, k=2 return 6
        post 1,  post 2, post 3
way1    0        0       1 
way2    0        1       0
way3    0        1       1
way4    1        0       0
way5    1        0       1
way6    1        1       0

-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Apr 04,2016
"""

class Solution:
    """
    不超过2个以上的相邻元素是同一个值，等价于第n次选择的元素不和n-2次，n-1次选择的元素是同一个即可。
    去除边界情况，第n次的值只依赖于第n-1,n-2次时选择了相同元素的情况数目，假如前两次选择了相同元素，
    那么本次只有k-1种方式，否则有k种方式。

    动态规划的状态转移公式：
    DP[i] = (DP[i-1] - {前两次选择了同一个元素的情况个数})*k + 前两次选择了同一个元素的情况个数*(k-1)，其中i>=3
    前两次选择了同一个元素的情况个数[0] = k，当n==3时，明显第1次和第2次选择同一个元素的情况个数为k
    前两次选择了同一个元素的情况个数 = 上一次所有的选择方式总数 - 之前一次选择了同一个元素的情况个数

    比如n=5,k=3:
    那么第一次选择时，有3种方式
    第二次选择时，也是3种方式，此时一共有3*3＝9种方式，其中有3种情况选择了同一个元素
    第三次选择时，去除之前选择了同一个元素的3种方式，本次可以有(9-3)*3种方式，另外之前选择了同一个元素的3种方式，本次只能有3*2种方式，此时共(9-3)*3+3*2=24种方式
    第四次选择时，之前的(9-3)*3种方式中，必然有6种方式选择了同一个元素，因此本次选择方式总数:(24-6)*3+6*2=66
    第五次选择时，之前的(24-6)*3种方式中，必然有18种方式选择了同一个元素，因此本次选择方式总数:(66-18)*3+18*2=180

    边界情况:
    n>=3 and k==1
    """
    # @param {int} n non-negative integer, n posts
    # @param {int} k non-negative integer, k colors
    # @return {int} an integer, the total number of ways
    def numWays(self, n, k):
        if k == 1 and n >=3:
            return 0
        #init dynamic programming array
        dp = [0] * (n+1)
        if n >= 1:
            dp[1] = k
        if n >= 2:
            dp[2] = k*k
        i = 3
        same_adjacent_counter = k
        while i <= n:
            #the formula of state transformation
            dp[i] = (dp[i-1] - same_adjacent_counter) * k + same_adjacent_counter * (k-1)
            #update the same_adjacent_counter value for the next calculation
            same_adjacent_counter = dp[i-1] - same_adjacent_counter
            i += 1
        return dp[n]

def main():
    pass

if __name__ == '__main__':
    main()
