# Problem: Game of Life - https://leetcode.com/problems/game-of-life/description/

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rl, cl = len(board), len(board[0])
        def cntN(r,c):
            live_cnt, dead_cnt = 0, 0
            for i in range(r-1,r+2):
                for j in range(c-1,c+2):
                    if (i==r and j==c) or i<0 or j<0 or i==rl or j==cl:
                        continue
                    if board[i][j] in [1,3]: 
                        live_cnt +=1
                    else:
                        dead_cnt +=1
            return [live_cnt, dead_cnt]


        for row in range(rl):
            for col in range(cl):
                n_cnt = cntN(row,col)
                if board[row][col] == 1:
                    if n_cnt[0] in [2,3]:
                        board[row][col] = 3
                elif n_cnt[0] == 3:
                        board[row][col] = 2
        
        for row in range(rl):
            for col in range(cl):
                if board[row][col] in [2,3]:
                    board[row][col] = 1
                else:
                    board[row][col] = 0