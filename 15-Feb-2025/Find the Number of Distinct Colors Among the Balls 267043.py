# Problem: Find the Number of Distinct Colors Among the Balls - https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        color_fre = defaultdict(int)
        color_map = defaultdict(int)
        res = []
        for q in queries:
            if q[0] in color_map:
                prev_color = color_map[q[0]]
                color_fre[prev_color] -=1
                if color_fre[prev_color] <=0:
                    del color_fre[prev_color]
            color_map[q[0]] = q[1]
            color_fre[q[1]] += 1
            res.append(len(color_fre))
        return res
        

          