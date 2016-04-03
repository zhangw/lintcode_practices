# -*- coding: utf-8 -*-
"""
insert_interval.py
------------------
插入区间
给出一个无重叠的按照区间起始端点排序的区间列表。
在列表中插入一个新的区间，你要确保列表中的区间仍然有序且不重叠(如果有必要的话，可以合并区间)。

样例：
插入区间[2, 5] 到 [[1,2], [5,9]]，我们得到 [[1,9]]。
插入区间[3, 4] 到 [[1,2], [5,9]]，我们得到 [[1,2], [3,4], [5,9]]。
--------------------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 24,2016
"""
class Interval(object):
    """
    Definition of Interval.
    """
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):
        return str([self.start, self.end])

class Solution:
    """
    Insert a new interval into a sorted non-overlapping interval list.
    @param intevals: Sorted non-overlapping interval list
    @param newInterval: The new interval.
    @return: A new sorted non-overlapping interval list with the new interval.
    """
    def insert(self, intervals, newInterval):
        results = []
        if intervals != None and newInterval != None:
            if len(intervals) == 0:
                results.append(newInterval)
            else:
                length = len(intervals)
                for i in range(0,length):
                    oldInterval = intervals[i]
                    #firstly consider that new and old intervals don't have intersection set
                    if newInterval.end < oldInterval.start:
                        #directly insert here and add all the other intervals at tail, return it
                        results.append(newInterval)
                        results += intervals[i:]
                        return results
                    elif newInterval.start > oldInterval.end:
                        #add the old interval and continue the loop
                        results.append(oldInterval)
                        continue
                    #consider that new and old intervals have intersection set
                    else:
                        #return the minimal number as start
                        start = newInterval.start if newInterval.start <= oldInterval.start else oldInterval.start
                        #return the max number as end
                        end = newInterval.end if newInterval.end >= oldInterval.end else oldInterval.end
                        #update the new interval and continue the loop
                        newInterval.start = start
                        newInterval.end = end
                        continue
                #NOTE:must add the last updated interval to results
                results.append(newInterval)
            return results
        else:
            return intervals
def main():
    intervals = [Interval(1,2),Interval(5,9)]
    print '初始的区间:', intervals
    solution = Solution()
    while True:
        start_and_end = raw_input("请输入要插入的新区间,比如[2,5]:\n")
        start_and_end = eval(start_and_end)
        start = start_and_end[0]
        end = start_and_end[1]
        print "插入区间[%d, %d]后，变为:"%(start, end), solution.insert(intervals, Interval(start, end))
        raw_input("press any key to continue...")

if __name__ == '__main__':
    main()
