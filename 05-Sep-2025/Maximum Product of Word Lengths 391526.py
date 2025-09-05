# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        masks = [0] * n
        word_len = [len(word) for word in words]

        for i, word in enumerate(words):
            for char in word:
                masks[i] = masks[i] | 1 << (ord(char) - ord('a'))

        res = 0
        for i in range(n):
            for j in range(i+1, n):
                if masks[i] & masks[j] == 0:
                    res = max(res, word_len[i] * word_len[j])
        return res

        
        