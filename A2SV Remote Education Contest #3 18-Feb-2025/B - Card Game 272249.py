# Problem: B - Card Game - https://codeforces.com/gym/588094/problem/B

from collections import defaultdict
n = int(input())

cards = list(map(int, input().split()))

idx_map = defaultdict(list)
for c in range(n):
    idx_map[cards[c]] += [c+1]

cards.sort()
left, right = 0, n-1
while left < right:
    left_idx = idx_map[cards[left]].pop(0)
    right_idx = idx_map[cards[right]].pop(0)
    print(f"{left_idx} {right_idx}")
    left +=1
    right -=1