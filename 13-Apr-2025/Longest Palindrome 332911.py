# Problem: Longest Palindrome - https://leetcode.com/problems/longest-palindrome/

class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt_map = Counter(s)
        n = len(cnt_map)
        res = 0
        chance = False

        for char in cnt_map:
            if cnt_map[char] % 2 == 0:
                res += cnt_map[char] 
            else:
                res += cnt_map[char] - 1
                chance = True
        if chance:
            res += 1
        return res