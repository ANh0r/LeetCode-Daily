class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        dp = [-1] * n
        def dfs(i):
            if dp[i] < 0:
                dp[i] = 0
                dp[i] = +all(map(dfs, graph[i]))
            return dp[i]
        return [*filter(dfs, range(n))]