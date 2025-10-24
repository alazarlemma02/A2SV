# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            val = 1 if direction == 1 else -1
            diff[start] += val
            if end + 1 < len(diff):
                diff[end + 1] -= val

        for i in range(1, n):
            diff[i] += diff[i - 1]

        res = []
        for i, ch in enumerate(s):
            shift_val = diff[i] % 26 
            new_char = chr((ord(ch) - ord('a') + shift_val) % 26 + ord('a'))
            res.append(new_char)

        return ''.join(res)