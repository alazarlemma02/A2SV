# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rl, cl = len(board), len(board[0])
        visited = [[0]*cl for _ in range(rl)]

        def dfs(row, col, cur):
            if cur >= len(word): 
                return True
            if row < 0 or row >= rl or col < 0 or col >= cl :
                return False
            if visited[row][col] or word[cur] != board[row][col]:
                return False

            visited[row][col] = True
            top = dfs(row-1,col, cur+1) 
            left = dfs(row, col-1, cur+1) 
            bottom = dfs(row+1, col, cur+1)
            right = dfs(row, col+1, cur+1)
            visited[row][col] = False

            return top or left or bottom or right

        for row in range(rl):
            for col in range(cl):
                if dfs(row, col, 0):
                    return True
        return False





        