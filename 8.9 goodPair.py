# 复杂度 O(N)
from collections import Counter
from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        print([v * (v - 1) // 2 for v in Counter(nums).values()])
        return sum(v * (v - 1) // 2 for v in Counter(nums).values())


'''# 复杂度 O(N^2)
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] == nums[j]:
                    res += 1
        return res

作者：maxming0
链接：https://leetcode-cn.com/problems/number-of-good-pairs/solution/python3on2onshi-pin-jiang-jie-liang-chong-si-lu-by/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

t = Solution()
t.numIdenticalPairs([1,2,3,4,5,4,3,2,1,1,1])