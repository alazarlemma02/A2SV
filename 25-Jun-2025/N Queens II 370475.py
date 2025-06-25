# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0]*n for _ in range(n)]
        results = []

        def helper(row):
            if row == n:
                results.append(1)
                return

            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = 1
                    helper(row+1)
                    board[row][col] = 0
            return False

        def isSafe(row, col):
            for r in range(row+1):
                if board[r][col]: return False

            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c]: return False
                r -=1
                c -=1

            r, c = row, col
            while r >= 0 and c < n:
                if board[r][c]: return False
                r -=1
                c +=1

            return True
  
        helper(0)
        return len(results)