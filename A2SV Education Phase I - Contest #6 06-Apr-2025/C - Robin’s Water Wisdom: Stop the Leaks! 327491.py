# Problem: C - Robin’s Water Wisdom: Stop the Leaks! - https://codeforces.com/gym/594356/problem/C

def waterWisdom(A,B,s):
    curr_total = sum(s)
    idx1 = s[0]

    min_holes = 0
    if (idx1/curr_total)*A >= B:
        return min_holes

    others = sorted(s[1:])
    right = len(others)-1

    while right >= 0:
        curr_total -= others[right]
        min_holes +=1
        if (idx1/curr_total)*A >= B:
            return min_holes
        right -=1
    return len(s)-1

n, A, B = map(int, input().split())

s = list(map(int, input().split()))

print(waterWisdom(A,B,s))

