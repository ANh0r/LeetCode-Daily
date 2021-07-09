class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cand1 = -1
        n = len(nums)
        for i in range(n):
            if nums[i] == cand1:
                count += 1
            elif nums[i] != cand1 and count == 0:
                cand1 = nums[i]
            else:
                count -= 1
        count1 = 0
        for i in range(n):
            if nums[i] == cand1:
                count1 += 1
        if count1 > n//2:
            return cand1
        else:
            return -1