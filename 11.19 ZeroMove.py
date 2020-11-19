class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort(key=bool, reverse=True)
        # 只对布尔值排序，意思是排序排0和非0 ，非0内部的顺序不变
        # 举例: 1 2 3 4 0正序: 0 1 2 3 4 逆序: 1 2 3 4 0