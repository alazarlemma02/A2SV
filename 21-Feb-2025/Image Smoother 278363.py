# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rl, cl = len(img), len(img[0])
        new_img = [[0] * cl for _ in range(rl)]

        for row in range(rl):
            for col in range(cl):
                total, div= 0, 0
                for r in range(row-1, row+2):
                    for c in range(col-1, col+2):
                        if 0 <= r < rl and 0 <= c < cl:
                            total += img[r][c]
                            div += 1
                average = total // div
                new_img[row][col] = average
        return new_img