from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return True
        if 1 not in nums:
            return True
        p = nums.index(1)
        l = len(nums)
        for q in range(nums.index(1) + 1, l):
            if nums[q] == 1:
                if q - p >= k + 1:
                    p = q
                else:
                    return False
        return True


t = Solution()
print(t.kLengthApart([0,0,0],2))




