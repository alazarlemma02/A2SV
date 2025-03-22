# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s2), len(s1)
        if m > n:
            return False

        s1_map = Counter(s1)
        s2_map = Counter(s2[:m])

        if s1_map == s2_map:
            return True

        for i in range(m, n):
            s2_map[s2[i]] += 1
            s2_map[s2[i - m]] -= 1
            if s2_map[s2[i - m]] == 0:
                del s2_map[s2[i - m]]

            if s1_map == s2_map:
                return True

        return False