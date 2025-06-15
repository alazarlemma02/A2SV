# Problem: Median of Two Sorted Arrays - https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        res = 0
        m, n = len(nums1), len(nums2)
        if m > n:
            return self.findMedianSortedArrays(nums2, nums1)

        start, end = 0, m
        total_partition = (m + n + 1) // 2
        even = (m + n) % 2 == 0

        while start <= end:
            mid = (end + start) // 2
            y = total_partition - mid

            maxleftM = float('-inf') if mid == 0 else nums1[mid-1]
            maxleftN = float('-inf') if y == 0 else nums2[y-1]

            minrightM = float('inf') if mid == m else nums1[mid]
            minrightN = float('inf') if y == n else nums2[y]
            
            if maxleftM <= minrightN and maxleftN <= minrightM:
                if even:
                    l, r = max(maxleftM, maxleftN), min(minrightM, minrightN)
                    return (l + r) / 2
                else:
                    return max(maxleftM, maxleftN)
                
            elif maxleftN > minrightM:
                start = mid + 1
            else:
                end = mid - 1
