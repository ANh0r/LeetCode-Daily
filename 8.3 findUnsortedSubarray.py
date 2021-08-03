class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        A = sorted(nums)
        left = 0
        right = len(A) - 1
        length = 0
        while left <= right and nums[left] == A[left]:
            left += 1

        if left - 1 == right:
            return 0
        while nums[right] == A[right]:
            right -= 1
        return right - left + 1