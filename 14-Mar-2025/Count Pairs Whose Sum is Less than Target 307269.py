# Problem: Count Pairs Whose Sum is Less than Target - https://leetcode.com/problems/count-pairs-whose-sum-is-less-than-target/

class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        count = 0

        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                if 0 <= i < j < n and nums[i] + nums[j] < target:
                    count +=1
        return count