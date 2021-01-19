class DSU:
    def __init__(self,n: int):
        self.p = [i for i in range(n)]
        self.part = n
    def find(self,x: int) -> int:
        if x != self.p[x]: self.p[x] = self.find(self.p[x])
        return self.p[x]
    def merge(self,x: int,y: int):
        rx , ry = self.find(x) , self.find(y)
        if rx == ry: return
        self.p[rx] = ry
        self.part -= 1
        return
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def Manhattan(p1,p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                edges.append([i,j,Manhattan(points[i],points[j])])
        edges.sort(key = lambda x : x[2])
        n = len(points)
        dsu = DSU(n)
        ans = 0
        for e in edges:
            fa1 = dsu.find(e[0])
            fa2 = dsu.find(e[1])
            if fa1 != fa2:
                ans += e[2]
                dsu.merge(e[0],e[1])
            if dsu.part == 1:
                break
        return ans
"""
Kruskal MST 并查集
"""