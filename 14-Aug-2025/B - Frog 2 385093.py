# Problem: B - Frog 2 - https://atcoder.jp/contests/dp/tasks/dp_b

def solve(n, k, h):
    dp = [0] * n

    for i in range(1, n):
        cost = float('inf')
        for j in range(1, min(i, k)+1):
            cost = min(cost, dp[i-j] + abs(h[i] - h[i-j]))
        dp[i] = cost
    return dp[-1]

n, k = map(int, input().split())
h = list(map(int, input().split()))
print(solve(n, k, h))