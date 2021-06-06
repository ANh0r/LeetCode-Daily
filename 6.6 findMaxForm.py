class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        if len(strs) == 0:
            return 0
        dp = [[0] * (n+1) for _ in range(m+1)]
        for strs_item in strs:
            zeros = strs_item.count("0")
            ones = len(strs_item) - zeros
            for i in range(m, zeros - 1, -1):
                for j in range(n, ones - 1, -1):
                    dp[i][j] = max(dp[i][j], 1+dp[i- zeros][j-ones])
        return dp[m][n]