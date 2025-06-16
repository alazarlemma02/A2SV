# Problem: Cities and Roads - https://www.eolymp.com/en/contests/9060/problems/78597

# example below, replace it with your solution
def solve(matrix):
    if not len(matrix): return 0
    rl, cl = len(matrix), len(matrix[0])
    res = 0
    for row in range(rl):
        for col in range(cl):
            if matrix[row][col]:
                res += 1
    return res // 2

n = int(input())
matrix = []
for _ in range(n):
    curr = list(map(int, input().split()))
    matrix.append(curr)
print(solve(matrix))