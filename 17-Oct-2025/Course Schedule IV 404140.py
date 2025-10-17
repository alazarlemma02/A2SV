# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for p, c in prerequisites:
            graph[c].append(p)

        def dfs(cour):
            if cour not in pre_map:
                pre_map[cour] = set()
                for preq in graph[cour]:
                    pre_map[cour] |= dfs(preq)
                pre_map[cour].add(cour)
            return pre_map[cour]

        pre_map = defaultdict(set)
        for cour in range(numCourses):
            dfs(cour)

        res = []
        for u, v in queries:
            res.append(u in pre_map[v])
        return res
        