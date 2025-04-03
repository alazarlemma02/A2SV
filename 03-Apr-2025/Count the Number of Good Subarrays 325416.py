# Problem: Count the Number of Good Subarrays - https://leetcode.com/problems/count-the-number-of-good-subarrays/description/

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        right, good_sub = 0, 0
        num_map = defaultdict(int)
        pairs = 0

        for left in range(n):
            while right < n and pairs < k:
                num_map[nums[right]] +=1
                pairs += num_map[nums[right]] - 1
                right +=1

            if pairs >= k:
                good_sub += n - right + 1
            else:
                return good_sub

            num_map[nums[left]] -=1
            pairs -= num_map[nums[left]]

        return good_sub        