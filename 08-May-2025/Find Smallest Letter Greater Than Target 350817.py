# Problem: Find Smallest Letter Greater Than Target - https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        n = len(letters)

        left, right = 0, n-1
        res = letters[0]

        while left <= right:
            mid = (right + left) // 2
            if letters[mid]  > target:
                res = letters[mid]
                right = mid -1
            else:
                left = mid + 1
        return res

            

        