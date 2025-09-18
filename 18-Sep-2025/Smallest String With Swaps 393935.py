# Problem: Smallest String With Swaps - https://leetcode.com/problems/smallest-string-with-swaps/

class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        parent = list(range(n))


        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
        
        def union(a, b):
            parent[find(a)] = find(b)

        for a, b in pairs:
            union(a, b)

        groups = defaultdict(list)
        for i in range(n):
            root = find(i)
            groups[root].append(i)

        res = list(s)
        for indices in groups.values():
            chars = [s[i] for i in indices]
            indices.sort()
            chars.sort()
            for i, ch in zip(indices, chars):
                res[i] = ch

        return "".join(res)