# Problem: Segment with Small Sum - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/A

n, s = map(int, input().split())
a = list(map(int, input().split()))

longest_seg = float('-inf')
curr_seg = 0
i = 0

for j in range(n):

    curr_seg += a[j]

    while curr_seg > s:
        prev_sum = curr_seg
        curr_seg -= a[i]
        i +=1

    longest_seg = max(longest_seg, j - i + 1)


print(longest_seg)
