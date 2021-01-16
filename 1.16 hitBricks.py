class Solution:
    def hitBricks(self, grid: List[List[int]], hits: List[List[int]]) -> List[int]:
        # ==================== 并查集模板 =========================
        def find(x):
            parent.setdefault(x, x)
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            rootx, rooty = find(x), find(y)
            if rootx != rooty:
                if rank[rootx] < rank[rooty]:
                    parent[rootx] = rooty
                    count[rooty] += count[rootx]
                else:
                    parent[rooty] = rootx
                    count[rootx] += count[rooty]
                    if rank[rootx] == rank[rooty]: rank[rootx] += 1

        # =============== 第一步：将所有hits标记的砖块打碎 ==================
        nr, nc = len(grid), len(grid[0])  # 排列长度
        original_grid = copy.deepcopy(grid)  # 复制原图

        for i, j in hits: grid[i][j] = 0  # 打碎所有砖块

        # =============== 第二步：将砖块与相邻砖块连接起来 ==================
        parent = {nr * nc: nr * nc}  # 记录各个位置的父节点（初始一个虚拟屋顶）
        rank = [0] * (nr * nc + 1)  # 记录各个位置的rank（包含屋顶）
        count = [1] * (nr * nc) + [0]  # 记录各个位置连接的节点的数量（包含屋顶）

        for j in range(nc):
            if grid[0][j] == 1: union(j, nr * nc)  # 将最上面一排与屋顶连接

        for r in range(1, nr):  # 将剩余砖块相互连接
            for c in range(nc):
                if grid[r][c] == 1:
                    if grid[r - 1][c] == 1: union(r * nc + c, (r - 1) * nc + c)
                    if c > 0 and grid[r][c - 1] == 1: union(r * nc + c, r * nc + c - 1)

        # =============== 第三步：按照hits逆序往回补充砖块 ==================
        res = []
        for r, c in hits[::-1]:  # 逆序遍历hits
            if original_grid[r][c] == 0:  # 若原grid当中这个位置本身没有砖块，即空白
                res.append(0)  # 则没有砖块掉落
                continue
            origin = count[find(nr * nc)]  # 找到原先与屋顶连接的砖块的数量
            if r == 0: union(c, nr * nc)  # 若当前打击位置是第一排， 则将补回的砖块与屋顶连接
            for x, y in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:  # 依次查看四个方向
                if 0 <= x < nr and 0 <= y < nc and grid[x][y] == 1:  # 若存在砖块
                    union(r * nc + c, x * nc + y)  # 则将其与当前砖块连接
            current = count[find(nr * nc)]  # 连接完成之后，再找到现在与屋顶连接的砖块数量
            res.append(max(0, current - origin - 1))  # 计算差值（注意需要减去当前这块砖，因为不算做掉落）
            grid[r][c] = 1  # 补回砖块

        return res[::-1]  # 逆序返回结果