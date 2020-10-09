from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0] * 3
        for n in nums: cnt[n] += 1
        i = 0
        # print(cnt[0])
        for cur in range(3):
            for j in range(cnt[cur]):
                nums[i] = cur
                i += 1

                '''class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        ptr = 0
        for i in range(n):
            if nums[i] == 0:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
        for i in range(ptr, n):
            if nums[i] == 1:
                nums[i], nums[ptr] = nums[ptr], nums[i]
                ptr += 1
。'''

t = Solution()
t.sortColors([0,0,0,0,0,1,1,2,2])
