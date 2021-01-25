class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        N = len(grid)
        parent = [i for i in range(4 * N * N)]  # 开始的时候每个节点的帮主都是自己

        def find(parent, x):  # 寻找每个节点的帮主
            if parent[x] == x:
                return parent[x]
            return find(parent, parent[x])

        def union(parent, x, y):  # 两个人相遇， 那么各自去找教主，教主对决
            x_root = find(parent, x)
            y_root = find(parent, y)
            if x_root != y_root:  # 教主不同
                parent[x_root] = y_root  # 对决赢的成为新教主

        def union_find(grid):
            for r, row in enumerate(grid):
                for c, val in enumerate(row):
                    top = 4 * (r * N + c)
                    if val in ['/', ' ']:
                        union(parent, top + 0, top + 1)
                        union(parent, top + 2, top + 3)
                    if val in ['\\', ' ']:
                        union(parent, top + 0, top + 2)
                        union(parent, top + 1, top + 3)

                    if r + 1 < N:
                        union(parent, top + 3, top + (4 * N) + 0)
                    if r - 1 >= 0:  # 这部分其实是多于的
                        union(parent, top + 0, top - (4 * N) + 3)
                    if c + 1 < N:
                        union(parent, top + 2, top + 4 + 1)
                    if c - 1 >= 0:  # 这部分其实也是多于的
                        union(parent, top + 1, top - 4 + 2)

            return sum(parent[x] == x for x in range(4 * N * N))

        return union_find(grid)