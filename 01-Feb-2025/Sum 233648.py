# Problem: Sum - https://codeforces.com/contest/1742/problem/A

t = input()

for _ in range(int(t)):
    n = list(map(int, input().split()))
    if n[1]+n[2]==n[0]:
        print("YES")
    elif n[0]+n[2]==n[1]:
        print("YES")
    elif n[0]+n[1]==n[2]:
        print("YES")
    else:
        print("NO")