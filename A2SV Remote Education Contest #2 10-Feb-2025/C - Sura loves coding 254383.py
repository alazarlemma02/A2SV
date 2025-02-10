# Problem: C - Sura loves coding - https://codeforces.com/gym/586622/problem/C

def sureLovesCoding(n, s):
    res = ""
    count = n
    for char in s:
        if count % 2 ==0:
            res = char + res
        else:
            res += char
        count -=1
    return res

n = int(input())
s = list(input())

result = sureLovesCoding(n, s)
print(result)


