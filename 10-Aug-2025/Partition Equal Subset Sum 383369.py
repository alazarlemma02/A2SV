# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            return False
        target = total // 2
        dp = set([0])

        for num in nums[::-1]:
            next = set()
            for i in dp:
                if i + num == target:
                    return True
                next.add(i+num)
                next.add(i)
            dp = next
        return True if target in dp else False