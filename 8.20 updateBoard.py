from typing import List


class Solution:
    DIRECITONS = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, 1), (-1, -1), (1, -1))

    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        m, n = len(board), len(board[0])
        check = lambda i, j, char: 0 <= i < m and 0 <= j < n and board[i][j] == char

        def count_miners(i, j):
            miners = 0
            for ni, nj in Solution.DIRECITONS:
                ni, nj = ni + i, nj + j
                miners += check(ni, nj, 'M')

            return miners

        def dfs(i, j):  # 这里是逻辑主体
            miners = count_miners(i, j)
            if not miners:
                board[i][j] = 'B'
                for ni, nj in Solution.DIRECITONS:
                    ni, nj = ni + i, nj + j
                    if check(ni, nj, 'E'): dfs(ni, nj)

            else:
                board[i][j] = str(miners)

            return board  # 返不返回都行，不返回就在外面return board

        return dfs(*click)


'''

感觉主要两个条件容易糊涂：

当遍历到临近有***以后，填好数字，然后直接返回，不继续延申
方向是8个方向，不是普通迷宫的四个方向
剩下就是体力活了，补充一个python的dfs

'''