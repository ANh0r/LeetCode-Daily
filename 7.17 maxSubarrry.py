class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1], 0)
        return max(nums)
"""
dp
最后一个数一定加进去
看前面大于0还是小于0，大于0就加上，小于0就舍弃
"""