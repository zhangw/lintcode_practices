# -*- coding: utf-8 -*-
"""
longest_words.py
----------------
最长单词
给一个词典，找出其中所有最长的单词。

样例:
在词典
{
  "dog",
  "google",
  "facebook",
  "internationalization",
  "blabla"
}
中, 最长的单词集合为 ["internationalization"]

在词典
{
  "like",
  "love",
  "hate",
  "yes"
}
中，最长的单词集合为 ["like", "love", "hate"]

挑战:
遍历两次的办法很容易想到，如果只遍历一次你有没有什么好办法？
---------------------------------------------------
Created by <jimokanghanchao@gmail.com> on Jan 26,2016
"""

class Solution:
    # @param dictionary: a list of strings
    # @return: a list of strings
    def longestWords(self, dictionary):
        results = []
        longest = 0
        length = len(dictionary)
        i = 0
        #once traversal
        while i < length:
            word = dictionary[i]
            temp_length = len(word)
            if longest < temp_length:
                results = []
                results.append(word)
                longest = temp_length
            elif longest == temp_length:
                results.append(word)
            i += 1
        return results

def main():
    dictionarywords = ["dog","love","google","amazon","facebook","network","pythoner"]
    solution = Solution()
    print "given the dictionary=>", dictionarywords
    print "the longest words in it=>", solution.longestWords(dictionarywords)

if __name__ == '__main__':
    main()

