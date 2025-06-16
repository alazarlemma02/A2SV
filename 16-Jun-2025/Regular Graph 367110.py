# Problem: Regular Graph - https://basecamp.eolymp.com/en/problems/5076

# example below, replace it with your solution
def solve(n, m):
    degrees = [0]*(n+1)
    for _ in range(m):
        a, b = map(int, input().split())
        degrees[a] +=1
        degrees[b] +=1
    check = len(set(degrees[1:])) == 1
    if check:
        return "YES"
    return "NO"

n, m = map(int, input().split())
print(solve(n, m))
