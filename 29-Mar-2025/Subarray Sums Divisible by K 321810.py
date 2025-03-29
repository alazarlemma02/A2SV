# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        sub_map = {0: 1}
        prx_sum = 0
        cnt = 0

        for num in nums:
            prx_sum += num
            rem = prx_sum % k
            if rem in sub_map:
                cnt += sub_map[rem]
                sub_map[rem] += 1
            else:
                sub_map[rem] = 1
        return cnt
        