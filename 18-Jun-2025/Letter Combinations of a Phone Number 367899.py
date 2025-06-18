# Problem: Letter Combinations of a Phone Number - https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        digit_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }
        n = len(digits)
        res = []
        def backtracking(idx, curr):
            if idx == n:
                res.append("".join(curr))
                return  

            for l in digit_map[digits[idx]]:
                curr.append(l)
                backtracking(idx+1, curr)
                curr.pop()    

        backtracking(0, [])
        return res

        