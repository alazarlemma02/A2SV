# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res = []
        for num in nums1:
            ng = -1
            idx = nums2.index(num)
            for n in range(idx, len(nums2)):
                if nums2[n]>num:
                    ng = nums2[n]
                    break
            res.append(ng)
        return res
            
            
        
        