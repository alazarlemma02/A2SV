# Problem: Less or Equal - https://codeforces.com/problemset/problem/977/C

def lessrOrEqual(n,k,a):
    a.sort()

    if k == 0:
        return a[0]-1 if a[0]>1 else -1
    kth = a[k-1]

    if k < n  and  a[k]==kth:
        return -1
    return kth


n, k = map(int, input().split())

a = list(map(int, input().split()))

print(lessrOrEqual(n,k,a))
