# Problem: N Queens - https://leetcode.com/problems/n-queens/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[False]*n for _ in range(n)]
        results = []

        def queens(row):
            if row == n:
                results.append(place(board))
                return

            for col in range(n):
                if isSafe(row, col):
                    board[row][col] = True
                    queens(row+1)
                    board[row][col] = False
            

        def isSafe(row, col):
            for i in range(row+1):
                if board[i][col]:
                    return False

            i, j = row-1, col-1
            while i >= 0 and j >=0:
                if board[i][j]:
                    return False
                i -=1
                j -=1

            i, j = row-1, col+1
            while i >= 0 and j < n:
                if board[i][j]:
                    return False
                i -=1
                j +=1

            return True


        def place(board):
            ans = []
            for row in board:
                res = ''
                for cell in row:
                    if cell:
                        res += 'Q'
                    else:
                        res += '.'
                ans.append(res)
            return ans

        queens(0)
        return results
