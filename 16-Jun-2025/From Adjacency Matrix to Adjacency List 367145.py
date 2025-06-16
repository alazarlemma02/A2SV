# Problem: From Adjacency Matrix to Adjacency List - https://www.eolymp.com/en/contests/9060/problems/78603

# example below, replace it with your solution
from collections import defaultdict
def solve(matrix, n):
    MAP = defaultdict(list)
    rl, cl = len(matrix), len(matrix[0])
    for row in range(rl):
        for col in range(cl):
            if matrix[row][col]:
                MAP[row+1] += [str(col+1)]
    
    for key in MAP:
        length = len(MAP[key])
        print(length, " ".join(MAP[key]))

n = int(input())
matrix = []
for _ in range(n):
    cur = list(map(int, input().split()))
    matrix.append(cur)
solve(matrix, n)
