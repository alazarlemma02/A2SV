# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def winner(left, right):
            if left == right:
                return nums[left]

            take_left = nums[left] - winner(left + 1, right)

            take_right = nums[right] - winner(left, right - 1)

            return max(take_left, take_right)

        return winner(0, len(nums)-1) >= 0

        