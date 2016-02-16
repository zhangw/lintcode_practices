# -*- coding: utf-8 -*-
"""
search_insert_position.py
-------------------------
搜索插入位置
给定一个排序数组和一个目标值，如果在数组中找到目标值则返回索引。如果没有，返回到它将会被按顺序插入的位置。
你可以假设在数组中无重复元素。

样例:
[1,3,5,6]，5 → 2
[1,3,5,6]，2 → 1
[1,3,5,6]，7 → 4
[1,3,5,6]，0 → 0
-----------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Feb 16,2016
"""
class Solution:
    """
    使用经典的二分法搜索插入的位置。
    1.初始化插入位置在数组的中间(length/2)
    
    2.和中间数判断大小关系并循环进行二分查找，如果相等，结束查找。如果子数组元素个数小于2，结束查找。
      中间数middle = array[length/2]
      左边的数组 = array[:middle](不包含中间数)
      右边的数组 = array[middle:](包含中间数)
      如果在左边的数组中，新的插入位置 = 旧的插入位置 - (左边数组的length+1)/2 (这里的加1很重要,相当于左边的插入位置要多移动一个元素的位置,因为不包含中间数)
      如果在右边的数组中，新的插入位置 = 旧的插入位置 + (右边数组的length)/2 (这里的不加1也很重要)

    3.验证插入位置对应的数是否小于要插入的数，如果是，插入位置向后+1。
    """
    """
    @param A : a list of integers
    @param target : an integer to be inserted
    @return : an integer
    """
    def searchInsert(self, A, target):
        position = None
        origin = A
        while True:
            if A != None:
                length = len(A)
                if length == 1:
                    if position == None:
                        position = 0
                    break
                elif length > 1:
                    middle = length/2
                    #init position
                    if position == None:
                        position = middle
                    if target == A[middle]:
                        break
                    elif target < A[middle]:
                        A = A[:middle]
                        #important to plus 1
                        position -= (len(A)+1)/2
                        continue
                    else:
                        A = A[middle:]
                        position += len(A)/2
                        continue
                else:
                    if position == None:
                        return 0
                    break
            return position
        if target <= origin[position]:
            return position
        else:
            #important to plus 1
            return position + 1

def main():
    n = raw_input("输入整数数组的长度,比如10:\n")
    n = int(n) if n != '' else 10
    import utils.RandomOrg.RandomOrgApi as random
    api = random.RandomOrgApi()
    array = api.integer_sets.generate(sets=1,num=n,min=-n/2,max=n,commas="on",order="index",format="plain",rnd="new")
    array.sort()
    print "随机生成的数组:", array
    solution = Solution()
    target = raw_input("输入要插入的整数:\n")
    target = int(target)
    print "%d可以在数组中插入的位置:%d" % (target, solution.searchInsert(array, target))

if __name__ == '__main__':
    main()