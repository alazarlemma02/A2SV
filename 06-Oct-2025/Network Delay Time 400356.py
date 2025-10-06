# Problem: Network Delay Time - https://leetcode.com/problems/network-delay-time/description/

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        shortest_times = {}
        min_heap = [(0, k)]

        while min_heap:
            time_dis, node = heapq.heappop(min_heap)

            if node not in shortest_times:
                shortest_times[node] = time_dis
                
                for ngh, ngh_time in graph[node]:
                    if ngh not in shortest_times:
                        heapq.heappush(min_heap, (time_dis + ngh_time, ngh))

        if len(shortest_times) == n:
            return max(shortest_times.values())
        return -1

        