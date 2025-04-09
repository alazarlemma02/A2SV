# Problem: Number of Substrings Containing All Three Characters - https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        l, cntr= 0, 0
        
        cnt_map = defaultdict(int)

        for r in range(len(s)):
            cnt_map[s[r]] += 1
                
            while len(cnt_map) == 3: 
                cntr += len(s) - r
                cnt_map[s[l]] -= 1
                if cnt_map[s[l]] == 0:
                    del cnt_map[s[l]]
                
                l += 1

        return cntr

        