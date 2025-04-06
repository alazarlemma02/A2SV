# Problem: C - The Quantum Canyon Conundrum - https://codeforces.com/gym/596004/problem/C

def solve(n, a):

    new_a = [a[0]]
    for i in range(n):
        if new_a[-1] != a[i]:
            new_a.append(a[i])

    cnt_canyon = 0
    k = len(new_a)
    if k == 1 or k ==2:
        return "YES"
    for i in range(k):
        if i == 0 and new_a[i+1] > new_a[i]:
            cnt_canyon += 1
        elif i == k-1 and new_a[i-1] > new_a[i]:
            cnt_canyon +=1
        else:
            if new_a[i-1] > new_a[i] and new_a[i] < new_a[i+1]:
                cnt_canyon +=1
    if cnt_canyon != 1:
        return "NO"
    return "YES"

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(solve(n, a))
