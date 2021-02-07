class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        count = 0
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                count += 1
                if i+1 < len(nums) and i-2 >= 0:
                    if nums[i+1] < nums[i-1] and nums[i-2] > nums[i]:
                        return False
            if count > 1:
                return False
        return True