from typing import List
#
'''本题给定的矩阵中有三种元素：

字母 X；
被字母 X 包围的字母 O；
没有被字母 X 包围的字母 O。
本题要求将所有被字母 X 包围的字母 O都变为字母 X ，但很难判断哪些 O 是被包围的，哪些 O 不是被包围的。

注意到题目解释中提到：任何边界上的 O 都不会被填充为 X。 我们可以想到，所有的不被包围的 O 都直接或间接与边界上的 O 相连。我们可以利用这个性质判断 O 是否在边界上，具体地说：

对于每一个边界上的 O，我们以它为起点，标记所有与它直接或间接相连的字母 O；
最后我们遍历这个矩阵，对于每一个字母：
如果该字母被标记过，则该字母为没有被字母 X 包围的字母 O，我们将其还原为字母 O；
如果该字母没有被标记过，则该字母为被字母 X 包围的字母 O，我们将其修改为字母 X

作者：LeetCode-Solution
链接：https://leetcode-cn.com/problems/surrounded-regions/solution/bei-wei-rao-de-qu-yu-by-leetcode-solution/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        n, m = len(board), len(board[0])

        def dfs(x, y):
            if not 0 <= x < n or not 0 <= y < m or board[x][y] != 'O':
                return

            board[x][y] = "A"
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)

        for i in range(n):
            dfs(i, 0)
            dfs(i, m - 1)

        for i in range(m - 1):
            dfs(0, i)
            dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if board[i][j] == "A":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"



#
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         if not board:
#             return
#
#         n, m = len(board), len(board[0])
#         que = collections.deque()
#         for i in range(n):
#             if board[i][0] == "O":
#                 que.append((i, 0))
#             if board[i][m - 1] == "O":
#                 que.append((i, m - 1))
#         for i in range(m - 1):
#             if board[0][i] == "O":
#                 que.append((0, i))
#             if board[n - 1][i] == "O":
#                 que.append((n - 1, i))
#
#         while que:
#             x, y = que.popleft()
#             board[x][y] = "A"
#             for mx, my in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
#                 if 0 <= mx < n and 0 <= my < m and board[mx][my] == "O":
#                     que.append((mx, my))
#
#         for i in range(n):
#             for j in range(m):
#                 if board[i][j] == "A":
#                     board[i][j] = "O"
#                 elif board[i][j] == "O":
#                     board[i][j] = "X"



'''
给定一个二维的矩阵，包含 'X' 和 'O'（字母 O）。

找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。

示例:

X X X X
X O O X
X X O X
X O X X
运行你的函数后，矩阵变为：

X X X X
X X X X
X X X X
X O X X
解释:

被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''