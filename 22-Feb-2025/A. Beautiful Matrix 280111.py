# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

def beautifulMatrix(matrix):
    rl, cl = len(matrix), len(matrix[0])
    rc = cc = rl // 2
    res = 0
    for row in range(rl):
        for col in range(cl):
            if matrix[row][col] == 1:
                res = abs(row-rc) + abs(col-cc)
                return res


matrix = [list(map(int, input().split())) for _ in range(5)]
print(beautifulMatrix(matrix=matrix))