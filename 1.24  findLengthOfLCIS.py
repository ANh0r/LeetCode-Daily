class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        # ans = 0
        # n = len(nums)
        # start = 0

        # for i in range(n):
        #     if i > 0 and nums[i] <= nums[i - 1]:
        #         start = i
        #     ans = max(ans, i - start + 1)

        # return ans
        n = len(nums)
        if n == 0:
            return 0
        dp = [1] * n
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                dp[i] = dp[i - 1] + 1
        return max(dp)

"""
最长连续子序列
"""