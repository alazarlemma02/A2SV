# Problem: Fox And Snake - https://codeforces.com/problemset/problem/510/A

rl, cl = map(int, input().split())

left = False
right = True

for row in range(rl):
    for col in range(cl):
        if row % 2 == 0:
            print("#",end="")
        else:
            if col == cl-1 and right:
                print("#",end="")
            elif col == 0 and left:
                print("#",end="")
            else:
                print(".",end="")
    if row % 2 != 0:
        left, right = right, left
    print()