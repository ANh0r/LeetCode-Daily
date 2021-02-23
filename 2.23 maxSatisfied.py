class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], X: int) -> int:
        # x大小得窗口内得原本不满意得顾客 加上 整个数组里面本身就满意的顾客
        maxcus,res,allcnt,cnt = 0,0,0,0
        n = len(customers)
        # 不考虑x分钟时得最大满意数量
        for i in range(n):
            if grumpy[i] == 0:
                allcnt += customers[i]
        i, j = 0, 0
        while j < n:
            if grumpy[j] == 1:
                res += customers[j]
            cnt += 1
            while cnt > X:
                cnt -= 1
                if grumpy[i] == 1:
                    res -= customers[i]
                i += 1
            maxcus = max(maxcus, res+allcnt)
            j += 1
        return maxcus