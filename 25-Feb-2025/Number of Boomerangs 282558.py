# Problem: Number of Boomerangs - https://leetcode.com/problems/number-of-boomerangs/description/

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2: return 0

        total_boomerangs = 0
        for point in points:
            dist_map = defaultdict(int)
            for point2 in points:
                x = (point2[0]-point[0])**2
                y = (point2[1]-point[1])**2
                dist = x + y
                dist_map[dist] += 1
            for dis in dist_map:
                total_boomerangs += dist_map[dis] * (dist_map[dis]-1)

        return total_boomerangs
        

        