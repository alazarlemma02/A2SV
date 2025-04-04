# Problem: Sereja and Dima - https://codeforces.com/problemset/problem/381/A

n = int(input())

cards = list(map(int, input().split()))

s, d = 0, 0

left, right = 0, n-1
turn = 0
while left <= right:
    if turn % 2 == 0:
        s += max(cards[left], cards[right])
    else:
        d += max(cards[left], cards[right])
    if cards[left] >= cards[right]:
        left += 1
    else:
        right -= 1
    turn +=1
print(s, d)