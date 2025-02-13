# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_map = {}
        for s_char, t_char in zip(s,t):
            if s_char in s_map:
                if s_map[s_char] != t_char:
                    return False
            elif t_char in s_map.values():
                return False
            else:
                s_map[s_char] = t_char
        return True 
        