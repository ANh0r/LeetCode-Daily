class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        money, buy = 0, int(1e9)
        for i in prices:
            if i >= buy: money += i - buy
            buy = i
        return money


'''
在第i天买入， 如果第i+1天的值大于第i天，那么在第i+1天卖出，同时在第i+1天再买入； 如果第i+1天的值小于第i天，那么将买入时间调整为第i+1天
是因为本题中允许当天卖出立即买入
'''

ans = Solution()
print(ans.maxProfit([1,2,3,5,5,67,5]))

