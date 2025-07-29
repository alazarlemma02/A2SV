# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque

n, m = map(int, input().split())
start, end = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    v, u = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

def bfs():
    while qu:
        curr = qu.popleft()
        if curr == end:
            path = []
            cnt = 0
            while curr:
                path.append(str(curr))
                curr = visited[curr]
                cnt +=1
            print(cnt-1)
            print(" ".join(path[::-1]))
            return
        for ngh in graph[curr]:
            if ngh not in visited:
                visited[ngh] = curr
                qu.append(ngh)
    print(-1)
    return

qu = deque([start])
visited = {}
visited[start] = None
bfs()