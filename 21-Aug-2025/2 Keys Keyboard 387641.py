# Problem: 2 Keys Keyboard - https://leetcode.com/problems/2-keys-keyboard/description/

class Solution:
    def minSteps(self, n: int) -> int:
        if n == 1:
            return 0
        if n == 2:
            return n

        memo = {}
        def dfs(cnt, prev):
            if cnt > n:
                return 1001
            if cnt == n:
                return 0
            if (cnt, prev) in memo:
                return memo[(cnt, prev)]
            
            paste = 1 + dfs(cnt+prev, prev)
            cpy = 2 + dfs(cnt+cnt, cnt)
            
            memo[(cnt, prev)] = min(cpy, paste)
            return memo[(cnt, prev)]

        return 2 + dfs(2, 1)