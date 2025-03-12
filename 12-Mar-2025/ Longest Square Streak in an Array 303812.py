# Problem:  Longest Square Streak in an Array - https://leetcode.com/problems/longest-square-streak-in-an-array/description/?envType=problem-list-v2&envId=sorting

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()

        sqrt_map = defaultdict(int)

        for num in nums:
            sqrt_map[num**2] = num
        
        output = 0
        for num in nums:
            count = 0
            sq = num**2
            while sq in sqrt_map:
                count +=1
                sq = sqrt_map[sq]
            output = max(output, count)

        return -1 if output<=1 else output

            



        