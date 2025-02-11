# Problem: Maximum Number of Pairs in Array - https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        count = 0
        leftover = 0
        nums_map = Counter(nums)
        for num in nums_map:
            if nums_map[num]%2==0:
                count += nums_map[num]//2
            else:
                count += nums_map[num]//2
                leftover += nums_map[num]%2
        return [count, leftover]
        