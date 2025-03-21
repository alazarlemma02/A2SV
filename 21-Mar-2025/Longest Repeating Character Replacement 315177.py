# Problem: Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        max_sub = 0
        i, curr = 0, k
        prev = 0
        s_map = defaultdict(int)
        
        for j in range(n):

            s_map[s[j]] +=1
            prev = max(prev, s_map[s[j]])

            while (j - i + 1) - prev > k:
                s_map[s[i]] -=1
                i += 1
            max_sub = max(max_sub, (j-i+1))

        return max_sub             
        
