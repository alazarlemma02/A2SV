# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area, left, right = 0, 0, n-1

        while left < right:
            min_height = min(height[left], height[right])
            width = right - left

            area = max(area, (min_height*width))

            if height[right] < height[left]:
                right -=1
            else:
                left +=1
        return area

        