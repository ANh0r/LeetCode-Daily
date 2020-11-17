class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        return sorted([[i, j] for i in range(R) for j in range(C)], key=lambda x: abs(x[0] - r0) + abs(x[1] - c0))
    """
    返回曼哈顿距离排序后的所有坐标
    给定：RC为R行C列
    r0 c0是曼哈顿距离计算的基准点"""