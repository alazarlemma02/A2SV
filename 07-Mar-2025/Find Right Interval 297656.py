# Problem: Find Right Interval - https://leetcode.com/problems/find-right-interval/

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        sorted_intervals = []

        for i in range(n):
            sorted_intervals.append([intervals[i],i])
        sorted_intervals.sort()

        right_intervals = [-1] * n

        def binSearch(end):
            if sorted_intervals[n-1][0][0] < end: return -1

            low, high = 0, n-1
            while low <= high:
                mid = (low + high)//2
                if sorted_intervals[mid][0][0] >= end:
                    high = mid - 1
                else:
                    low = mid + 1
            return sorted_intervals[low][1]
            
        for i in range(n):
            right_intervals[i] = binSearch(intervals[i][1])

        return right_intervals

