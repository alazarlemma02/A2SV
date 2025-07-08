# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graphR, graphB = defaultdict(list), defaultdict(list)

        for u, v in redEdges:
            graphR[u].append(v)
        for u, v in blueEdges:
            graphB[u].append(v)

        res = [-1] * n

        visited = set()
        qu = deque()

        qu.append((0, 0, -1))
        visited.add((0, -1))
        res[0] = 0

        while qu:
            node, dist, last_color = qu.popleft()

            if last_color != 0:
                for ngh in graphR[node]:
                    if (ngh, 0) not in visited:
                        visited.add((ngh, 0))
                        if res[ngh] == -1:
                            res[ngh] = dist + 1
                        qu.append((ngh, dist + 1, 0))

            if last_color != 1:
                for ngh in graphB[node]:
                    if (ngh, 1) not in visited:
                        visited.add((ngh, 1))
                        if res[ngh] == -1:
                            res[ngh] = dist + 1
                        qu.append((ngh, dist + 1, 1))

        return res