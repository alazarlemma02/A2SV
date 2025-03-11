# Problem: Number of smaller - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/B

n, m = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

res = []
prev = 0

for num in b:
    while prev < len(a) and a[prev] < num:
        prev +=1
    res.append(prev)

print(" ".join(map(str, res)))
