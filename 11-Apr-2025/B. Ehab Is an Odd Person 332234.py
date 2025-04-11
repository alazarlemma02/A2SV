# Problem: B. Ehab Is an Odd Person - https://codeforces.com/problemset/problem/1174/B

def solve(n, a):
    has_even = any(x % 2 == 0 for x in a)
    has_odd = any(x % 2 == 1 for x in a)

    if has_even and has_odd:
        a.sort()
    return " ".join(map(str, a))

n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))
