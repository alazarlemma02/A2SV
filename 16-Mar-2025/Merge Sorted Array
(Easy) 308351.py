# Problem: Merge Sorted Array
(Easy) - https://leetcode.com/problems/merge-sorted-array/

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m, 0

        while j < n:
            nums1[i] = nums2[j]
            i +=1
            j +=1
        nums1.sort()
                    
        