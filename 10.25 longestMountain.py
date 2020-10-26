"""解题思路
参数定义
up：数组，up[i]
表示以i点为终点从左到右连续上升的山峰的个数
down：数组，down[i]
表示以i为终点从右到左连续上升的山峰的个数
res：记录山脉的最大长度
初始化
每一个山峰可作为一个独立的个体，所以up和down的每一个初始化为1
思路
由于up[i]
和down[i]
分别表示左右连续上升的山峰的个数，所以当某个山峰的左右山峰都小于自己，则可形成山脉，而up[i] + down[i] - 1
记为这段山脉的长度
可能存在多段山脉，利用res记录当前的最长的山脉长度
示例：[2, 1, 4, 7, 3, 2, 5]
对应的up为[1, 1, 2, 3, 1, 1, 1]，down为[2, 1, 1, 3, 2, 1, 1]，当山峰为7时，行成的山脉为[1, 4, 7, 3, 2]，长度为up[i] + down[i] - 1 = 5
复杂度分析
时间复杂度：O(N)
空间复杂度：O(N)
代码"""
from typing import List


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        if not A:
            return 0
        n = len(A)
        up = [1] * n
        down = [1] * n
        for i in range(1, n):
            if A[i] > A[i - 1]:
                up[i] = up[i - 1] + 1

            if A[n - i - 1] > A[n - i]:
                down[n - i - 1] = down[n - i] + 1

        res = 0
        for i in range(1, n - 1):
            if A[i - 1] < A[i] and A[i] > A[i + 1]:
                res = max(res, up[i] + down[i] - 1)
        return res
