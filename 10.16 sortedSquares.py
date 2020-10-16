class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([i*i for i in A])


"""
非有序数组 平方后排序"""