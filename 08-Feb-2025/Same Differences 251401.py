# Problem: Same Differences - https://codeforces.com/problemset/problem/1520/D

test_cases = int(input())

for _ in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    MAP = {}
    for i in range(n):
        if a[i]-i in MAP:
            count += MAP[a[i]-i]
            MAP[a[i]-i] += 1
        else:
            MAP[a[i]-i] = 1
    print(count)
