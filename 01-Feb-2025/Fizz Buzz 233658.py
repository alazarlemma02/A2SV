# Problem: Fizz Buzz - https://leetcode.com/problems/fizz-buzz/description/

class Solution(object):
    def fizzBuzz(self, n):
        result = []
        idx = 1
        while idx <= n:
            if idx % 3 == 0 and idx % 5 == 0:
                result.append("FizzBuzz")
            elif idx % 3 == 0:
                result.append("Fizz")
            elif idx % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(idx))
            idx+=1
        return result
        