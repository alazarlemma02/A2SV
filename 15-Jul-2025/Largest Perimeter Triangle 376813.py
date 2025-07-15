# Problem: Largest Perimeter Triangle - https://leetcode.com/problems/largest-perimeter-triangle/

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        n = len(nums)
        a, b, c = 0, 1, 2

        while c <= n-1:
            if nums[b] + nums[c] > nums[a]:
                return nums[a] + nums[b] + nums[c]
            a +=1
            b +=1
            c +=1
        return 0

            

        