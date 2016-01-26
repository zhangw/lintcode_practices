# -*- coding: utf-8 -*-
"""
majority_number.py
------------------
主元素
给定一个整型数组，找出主元素，它在数组中的出现次数严格大于数组元素个数的二分之一。

样例:
给出数组[1,1,1,1,2,2,2]，返回 1

挑战:
要求时间复杂度为O(n)，空间复杂度为O(1)

参考:
http://www.douban.com/note/505717075/?start=0&post=ok#last
http://www.jiuzhang.com/problem/37/
http://m.oschina.net/blog/85993
----------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 26,2016
"""

class Solution:
    """
    @param nums: A list of integers
    @return: The majority number
    """
    def majorityNumber(self, nums):
        if nums != None:
            length = len(nums)
            if length == 0:
                return None
            if length == 1:
                return nums[0]
            else:
                #假定第一个数是主元素
                candidate_majority = nums[0]
                #被假定的主元素出现的次数
                counter = 1
                i = 1
                n = length
                #从第二个数开始遍历数组
                while i < n:
                    temp = nums[i]
                    i += 1
                    #如果当前这个数和假定的主元素相同，增加计数
                    if candidate_majority == temp:
                        counter += 1
                    else:
                        #当前这个数和假定的主元素不同，减少计数
                        counter -= 1
                        #假定的主元素和这个数至少有一个数一定不是真正的主元素
                        #因此两个数抵消之后，主元素在剩下的数组长度中也一定满足严格大于二分之一的条件
                        length -= 2
                        #假定的主元素和其它与之不相等的数，都被抵消，重新假定主元素
                        if counter == 0:
                            if i < n:
                                #假定下一个尚未遍历的数是主元素
                                candidate_majority = nums[i]
                                #从下下一个数开始重新遍历
                                i += 1
                                counter = 1
                #如果假定的主元素计数器的值，严格大于抵消之后的数组长度的二分之一，那么找到主元素
                if counter > length/2:
                    return candidate_majority
                else:
                    return None
        else:
            return None

def main():
    n = raw_input("正在随机生成一个含有主元素的整数数组,请输入数组的长度N,比如50:\n")
    n = int(n) if n != '' else 50
    array = []
    import random
    m = int(random.random()*10*n)
    array = [m] * n
    c = int(random.random()*n/2)
    c = c-1 if c == n/2 else c
    while c > 0:
        c -= 1
        i = int(random.random()*n)
        i = i - 1 if i == n else i
        random.seed(c**2)
        array[i] = int(random.random()*n)
    print "给定数组=>", array 
    solution = Solution()
    majority = solution.majorityNumber(array)
    if majority != None:
        print "数组中的主元素=>", majority, ",出现的次数:%d" % array.count(majority)
    else:
        print "数组中不存在主元素"

if __name__ == '__main__':
    main()

