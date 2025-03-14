# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort()
        min_time = 0
        n = len(processorTime)
        task_len = n * 4
        curr = 0
        curr_len = task_len-1

        for i in range(n):
            avail = processorTime[i]
            curr = tasks[curr_len] + avail
            min_time = max(min_time, curr)
            curr_len -=4
        return min_time






        