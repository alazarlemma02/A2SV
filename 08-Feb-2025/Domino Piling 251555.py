# Problem: Domino Piling - https://codeforces.com/problemset/problem/50/A

def dominoPiling(m, n):
    larger_area = m * n
    qube_area = 2 * 1
    print(larger_area // qube_area)

m, n = list(map(int, input().split()))
dominoPiling(m, n)