# Problem: Team - https://codeforces.com/contest/231/problem/A

problem_count = 0
for _ in range(int(input())):
    view = map(int, input().split())
    if sum(view) > 1:
        problem_count +=1
print(problem_count)