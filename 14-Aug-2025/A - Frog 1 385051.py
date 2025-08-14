# Problem: A - Frog 1 - https://atcoder.jp/contests/dp/tasks/dp_a

def solve(n, h):
    dp = [0] * n
    dp[1] = abs(h[1] - h[0])
    i = 2
    while i < n:
        cost = min(
            dp[i-1] + abs(h[i] - h[i-1]),
            dp[i-2] + abs(h[i] - h[i-2])
        )
        dp[i] = cost
        i +=1
    return dp[-1]

n = int(input())
h = list(map(int, input().split()))
print(solve(n, h))