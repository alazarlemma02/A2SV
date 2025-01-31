# Problem: Watermelon - https://codeforces.com/problemset/problem/4/A

testCase = int(input())
if testCase <=2:
    print("NO")
    exit()
result = testCase-2
if result%2==0:
    print("YES")
else:
    print("NO")
