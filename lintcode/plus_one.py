# -*- coding: utf-8 -*-
"""
plus_one.py
-----------
加一
给定一个非负数，表示一个数字数组，在该数的基础上+1，返回一个新的数组。
该数字按照大小进行排列，最大的数在列表的最前面。

样例：
给定 [1,2,3] 表示 123, 返回 [1,2,4].
给定 [9,9,9] 表示 999, 返回 [1,0,0,0].
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 15,2016
"""
class Solution:
    # @param {int[]} digits a number represented as an array of digits
    # @return {int[]} the result
    def plusOne(self, digits):
        if digits != None:
            carry = 1
            ret = [value for value in digits]
            for i in range(len(ret)-1,-1,-1):
                plused = ret[i] + carry
                if plused == 10:
                    ret[i] = 0
                else:
                    carry = 0
                    ret[i] = plused
                    break
            if carry == 1:
                ret = [1] + ret
            return ret
        return None

def main():
    n = raw_input("输入数字数组的长度,比如10:\n")
    n = int(n) if n != '' else 10
    import utils.RandomOrg.RandomOrgApi as random
    api = random.RandomOrgApi()
    digits = api.integers.generate(num=n,min=0,max=9,col=1,base=10,format="plain",rnd="new")
    print "随机生成的数字数组:", digits
    solution = Solution()
    print solution.plusOne(digits)

if __name__ == '__main__':
    main()
