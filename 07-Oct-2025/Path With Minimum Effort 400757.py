# Problem: Path With Minimum Effort - https://leetcode.com/problems/path-with-minimum-effort/description/

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rl, cl = len(heights), len(heights[0])

        visited = set()
        min_heap = [[0, 0, 0]]

        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while min_heap:
            dist, row, col = heapq.heappop(min_heap)

            if (row, col) not in visited:
                visited.add((row, col))
                if (row, col) == (rl - 1, cl - 1):
                    return dist

                for dr, dc in dirs:
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < rl and 0 <= new_col < cl and (new_row, new_col) not in visited:
                        new_dist = max(dist, abs(heights[row][col] - heights[new_row][new_col]))
                        heapq.heappush(min_heap, [new_dist, new_row, new_col])
        