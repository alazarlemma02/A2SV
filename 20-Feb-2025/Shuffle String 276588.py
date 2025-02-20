# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution(object):
    def restoreString(self, s, indices):
        shuffled = [''] * len(s)
        
        for i, char in enumerate(s):
            shuffled[indices[i]] = char
        
        return ''.join(shuffled)
        