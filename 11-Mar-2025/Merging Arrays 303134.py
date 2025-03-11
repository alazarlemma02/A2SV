# Problem: Merging Arrays - https://codeforces.com/edu/course/2/lesson/9/1/practice/contest/307092/problem/A

n, m = map(int, input().split())


a = list(map(int, input().split()))
b = list(map(int, input().split()))

ap, bp = 0, 0

res = []

while ap < n and bp < m:

    if a[ap] < b[bp]:
        res.append(a[ap])
        ap +=1
    else:
        res.append(b[bp])
        bp +=1

res.extend(a[ap:])
res.extend(b[bp:])
print(" ".join(map(str,res)))
