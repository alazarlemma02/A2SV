# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)

        min_opp = float("inf")

        i, count = 0, 0

        for j in range(n):

            if blocks[j] == "W":
                count +=1

            if j+1 >= k:
                min_opp = min(min_opp, count)
                if blocks[i] == "W":
                    count -=1
                i +=1
            
        return min_opp            


        