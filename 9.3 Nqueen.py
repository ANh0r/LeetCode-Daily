class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col,diagonal1,diagonal2 = [],[],[]
        currentanswer = []
        resultanswer = []
        strings = ''
        for i in range(n):
            strings = strings+'.'
        # 提前形成'...'这样的字符串，后面产生答案的时候只需更改其中的Q即可

        def solves(self, n: int, currentrow: int):
            # 一行一行地进行dfs深搜
            if currentrow == n:
                # 行遍历完之后退出
                resultanswer.append(currentanswer[:])
                return
            for i in range(n):
                # 当前形成的坐标为(currentrow,i)
                if i not in col:
                    # col数组记录之前访问的列,i not in col表明与先前的坐标不在一列
                    flag = True
                    for j in range(len(diagonal1)):
                        if currentrow+diagonal1[j] == i:
                            # diagonal1记录y=kx+b1中的b1的值，如果满足方程证明与之前的点在同一条对角线上
                            flag = False
                            break
                        elif currentrow+i == diagonal2[j]:
                            # diagonal2记录y=kx+b2中的b2的值，如果满足方程证明与之前的点在同一条对角线上
                            flag = False
                            break
                    if flag == True:
                        # 与先前的列和对角线都不重合的情况下
                        currentstring = strings[0:i]
                        currentstring = currentstring+'Q'
                        currentstring = currentstring+strings[i+1:n]
                        currentanswer.append(currentstring)
                        #   将列标记为'Q'形成当前行的字符串
                        col.append(i)
                        diagonal1.append(i-currentrow)
                        diagonal2.append(i+currentrow)
                        # 标记当前访问的列以及两条对角线对应的b1,b2
                        solves(self,n,currentrow+1)
                        currentanswer.pop()
                        col.pop()
                        diagonal1.pop()
                        diagonal2.pop()
                        # 当前回溯返回的时候不要忘记将先前的坐标从数组中去除，进行对下一列点的回溯
        solves(self,n,0)
        #   初始搜索从0开始
        return resultanswer
"""
上图为 8 皇后问题的一种解法。

给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。

每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。

"""

'''class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        g = [['.'] * n for _ in range(n)]
        cols = [False] * n
        dg = [0] * (2 * n)
        udg = [0] * (2 * n)
        self.res = []
        self.dfs(0, n, cols, dg, udg,g)
        return self.res
    def dfs(self, row, n, cols, dg, udg,g):
        if row == n:
            res = []
            for i in range(n):
                res.append(''.join(g[i]))
            self.res.append(res)
            return 
        for c in range(n):
            if cols[c] or dg[c - row + n] or udg[c + row]:
                continue
            g[row][c] = 'Q'
            cols[c] = dg[c - row + n] = udg[c + row] = True
            self.dfs(row + 1, n, cols, dg, udg,g)
            cols[c] = dg[c - row + n] = udg[c + row] = False
            g[row][c] = '.'
            '''