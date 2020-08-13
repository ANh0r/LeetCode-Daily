from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        sum = 0
        for ind in coins:
            if ind % 2 ==0:
                sum += ind//2
            elif ind %2 ==1:
                sum += ind //2 + 1
        return sum

#return sum((c + 1) // 2 for c in coins) 或者直接加一在除以二也可以，算向上取整数

t = Solution()
print(t.minCount([1,2,4]))