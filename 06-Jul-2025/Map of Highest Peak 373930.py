# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rl, cl = len(isWater), len(isWater[0])
        height = [[-1] * cl for _ in range(rl)]
        queue = deque()

        for i in range(rl):
            for j in range(cl):
                if isWater[i][j] == 1:
                    height[i][j] = 0
                    queue.append((i, j))

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in dirs:
                crow, ccol = r + dr, c + dc
                if 0 <= crow < rl and 0 <= ccol < cl and height[crow][ccol] == -1:
                    height[crow][ccol] = height[r][c] + 1
                    queue.append((crow, ccol))

        return height