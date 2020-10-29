class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dir_ = {(0,1),(1,0)}
        num = 0
        m,n = len(grid),len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    num += 1
        num *= 4
        for x in range(m):
            for y in range(n):
                if grid[x][y] == 1:
                    for dx,dy in dir_:
                        if x + dx < 0 or x + dx >= m or y + dy < 0 or y + dy >= n:
                            continue
                        if grid[x + dx][y + dy] == 1:
                            num -= 2
        return num
    