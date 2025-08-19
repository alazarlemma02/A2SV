# Problem: C - Vacation - https://atcoder.jp/contests/dp/tasks/dp_c

import sys
sys.setrecursionlimit(2 * 10**5)

def solve(matrix, n):
    memo = {}
    def dfs(idx, curr):
        if idx >= n:
            return 0

        if (idx, curr) in memo:
            return memo[(idx, curr)]

        res = 0
        if curr == -1:
            res = max(res, matrix[idx][0] + dfs(idx+1, 0))
            res = max(res, matrix[idx][1] + dfs(idx+1, 1))
            res = max(res, matrix[idx][2] + dfs(idx+1, 2))
        elif curr == 0:
            res = max(res, matrix[idx][1] + dfs(idx+1, 1))
            res = max(res, matrix[idx][2] + dfs(idx+1, 2))

        elif curr == 1:
            res = max(res, matrix[idx][0] + dfs(idx+1, 0))
            res = max(res, matrix[idx][2] + dfs(idx+1, 2))
        else:
            res = max(res, matrix[idx][0] + dfs(idx+1, 0))
            res = max(res, matrix[idx][1] + dfs(idx+1, 1))
        memo[(idx, curr)] = res
        return res

    return dfs(0, -1)


n = int(input())
matrix = []
for _ in range(n):
    a, b, c = map(int, input().split())
    matrix.append([a, b, c])
print(solve(matrix, n))
