"""给定两个数组，编写一个函数来计算它们的交集。

 

示例 1：

输入：nums1 = [1,2,2,1], nums2 = [2,2]
输出：[2]
示例 2：

输入：nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出：[9,4]
"""
from typing import List

class Solution:

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1)<len(set2):
            return self.set_interserction(set1,set2)
        else:
            return self.set_interserction(set2,set1)

    def set_interserction(self,set1,set2):
        return [x for x in set1 if x in set2]


''' 另外：
        set1 = set(nums1)
        set2 = set(nums2)
        return list(set2 & set1)
'''

t = Solution()
print(t.intersection([1,2,3,4,5],[1,2,3,4,5,6,6]))
