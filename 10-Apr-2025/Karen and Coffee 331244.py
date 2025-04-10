# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

from collections import defaultdict

n, k, q = map(int, input().split())
map1 = defaultdict(int)

for _ in range(n):
    a, b = map(int, input().split())
    map1[a] += 1
    map1[b+1] -= 1

max_temp = 2*10**5+1
count = [0] * max_temp
for i in range(1, max_temp):
    count[i] = count[i-1] + map1[i]

admissible = [0] * max_temp
for i in range(1, max_temp):
    admissible[i] = 1 if count[i] >= k else 0

prefix = [0] * max_temp
for i in range(1, max_temp):
    prefix[i] = prefix[i-1] + admissible[i]


for _ in range(q):
    left, right = map(int, input().split())
    print(prefix[right] - prefix[left-1])

