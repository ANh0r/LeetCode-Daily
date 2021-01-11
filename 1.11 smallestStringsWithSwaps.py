class Solution:
    def bfs(self, res, graph, visited, x):
        queue = collections.deque([x])
        visited[x] = 1
        res.append(x)

        while queue:
            cur_node = queue.popleft()
            for neighbor in graph[cur_node]:
                if visited[neighbor]:
                    continue
                visited[neighbor] = 1
                res.append(neighbor)
                queue.append(neighbor)

    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # 建图
        graph = [[] for _ in range(len(s))]
        visited = [0] * len(s)
        for x, y in pairs:
            graph[x].append(y)
            graph[y].append(x)

        res = list(s)
        for i in range(len(s)):
            if not visited[i]:
                # 获取联通节点
                connected_nodes = []
                self.bfs(connected_nodes, graph, visited, i)
                # 重新赋值
                indices = sorted(connected_nodes)
                string = sorted(res[node] for node in connected_nodes)
                for j, ch in zip(indices, string):
                    res[j] = ch

        return "".join(res)
"""
给你一个字符串 s，以及该字符串中的一些「索引对」数组 pairs，其中 pairs[i] = [a, b] 表示字符串中的两个索引（编号从 0 开始）。

你可以 任意多次交换 在 pairs 中任意一对索引处的字符。

返回在经过若干次交换后，s 可以变成的按字典序最小的字符串。

 

示例 1:

输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释： 
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"
示例 2：

输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"
"""