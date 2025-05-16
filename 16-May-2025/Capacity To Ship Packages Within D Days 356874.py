# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        n = len(weights)

        def checkCap(capacity):
            cap, day_cnt = 0, 1

            for right in range(n):

                if cap + weights[right] > capacity:
                    cap = 0
                    day_cnt +=1

                cap += weights[right]

            return day_cnt <= days

        left, right = max(weights), sum(weights)

        while left < right:
            mid = (right + left)//2
            
            if checkCap(mid):
                right = mid
            else:
                left = mid + 1
        return left
                
            