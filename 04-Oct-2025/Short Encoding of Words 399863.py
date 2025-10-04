# Problem: Short Encoding of Words - https://leetcode.com/problems/short-encoding-of-words/

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        
        for w in list(words):
            for i in range(1, len(w)):
                sfx = w[i:]
                if sfx in words:
                    words.remove(sfx)
        
        return sum(len(w) + 1 for w in words)