# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        s_map = defaultdict(int)
        max_sub = 0

        i = 0

        for j in range(n):

            s_map[s[j]] +=1

            while s_map[s[j]] > 1:
                s_map[s[i]] -=1
                i +=1
            
            max_sub = max(max_sub, j - i + 1)

        return max_sub


        