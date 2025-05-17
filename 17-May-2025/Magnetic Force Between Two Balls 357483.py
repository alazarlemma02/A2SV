# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()

        def check(pos):
            cnt = 1
            last_ball = position[0]

            for p in position:
                if p - last_ball >= pos:
                    cnt +=1
                    last_ball = p
            return cnt >= m


        left, right = 1, max(position)
        while left <= right:
            mid = (right + left) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
        