class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0]*len(nums2) for _ in range(len(nums1))]
        dp[0][0] = 1 if nums1[0]==nums2[0] else 0
        for i in range(1, len(nums1)):
            if nums1[i] == nums2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = dp[i-1][0]
        for j in range(1, len(nums2)):
            if nums1[0] == nums2[j]:
                dp[0][j] = 1
            else:
                dp[0][j] = dp[0][j-1]

        for i in range(1, len(nums1)):
            for j in range(1, len(nums2)):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[-1][-1]