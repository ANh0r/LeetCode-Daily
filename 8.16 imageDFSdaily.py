from collections import deque
from queue import Queue
from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # 起始颜色和目标颜色相同，则直接返回原图
        if newColor == image[sr][sc]:
            return image
        # 设置四个方向偏移量，一种常见的省事儿技巧
        directions = {(1, 0), (-1, 0), (0, 1), (0, -1)}
        # 构造一个队列，先把起始点放进去
        que = Queue()
        que.put((sr, sc))
        # 记录初始颜色
        originalcolor = image[sr][sc]
        # 当队列不为空
        while not que.empty():
            # 取出队列的点并染色
            point = que.get()
            image[point[0]][point[1]] = newColor
            # 遍历四个方向
            for direction in directions:
                # 新点是(new_i,new_j)
                new_i = point[0] + direction[0]
                new_j = point[1] + direction[1]
                # 如果这个点在定义域内并且它和原来的颜色相同
                if 0 <= new_i < len(image) and 0 <= new_j < len(image[0]) and image[new_i][new_j] == originalcolor:
                    que.put((new_i, new_j))
        return image


class Solution2:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        p = image[sr][sc]
        if p == newColor:
            return image

        def dfs(x: int, y: int) -> None:
            if x in {-1, row} or y in {-1, col} or image[x][y] != p:
                return
            image[x][y] = newColor
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
            dfs(x, y + 1)
            return image

        return dfs(sr, sc)

class Solution3:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        p = image[sr][sc]
        deq = deque([(sr, sc)])
        if p == newColor:
            return image
        while deq:
            x, y = deq.popleft()
            if x in {-1, row} or y in {-1, col} or image[x][y] != p:
                continue
            image[x][y] = newColor
            deq.extend([(x-1, y), (x, y-1), (x+1, y), (x, y+1)])
        return image


