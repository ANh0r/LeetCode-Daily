class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 3:
            return 0

        res = 0  # 记录等差数列的个数
        k = 2  # 记录一个连续子序列中差相等的元素个数
        subVal = nums[1] - nums[0]  # 记录当前两个差值

        for i in range(2, length):
            temp = nums[i] - nums[i - 1]
            if temp == subVal:
                k += 1

            else:
                if k >= 3:
                    res += (k - 1) * (k - 2) // 2

                k = 2  # 任意两个数都可以构成长度为2的连续子序列， 只是要看第三个值能否组成等差
                subVal = temp

        # 最后一波的k 并没有被计算
        if k >= 3:
            res += (k - 1) * (k - 2) // 2

        return res