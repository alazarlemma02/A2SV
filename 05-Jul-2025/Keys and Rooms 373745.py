# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)

        for i in range(len(rooms)):
            graph[i] = rooms[i]
        
        def bfs(node):
            qu = deque([node])
            while qu:
                curr = qu.popleft()
                visited.add(curr)
                for ngh in graph[curr]:
                    if ngh not in visited:
                        qu.append(ngh)

        all_rooms = set(range(0, len(rooms)))
        visited = set()
        bfs(0)
        return all_rooms == visited
        