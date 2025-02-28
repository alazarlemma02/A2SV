# Problem: Image Overlap - https://leetcode.com/problems/image-overlap/description/

class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        rl, cl = len(img1), len(img1[0])
        img1_ones, img2_ones = [], []

        for row in range(rl):
            for col in range(cl):
                if img1[row][col] == 1:
                    img1_ones.append((row,col))
                if img2[row][col] == 1:
                    img2_ones.append((row,col))
        print(img1_ones)
        print(img2_ones)

        count_map = defaultdict(int)

        for i in range(len(img1_ones)):
            for j in range(len(img2_ones)):
                diff = (img2_ones[j][0] - img1_ones[i][0], img2_ones[j][1] - img1_ones[i][1])
                count_map[diff] +=1
        
        max_overlap = 0
        for val in count_map.values():
            max_overlap = max(max_overlap, val)
        return max_overlap

        
            


        