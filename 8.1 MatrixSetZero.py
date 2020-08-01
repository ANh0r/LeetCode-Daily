from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_width = len(matrix)
        matrix_height = len(matrix[0])
        rows = []
        cols = []
        for i in range(matrix_width):
            for j in range(matrix_height):
                if matrix[i][j] == 0:
                    rows.append(i)
                    cols.append(j)

        # 先将行置为0
        for i in rows:
            matrix[i] = [0 for _ in range(matrix_height)]

        # 将列置为0
        for i in range(matrix_width):
            for j in range(matrix_height):
                if j in cols:
                    matrix[i][j] = 0

        return matrix


