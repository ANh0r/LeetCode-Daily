class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1:
            return -1

        edges = collections.defaultdict(list)
        for x, y in connections:
            edges[x].append(y)
            edges[y].append(x)

        seen = set()

        def dfs(u: int):
            seen.add(u)
            for v in edges[u]:
                if v not in seen:
                    dfs(v)

        ans = 0
        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1

        return ans - 1