# Problem: D - Adjacents, ewww ! - https://codeforces.com/gym/588094/problem/D

t = int(input())

for _ in range(t):
    n = int(input())

    if n ==2:
        print(-1)
        continue
    
    matrix = [[0]*n for _ in range(n)]

    odd = 1
    for i in range(n):
        for j in range(n):
            if odd <= n**2:
                matrix[i][j] = odd
                odd += 2
    even = 2
    for i in range(n):
        for j in range(n):
            if matrix[i][j] == 0:
                matrix[i][j] = even
                even += 2

    for row in matrix:
        print(*row)
