class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if not prices:
            return 0
        n = len(prices)
        dp = [[0]*2 for _ in range(n)]
        # 初始化第一天
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1,n):
            # 求第i天的买入最大利润，卖出最大利润
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i]-fee)
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        return dp[-1][0]
"""
dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i]-fee)  卖出   
dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])      买入 
买股票 需要手续费
"""
"""
n = len(prices)
        if n < 2:
             return 0
        ans = 0
        minimum = prices[0]
        for i in range(1, n):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] > minimum + fee:
                ans += prices[i]-fee-minimum
                minimum = prices[i]-fee
        return ans
"""