# -*- coding: utf-8 -*-
"""
hash_function.py
----------------
哈希函数
在数据结构中，哈希函数是用来将一个字符串（或任何其他类型）转化为小于哈希表大小且大于等于零的整数。
一个好的哈希函数可以尽可能少地产生冲突。一种广泛使用的哈希函数算法是使用数值33，假设任何字符串都是基于33的一个大整数，比如：
hashcode("abcd") = (ascii(a) * 33**3 + ascii(b) * 33**2 + ascii(c) *33 + ascii(d)) % HASH_SIZE 
                 = (97* 33**3 + 98 * 33**2 + 99 * 33 +100) % HASH_SIZE
                 = 3595978 % HASH_SIZE

其中HASH_SIZE表示哈希表的大小(可以假设一个哈希表就是一个索引0 ~ HASH_SIZE-1的数组)。

给出一个字符串作为key和一个哈希表的大小，返回这个字符串的哈希值。
样例:
对于key="abcd" 并且 size=100， 返回 78
注意:
对于这个问题你不需要自己设计hash算法，你只需要实现上述描述的hash算法即可。
----------------------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 24,2016
"""

class Solution:
    """
    @param key: A String you should hash
    @param HASH_SIZE: An integer
    @return an integer
    """
    def hashCode(self, key, HASH_SIZE):
        if key == None or len(key) == 0:
            return 0
        n = len(key) - 1
        s = 0
        HASH_BASE = 33
        #使用等差数列的求和公式简化计算,当key="aaaa..."
        if key.count(key[0]) == len(key):
            s = ord(key[0]) * (pow(HASH_BASE,n+1) - 1) / (HASH_BASE-1)
            return s%HASH_SIZE
        for c in key:
            s += ord(c) * pow(HASH_BASE,n)
            n -= 1
        return s%HASH_SIZE

def main():
    key = "A"*2**16
    print len(key)
    solution = Solution()
    print solution.hashCode(key,1000)

if __name__ == '__main__':
    main()

