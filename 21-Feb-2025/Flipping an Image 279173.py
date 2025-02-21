# Problem: Flipping an Image - https://leetcode.com/problems/flipping-an-image/description/

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rl, cl = len(image), len(image[0])
        new_img = [[0] * cl for _ in range(rl)]

        for row in range(rl):
            n = cl-1
            for col in range(cl):
                current = image[row][col]
                if current==1:
                    new_img[row][n] = 0
                else:
                    new_img[row][n] = 1
                n -=1
                
        return new_img
        