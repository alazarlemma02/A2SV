# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rl, cl = len(maze), len(maze[0])

        def inbound(row, col):
            return row >= 0 and col >= 0 and row < rl and col < cl

        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = "+"
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        while queue:
            row, col, dist = queue.popleft()
            for dx, dy in dirs:
                cr, cc = row + dx, col + dy
                if inbound(cr, cc) and maze[cr][cc] == ".":
                    if cr == 0 or cc == 0 or cr == rl-1 or cc == cl-1:
                        return dist + 1
                    queue.append((cr, cc, dist+1))
                    maze[cr][cc] = "+"       
            
        return -1
        