# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        tasks.sort()
        wait_heap, time, res, i = [], 0, [], 0
        
        while i < n or wait_heap:
            if not wait_heap and i < n and time < tasks[i][0]:
                time = tasks[i][0]

            while i < n and tasks[i][0] <= time:
                heapq.heappush(wait_heap, (tasks[i][1], tasks[i][2]))
                i+=1

            pt, idx = heapq.heappop(wait_heap)
            res.append(idx)
            time += pt
        
        return res


        
                


        
        