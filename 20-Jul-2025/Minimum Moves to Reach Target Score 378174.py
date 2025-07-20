# Problem: Minimum Moves to Reach Target Score - https://leetcode.com/problems/minimum-moves-to-reach-target-score/

class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target > 1 and maxDoubles==0:
            return target-1
        canDivide = maxDoubles
        cnt = 0

        curr = target
        while curr > 1:
            if canDivide == 0:
                return cnt + curr -1
            if curr % 2 == 0 and canDivide > 0:
                curr //=2
                canDivide -=1
            else:
                curr -= 1
            cnt +=1
        return cnt