# Problem: Reduction Operations to Make the Array Elements Equal - LeetCode - https://leetcode.com/problems/reduction-operations-to-make-the-array-elements-equal/description/

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)

        count, i = 0, 0
        prev = nums[0]
        while i < len(nums):
            curr = nums[i]
            if prev != curr:
                count += n - i
            i +=1
            prev = curr
        return count
        

        