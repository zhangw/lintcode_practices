# -*- coding: utf-8 -*-
"""
merge_intervals.py
------------------
合并区间
给出若干闭合区间，合并所有重叠的部分。

样例：
给出的区间列表 => 合并后的区间列表：

[                     [
  [1, 3],               [1, 6],
  [2, 6],      =>       [8, 10],
  [8, 10],              [15, 18]
  [15, 18]            ]
]

挑战：
O(nlogn) 的时间和 O(1) 的额外空间。
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 03,2016
"""
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __str__(self):
        return str([self.start, self.end])

    __repr__ = __str__

class Solution:
    # @param intervals, a list of Interval
    # @return a list of Interval
    def merge(self, intervals):
        if intervals == None:
            return None
        else:
            length = len(intervals)
            if length > 2:
                left = intervals[:length/2]
                right = intervals[length/2:]
                #recurrence
                merged_left = self.merge(left)
                merged_right = self.merge(right)
                #merge left intervals and right intervals
                return self.merge_left_right(merged_left, merged_right)
            elif length == 2:
                #merge 2 intervals
                prev = intervals[0]
                next = intervals[1]
                if prev.end < next.start:
                    return intervals
                elif prev.start > next.end:
                    return [next,prev]
                else:
                    prev.start = min(prev.start, next.start)
                    prev.end = max(prev.end, next.end)
                    return [prev]
            else:
                return intervals
    
    def merge_left_right(self, merged_left, merged_right):
        result = []
        while len(merged_left) > 0 and len(merged_right) > 0:
            head_left = merged_left[0]
            head_right = merged_right[0]
            if head_left.end < head_right.start:
                #add the left interval
                result.append(head_left)
                merged_left = merged_left[1:]
                continue
            if head_left.start > head_right.end:
                #add the right interval
                result.append(head_right)
                merged_right = merged_right[1:]
                continue
            if head_left.end <= head_right.end:
                #merge 2 intervals and update the right one
                head_right.start = min(head_left.start, head_right.start)
                merged_left = merged_left[1:]
                continue
            else:
                #merge 2 intervals and update the left one
                head_left.start = min(head_left.start, head_right.start)
                merged_right = merged_right[1:]
                continue
        #add the remaining intervals
        if len(merged_left) > 0:
            result += merged_left
        if len(merged_right) > 0:
            result += merged_right
        return result

def main():
    n = raw_input("请输入需要合并的整数区间集合的大小，比如10:\n")
    n = int(n) if n != '' else 10
    from utils.RandomOrg import RandomOrgApi as random
    api = random.RandomOrgApi()
    #https://www.random.org/integer-sets/?sets=1&num=100&min=1&max=200&commas=on&order=index&format=plain&rnd=new
    array = api.integer_sets.generate(sets=1,num=2*n,min=0,max=10*n,col=1,commas="on",order="index",format="plain",rnd="new")
    intervals = []
    print array
    for i in range(0,2*n-1):
        s = min(array[i], array[i+1])
        e = max(array[i], array[i+1])
        interval = Interval(s, e)   
        intervals.append(interval)
    print "需要合并的区间:", intervals
    solution = Solution()
    print "合并后的区间:", solution.merge(intervals)

if __name__ == '__main__':
    main()
