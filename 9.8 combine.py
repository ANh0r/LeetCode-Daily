"""
给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。

示例:

输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

return list(itertools.combinations(range(1,n+1),k))
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n < k or n < 1:
            return []
        if k == 0:
            return [[]]
        if n == k:
            return [[i for i in range(1, n + 1)]]
        ans1 = self.combine(n - 1, k - 1)
        ans2 = self.combine(n - 1, k)
        # printrint(n, k, ans1, ans2)
        if ans1:
            for i in ans1:
                i.append(n)
        return ans1 + ans2


t = Solution()
print(t.combine(4,3))