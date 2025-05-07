# Problem: Guess Number Higher or Lower  - https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        min, max = 1, n
        while min<=max:
            mid = (min+max)//2
            pick = guess(mid)
            if  pick == 0:
                return mid
            elif pick == -1:
                max = mid-1
            else:
                min = mid+1
        return min
        