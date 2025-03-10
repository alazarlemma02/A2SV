# Problem: A - Zoro’s Bounty Dilemma - https://codeforces.com/gym/594356/problem/A

t = int(input())

for _ in range(t):
    s = list(map(str, input().split()))
    if ">" in s[0] and "<" in s[0]:
        print("?")
    elif ">" in s[0]:
        print(">")
    elif "<" in s[0]:
        print("<")
    else:
        print("=")

