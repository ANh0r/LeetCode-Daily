from typing import List


class Solution:
    def exchange(self, nums: List[int]) -> List[int]:
        i = 0
        for j in range (len(nums)):
            if nums[j]%2 == 1:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        return nums


t = Solution()
print(t.exchange([1,4,5,6,7,8]))