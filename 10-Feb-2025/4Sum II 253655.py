# Problem: 4Sum II - https://leetcode.com/problems/4sum-ii/

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count = 0
        sum_map = {}
        for i in nums1:
            for j in nums2:
                res = i + j
                if res in sum_map:
                    sum_map[res] +=1
                else:
                    sum_map[res] =1
        for k in nums3:
            for l in nums4:
                res = -(k + l)
                if res in sum_map:
                    count += sum_map[res]

        return count