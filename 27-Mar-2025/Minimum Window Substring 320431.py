# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        t_map = Counter(t)
        s_map = defaultdict(int)

        if n == 0 or m == 0: return ""

        i, res = 0, ""
        have, need = 0, len(t_map)
        min_count = float("inf")

        for j in range(m):
            s_map[s[j]] +=1

            if s[j] in t_map and s_map[s[j]] == t_map[s[j]]:
                have +=1

            while have == need:
                if (j-i+1) < min_count:
                    min_count = (j-i+1)
                    res = s[i:j+1]

                s_map[s[i]] -=1
                if s[i] in t_map and s_map[s[i]] < t_map[s[i]]:
                    have -=1
                i +=1

            
        return res if min_count != float("inf") else ""



        