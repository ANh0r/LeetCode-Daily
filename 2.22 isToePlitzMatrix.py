class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        col_len = len(matrix) #3
        row_len = len(matrix[0]) #4
        if col_len == 1 or row_len == 1:
            return True
        for i in range(len(maatrix) - 1):
            if matrix[i][:-1] != matrix[i + 1][1:]:
                return False
        return True
"""
只需判断：前行中除最后一个元素外剩余的元素完全等于后行中除第一个元素外剩余的元素。
托普利茨矩阵
"""