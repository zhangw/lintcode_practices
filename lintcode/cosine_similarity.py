# -*- coding: utf-8 -*-
"""
cosine_similarity.py
--------------------
Cosine similarity is a measure of similarity between two vectors of an inner product space that measures the cosine of the angle between them. 
The cosine of 0° is 1, and it is less than 1 for any other angle.

Here is the formula:
http://www.lintcode.com/media/problem/cosine-similarity.png

Given two vectors A and B with the same size, calculate the cosine similarity.
Return 2.0000 if cosine similarity is invalid (for example A = [0] and B = [0]).
--------------------------------------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 22,2016
"""

class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: Cosine similarity.
    """
    def cosineSimilarity(self, A, B):
        ERROR_VALUE = 2.0000
        if len(A) != len(B):
            return ERROR_VALUE
        if len(A) == 0 or len(B) == 0:
            return ERROR_VALUE
        if A.count(0) == len(A) or B.count(0) == len(B):
            return ERROR_VALUE
        N = len(A)
        #refer to the formula:http://www.lintcode.com/media/problem/cosine-similarity.png
        dividend, multipliers = 0, {'a':0,'b':0}
        for n in range(0,N):
            dividend += A[n] * B[n]
            multipliers['a'] += A[n] * A[n]
            multipliers['b'] += B[n] * B[n]
        import math
        divisor = math.sqrt(multipliers['a']) * math.sqrt(multipliers['b'])
        return round(dividend/divisor,4)

def main():
    vectorA = [1,2,3]
    vectorB = [3,0,5]
    solution = Solution()
    print 'cosine similarity:%s' % solution.cosineSimilarity(vectorA,vectorB)

if __name__ == '__main__':
    main()
