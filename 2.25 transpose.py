class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        return [[x[i] for x in matrix] for i in range(len(matrix[0]))]