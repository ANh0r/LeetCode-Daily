class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # dfs
        def dfs(p):
            if p[-1] == target:
                ret.append(p[:])
            else:
                for i in graph[p[-1]]:
                    p.append(i)
                    dfs(p)
                    p.pop()

        ret = []
        target = len(graph) - 1
        dfs([0])
        return ret