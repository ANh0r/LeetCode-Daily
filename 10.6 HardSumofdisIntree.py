
from typing import List
"""
给定一个无向、连通的树。树中有 N 个标记为 0...N-1 的节点以及 N-1 条边 。

第 i 条边连接节点 edges[i][0] 和 edges[i][1] 。

返回一个表示节点 i 与其他所有节点距离之和的列表 ans。

示例 1:

输入: N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
输出: [8,12,6,10,10,10]
解释: 
如下为给定的树的示意图：
  0
 / \
1   2
   /|\
  3 4 5

我们可以计算出 dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5) 
也就是 1 + 1 + 2 + 2 + 2 = 8。 因此，answer[0] = 8，以此类推。


"""
class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        def dfs1(u, f):
            sz[u] = 1
            dp[u] = 0
            for v in graph[u]:
                if v == f:
                    continue
                dfs1(v, u)
                dp[u] += (dp[v] + sz[v])
                sz[u] += sz[v]

        def dfs2(u, f):
            ans[u] = dp[u]
            for v in graph[u]:
                if v == f:
                    continue
                pu = dp[u]
                pv = dp[v]
                su = sz[u]
                sv = sz[v]
                dp[u] -= (dp[v] + sz[v])
                sz[u] -= sz[v]
                dp[v] += (dp[u] + sz[u])
                sz[v] += sz[u]
                dfs2(v, u)
                dp[u] = pu
                dp[v] = pv
                sz[u] = su
                sz[v] = sv

        ans = [0 for i in range(N)]
        sz = [0 for i in range(N)]
        dp = [0 for i in range(N)]
        graph = [[] for i in range(N)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            graph[u].append(v)
            graph[v].append(u)
        dfs1(0, -1)
        dfs2(0, -1)
        return ans