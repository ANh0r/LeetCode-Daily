class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if not m:
            return False
        n = len(board[0])
        # 最主要八行提速
        ans = []
        for b in board:
            ans += b
        need = Counter(word)
        ans = Counter(ans)
        for k, v in need.items():
            if v > ans[k]:
                return False

        ans = [[False] * n for _ in range(m)]

        def back(i, j, word):
            if not word:
                return True
            # 定义上下左右四个行走方向
            for (x, y) in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
                cur_i, cur_j = i + x, j + y
                # 越界，忽略
                if cur_i < 0 or cur_i >= m or cur_j < 0 or cur_j >= n:
                    continue
                # 如果当前位置不等于word首字母 或是 已经使用过的元素，忽略
                if board[cur_i][cur_j] != word[0] or ans[cur_i][cur_j] == True:
                    continue
                ans[cur_i][cur_j] = True
                if back(cur_i, cur_j, word[1:]):
                    return True
                ans[cur_i][cur_j] = False
                # print(ans, word)
            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    # 将该元素标记为已使用
                    ans[i][j] = True
                    if back(i, j, word[1:]):
                        return True
                    # 回溯
                    ans[i][j] = False
        return False
    # def exist(self, board: List[List[str]], word: str) -> bool:
    #     directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    #
    #     def check(i: int, j: int, k: int) -> bool:
    #         if board[i][j] != word[k]:
    #             return False
    #         if k == len(word) - 1:
    #             return True
    #
    #         visited.add((i, j))
    #         result = False
    #         for di, dj in directions:
    #             newi, newj = i + di, j + dj
    #             if 0 <= newi < len(board) and 0 <= newj < len(board[0]):
    #                 if (newi, newj) not in visited:
    #                     if check(newi, newj, k + 1):
    #                         result = True
    #                         break
    #
    #         visited.remove((i, j))
    #         return result
    #
    #     h, w = len(board), len(board[0])
    #     visited = set()
    #     for i in range(h):
    #         for j in range(w):
    #             if check(i, j, 0):
    #                 return True
    #
    #     return False
"""
给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false

"""