class Solution:
    def search(self, nums: List[int], target: int) -> int:
        index = bisect_left(nums, target)
        ans = 0
        while index < len(nums):
            if nums[index] == target:
                ans += 1
            if nums[index] > target:
                break
            index += 1

        return ans