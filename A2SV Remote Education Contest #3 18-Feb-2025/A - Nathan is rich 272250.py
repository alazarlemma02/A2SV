# Problem: A - Nathan is rich - https://codeforces.com/gym/588094/problem/A

t = int(input())

for v in range(t):
    n = int(input())
    if n <=2:
        print(n//2)
    elif n % 4==0:
        print(n//4)
    else:
        r4 = n // 4
        r2 = (n - r4*4) // 2
        print(r4 + r2)