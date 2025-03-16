# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n, m = len(firstList), len(secondList)
        intersection = []
        if n == 0 or m==0: return intersection
        
        i, j = 0, 0

        while i < n and j < m:
            starti, endi = firstList[i]
            startj, endj = secondList[j]

            if startj > endi:
                i +=1
            elif starti > endj:
                j +=1
            else:
                res = [max(starti,startj), min(endi, endj)]
                intersection.append(res)

                if endi < endj:
                    i +=1
                else:
                    j +=1
        return intersection

        