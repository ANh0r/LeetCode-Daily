import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1 = collections.Counter(nums1)
        num2 = collections.Counter(nums2)
        num = num1 & num2
        print(num.elements())
        return list(num.elements())


t =Solution()
print(t.intersect([1,2,3],[2,3,4]))