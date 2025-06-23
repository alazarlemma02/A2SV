# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        def dfs(row, col):
            if row < 0 or row >= rl or col < 0 or col >= cl or board[row][col] != "O":
                return
            board[row][col] = "#"

            dfs(row-1, col)
            dfs(row, col-1)
            dfs(row+1, col)
            dfs(row, col+1)
            
        rl, cl = len(board), len(board[0])
        for row in range(rl):
            for col in range(cl):
                if board[row][col] == "O" and (row in [0, rl-1] or col in [0, cl-1]):
                    dfs(row, col)
        
        for row in range(rl):
            for col in range(cl):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "#":
                    board[row][col] = "O"

        