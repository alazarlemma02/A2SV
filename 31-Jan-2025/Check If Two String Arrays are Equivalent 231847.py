# Problem: Check If Two String Arrays are Equivalent - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        ans = "".join(word1)=="".join(word2)
        return ans
        