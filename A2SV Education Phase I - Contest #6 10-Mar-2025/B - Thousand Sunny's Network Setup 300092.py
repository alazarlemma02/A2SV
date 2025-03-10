# Problem: B - Thousand Sunny's Network Setup - https://codeforces.com/gym/594356/problem/B

n, k = map(int, input().split())

a = list(map(int, input().split()))

a.sort(reverse=True)

print(a[k-1])
