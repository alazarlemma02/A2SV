# Problem: Heaters - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        n, m = len(heaters), len(houses)
        heaters.sort()
        rad = 0

        def pos_search(house):
            left, right = -1, n
            while right > left + 1:
                mid = (right + left) // 2
                if heaters[mid] < house:
                    left = mid
                else:
                    right = mid
                
            left_dist = float('inf') if left == -1 else abs(heaters[left] - house)
            right_dist = float('inf') if right == n else abs(heaters[right] - house)

            return min(left_dist, right_dist)

        for house in houses:
            curr = pos_search(house)
            rad = max(rad, curr)

        return rad        