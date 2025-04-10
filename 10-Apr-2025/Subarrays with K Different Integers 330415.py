# Problem: Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:

        def counter(new_k):
            if new_k <= 0: return 0
            n = len(nums)
            i, cnt_map, cntr = 0, defaultdict(int), 0
            for j in range(n):
                cnt_map[nums[j]] +=1

                while len(cnt_map) > new_k:
                    cnt_map[nums[i]] -= 1
                    if cnt_map[nums[i]] == 0:
                        del cnt_map[nums[i]]
                    i += 1

                cntr += j - i + 1
            return cntr
        
        return counter(k) - counter(k-1)
        