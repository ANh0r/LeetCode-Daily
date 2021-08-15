class Solution:
    def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
        # 从1开始到N每次刷新m*n的矩阵dp，记录第k次矩阵里每个点能飞出边界的路径数
        # 第k次的dp[i][j]所代表的路径和等于上下左右的节点第k-1次路径的累加和
        # 如果ij代表的是边界的点，那么可能它往上下左右移动会出现直接出界的情况，此时直接+1。
        # 每次只需要维护两个m*n的矩阵，一个是第k次的，一个是第k-1次的

        pre = [[0] * n for i in range(m)]

        # 参考了别人的解法，设置这个方向数组，省了很长的if else
        # 用for循环完成上下左右移动
        dirc = [[0, -1], [-1, 0], [0, 1], [1, 0]]

        # 要生成N次新的dp，每一次都是基于前一次的dp
        for k in range(N):
            # 生成第k次的空白矩阵cur
            cur = [[0] * n for i in range(m)]
            # 开始根据pre填写cur
            for x in range(m):
                for y in range(n):
                    # 开始上下左右移动
                    for d in dirc:
                        move_x = x + d[0]
                        move_y = y + d[1]
                        # 如果移动过后已经出了边界这时直接+1，
                        # xy移动前就在边界上，这1次出界的移动带来了1条新路径
                        if move_x == -1 or move_y == -1 or move_x == m or move_y == n:
                            cur[x][y] += 1
                        # 每次增加的路径一定只跟上一次的点有关，跟本次的上下左右没有任何关系，记住这个
                        else:
                            cur[x][y] += pre[move_x][move_y]
            pre = cur
        # 不要忘记取模，我也是醉了，查了半天
        return pre[i][j] % 1000000007