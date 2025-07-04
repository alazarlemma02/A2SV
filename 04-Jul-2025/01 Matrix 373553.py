# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rl, cl = len(mat), len(mat[0])
        res = [[-1] * cl for _ in range(rl)]
        queue = deque()

        for row in range(rl):
            for col in range(cl):
                if mat[row][col] == 0:
                    res[row][col] = 0
                    queue.append((row, col))

        dir = [(-1, 0),  (1, 0), (0, -1), (0, 1)]
        while queue:        
            r, c = queue.popleft()

            for dr, dc in dir:
                crow, ccol = r + dr, c + dc
                if 0 <= crow < rl and 0 <= ccol < cl and res[crow][ccol]==-1:
                    res[crow][ccol] = res[r][c] + 1
                    queue.append((crow, ccol))

        return res
