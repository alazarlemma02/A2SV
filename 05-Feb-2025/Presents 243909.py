# Problem: Presents - https://codeforces.com/problemset/problem/136/A

def giftRecievers(n, gifts):
    friends = []
    for f in range(n):
        friends.append([gifts[f], f+1])

    friends.sort()

    ans = []
    for i in range(len(friends)):
        ans.append(str(friends[i][1]))

    print(" ".join(ans))

n = int(input())
gifts = list(map(int, input().split()))
giftRecievers(n, gifts)
