# Problem: Assign Cookies - https://leetcode.com/problems/assign-cookies

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        len_g, len_s = len(g), len(s)

        if len_s < 1: return 0
        g.sort()
        s.sort()
        left, right, count = 0, 0, 0

        while left < len_g and right < len_s:
            if s[right] >= g[left]:
                count +=1
                left +=1
            right +=1
        return count