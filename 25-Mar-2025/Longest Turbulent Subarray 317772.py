# Problem: Longest Turbulent Subarray - https://leetcode.com/problems/longest-turbulent-subarray/

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 1: return 1

        i, j, max_tur = 1, 1, 1 

        for k in range(1, n):
            if arr[k] > arr[k-1]:
                i = j + 1
                j = 1
            elif arr[k] < arr[k-1]:
                j = i + 1
                i = 1
            else:
                i = j = 1
            max_tur = max(max_tur, i, j)

        return max_tur
