# -*- coding: utf-8 -*-
"""
longest_increasing_continuous_subsequence.py
--------------------------------------------
最长上升连续子序列
给定一个整数数组（下标从 0 到 n-1， n 表示整个数组的规模），请找出该数组中的最长上升连续子序列。
（最长上升连续子序列可以定义为从右到左或从左到右的序列。）

样例:
给定 [5, 4, 2, 1, 3], 其最长上升连续子序列（LICS）为 [5, 4, 2, 1], 返回 4.
给定 [5, 1, 2, 3, 4], 其最长上升连续子序列（LICS）为 [1, 2, 3, 4], 返回 4.
---------------------------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 26,2016
"""

class Solution:
    """
    use a loop to implement.
    """
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        #the longest length of increasing continuous subsequence
        longest = 0
        while True:
            if A != None:
                length = len(A)
                #in this case, there's no need to continue the calculation, directly return it.
                if length <= longest:
                    return longest
                else:
                    if length <= 1:
                        #consider the edge case
                        return max(longest, length)
                    else:
                        #the current length of increasing continuous subsequence
                        counter = 1
                        #indicates whether increasing or not 
                        is_increase = None
                        #indicates whether continue the while loop or not
                        is_goto_while = False
                        for i in range(1, length):
                            temp = A[i] - A[i-1]
                            if temp == 0:
                                #update the longest value and recalculate from index:i+1
                                longest = max(longest, counter)
                                A = A[i+1:]
                                is_goto_while = True
                                break
                            else:
                                temp = temp > 0
                                if is_increase != None:
                                    if temp == is_increase:
                                        #increase the counter
                                        counter += 1
                                    else:
                                        #update the longest value and recalculate from index:i-1
                                        longest = max(longest, counter)
                                        A = A[i-1:]
                                        is_goto_while = True
                                        break
                                else:
                                    #increase the counter, and reinitialize is_increase variable
                                    counter += 1
                                    is_increase = temp
                        if is_goto_while == False:
                            #end the whole calculation, and update the longest value
                            longest = max(longest, counter)
                        else:
                            continue
            #finally return
            return longest

class RecursiveSolution:
    """
    use recursive way to implement.
    """
    def __init__(self):
        #save length of all the subsequences
        self.results = []
    
    # @param {int[]} A an array of Integer
    # @return {int}  an integer
    def longestIncreasingContinuousSubsequence(self, A):
        if A != None:
            length = len(A)
            if len(self.results) > 0 and max(self.results) >= length:
                #in this case, there is no need to continue the recursion, so end it.
                pass
            else:
                if length <= 1:
                    self.results.append(length)
                else:
                    #length of the increasing continuous subsequence
                    counter = 1
                    #indicates whether increasing or not
                    is_increase = None
                    for i in range(1,length):
                        temp = A[i] - A[i-1]
                        if temp == 0:
                            #save current length value and recalculate from index:i+1
                            self.results.append(counter)
                            return self.longestIncreasingContinuousSubsequence(A[i+1:])
                        else:
                            temp = temp > 0
                            if is_increase != None:
                                #increase the length value
                                if temp == is_increase:
                                    counter += 1
                                else:
                                    #save current length value and recalculate from index:i-1
                                    self.results.append(counter)
                                    return self.longestIncreasingContinuousSubsequence(A[i-1:])
                            else:
                                #initialize the variable and increase the length value
                                is_increase = temp
                                counter += 1
                    #end the loop, save the length value
                    self.results.append(counter)
        else:
            self.results.append(0)
        #return the longest length
        return max(self.results)

def main():
    n = raw_input("开始随机生成一个整数数组,请输入数组的长度N,比如50:\n")
    n = int(n) if n != '' else 50
    A = []
    import random
    for i in range(0,int(n)):
        A.append(int(random.random()*n*10))
    print "数组=>", A
    solution = RecursiveSolution()
    print "使用递归方法计算最长连续上升子序列的长度为:%d" % solution.longestIncreasingContinuousSubsequence(A)
    solution = Solution()
    print "使用循环方法计算最长连续上升子序列的长度为:%d" % solution.longestIncreasingContinuousSubsequence(A)

if __name__ == '__main__':
    main()
