# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            a, b = edges[i]
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])

        visited = set()
        hq = [(-1, start_node)]

        while hq:
            prob, node = heapq.heappop(hq)
            visited.add(node)

            if node == end_node:
                return -prob

            for ngh, ngh_prob in graph[node]:
                if ngh not in visited:
                    heapq.heappush(hq, (prob*ngh_prob, ngh))
        return 0