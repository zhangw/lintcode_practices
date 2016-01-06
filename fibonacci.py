# -*- coding: utf-8 -*-
"""
fibonacci.py

Created by <jimokanghanchao@gmail.com> on Jan 06,2016
"""
class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def __init__(self):
        #cache the result to reduce the duplicate calculations
        self.caches = {1:0,2:1}

    def fibonacci(self, n):
        # write your code here
        if n == 1 or n == 2:
            return self.caches[n]
        else:
            if self.caches.has_key(n-1):
                n_1 = self.caches[n-1]
            else:
                n_1 = self.fibonacci(n-1)
            if self.caches.has_key(n-2):
                n_2 = self.caches[n-2]
            else:
                n_2 = self.fibonacci(n-2)
            self.caches[n] = n_1 + n_2
            return self.caches[n]

if __name__ == '__main__':
    solution = Solution()
    n = raw_input('input the N number in fibonacci:\n')
    try:
      n = int(n)
      if n >= 1:
        ret = solution.fibonacci(n)
        print 'result:%d' % ret
    except:
      pass
