# Problem: Books - https://codeforces.com/contest/279/problem/B

def books(n,t,a):
    left, right = 0, 0
    max_count = 0
    curr = 0

    while right < n:
        curr += a[right]
        while curr > t:
            curr -= a[left]
            left +=1
        max_count = max(max_count, right-left+1)
        right +=1

    return max_count

n, t = map(int, input().split())
a = list(map(int, input().split()))

print(books(n,t,a))
