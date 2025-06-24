# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        def dfs(i):
            visited.add(i)
            for j in range(n):
                if j not in visited and isConnected[i][j]:
                    dfs(j)

        visited = set()
        province = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                province +=1
        return province
