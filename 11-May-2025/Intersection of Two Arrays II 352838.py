# Problem: Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution(object):
    def intersect(self, nums1, nums2):
        count_map = {}
        for num in nums1:
            if num in count_map:
                count_map[num]+=1
            elif num in nums2:
                count_map[num]=1
        res = []
        for num in nums2:
            if num in count_map and count_map[num]>0:
                res.append(num)
                count_map[num]-=1
        return res
        