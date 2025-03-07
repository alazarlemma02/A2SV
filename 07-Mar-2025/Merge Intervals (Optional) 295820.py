# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) < 2: return intervals 
        res = []
        intervals.sort()
        for i in range(len(intervals)):
            if len(res) > 0:
                last = res[-1]
                if last[1] >= intervals[i][0]:
                    if res[-1][1] >= intervals[i][1]:
                        continue
                    res[-1][1] = intervals[i][1]
                else:
                    res.append(intervals[i])
            else:
                res.append(intervals[i])
        return res

