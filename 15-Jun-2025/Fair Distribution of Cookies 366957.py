# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)

        def dfs(i, dist):
            nonlocal res
            if i >= n:
                res = min(res, max(dist))
                return 
            elif max(dist) > res:
                return
                
            for j in range(k):
                dist[j] += cookies[i]
                dfs(i+1, dist)
                dist[j] -= cookies[i]

            return res

        res = float('inf')
        dist = [0]*k
        return dfs(0, dist)

        

