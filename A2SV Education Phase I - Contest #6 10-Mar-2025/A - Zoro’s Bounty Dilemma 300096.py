# Problem: A - Zoro’s Bounty Dilemma - https://codeforces.com/gym/594356/problem/A

n, k = map(int, input().split())
 
a = list(map(int, input().split()))
 
a.sort(reverse=True)
 
print(a[k-1])