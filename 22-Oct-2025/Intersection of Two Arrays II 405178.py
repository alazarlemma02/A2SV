# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution(object):
    def intersect(self, nums1, nums2):
        count_map = {}
        for num in nums1:
            count_map[num] = count_map.get(num, 0) + 1

        res = []
        for num in nums2:
            if count_map.get(num, 0) > 0:
                res.append(num)
                count_map[num] -= 1

        return res
        