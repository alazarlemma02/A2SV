# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        cnt = 0
        prev = intervals[0][1]

        for start, end in intervals[1:]:
            if start < prev:
                cnt +=1
            else:
                prev = end
        return cnt
        
