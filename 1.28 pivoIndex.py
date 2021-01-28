class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        prefix = [0]
        sum_ = 0
        for i in range(n):
            sum_ += nums[i]
            prefix.append(sum_)
        ans = -1
        for j in range(n):
            if prefix[j] == prefix[-1]-prefix[j+1]:
                ans = j
                break
        return ans