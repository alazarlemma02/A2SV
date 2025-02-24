# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rl, cl = len(mat), len(mat[0])
        sum_map = defaultdict(list)
        res = []

        for row in range(rl):
            for col in range(cl):
                sum_map[row+col] += [(row,col)]
        
 
        for key in sum_map:
            if key % 2 ==0:
                for idx in reversed(sum_map[key]):
                    res.append(mat[idx[0]][idx[1]])
            else:
                for idx in sum_map[key]:
                    res.append(mat[idx[0]][idx[1]])
        return res
        