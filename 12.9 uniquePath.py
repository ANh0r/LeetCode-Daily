class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, n - 1)

"""
从左上到右下不同路径的数量
"""