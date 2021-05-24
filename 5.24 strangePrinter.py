class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[float('inf')] * n for _ in range(n)]
        for i in range(n-1,-1,-1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    minn = float('inf')
                    for k in range(i, j):
                        if dp[i][k] + dp[k+1][j] < minn:
                            minn = dp[i][k] + dp[k+1][j]
                    dp[i][j] = minn
        return dp[0][n-1]