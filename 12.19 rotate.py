class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i,row in enumerate(matrix):
            for j,num in enumerate(row):
                if j>i:# 上三角
                    tmp=num
                    matrix[i][j]=matrix[j][i]
                    matrix[j][i]=tmp
        for i,row in enumerate(matrix):
            row.reverse()
"""
先沿对角对称，然后每行按中轴对称
"""