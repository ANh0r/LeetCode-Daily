"""这道题非常好,可以用的图的DFS 和 BFS来做.

首先,我们要把除法运算转化成图表示,比如a->b = 2.0 b->c = 3.0,a,b,c看出节点,相处所的值为权值.那么a/c = ?就是相当于,a->c <==> a->b->c = 2.0*3.0= 6,所以我们要把已知条件建图!

接下来,就是遍历方法,这里有两种方法,

一种是DFS,一种是BFS

这两种方法还是看代码一步一步理解较好!"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
# DFS
        def calcEquation(self, equations, values, queries):
            """
            :type equations: List[List[str]]
            :type values: List[float]
            :type queries: List[List[str]]
            :rtype: List[float]
            """
            from collections import defaultdict
            graph = defaultdict(set)
            weight = defaultdict()
            lookup = {}
            # 建图
            for idx, equ in enumerate(equations):
                graph[equ[0]].add(equ[1])
                graph[equ[1]].add(equ[0])
                weight[tuple(equ)] = values[idx]
                weight[(equ[1], equ[0])] = float(1 / values[idx])

            # 深度遍历(DFS)
            def dfs(start, end, vistied):
                # 当图中有此边,直接输出
                if (start, end) in weight:
                    return weight[(start, end)]
                # 图中没有这个点
                if start not in graph or end not in graph:
                    return 0
                # 已经访问过
                if start in vistied:
                    return 0
                vistied.add(start)
                res = 0
                for tmp in graph[start]:
                    res = (dfs(tmp, end, vistied) * weight[(start, tmp)])
                    # 只要遍历到有一个不是0的解就跳出
                    if res != 0:
                        # 添加此边,以后访问节省时间
                        weight[(start, end)] = res
                        break
                vistied.remove(start)
                return res

            res = []
            for que in queries:
                # 用集合记录是否已经访问节点
                tmp = dfs(que[0], que[1], set())
                if tmp == 0:
                    tmp = -1.0
                res.append(tmp)
            return res
    # BFS
        def calcEquation1(self, equations, values, queries):
            from collections import defaultdict, deque
            graph = defaultdict(set)
            weight = defaultdict()
            lookup = {}
            # 建图
            for idx, equ in enumerate(equations):
                graph[equ[0]].add(equ[1])
                graph[equ[1]].add(equ[0])
                weight[tuple(equ)] = values[idx]
                weight[(equ[1], equ[0])] = float(1 / values[idx])
            res = []
            for start, end in queries:
                if (start, end) in weight:
                    res.append(weight[(start, end)])
                    continue
                if start not in graph or end not in graph:
                    res.append(-1)
                    continue
                if start == end:
                    res.append(1.0)
                    continue
                stack = deque()
                # 将从start点可以到达下一个节点压入栈内
                for tmp in graph[start]:
                    stack.appendleft((tmp, weight[(start, tmp)]))
                # 记录访问节点
                visited = {start}
                # 为了跳出双循环
                flag = False
                while stack:
                    c, w = stack.pop()
                    if c == end:
                        flag = True
                        res.append(w)
                        break
                    visited.add(c)
                    for n in graph[c]:
                        if n not in visited:
                            weight[(start, n)] = w * weight[(c, n)]
                            stack.appendleft((n, w * weight[(c, n)]))
                if flag:
                    continue
                res.append(-1.0)
            return res